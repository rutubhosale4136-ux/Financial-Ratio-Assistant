"""Professional Financial Analytics Dashboard.

College Project: Financial Statement Ratio Analysis Assistant
This module renders the Step 5 professional dashboard:
- White and navy-blue theme
- User welcome header
- Indian financial formatting (INR ₹, Lakhs/Crores, DD-MM-YYYY, April-March FY)
- Summary metric cards (Companies, Analyses, Reports, Revenue, Net Profit)
- Interactive Plotly performance charts (with informative empty states)
- Recent financial analyses table
- Quick action navigation cards
- Strict user data isolation
"""

import pandas as pd
import streamlit as st
import database
import visualization


# ============================================================================
# Indian Financial Formatting Helpers
# ============================================================================

def format_indian_currency(amount, compact=False) -> str:
    """Format numeric values into Indian Rupee (₹) format with Indian comma grouping.

    Follows the 3,2,2 grouping convention (e.g., ₹ 12,34,567).
    When compact=True:
        >= 1,00,00,000 -> ₹ X.XX Cr
        >= 1,00,000    -> ₹ X.XX Lakh
    """
    if amount is None:
        return "₹ 0"
    try:
        val = float(amount)
    except (ValueError, TypeError):
        return "₹ 0"

    sign = "-" if val < 0 else ""
    abs_val = abs(val)

    if compact:
        if abs_val >= 10_000_000:
            return f"{sign}₹ {abs_val / 10_000_000:.2f} Cr"
        elif abs_val >= 100_000:
            return f"{sign}₹ {abs_val / 100_000:.2f} Lakh"

    # Full Indian comma grouping
    parts = f"{abs_val:.2f}".split(".")
    integer_part, decimal_part = parts[0], parts[1]

    if len(integer_part) <= 3:
        formatted = integer_part
    else:
        last_three = integer_part[-3:]
        remaining = integer_part[:-3]
        groups = []
        while len(remaining) > 2:
            groups.insert(0, remaining[-2:])
            remaining = remaining[:-2]
        if remaining:
            groups.insert(0, remaining)
        formatted = ",".join(groups) + "," + last_three

    result = f"{formatted}" if decimal_part == "00" else f"{formatted}.{decimal_part}"
    return f"{sign}₹ {result}"


def format_indian_date(date_str) -> str:
    """Format ISO or SQLite date string to Indian DD-MM-YYYY format."""
    if not date_str:
        return "N/A"
    try:
        clean_date = str(date_str).strip().split(" ")[0]
        parts = clean_date.split("-")
        if len(parts) == 3 and len(parts[0]) == 4:
            return f"{parts[2]}-{parts[1]}-{parts[0]}"
        return str(date_str)
    except Exception:
        return str(date_str)


# ============================================================================
# Dashboard Render Function
# ============================================================================

