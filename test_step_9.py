"""Test suite for Step 9: Financial Insights and Rule-Based Interpretation."""

import os
import tempfile
from pathlib import Path
import database
import calculations
import analysis


def test_single_ratio_evaluations():
    print("\n[Test 1] Deterministic Evaluation of Individual Ratios")
    # Current Ratio
    e_cr_high = analysis.evaluate_single_ratio("current_ratio", 2.2)
    assert e_cr_high["status"] == analysis.STATUS_HEALTHY
    assert e_cr_high["badge_color"] == "green"
    assert e_cr_high["score"] == 100.0

    e_cr_mod = analysis.evaluate_single_ratio("current_ratio", 1.5)
    assert e_cr_mod["status"] == analysis.STATUS_MODERATE
    assert e_cr_mod["badge_color"] == "blue"

    e_cr_low = analysis.evaluate_single_ratio("current_ratio", 0.9)
    assert e_cr_low["status"] == analysis.STATUS_ATTENTION
    assert e_cr_low["badge_color"] == "red"

    # Missing / None
    e_cr_none = analysis.evaluate_single_ratio("current_ratio", None)
    assert e_cr_none["status"] == analysis.STATUS_NA
    assert e_cr_none["badge_color"] == "grey"

    # Net Profit Margin
    e_npm_loss = analysis.evaluate_single_ratio("net_profit_margin", -2.5)
    assert e_npm_loss["status"] == analysis.STATUS_ATTENTION
    assert e_npm_loss["badge_color"] == "red"

    e_npm_healthy = analysis.evaluate_single_ratio("net_profit_margin", 18.0)
    assert e_npm_healthy["status"] == analysis.STATUS_HEALTHY

    # Debt-to-Equity
    e_de_healthy = analysis.evaluate_single_ratio("debt_to_equity", 0.5)
    assert e_de_healthy["status"] == analysis.STATUS_HEALTHY

    e_de_high = analysis.evaluate_single_ratio("debt_to_equity", 2.5)
    assert e_de_high["status"] == analysis.STATUS_ATTENTION
    print("  --> Individual ratio evaluations verified against deterministic thresholds.")


def test_comprehensive_health_score():
    print("\n[Test 2] Comprehensive Financial Health Scoring & Categorization")
    # Sample dataset ratios
    sample_stmt = {
        "revenue": 10000000.0,
        "cost_of_goods_sold": 6000000.0,
        "gross_profit": 4000000.0,
        "operating_expenses": 1500000.0,
        "operating_income": 2500000.0,
        "interest_expense": 500000.0,
        "tax_expense": 500000.0,
        "net_income": 1500000.0,
        "current_assets": 3000000.0,
        "cash_and_cash_equivalents": 1000000.0,
        "inventory": 1200000.0,
        "total_assets": 8000000.0,
        "current_liabilities": 1500000.0,
        "total_liabilities": 3500000.0,
        "total_debt": 2000000.0,
        "shareholders_equity": 4500000.0,
        "opening_inventory": 1000000.0,
        "closing_inventory": 1400000.0,
        "opening_total_assets": 7000000.0,
        "closing_total_assets": 9000000.0,
        "operating_cash_flow": 2200000.0,
        "capital_expenditure": 700000.0,
    }
    ratios = calculations.calculate_all_ratios(sample_stmt)
    health = analysis.compute_comprehensive_financial_health(ratios)

    assert health["overall_score"] >= 80.0, f"Expected strong score, got {health['overall_score']}"
    assert health["health_grade"] == "Strong Financial Position"
    assert health["grade_color"] == "green"
    assert "Liquidity" in health["category_scores"]
    assert "Profitability" in health["category_scores"]
    assert "Solvency" in health["category_scores"]
    assert "Efficiency" in health["category_scores"]
    assert "Cash Flow" in health["category_scores"]
    assert len(health["strengths"]) > 0
    print(f"  --> Overall Score: {health['overall_score']}/100 ({health['health_grade']}) PASSED.")


def test_user_data_isolation():
    print("\n[Test 3] User Data Isolation in Insights")
    temp_dir = tempfile.mkdtemp()
    temp_db = Path(temp_dir) / "test_insights_iso.db"
    database.init_db(temp_db)

    u1 = database.create_user("User A", "usera@test.com", "h1", "s1", temp_db)
    u2 = database.create_user("User B", "userb@test.com", "h2", "s2", temp_db)

    c1 = database.create_company(u1, "Company Alpha", "IT", "FY 2024-25", "", temp_db)
    database.save_full_analysis(
        u1, c1,
        {"financial_year": "FY 2024-25", "revenue": 5000000.0, "net_income": 1000000.0},
        {"current_ratio": 2.0},
        temp_db,
    )

    # User 1 statements exist
    stmts_u1 = database.list_statements(u1, db_path=temp_db)
    assert len(stmts_u1) == 1

    # User 2 has NO statements
    stmts_u2 = database.list_statements(u2, db_path=temp_db)
    assert len(stmts_u2) == 0

    # Test that ratios fetched from database (with id, user_id, statement_id, calculated_at timestamp)
    # can be evaluated without ValueError: could not convert string to float
    db_ratios = database.get_ratios(u1, stmts_u1[0]["id"], db_path=temp_db)
    assert db_ratios is not None
    assert "calculated_at" in db_ratios
    health_from_db = analysis.compute_comprehensive_financial_health(db_ratios)
    assert health_from_db is not None
    assert "overall_score" in health_from_db
    print("  --> Evaluated DB ratios with timestamp metadata successfully.")

    try:
        os.remove(temp_db)
        os.rmdir(temp_dir)
    except Exception:
        pass
    print("  --> Data isolation verified: User 2 cannot access User 1's statements or insights.")


if __name__ == "__main__":
    print("=" * 60)
    print("RUNNING STEP 9 FINANCIAL INSIGHTS TESTS")
    print("=" * 60)
    test_single_ratio_evaluations()
    test_comprehensive_health_score()
    test_user_data_isolation()
    print("\n" + "=" * 60)
    print("ALL STEP 9 TESTS PASSED! (100% SUCCESS)")
    print("=" * 60)
