"""Automated test suite for Step 5: Professional Dashboard and Indian Financial Formatting."""

import os
import tempfile
import unittest.mock as mock
from pathlib import Path
import database
import authentication
import visualization
from pages import dashboard


def test_indian_formatting():
    print("\n[Test 1] Indian Currency & Date Formatting")
    # Currency tests
    assert dashboard.format_indian_currency(0) == "₹ 0"
    assert dashboard.format_indian_currency(None) == "₹ 0"
    assert dashboard.format_indian_currency(500) == "₹ 500"
    assert dashboard.format_indian_currency(1500) == "₹ 1,500"
    assert dashboard.format_indian_currency(150000) == "₹ 1,50,000"
    assert dashboard.format_indian_currency(150000, compact=True) == "₹ 1.50 Lakh"
    assert dashboard.format_indian_currency(12500000) == "₹ 1,25,00,000"
    assert dashboard.format_indian_currency(12500000, compact=True) == "₹ 1.25 Cr"
    assert dashboard.format_indian_currency(-450000) == "-₹ 4,50,000"
    assert dashboard.format_indian_currency(-450000, compact=True) == "-₹ 4.50 Lakh"
    assert dashboard.format_indian_currency(12345678.50) == "₹ 1,23,45,678.50"

    # Date formatting tests
    assert dashboard.format_indian_date("2026-11-15 16:46:36") == "15-11-2026"
    assert dashboard.format_indian_date("2026-04-01") == "01-04-2026"
    assert dashboard.format_indian_date(None) == "N/A"
    print("  --> Indian currency (₹, Lakhs/Crores) and date (DD-MM-YYYY) tests PASSED.")


def test_database_dashboard_summary():
    print("\n[Test 2] Database dashboard_summary with Financial Aggregates")
    temp_dir = tempfile.mkdtemp()
    temp_db = Path(temp_dir) / "test_dash.db"
    database.init_db(temp_db)

    # Register 2 users
    u1 = database.create_user("Asha Rao", "asha@dash.com", "hash1", "salt1", temp_db)
    u2 = database.create_user("Rohan Gupta", "rohan@dash.com", "hash2", "salt2", temp_db)

    # Initially both users have 0 records
    sum1_empty = database.dashboard_summary(u1, temp_db)
    assert sum1_empty["total_companies"] == 0
    assert sum1_empty["total_analyses"] == 0
    assert sum1_empty["total_reports"] == 0
    assert sum1_empty["total_revenue"] == 0.0
    assert sum1_empty["total_net_profit"] == 0.0
    assert sum1_empty["recent_analyses"] == []

    # User 1 creates a company and financial statement
    c1 = database.create_company(u1, "Reliance Textiles", "Manufacturing", "FY 2024-25", "", temp_db)
    database.save_full_analysis(
        u1,
        c1,
        {"financial_year": "FY 2024-25", "revenue": 5000000.0, "net_income": 750000.0},
        {"current_ratio": 2.1, "net_profit_margin": 15.0},
        temp_db,
    )

    # User 1 summary must reflect the saved amounts
    sum1 = database.dashboard_summary(u1, temp_db)
    assert sum1["total_companies"] == 1
    assert sum1["total_analyses"] == 1
    assert sum1["total_revenue"] == 5000000.0
    assert sum1["total_net_profit"] == 750000.0
    assert len(sum1["recent_analyses"]) == 1
    assert sum1["recent_analyses"][0]["company_name"] == "Reliance Textiles"

    # User 2 must STILL have 0 records (Strict Isolation)
    sum2 = database.dashboard_summary(u2, temp_db)
    assert sum2["total_companies"] == 0
    assert sum2["total_analyses"] == 0
    assert sum2["total_revenue"] == 0.0
    assert sum2["total_net_profit"] == 0.0
    assert sum2["recent_analyses"] == []
    print("  --> Database summary, aggregates, and user isolation PASSED.")

    # Clean up
    try:
        os.remove(temp_db)
        os.rmdir(temp_dir)
    except Exception:
        pass


def test_visualization_charts():
    print("\n[Test 3] Plotly Performance Chart Generation")
    # Empty records
    empty_fig = visualization.create_performance_overview_chart([])
    assert empty_fig is None

    # Sample records
    sample_data = [
        {
            "company_name": "Bharat Electronics",
            "financial_year": "FY 2024-25",
            "total_revenue": 12000000.0,
            "net_profit": 2400000.0,
        },
        {
            "company_name": "Tata Motors",
            "financial_year": "FY 2024-25",
            "total_revenue": 45000000.0,
            "net_profit": 6000000.0,
        },
    ]
    fig = visualization.create_performance_overview_chart(sample_data)
    assert fig is not None
    assert len(fig.data) == 2  # Revenue and Net Profit traces
    assert fig.data[0].name == "Total Revenue (₹)"
    assert fig.data[1].name == "Net Profit (₹)"
    print("  --> Plotly chart generation & styling PASSED.")


def test_dashboard_render_simulation():
    print("\n[Test 4] Dashboard Render Execution Simulation")
    # Simulate render_dashboard for a mock user using mocks for streamlit UI calls
    mock_user = {"id": 1, "full_name": "Ruturaj Bhosale", "email": "rutu522@gmail.com"}

    with mock.patch("pages.dashboard.st") as mock_st, \
         mock.patch("pages.dashboard.database") as mock_db, \
         mock.patch("pages.dashboard.visualization") as mock_viz:

        # Mock database return for 0 records
        mock_db.dashboard_summary.return_value = {
            "total_companies": 0,
            "total_analyses": 0,
            "total_reports": 0,
            "total_revenue": 0.0,
            "total_net_profit": 0.0,
            "recent_analyses": [],
        }
        mock_db.list_analyses.return_value = []
        mock_st.columns.side_effect = lambda n: [mock.MagicMock() for _ in range(n if isinstance(n, int) else len(n))]

        # Call render_dashboard for empty state
        dashboard.render_dashboard(mock_user)
        assert mock_db.dashboard_summary.called

        # Mock database return with 1 analysis
        mock_db.dashboard_summary.return_value = {
            "total_companies": 1,
            "total_analyses": 1,
            "total_reports": 0,
            "total_revenue": 1000000.0,
            "total_net_profit": 150000.0,
            "recent_analyses": [{
                "company_name": "Test Co",
                "financial_year": "FY 2025-26",
                "analysis_date": "2026-11-15",
                "total_revenue": 1000000.0,
                "net_profit": 150000.0,
                "ratios_calculated": 10,
                "report_generated": 0,
            }],
        }
        mock_db.list_analyses.return_value = [{
            "company_name": "Test Co",
            "financial_year": "FY 2025-26",
            "total_revenue": 1000000.0,
            "net_profit": 150000.0,
        }]
        dashboard.render_dashboard(mock_user)
        print("  --> Dashboard render simulation (both empty and populated states) PASSED.")


if __name__ == "__main__":
    print("=" * 60)
    print("RUNNING STEP 5 PROFESSIONAL DASHBOARD VERIFICATION TESTS")
    print("=" * 60)
    test_indian_formatting()
    test_database_dashboard_summary()
    test_visualization_charts()
    test_dashboard_render_simulation()
    print("\n" + "=" * 60)
    print("ALL STEP 5 TESTS PASSED SUCCESSFULLY! (100% PASS)")
    print("=" * 60)