def render_dashboard(user: dict, on_navigate_callback=None):
    """Render the full professional dashboard for the authenticated user.

    Args:
        user: Authenticated user dictionary from session state.
        on_navigate_callback: Optional callable(target_page_name) to switch screens.
    """
    user_id = user["id"]
    user_name = user["full_name"]
    user_email = user["email"]

    # 1. Fetch user-scoped financial data from database
    summary = database.dashboard_summary(user_id)
    recent_analyses = summary.get("recent_analyses") or []

    # ------------------------------------------------------------------------
    # 1. Welcome Header Banner
    # ------------------------------------------------------------------------
    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, #142B4A 0%, #1D3D66 50%, #2878D0 100%);
                    color: white; padding: 24px 28px; border-radius: 14px; margin-bottom: 24px;
                    box-shadow: 0 4px 14px rgba(20, 43, 74, 0.12);">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <div>
                    <h2 style="color: #FFFFFF; margin: 0 0 6px 0; font-weight: 700; font-size: 1.75rem;">
                        Welcome back, {user_name}! 👋
                    </h2>
                    <p style="color: #E2E8F0; margin: 0; font-size: 0.95rem;">
                        Financial Statement Ratio Analysis Assistant &bull; Indian Rupee (₹) Financial Workspace
                    </p>
                </div>
                <div style="text-align: right; margin-top: 8px;">
                    <span style="background: rgba(255, 255, 255, 0.18); padding: 6px 14px;
                                 border-radius: 20px; font-size: 0.82rem; font-weight: 600; border: 1px solid rgba(255, 255, 255, 0.25);">
                        Account #{user_id} &bull; {user_email}
                    </span>
                    <div style="color: #93C5FD; font-size: 0.8rem; margin-top: 6px; font-weight: 500;">
                        Standard Indian FY: April 1 &ndash; March 31
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ------------------------------------------------------------------------
    # 2. Key Metrics - Primary Counters
    # ------------------------------------------------------------------------
    st.markdown("### 📌 Workspace Highlights")
    m_col1, m_col2, m_col3 = st.columns(3)

    with m_col1:
        st.markdown('<div class="kpi-card kpi-blue">', unsafe_allow_html=True)
        st.metric(
            label="🏢 Total Companies Analyzed",
            value=summary["total_companies"],
            help="Total companies registered under your account.",
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with m_col2:
        st.markdown('<div class="kpi-card kpi-teal">', unsafe_allow_html=True)
        st.metric(
            label="📊 Total Financial Analyses",
            value=summary["total_analyses"],
            help="Total completed financial ratio analyses saved in SQLite.",
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with m_col3:
        st.markdown('<div class="kpi-card kpi-purple">', unsafe_allow_html=True)
        st.metric(
            label="📑 PDF Reports Generated",
            value=summary["total_reports"],
            help="Total official PDF analysis reports downloaded.",
        )
        st.markdown('</div>', unsafe_allow_html=True)

    # ------------------------------------------------------------------------
    # 3. Key Metrics - Financial Totals (INR ₹)
    # ------------------------------------------------------------------------
    st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
    f_col1, f_col2, f_col3 = st.columns(3)

    total_revenue = summary.get("total_revenue", 0.0)
    total_profit = summary.get("total_net_profit", 0.0)

    # Calculate average profit margin if revenue > 0
    margin_pct = (total_profit / total_revenue * 100) if total_revenue > 0 else 0.0

    with f_col1:
        st.markdown('<div class="kpi-card kpi-blue">', unsafe_allow_html=True)
        st.metric(
            label="💰 Total Revenue Tracked",
            value=format_indian_currency(total_revenue, compact=True),
            delta=f"Full: {format_indian_currency(total_revenue, compact=False)}" if total_revenue > 0 else None,
            delta_color="off",
            help="Cumulative revenue recorded across all your financial statements.",
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with f_col2:
        st.markdown('<div class="kpi-card kpi-green">', unsafe_allow_html=True)
        st.metric(
            label="📈 Total Net Profit",
            value=format_indian_currency(total_profit, compact=True),
            delta=f"Full: {format_indian_currency(total_profit, compact=False)}" if total_profit != 0 else None,
            delta_color="normal" if total_profit >= 0 else "inverse",
            help="Cumulative net profit recorded across all your financial statements.",
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with f_col3:
        st.markdown('<div class="kpi-card kpi-amber">', unsafe_allow_html=True)
        st.metric(
            label="🎯 Overall Net Profit Margin",
            value=f"{margin_pct:.2f}%" if total_revenue > 0 else "0.00%",
            delta="Healthy (≥ 10%)" if margin_pct >= 10.0 else ("Low (< 10%)" if total_revenue > 0 else None),
            delta_color="normal" if margin_pct >= 10.0 else "inverse",
            help="Aggregate net profit margin across tracked statements.",
        )
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # ------------------------------------------------------------------------
    # 4. Quick Action Buttons
    # ------------------------------------------------------------------------
    st.markdown("### ⚡ Quick Actions")
    q_col1, q_col2, q_col3, q_col4 = st.columns(4)

    with q_col1:
        if st.button("🏢 Add Company", use_container_width=True, type="secondary"):
            if on_navigate_callback:
                on_navigate_callback("Company Management")
            else:
                st.session_state["nav_selection"] = "Company Management"
                st.rerun()

    with q_col2:
        if st.button("📑 Enter Statement", use_container_width=True, type="secondary"):
            if on_navigate_callback:
                on_navigate_callback("Financial Statements")
            else:
                st.session_state["nav_selection"] = "Financial Statements"
                st.rerun()

    with q_col3:
        if st.button("📈 Calculate Ratios", use_container_width=True, type="secondary"):
            if on_navigate_callback:
                on_navigate_callback("Ratio Analysis")
            else:
                st.session_state["nav_selection"] = "Ratio Analysis"
                st.rerun()

    with q_col4:
        if st.button("📄 Generate Report", use_container_width=True, type="secondary"):
            if on_navigate_callback:
                on_navigate_callback("Reports")
            else:
                st.session_state["nav_selection"] = "Reports"
                st.rerun()

    st.markdown("---")

    # ------------------------------------------------------------------------
    # 5. Financial Performance Charts (Plotly)
    # ------------------------------------------------------------------------
    st.markdown("### 📊 Financial Performance Overview")

    all_analyses = database.list_analyses(user_id)

    if all_analyses and len(all_analyses) > 0:
        fig = visualization.create_performance_overview_chart(all_analyses)
        if fig is not None:
            st.plotly_chart(fig, use_container_width=True)
    else:
        # Informative Empty State for Performance Charts
        st.markdown(
            """
            <div style="background-color: #FFFFFF; border: 1.5px dashed #CBD5E1;
                        border-radius: 10px; padding: 32px 24px; text-align: center; margin-bottom: 20px;">
                <div style="font-size: 2.2rem; margin-bottom: 10px;">📊</div>
                <h4 style="color: #1E3A8A; margin-bottom: 6px; font-weight: 600;">No Financial Records to Display</h4>
                <p style="color: #64748B; max-width: 580px; margin: 0 auto 16px auto; font-size: 0.95rem;">
                    Once you add companies and input financial figures in <b>Company Management & Financial Statements</b>,
                    interactive Plotly charts comparing Revenue, Net Profit, and Ratios in Indian Rupees (₹) will appear here automatically.
                </p>
                <span style="display: inline-block; background-color: #EFF6FF; color: #1E40AF;
                             font-size: 0.85rem; font-weight: 500; padding: 6px 16px; border-radius: 20px;">
                    Ready for Data &bull; Database Scoped to Account #{}
                </span>
            </div>
            """.format(user_id),
            unsafe_allow_html=True,
        )

    # ------------------------------------------------------------------------
    # 6. Recent Financial Analyses Section
    # ------------------------------------------------------------------------
    st.markdown("### 🕒 Recent Financial Analyses")

    if recent_analyses and len(recent_analyses) > 0:
        # Prepare structured display table
        table_rows = []
        for row in recent_analyses:
            table_rows.append({
                "Company Name": row.get("company_name", "N/A"),
                "Financial Year": row.get("financial_year", "N/A"),
                "Analysis Date": format_indian_date(row.get("analysis_date")),
                "Total Revenue": format_indian_currency(row.get("total_revenue")),
                "Net Profit": format_indian_currency(row.get("net_profit")),
                "Ratios Computed": f"{row.get('ratios_calculated', 0)} Ratios",
                "Reports": f"{row.get('report_generated', 0)} Generated",
            })
        df_recent = pd.DataFrame(table_rows)
        st.dataframe(df_recent, use_container_width=True, hide_index=True)
    else:
        # Clean Empty State for Recent Analyses
        st.markdown(
            """
            <div style="background-color: #FFFFFF; border: 1px solid #E2E8F0;
                        border-radius: 10px; padding: 24px; text-align: center;">
                <p style="color: #64748B; margin: 0; font-size: 0.95rem;">
                    ℹ️ No recent analyses found. Saved ratio calculations and performance insights will be cataloged here.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )


