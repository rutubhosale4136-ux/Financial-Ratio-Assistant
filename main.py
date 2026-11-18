"""Application entry point for Financial Statement Ratio Analysis Assistant.

College Project
This file handles:
1. Streamlit configuration, metadata, and custom styling.
2. SQLite database initialization.
3. Authentication gate (unauthenticated users see login/registration).
4. Professional Sidebar with user account details and navigation menu.
5. Routing to dashboard and placeholder pages for upcoming steps.
6. Clean logout handling.
"""

import streamlit as st
import database
import authentication
from pages import dashboard, companies, financial_statements, ratio_analysis, financial_insights, comparison, reports, history


# Standard sidebar navigation items
NAV_ITEMS = [
    "📊 Dashboard",
    "🏢 Company Management",
    "📑 Financial Statements",
    "📈 Ratio Analysis",
    "💡 Financial Insights",
    "🔄 Financial Comparison",
    "📄 Reports",
    "🕒 Analysis History",
]


def load_custom_css():
    """Load custom CSS stylesheet if present."""
    try:
        with open("assets/style.css", "r", encoding="utf-8") as f:
            css = f.read()
            if css.strip():
                st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass


def render_feature_placeholder(feature_title: str, upcoming_step: str, description: str):
    """Render a clean placeholder for features to be built in subsequent steps."""
    st.markdown(f"## {feature_title}")
    st.markdown(f"<p style='color: #64748B;'>{description}</p>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <div style="background-color: #FFFFFF; border: 1.5px dashed #CBD5E1;
                    border-radius: 12px; padding: 36px 24px; text-align: center; margin-top: 16px;">
            <div style="font-size: 2.5rem; margin-bottom: 12px;">🚧</div>
            <h3 style="color: #1E3A8A; margin-bottom: 8px;">Scheduled for {upcoming_step}</h3>
            <p style="color: #64748B; max-width: 550px; margin: 0 auto 20px auto; font-size: 0.95rem;">
                This module will be fully activated in {upcoming_step} following the project roadmap.
                Please explore the <b>Dashboard</b> in the meantime.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, _ = st.columns([1, 1, 2])
    with col1:
        if st.button("⬅️ Back to Dashboard", use_container_width=True, type="primary"):
            st.session_state["nav_selection"] = "Dashboard"
            st.rerun()


def render_sidebar(user: dict) -> str:
    """Render the professional sidebar with user badge, navigation, and logout."""
    with st.sidebar:
        # App branding in sidebar
        st.markdown(
            """
            <div style="padding-bottom: 14px; border-bottom: 1px solid rgba(255, 255, 255, 0.12); margin-bottom: 16px;">
                <h3 style="color: #FFFFFF; margin: 0; font-size: 1.25rem; font-weight: 700;">📈 Financial Assistant</h3>
                <span style="color: #93C5FD; font-size: 0.8rem; font-weight: 500;">Indian Rupee (₹) Workspace</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # User profile badge
        user_name = user["full_name"]
        user_email = user["email"]
        user_id = user["id"]

        st.markdown(
            f"""
            <div style="background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.14);
                        border-radius: 10px; padding: 12px; margin-bottom: 16px;">
                <div style="font-size: 0.72rem; color: #93C5FD; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">
                    Logged In User
                </div>
                <div style="font-weight: 700; color: #FFFFFF; font-size: 1rem; margin-top: 2px;">
                    {user_name}
                </div>
                <div style="font-size: 0.8rem; color: #CBD5E1;">
                    {user_email}
                </div>
                <div style="display: inline-block; background-color: #2878D0; color: #FFFFFF;
                            font-size: 0.72rem; font-weight: 600; padding: 2px 8px; border-radius: 10px; margin-top: 6px;">
                    Account #{user_id}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<p style='font-size: 0.75rem; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px;'>NAVIGATION</p>", unsafe_allow_html=True)

        # Check if programmatic navigation was requested (e.g. Quick Action buttons)
        # We update sidebar_nav HERE before st.radio is instantiated on this script run
        if "nav_selection" in st.session_state:
            target = st.session_state.pop("nav_selection")
            for item in NAV_ITEMS:
                if target in item:
                    st.session_state["sidebar_nav"] = item
                    break

        # Default navigation selection
        if "sidebar_nav" not in st.session_state:
            st.session_state["sidebar_nav"] = "📊 Dashboard"

        # Sidebar radio navigation (controlled cleanly by st.session_state["sidebar_nav"])
        selection = st.radio(
            "Navigation Menu",
            NAV_ITEMS,
            label_visibility="collapsed",
            key="sidebar_nav",
        )

        st.markdown("---")

        # Logout button
        if st.button("🚪 Log Out", use_container_width=True, type="secondary"):
            authentication.logout()

        # Footer
        st.markdown(
            """
            <div style="text-align: center; color: #94A3B8; font-size: 0.75rem; margin-top: 20px;">
                Financial Ratio Assistant &bull; v1.0<br>Standard April&ndash;March FY
            </div>
            """,
            unsafe_allow_html=True,
        )

        return selection


def navigate_to(page_keyword: str):
    """Callback to switch navigation page safely from buttons without widget key conflict."""
    st.session_state["nav_selection"] = page_keyword
    st.rerun()


def main():
    # Streamlit page configuration
    st.set_page_config(
        page_title="Financial Statement Ratio Analysis Assistant",
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Initialize permanent SQLite tables
    database.init_db()

    # Load white & navy CSS
    load_custom_css()

    # Authentication Gate
    if not authentication.is_authenticated():
        authentication.render_auth_page()
        return

    # Authenticated user session
    current_user = authentication.get_current_user()

    # Render sidebar navigation
    selected_page = render_sidebar(current_user)

    # Page Routing
    if "Dashboard" in selected_page:
        dashboard.render_dashboard(current_user, on_navigate_callback=navigate_to)
    elif "Company Management" in selected_page:
        companies.render_companies_page(current_user)
    elif "Financial Statements" in selected_page:
        financial_statements.render_statements_page(current_user)
    elif "Ratio Analysis" in selected_page:
        ratio_analysis.render_ratio_analysis_page(current_user)
    elif "Financial Insights" in selected_page:
        financial_insights.render_financial_insights_page(current_user)
    elif "Financial Comparison" in selected_page:
        comparison.render_comparison_page(current_user)
    elif "Reports" in selected_page:
        reports.render_reports_page(current_user)
    elif "Analysis History" in selected_page:
        history.render_history_page(current_user, on_navigate_callback=navigate_to)


if __name__ == "__main__":
    main()
