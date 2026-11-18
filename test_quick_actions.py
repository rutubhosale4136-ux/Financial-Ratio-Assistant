"""Test diagnostic script for Quick Action navigation mechanism."""

import main

NAV_ITEMS = main.NAV_ITEMS

def simulate_navigation(target_keyword, session_state):
    # Simulate button click
    session_state["nav_selection"] = target_keyword

    # Simulate next script execution in main.py BEFORE st.radio instantiation
    if "nav_selection" in session_state:
        target = session_state.pop("nav_selection")
        for item in NAV_ITEMS:
            if target in item:
                session_state["sidebar_nav"] = item
                break

    return session_state["sidebar_nav"]


def run_tests():
    print("Testing Quick Action Button Navigation Destinations:")
    session_state = {"sidebar_nav": "📊 Dashboard"}

    # Test 1: Add Company
    dest1 = simulate_navigation("Company Management", session_state)
    assert dest1 == "🏢 Company Management", f"Expected '🏢 Company Management', got '{dest1}'"
    print("  [Button 1: Add Company] ->", dest1, "OK")

    # Test 2: Enter Statement
    dest2 = simulate_navigation("Financial Statements", session_state)
    assert dest2 == "📑 Financial Statements", f"Expected '📑 Financial Statements', got '{dest2}'"
    print("  [Button 2: Enter Statement] ->", dest2, "OK")

    # Test 3: Calculate Ratios
    dest3 = simulate_navigation("Ratio Analysis", session_state)
    assert dest3 == "📈 Ratio Analysis", f"Expected '📈 Ratio Analysis', got '{dest3}'"
    print("  [Button 3: Calculate Ratios] ->", dest3, "OK")

    # Test 4: Generate Report
    dest4 = simulate_navigation("Reports", session_state)
    assert dest4 == "📄 Reports", f"Expected '📄 Reports', got '{dest4}'"
    print("  [Button 4: Generate Report] ->", dest4, "OK")

    # Test 5: Back to Dashboard
    dest5 = simulate_navigation("Dashboard", session_state)
    assert dest5 == "📊 Dashboard", f"Expected '📊 Dashboard', got '{dest5}'"
    print("  [Back to Dashboard] ->", dest5, "OK")

    print("\nAll 5 navigation targets verified!")


if __name__ == "__main__":
    run_tests()
