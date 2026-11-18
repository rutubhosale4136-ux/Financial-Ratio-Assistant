"""Unit and integration test suite for Step 11: PDF Reports Generation (ReportLab).

College Project: Financial Statement Ratio Analysis Assistant
Tests:
1. PDF generator builds valid PDF bytes with ReportLab (%PDF- header and %%EOF).
2. Proper Indian currency formatting (INR ₹, 3,2,2 grouping, Lakhs and Crores).
3. 14 Ratios diagnostic matrix and financial statement tables inclusion.
4. Edge cases: zero denominators (None / N/A), negative net profit, zero balances.
5. Database report tracking counter increment (mark_report_generated).
6. Multi-user isolation in PDF reporting.
7. Reports page rendering simulation (empty states & populated states).
"""

import os
import sqlite3
import tempfile
import unittest
from unittest.mock import MagicMock, patch

import database
import calculations
import analysis
import pdf_report
from pages import reports


class TestStep11PDFReports(unittest.TestCase):
    """Test suite for Step 11 PDF generation and reporting."""

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

        # Create company and statement for User 1
        self.company1_id = database.create_company(
            user_id=self.user1_id,
            company_name="Apex Motors Ltd",
            industry="Automotive",
            financial_year="FY 2025-26",
            description="Leading EV and commercial vehicle manufacturer.",
            db_path=self.db_path,
        )

        self.sample_statement_user1 = {
            "revenue": 50000000.0,            # ₹ 5.00 Cr
            "cost_of_goods_sold": 30000000.0, # ₹ 3.00 Cr
            "gross_profit": 20000000.0,       # ₹ 2.00 Cr
            "operating_expenses": 8000000.0,   # ₹ 80.00 Lakh
            "operating_income": 12000000.0,   # ₹ 1.20 Cr
            "interest_expense": 2000000.0,    # ₹ 20.00 Lakh
            "tax_expense": 2500000.0,         # ₹ 25.00 Lakh
            "net_income": 7500000.0,          # ₹ 75.00 Lakh
            "current_assets": 18000000.0,     # ₹ 1.80 Cr
            "cash_and_cash_equivalents": 6000000.0,
            "inventory": 5000000.0,
            "total_assets": 45000000.0,       # ₹ 4.50 Cr
            "current_liabilities": 9000000.0,  # ₹ 90.00 Lakh
            "total_liabilities": 18000000.0,
            "total_debt": 12000000.0,
            "shareholders_equity": 27000000.0,# ₹ 2.70 Cr
            "opening_inventory": 4500000.0,
            "closing_inventory": 5000000.0,
            "opening_total_assets": 40000000.0,
            "closing_total_assets": 45000000.0,
            "operating_cash_flow": 11000000.0,# ₹ 1.10 Cr
            "capital_expenditure": 4000000.0, # ₹ 40.00 Lakh
            "free_cash_flow": 7000000.0,      # ₹ 70.00 Lakh
        }

        # Calculate ratios and save full analysis in database
        self.ratios_user1 = calculations.calculate_all_ratios(self.sample_statement_user1)
        self.analysis_res1 = database.save_full_analysis(
            user_id=self.user1_id,
            company_id=self.company1_id,
            statement_data=self.sample_statement_user1,
            ratio_data=self.ratios_user1,
            db_path=self.db_path,
        )
        self.analysis1_id = self.analysis_res1["analysis_id"]

    def tearDown(self):
        """Clean up test database file."""
        if os.path.exists(self.db_path):
            try:
                os.remove(self.db_path)
            except Exception:
                pass

    def test_pdf_generation_bytes_and_structure(self):
        """Test that generate_pdf_report outputs valid PDF bytes with header, scorecard, and ratios."""
        company = database.get_company(self.company1_id, self.user1_id, db_path=self.db_path)
        statement = database.get_statement(self.analysis_res1["statement_id"], self.user1_id, db_path=self.db_path)
        health = analysis.compute_comprehensive_financial_health(self.ratios_user1)
        user = database.get_user_by_id(self.user1_id, db_path=self.db_path)

        pdf_bytes = pdf_report.generate_pdf_report(
            company=company,
            statement=statement,
            ratios=self.ratios_user1,
            health_eval=health,
            user=user,
        )

        self.assertIsInstance(pdf_bytes, bytes)
        self.assertTrue(len(pdf_bytes) > 10000, "PDF size should be substantial (at least 10 KB)")
        # PDF binary starts with standard %PDF magic bytes
        self.assertTrue(pdf_bytes.startswith(b"%PDF-"), "Generated file must start with %PDF- header")
        # PDF ends with %%EOF
        self.assertTrue(b"%%EOF" in pdf_bytes[-1024:], "Generated file must contain %%EOF marker")

    def test_indian_currency_and_ratio_formatting(self):
        """Verify Indian currency notation (₹), comma groupings, and ratio units."""
        sym = pdf_report.CURRENCY_SYMBOL
        self.assertEqual(pdf_report.format_inr(0), f"{sym} 0")
        self.assertEqual(pdf_report.format_inr(1234567), f"{sym} 12,34,567")
        self.assertEqual(pdf_report.format_inr(-500000), f"-{sym} 5,00,000")
        self.assertEqual(pdf_report.format_inr(25000000, compact=True), f"{sym} 2.50 Cr")
        self.assertEqual(pdf_report.format_inr(450000, compact=True), f"{sym} 4.50 Lakh")

        # Ratio formatting
        self.assertEqual(pdf_report.format_ratio_val("current_ratio", 2.0), "2.00x")
        self.assertEqual(pdf_report.format_ratio_val("gross_profit_margin", 40.0), "40.00%")
        self.assertEqual(pdf_report.format_ratio_val("free_cash_flow", 7000000.0), f"{sym} 70,00,000")
        self.assertEqual(pdf_report.format_ratio_val("current_ratio", None), "N/A")

    def test_edge_cases_zero_and_missing_values(self):
        """Test PDF generation with edge cases: N/A ratios, zero revenue, and negative profit."""
        sparse_statement = {
            "financial_year": "FY 2025-26",
            "revenue": 0.0,
            "cost_of_goods_sold": 0.0,
            "gross_profit": 0.0,
            "operating_expenses": 100000.0,
            "operating_income": -100000.0,
            "interest_expense": 0.0,  # Zero denominator for interest coverage
            "tax_expense": 0.0,
            "net_income": -100000.0,  # Negative bottom-line profit
            "current_assets": 50000.0,
            "cash_and_cash_equivalents": 10000.0,
            "inventory": 0.0,
            "total_assets": 200000.0,
            "current_liabilities": 0.0, # Zero denominator for liquidity ratios
            "total_liabilities": 50000.0,
            "total_debt": 0.0,
            "shareholders_equity": 150000.0,
            "opening_inventory": None, # Missing opening average balance
            "closing_inventory": 0.0,
            "opening_total_assets": None,
            "closing_total_assets": 200000.0,
            "operating_cash_flow": -80000.0,
            "capital_expenditure": 20000.0,
            "free_cash_flow": -100000.0,
        }

        ratios = calculations.calculate_all_ratios(sparse_statement)
        # Verify zero denominators return None
        self.assertIsNone(ratios["current_ratio"])
        self.assertIsNone(ratios["interest_coverage"])
        self.assertIsNone(ratios["inventory_turnover"])

        health = analysis.compute_comprehensive_financial_health(ratios)
        company = {"id": 99, "company_name": "Edge Case Corp", "industry": "Technology", "financial_year": "FY 2025-26"}

        # PDF must still generate without crashing or throwing division by zero
        pdf_bytes = pdf_report.generate_pdf_report(
            company=company,
            statement=sparse_statement,
            ratios=ratios,
            health_eval=health,
        )
        self.assertTrue(len(pdf_bytes) > 5000)

    def test_report_generation_counter_and_dashboard_integration(self):
        """Verify mark_report_generated increments report count and reflects in dashboard_summary."""
        # Initial summary before report download
        summary_before = database.dashboard_summary(self.user1_id, db_path=self.db_path)
        self.assertEqual(summary_before["total_reports"], 0)

        # Trigger download event
        reports.record_download_event(self.user1_id, self.analysis1_id)
        # Also run database.mark_report_generated directly with test db path
        database.mark_report_generated(self.user1_id, self.analysis1_id, db_path=self.db_path)

        # Summary after report download
        summary_after = database.dashboard_summary(self.user1_id, db_path=self.db_path)
        self.assertEqual(summary_after["total_reports"], 1)

    def test_multi_user_report_isolation(self):
        """Ensure User 2 cannot access or generate reports for User 1's company."""
        # User 2 attempts to query statements for User 1's company
        u2_statements = database.list_statements(user_id=self.user2_id, company_id=self.company1_id, db_path=self.db_path)
        self.assertEqual(len(u2_statements), 0, "User 2 must not see User 1's statements")

        # User 2 attempts to mark report generated on User 1's analysis
        res = database.mark_report_generated(user_id=self.user2_id, analysis_id=self.analysis1_id, db_path=self.db_path)
        self.assertFalse(res, "User 2 cannot increment report counter on User 1's analysis")

    @patch("streamlit.selectbox")
    @patch("streamlit.metric")
    @patch("streamlit.markdown")
    @patch("streamlit.download_button")
    def test_reports_page_render_simulation(self, mock_dl, mock_md, mock_metric, mock_select):
        """Simulate rendering the reports page with mocked Streamlit components."""
        orig_get_conn = database.get_connection
        with patch("database.get_connection", lambda db_path=None: orig_get_conn(self.db_path)):
            user1 = {"id": self.user1_id, "full_name": "Analyst One", "email": "analyst1@college.edu"}
            mock_select.side_effect = [self.company1_id, "FY 2025-26"]

            reports.render_reports_page(user1)

            # Assert download_button was invoked with PDF data
            self.assertTrue(mock_dl.called, "st.download_button must be rendered for download")
            call_kwargs = mock_dl.call_args[1]
            self.assertEqual(call_kwargs.get("mime"), "application/pdf")
            self.assertTrue(call_kwargs.get("file_name").startswith("Financial_Report_Apex_Motors_Ltd"))


if __name__ == "__main__":
    unittest.main()
