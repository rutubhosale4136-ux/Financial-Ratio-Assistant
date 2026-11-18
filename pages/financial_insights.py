"""Financial Insights Module.

College Project: Financial Statement Ratio Analysis Assistant
This module implements Step 9:
- Rule-based financial interpretation (Healthy, Moderate, Needs Attention, Not Available)
- Comprehensive financial health score (0 to 100%) across 5 core pillars
- Key Strengths and Critical Areas of Concern
- Actionable recommendations tailored to Indian corporate benchmarks
- Strict user data isolation
"""

import pandas as pd
import streamlit as st
import database
import calculations
import analysis
from pages.dashboard import format_indian_currency, format_indian_date


CATEGORIES = [
    ("💧 Liquidity", "Liquidity", ["current_ratio", "quick_ratio", "cash_ratio"]),
    ("📈 Profitability", "Profitability", ["gross_profit_margin", "net_profit_margin", "return_on_assets", "return_on_equity"]),
    ("🛡️ Solvency", "Solvency", ["debt_to_equity", "debt_ratio", "interest_coverage"]),
    ("⚙️ Efficiency", "Efficiency", ["inventory_turnover", "asset_turnover"]),
    ("💸 Cash Flow", "Cash Flow", ["operating_cash_flow_ratio", "free_cash_flow"]),
]


