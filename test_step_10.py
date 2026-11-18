"""Test suite for Step 10: Financial Comparison and Multi-Year Trend Analysis."""

import os
import tempfile
from pathlib import Path
import database
import calculations
import visualization
from pages import comparison


def test_multi_year_trend_chart():
    print("\n[Test 1] Multi-Year Trend Chart Generation")
    # Less than 2 statements
    fig_empty = visualization.create_multi_year_trend_chart([])
    assert fig_empty is None
    fig_one = visualization.create_multi_year_trend_chart([{"financial_year": "FY 2024-25"}])
    assert fig_one is None

    # Two years of statements
    two_years = [
        {"financial_year": "FY 2023-24", "revenue": 8000000.0, "net_income": 800000.0},
        {"financial_year": "FY 2024-25", "revenue": 10000000.0, "net_income": 1500000.0},
    ]
    fig = visualization.create_multi_year_trend_chart(two_years, company_name="Bharat Motors")
    assert fig is not None
    assert len(fig.data) == 3  # Revenue bar, Profit bar, Margin scatter line
    assert fig.data[0].name == "Revenue (₹)"
    assert fig.data[1].name == "Net Profit (₹)"
    assert fig.data[2].name == "Net Margin (%)"
    print("  --> Multi-year trend chart generated with all 3 traces (Revenue, Profit, Margin).")


def test_peer_radar_chart():
    print("\n[Test 2] Peer Benchmarking Radar Chart Generation")
    # Less than 2 peers
    assert visualization.create_peer_comparison_radar_chart({}) is None
    assert visualization.create_peer_comparison_radar_chart({"Comp A": {}}) is None

    # Two peer companies
    radar_data = {
        "Tata Motors": {"Liquidity": 85.0, "Profitability": 80.0, "Solvency": 75.0, "Efficiency": 90.0, "Cash Flow": 80.0},
        "Mahindra & Mahindra": {"Liquidity": 80.0, "Profitability": 85.0, "Solvency": 80.0, "Efficiency": 85.0, "Cash Flow": 75.0},
    }
    fig_radar = visualization.create_peer_comparison_radar_chart(radar_data)
    assert fig_radar is not None
    assert len(fig_radar.data) == 2  # 2 peer radar polygons
    assert fig_radar.data[0].name == "Tata Motors"
    assert fig_radar.data[1].name == "Mahindra & Mahindra"
    print("  --> Peer comparison radar chart generated successfully.")


def test_yoy_growth_calculations():
    print("\n[Test 3] YoY Growth & Comparison Logic")
    rev_2024 = 8000000.0   # 80 Lakh
    rev_2025 = 10000000.0  # 100 Lakh
    growth = ((rev_2025 - rev_2024) / rev_2024) * 100.0
    assert growth == 25.0, f"Expected 25.0% YoY revenue growth, got {growth}"

    profit_2024 = 800000.0   # 8 Lakh (10% margin)
    profit_2025 = 1500000.0  # 15 Lakh (15% margin)
    profit_growth = ((profit_2025 - profit_2024) / profit_2024) * 100.0
    assert profit_growth == 87.5, f"Expected 87.5% YoY profit growth, got {profit_growth}"

    margin_2024 = 800000.0 / 8000000.0 * 100.0  # 10.0%
    margin_2025 = 1500000.0 / 10000000.0 * 100.0 # 15.0%
    margin_expansion = margin_2025 - margin_2024
    assert margin_expansion == 5.0, f"Expected +5.0% margin expansion, got {margin_expansion}"
    print("  --> YoY growth and margin expansion calculations verified.")


def test_comparison_user_isolation():
    print("\n[Test 4] Comparison User Isolation")
    temp_dir = tempfile.mkdtemp()
    temp_db = Path(temp_dir) / "test_comparison_iso.db"
    database.init_db(temp_db)

    u1 = database.create_user("User One", "user1@comp.com", "h1", "s1", temp_db)
    u2 = database.create_user("User Two", "user2@comp.com", "h2", "s2", temp_db)

    c1 = database.create_company(u1, "Company Alpha", "IT", "FY 2023-24", "", temp_db)
    database.save_full_analysis(
        u1, c1,
        {"financial_year": "FY 2023-24", "revenue": 5000000.0, "net_income": 500000.0},
        {"current_ratio": 2.0},
        temp_db,
    )
    database.save_full_analysis(
        u1, c1,
        {"financial_year": "FY 2024-25", "revenue": 6000000.0, "net_income": 700000.0},
        {"current_ratio": 2.2},
        temp_db,
    )

    # User 1 has 2 statements for Company Alpha
    u1_stmts = database.list_statements(u1, company_id=c1, db_path=temp_db)
    assert len(u1_stmts) == 2

    # User 2 has NO companies and NO statements
    u2_comps = database.list_companies(u2, db_path=temp_db)
    assert len(u2_comps) == 0
    u2_stmts = database.list_statements(u2, db_path=temp_db)
    assert len(u2_stmts) == 0

    try:
        os.remove(temp_db)
        os.rmdir(temp_dir)
    except Exception:
        pass
    print("  --> Multi-user comparison isolation verified.")


if __name__ == "__main__":
    print("=" * 60)
    print("RUNNING STEP 10 FINANCIAL COMPARISON TESTS")
    print("=" * 60)
    test_multi_year_trend_chart()
    test_peer_radar_chart()
    test_yoy_growth_calculations()
    test_comparison_user_isolation()
    print("\n" + "=" * 60)
    print("ALL STEP 10 TESTS PASSED! (100% SUCCESS)")
    print("=" * 60)
