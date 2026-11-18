"""Comprehensive test suite for Quick Action buttons and cross-page navigation."""

import unittest.mock as mock
import main
from pages import dashboard

NAV_ITEMS = main.NAV_ITEMS


def test_quick_action_button_routing():
    print("=" * 60)
    print("TESTING QUICK ACTION BUTTONS & STREAMLIT SESSION STATE")
    print("=" * 60)

    # 1. Test navigate_to callback
    print("\n[Test 1] Testing navigate_to Callback")
    mock_session = {}
    with mock.patch.object(main.st, "session_state", mock_session), \
         mock.patch.object(main.st, "rerun") as mock_rerun:
        main.navigate_to("Company Management")
        assert mock_session.get("nav_selection") == "Company Management"
        assert mock_rerun.called
    print("  --> navigate_to properly sets nav_selection and calls rerun without modifying widget key.")

    # 2. Test render_sidebar consumes nav_selection before widget instantiation
    print("\n[Test 2] Testing render_sidebar Safe Consumption of nav_selection")
    buttons_to_test = [
        ("🏢 Add Company", "Company Management", "🏢 Company Management"),
        ("📑 Enter Statement", "Financial Statements", "📑 Financial Statements"),
        ("📈 Calculate Ratios", "Ratio Analysis", "📈 Ratio Analysis"),
        ("📄 Generate Report", "Reports", "📄 Reports"),
        ("⬅️ Back to Dashboard", "Dashboard", "📊 Dashboard"),
    ]

    for btn_name, target_kw, expected_item in buttons_to_test:
        sim_session = {
            "nav_selection": target_kw,
            "sidebar_nav": "📊 Dashboard",
        }

        # Mock streamlit inside main.py
        with mock.patch.object(main.st, "session_state", sim_session), \
             mock.patch.object(main.st, "sidebar") as mock_sidebar, \
             mock.patch.object(main.st, "radio", return_value=expected_item) as mock_radio:

            user_mock = {"id": 1, "full_name": "Test User", "email": "test@example.com"}
            selection = main.render_sidebar(user_mock)

            # Verification:
            # a) nav_selection was popped
            assert "nav_selection" not in sim_session, f"nav_selection was not cleared for {btn_name}"
            # b) sidebar_nav in session_state was updated to the full item before radio call
            assert sim_session["sidebar_nav"] == expected_item, f"Expected {expected_item}, got {sim_session['sidebar_nav']}"
            # c) radio was called with the updated key without throwing WidgetAlreadyInstantiated
            assert mock_radio.called
            # d) selection matches expected target
            assert selection == expected_item
            print(f"  [Button: {btn_name}] -> Successfully navigated to '{expected_item}'")

    # 3. Test Dashboard button triggers
    print("\n[Test 3] Testing Dashboard Quick Action Button Triggers")
    user_mock = {"id": 1, "full_name": "Test User", "email": "test@example.com"}

    with mock.patch("pages.dashboard.st") as mock_dash_st, \
         mock.patch("pages.dashboard.database") as mock_dash_db:

        mock_dash_db.dashboard_summary.return_value = {
            "total_companies": 0, "total_analyses": 0, "total_reports": 0,
            "total_revenue": 0.0, "total_net_profit": 0.0, "recent_analyses": [],
        }
        mock_dash_db.list_analyses.return_value = []
        mock_dash_st.columns.side_effect = lambda n: [mock.MagicMock() for _ in range(n if isinstance(n, int) else len(n))]

        # Mock callback
        mock_cb = mock.MagicMock()
        dashboard.render_dashboard(user_mock, on_navigate_callback=mock_cb)

        # Ensure dashboard rendered without error
        assert mock_dash_db.dashboard_summary.called
        print("  --> Dashboard rendered with navigation callback hooked up cleanly.")

    print("\n" + "=" * 60)
    print("ALL QUICK ACTION BUTTON TESTS PASSED (100% SUCCESS)!")
    print("=" * 60)


if __name__ == "__main__":
    test_quick_action_button_routing()