def render_financial_insights_page(user: dict):
    """Render the Financial Insights and rule-based interpretation screen."""
    user_id = user["id"]

    st.markdown(
        """
        <div style="margin-bottom: 20px;">
            <h1 style="color: #142B4A; font-weight: 700; margin-bottom: 4px;">
                💡 Financial Insights & Interpretation
            </h1>
            <p style="color: #5A6E85; font-size: 1rem; margin: 0;">
                Deterministic rule-based diagnosis of corporate financial health, operational efficiency, and risk factors.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 1. Fetch statements
    statements = database.list_statements(user_id)
    if not statements:
        st.info(
            "ℹ️ **No Financial Statements Found:** To view financial insights, "
            "please enter company statement data under **📑 Financial Statements**."
        )
        if st.button("📑 Enter Financial Statements", type="primary"):
            st.session_state["nav_selection"] = "Financial Statements"
            st.rerun()
        return

    # 2. Company & Financial Year Selection
    companies_lookup = {c["id"]: c for c in database.list_companies(user_id)}

    statement_labels = []
    statement_map = {}
    for s in statements:
        c_info = companies_lookup.get(s["company_id"])
        c_name = c_info["company_name"] if c_info else f"Company #{s['company_id']}"
        label = f"{c_name} &bull; {s['financial_year']} (ID #{s['id']})"
        statement_labels.append(label)
        statement_map[label] = s

    col_sel1, col_sel2 = st.columns([2, 1])
    with col_sel1:
        selected_label = st.selectbox(
            "Select Company & Financial Year for Diagnosis *",
            statement_labels,
            key="insights_statement_select",
        )
        active_statement = statement_map[selected_label]
        statement_id = active_statement["id"]
        active_company_id = active_statement["company_id"]
        active_company = companies_lookup.get(active_company_id, {})

    with col_sel2:
        st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
        st.caption(
            f"**Industry:** {active_company.get('industry', 'N/A')}<br>"
            f"**Evaluation Type:** Deterministic Rule-Based System",
            unsafe_allow_html=True,
        )

    # 3. Retrieve or calculate ratios
    ratios = database.get_ratios(user_id, statement_id)
    if not ratios:
        ratios = calculations.calculate_all_ratios(active_statement)

    # 4. Generate Comprehensive Health Evaluation
    health_report = analysis.compute_comprehensive_financial_health(ratios)
    overall_score = health_report["overall_score"]
    health_grade = health_report["health_grade"]
    cat_scores = health_report["category_scores"]
    strengths = health_report["strengths"]
    concerns = health_report["concerns"]
    all_evals = health_report["all_evaluations"]

    # Grade styling
    badge_bg = {
        "green": "#DCFCE7",
        "blue": "#DBEAFE",
        "orange": "#FEF3C7",
        "red": "#FEE2E2",
    }.get(health_report["grade_color"], "#F1F5F9")

    badge_fg = {
        "green": "#166534",
        "blue": "#1E40AF",
        "orange": "#92400E",
        "red": "#991B1B",
    }.get(health_report["grade_color"], "#0F172A")

    st.markdown("---")

    # ------------------------------------------------------------------------
    # EXECUTIVE FINANCIAL HEALTH SCORECARD
    # ------------------------------------------------------------------------
    st.markdown(
        f"""
        <div style="background-color: #FFFFFF; border: 1px solid #E2E8F0; border-left: 5px solid #2878D0; border-radius: 12px;
                    padding: 24px; margin-bottom: 24px; box-shadow: 0 2px 8px rgba(20, 43, 74, 0.04);">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <div>
                    <span style="color: #64748B; font-size: 0.82rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">
                        Executive Summary &bull; {active_company.get('company_name', 'Company')} ({active_statement['financial_year']})
                    </span>
                    <h2 style="color: #142B4A; margin: 4px 0 6px 0; font-weight: 800; font-size: 1.65rem;">
                        Overall Health Score: {overall_score} / 100
                    </h2>
                    <span style="background-color: {badge_bg}; color: {badge_fg}; font-size: 0.9rem;
                                 font-weight: 700; padding: 4px 14px; border-radius: 16px;">
                        {health_grade}
                    </span>
                </div>
                <div style="text-align: right; margin-top: 8px;">
                    <div style="color: #64748B; font-size: 0.85rem; font-weight: 500;">Evaluation Basis</div>
                    <div style="font-weight: 700; color: #142B4A; font-size: 0.95rem;">
                        14 Standard Financial Ratios
                    </div>
                    <div style="font-size: 0.8rem; color: #20A46B; font-weight: 600;">
                        Deterministic Financial Logic
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 5 Pillar Progress Cards
    p_col1, p_col2, p_col3, p_col4, p_col5 = st.columns(5)
    with p_col1:
        st.markdown('<div class="kpi-card kpi-blue">', unsafe_allow_html=True)
        st.metric("💧 Liquidity", f"{cat_scores.get('Liquidity', 0.0)}%", help="Ability to meet short-term commitments.")
        st.markdown('</div>', unsafe_allow_html=True)
    with p_col2:
        st.markdown('<div class="kpi-card kpi-green">', unsafe_allow_html=True)
        st.metric("📈 Profitability", f"{cat_scores.get('Profitability', 0.0)}%", help="Margin strength & capital returns.")
        st.markdown('</div>', unsafe_allow_html=True)
    with p_col3:
        st.markdown('<div class="kpi-card kpi-purple">', unsafe_allow_html=True)
        st.metric("🛡️ Solvency", f"{cat_scores.get('Solvency', 0.0)}%", help="Long-term debt safety & leverage.")
        st.markdown('</div>', unsafe_allow_html=True)
    with p_col4:
        st.markdown('<div class="kpi-card kpi-teal">', unsafe_allow_html=True)
        st.metric("⚙️ Efficiency", f"{cat_scores.get('Efficiency', 0.0)}%", help="Asset and inventory velocity.")
        st.markdown('</div>', unsafe_allow_html=True)
    with p_col5:
        st.markdown('<div class="kpi-card kpi-amber">', unsafe_allow_html=True)
        st.metric("💸 Cash Flow", f"{cat_scores.get('Cash Flow', 0.0)}%", help="Core cash backing and Free Cash Flow.")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # ------------------------------------------------------------------------
    # STRENGTHS & VULNERABILITIES CALLOUTS
    # ------------------------------------------------------------------------
    h_col1, h_col2 = st.columns(2)

    with h_col1:
        st.markdown("### 🏆 Key Financial Strengths")
        if strengths:
            for s in strengths[:4]:
                st.markdown(
                    f"""
                    <div style="background-color: #F0FDF4; border-left: 4px solid #10B981; border-radius: 6px;
                                padding: 12px 16px; margin-bottom: 12px;">
                        <div style="font-weight: 700; color: #166534; font-size: 0.95rem;">
                            ✓ {s['name']}: {s['headline']}
                        </div>
                        <div style="color: #374151; font-size: 0.85rem; margin-top: 4px;">
                            {s['detailed_insight']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        else:
            st.info("ℹ️ No dominant outlier strengths identified for this statement.")

    with h_col2:
        st.markdown("### ⚠️ Areas Requiring Attention")
        if concerns:
            for c in concerns[:4]:
                st.markdown(
                    f"""
                    <div style="background-color: #FEF2F2; border-left: 4px solid #EF4444; border-radius: 6px;
                                padding: 12px 16px; margin-bottom: 12px;">
                        <div style="font-weight: 700; color: #991B1B; font-size: 0.95rem;">
                            ⚠ {c['name']}: {c['headline']}
                        </div>
                        <div style="color: #374151; font-size: 0.85rem; margin-top: 4px;">
                            {c['detailed_insight']}
                        </div>
                        <div style="color: #7F1D1D; font-size: 0.82rem; margin-top: 4px; font-weight: 500;">
                            👉 <b>Action:</b> {c['recommendation']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        else:
            st.success("✅ **Zero Critical Vulnerabilities:** No ratios fell below minimum warning thresholds.")

    st.markdown("---")

    # ------------------------------------------------------------------------
    # DETAILED CATEGORIZED INSIGHTS TABS
    # ------------------------------------------------------------------------
    st.markdown("### 🔍 In-Depth Category Diagnosis")

    tab_liq, tab_prof, tab_solv, tab_eff, tab_cf = st.tabs([
        "💧 Liquidity",
        "📈 Profitability",
        "🛡️ Solvency",
        "⚙️ Efficiency",
        "💸 Cash Flow",
    ])

    def render_detailed_insight_card(key: str):
        item = all_evals.get(key)
        if not item:
            return

        status_colors = {
            "Healthy": ("#DCFCE7", "#166534", "✅"),
            "Moderate": ("#DBEAFE", "#1E40AF", "ℹ️"),
            "Needs Attention": ("#FEE2E2", "#991B1B", "⚠️"),
            "Not Available": ("#F1F5F9", "#475569", "⚪"),
        }
        bg, fg, icon = status_colors.get(item["status"], ("#F1F5F9", "#475569", "•"))

        val_display = (
            f"{item['value']:.2f}{item['unit']}"
            if item["value"] is not None and item["unit"] != "₹"
            else (format_indian_currency(item["value"]) if item["unit"] == "₹" else "N/A")
        )

        st.markdown(
            f"""
            <div style="background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 10px;
                        padding: 16px 20px; margin-bottom: 16px; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                    <div>
                        <h4 style="color: #1E3A8A; margin: 0 0 2px 0; font-size: 1.1rem; font-weight: 700;">
                            {item['name']} &mdash; <span style="color: #0F172A;">{val_display}</span>
                        </h4>
                        <span style="color: #64748B; font-size: 0.82rem; font-weight: 500;">
                            {item['headline']}
                        </span>
                    </div>
                    <div style="margin-top: 4px;">
                        <span style="background-color: {bg}; color: {fg}; font-size: 0.8rem;
                                     font-weight: 700; padding: 4px 10px; border-radius: 14px;">
                            {icon} {item['status']}
                        </span>
                    </div>
                </div>
                <div style="margin-top: 10px; padding-top: 8px; border-top: 1px solid #F1F5F9;">
                    <p style="color: #334155; font-size: 0.88rem; line-height: 1.45; margin: 0 0 8px 0;">
                        {item['detailed_insight']}
                    </p>
                    <div style="background-color: #F8FAFC; border-left: 3px solid #3B82F6; padding: 8px 12px; border-radius: 4px;">
                        <span style="color: #1E40AF; font-size: 0.82rem; font-weight: 600;">Strategic Guidance:</span>
                        <span style="color: #475569; font-size: 0.82rem;">{item['recommendation']}</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with tab_liq:
        st.markdown("#### 💧 Liquidity Health & Short-Term Obligations")
        render_detailed_insight_card("current_ratio")
        render_detailed_insight_card("quick_ratio")
        render_detailed_insight_card("cash_ratio")

    with tab_prof:
        st.markdown("#### 📈 Profitability Margins & Capital Productivity")
        render_detailed_insight_card("gross_profit_margin")
        render_detailed_insight_card("net_profit_margin")
        render_detailed_insight_card("return_on_assets")
        render_detailed_insight_card("return_on_equity")

    with tab_solv:
        st.markdown("#### 🛡️ Long-Term Solvency & Debt Gearing")
        render_detailed_insight_card("debt_to_equity")
        render_detailed_insight_card("debt_ratio")
        render_detailed_insight_card("interest_coverage")

    with tab_eff:
        st.markdown("#### ⚙️ Operational Asset & Inventory Velocity")
        render_detailed_insight_card("inventory_turnover")
        render_detailed_insight_card("asset_turnover")

    with tab_cf:
        st.markdown("#### 💸 Cash Flow Viability & Self-Funded Growth")
        render_detailed_insight_card("operating_cash_flow_ratio")
        render_detailed_insight_card("free_cash_flow")
