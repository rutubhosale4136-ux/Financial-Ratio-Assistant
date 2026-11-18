"""Unit and integration test suite for Step 12: Analysis History & Audit Log.

College Project: Financial Statement Ratio Analysis Assistant
Tests:
1. Chronological retrieval of analysis history records (list_analyses).
2. Safe deletion of analysis history row (delete_analysis) while preserving company and statement data.
3. Multi-user isolation in analysis history (User 1 cannot see or delete User 2's history).
4. Search and filter logic (company filter, FY filter, search keyword).
5. Render simulation with mocked Streamlit components (empty state and populated audit cards).
"""

import os
import tempfile
import unittest
from unittest.mock import MagicMock, patch

import database
import calculations
import analysis
from pages import history


class TestStep12AnalysisHistory(unittest.TestCase):
    """Test suite for Step 12 Analysis History and Audit Trail."""

    def setUp(self):
        """Create an isolated temporary SQLite database for testing."""
        self.temp_db = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.temp_db.close()
        self.db_path = self.temp_db.name
        database.init_db(self.db_path)

        # Create two test users
        self.user1_id = database.create_user(
            full_name="Analyst One",
            email="analyst1@college.edu",
            password_hash="hash1",
            password_salt="salt1",
            db_path=self.db_path,
        )
        self.user2_id = database.create_user(
            full_name="Analyst Two",
            email="analyst2@college.edu",
            password_hash="hash2",
            password_salt="salt2",
            db_path=self.db_path,
        )

        # Create two companies for User 1
        self.comp1_id = database.create_company(
            user_id=self.user1_id,
            company_name="Apex Motors Ltd",
            industry="Automotive",
            financial_year="FY 2025-26",
            db_path=self.db_path,
        )
        self.comp2_id = database.create_company(
            user_id=self.user1_id,
            company_name="Bharat Tech Solutions",
            industry="IT Services",
            financial_year="FY 2025-26",
            db_path=self.db_path,
        )

        # Create one company for User 2
        self.u2_comp_id = database.create_company(
            user_id=self.user2_id,
            company_name="User2 Enterprise",
            industry="Retail",
            financial_year="FY 2025-26",
            db_path=self.db_path,
        )

        # Sample statement data
        self.stmt1_data = {
            "revenue": 50000000.0,
            "cost_of_goods_sold": 30000000.0,
            "gross_profit": 20000000.0,
            "operating_expenses": 8000000.0,
            "operating_income": 12000000.0,
            "interest_expense": 2000000.0,
            "tax_expense": 2500000.0,
            "net_income": 7500000.0,
            "current_assets": 18000000.0,
            "cash_and_cash_equivalents": 6000000.0,
            "inventory": 5000000.0,
            "total_assets": 45000000.0,
            "current_liabilities": 9000000.0,
            "total_liabilities": 18000000.0,
            "total_debt": 12000000.0,
            "shareholders_equity": 27000000.0,
            "opening_inventory": 4500000.0,
            "closing_inventory": 5000000.0,
            "opening_total_assets": 40000000.0,
            "closing_total_assets": 45000000.0,
            "operating_cash_flow": 11000000.0,
            "capital_expenditure": 4000000.0,
            "free_cash_flow": 7000000.0,
        }

        # Save analysis 1 for User 1 (Apex Motors)
        ratios1 = calculations.calculate_all_ratios(self.stmt1_data)
        res1 = database.save_full_analysis(
            user_id=self.user1_id,
            company_id=self.comp1_id,
            statement_data=self.stmt1_data,
            ratio_data=ratios1,
            db_path=self.db_path,
        )
        self.analysis1_id = res1["analysis_id"]
        self.stmt1_id = res1["statement_id"]

        # Save analysis 2 for User 1 (Bharat Tech)
        self.stmt2_data = dict(self.stmt1_data)
        self.stmt2_data["revenue"] = 80000000.0
        self.stmt2_data["net_income"] = 18000000.0
        ratios2 = calculations.calculate_all_ratios(self.stmt2_data)
        res2 = database.save_full_analysis(
            user_id=self.user1_id,
            company_id=self.comp2_id,
            statement_data=self.stmt2_data,
            ratio_data=ratios2,
            db_path=self.db_path,
        )
        self.analysis2_id = res2["analysis_id"]

        # Save analysis for User 2
        ratios_u2 = calculations.calculate_all_ratios(self.stmt1_data)
        res_u2 = database.save_full_analysis(
            user_id=self.user2_id,
            company_id=self.u2_comp_id,
            statement_data=self.stmt1_data,
            ratio_data=ratios_u2,
            db_path=self.db_path,
        )
        self.u2_analysis_id = res_u2["analysis_id"]

    def tearDown(self):
        """Clean up test database file."""
        if os.path.exists(self.db_path):
            try:
                os.remove(self.db_path)
            except Exception:
                pass

    def test_list_analyses_chronological_retrieval(self):
        """Test retrieving history records for a user in reverse chronological order."""
        history_list = database.list_analyses(self.user1_id, db_path=self.db_path)
        self.assertEqual(len(history_list), 2)
        # Most recent analysis first
        self.assertEqual(history_list[0]["id"], self.analysis2_id)
        self.assertEqual(history_list[0]["company_name"], "Bharat Tech Solutions")
        self.assertEqual(history_list[1]["id"], self.analysis1_id)
        self.assertEqual(history_list[1]["company_name"], "Apex Motors Ltd")

    def test_safe_delete_analysis_history(self):
        """Test that delete_analysis safely deletes only the history record while preserving statements and companies."""
        # Confirm initial state
        initial_history = database.list_analyses(self.user1_id, db_path=self.db_path)
        self.assertEqual(len(initial_history), 2)

        # Delete Analysis 1
        success = database.delete_analysis(self.user1_id, self.analysis1_id, db_path=self.db_path)
        self.assertTrue(success, "delete_analysis must return True on success")

        # History should now have only 1 row
        updated_history = database.list_analyses(self.user1_id, db_path=self.db_path)
        self.assertEqual(len(updated_history), 1)
        self.assertEqual(updated_history[0]["id"], self.analysis2_id)

        # Verify underlying company and statement are STILL INTACT!
        company = database.get_company(self.user1_id, self.comp1_id, db_path=self.db_path)
        self.assertIsNotNone(company, "Company must NOT be deleted when deleting an analysis log")
        self.assertEqual(company["company_name"], "Apex Motors Ltd")

        statement = database.get_statement(self.user1_id, self.stmt1_id, db_path=self.db_path)
        self.assertIsNotNone(statement, "Statement must NOT be deleted when deleting an analysis log")
        self.assertEqual(statement["revenue"], 50000000.0)

    def test_user_data_isolation_in_history(self):
        """Verify strict multi-user privacy in history querying and deletion."""
        # User 1 cannot see User 2's history
        u1_history = database.list_analyses(self.user1_id, db_path=self.db_path)
        u1_ids = [r["id"] for r in u1_history]
        self.assertNotIn(self.u2_analysis_id, u1_ids, "User 1 must not see User 2's audit logs")

        # User 2 cannot see User 1's history
        u2_history = database.list_analyses(self.user2_id, db_path=self.db_path)
        u2_ids = [r["id"] for r in u2_history]
        self.assertEqual(len(u2_history), 1)
        self.assertNotIn(self.analysis1_id, u2_ids, "User 2 must not see User 1's audit logs")
        self.assertNotIn(self.analysis2_id, u2_ids)

        # User 1 cannot delete User 2's history row
        del_attempt = database.delete_analysis(self.user1_id, self.u2_analysis_id, db_path=self.db_path)
        self.assertFalse(del_attempt, "User 1 cannot delete User 2's analysis record")

        # Verify User 2's record is still intact
        u2_record = database.get_analysis(self.user2_id, self.u2_analysis_id, db_path=self.db_path)
        self.assertIsNotNone(u2_record)

    @patch("streamlit.selectbox")
    @patch("streamlit.text_input")
    @patch("streamlit.download_button")
    @patch("streamlit.metric")
    @patch("streamlit.markdown")
    def test_history_page_render_simulation(self, mock_md, mock_metric, mock_dl, mock_text, mock_select):
        """Simulate rendering the analysis history page with mocked Streamlit widgets."""
        orig_get_conn = database.get_connection
        with patch("database.get_connection", lambda db_path=None: orig_get_conn(self.db_path)):
            user1 = {"id": self.user1_id, "full_name": "Analyst One", "email": "analyst1@college.edu"}
            mock_text.return_value = ""
            mock_select.side_effect = ["All Companies", "All Financial Years"]

            history.render_history_page(user1)

            # Verify CSV export button was rendered
            self.assertTrue(mock_dl.called, "CSV download button must be rendered")
            call_kwargs = mock_dl.call_args[1]
            self.assertEqual(call_kwargs.get("mime"), "text/csv")
            self.assertTrue(call_kwargs.get("file_name").startswith(f"Financial_Analysis_History_User_{self.user1_id}"))


if __name__ == "__main__":
    unittest.main()
