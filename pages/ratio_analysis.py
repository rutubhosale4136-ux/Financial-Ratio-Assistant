"""Financial Ratio Analysis Module.

College Project: Financial Statement Ratio Analysis Assistant
This module implements Step 8:
- Professional ratio analysis dashboard grouped into 5 categories:
  1. Liquidity Ratios
  2. Profitability Ratios
  3. Solvency Ratios
  4. Efficiency Ratios
  5. Cash Flow Ratios
- Displays ratio name, calculated result, formula, short explanation, and financial interpretation
- Master summary table of all 14 ratios
- Strict user data isolation
"""

import pandas as pd
import streamlit as st
import database
import calculations
from pages.dashboard import format_indian_currency, format_indian_date


CATEGORIES = [
    ("💧 Liquidity", "Liquidity", ["current_ratio", "quick_ratio", "cash_ratio"]),
    ("📈 Profitability", "Profitability", ["gross_profit_margin", "net_profit_margin", "return_on_assets", "return_on_equity"]),
    ("🛡️ Solvency", "Solvency", ["debt_to_equity", "debt_ratio", "interest_coverage"]),
    ("⚙️ Efficiency", "Efficiency", ["inventory_turnover", "asset_turnover"]),
    ("💸 Cash Flow", "Cash Flow", ["operating_cash_flow_ratio", "free_cash_flow"]),
]


def render_ratio_analysis_page(user: dict):
    """Render the comprehensive financial ratio analysis screen."""
    user_id = user["id"]

    st.markdown(
        """
        <div style="margin-bottom: 20px;">
            <h1 style="color: #142B4A; font-weight: 700; margin-bottom: 4px;">
                📈 Financial Ratio Analysis
            </h1>
            <p style="color: #5A6E85; font-size: 1rem; margin: 0;">
                Comprehensive evaluation of liquidity, profitability, solvency, efficiency, and cash flows.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 1. Fetch user statements
    statements = database.list_statements(user_id)
    if not statements:
        st.info(
            "ℹ️ **No Financial Statements Found:** To view financial ratio analysis, "
            "please add a company and enter its statement data under **📑 Financial Statements**."
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

    # Select statement
    col_sel1, col_sel2 = st.columns([2, 1])
    with col_sel1:
        selected_label = st.selectbox(
            "Select Company & Financial Year for Analysis *",
            statement_labels,
        )
        active_statement = statement_map[selected_label]
        statement_id = active_statement["id"]
        active_company_id = active_statement["company_id"]
        active_company = companies_lookup.get(active_company_id, {})

    with col_sel2:
        st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
        st.caption(
            f"**Industry:** {active_company.get('industry', 'N/A')}<br>"
            f"**Last Updated:** {format_indian_date(active_statement['updated_at'])}",
            unsafe_allow_html=True,
        )

    # 3. Retrieve or calculate ratios for this statement
    ratios = database.get_ratios(user_id, statement_id)
    if not ratios:
        # Calculate and save if not present
        ratios = calculations.calculate_all_ratios(active_statement)

    st.markdown("---")

    # 4. Five Categorized Tabs
    tab_overview, tab_liq, tab_prof, tab_solv, tab_eff, tab_cf = st.tabs([
        "📊 Master Summary",
        "💧 Liquidity",
        "📈 Profitability",
        "🛡️ Solvency",
        "⚙️ Efficiency",
        "💸 Cash Flow",
    ])

    # Helper function to format ratio result value correctly
    def format_ratio_value(key: str, val):
        if val is None:
            return "N/A"
        meta = calculations.RATIO_METADATA.get(key, {})
        unit = meta.get("unit", "")
        if unit == "%":
            return f"{float(val):.2f}%"
        elif unit == "x":
            return f"{float(val):.2f}x"
        elif unit == "₹":
            return format_indian_currency(val, compact=False)
        return f"{float(val):.2f}"

    # Helper function to render a single ratio card
    def render_ratio_card(key: str):
        meta = calculations.RATIO_METADATA.get(key, {})
        raw_val = ratios.get(key)
        formatted_val = format_ratio_value(key, raw_val)
        status_label, badge_color, interp_text = calculations.interpret_ratio(key, raw_val)

        # Financial Category Coordinated Accents
        cat_meta = {
            "Liquidity": ("#2878D0", "#EFF6FF"),      # Royal Blue
            "Profitability": ("#20A46B", "#F0FDF4"),  # Green
            "Solvency": ("#8064C8", "#FAF5FF"),       # Purple
            "Efficiency": ("#13A89E", "#F0FDFA"),     # Teal
            "Cash Flow": ("#E99A35", "#FFFBEB"),      # Amber/Orange
        }.get(meta.get("category", ""), ("#2878D0", "#F8FAFC"))
        cat_border, cat_bg = cat_meta

        badge_bg_map = {
            "green": "#DCFCE7",
            "blue": "#DBEAFE",
            "orange": "#FEF3C7",
            "red": "#FEE2E2",
            "grey": "#F1F5F9",
        }
        badge_text_map = {
            "green": "#20A46B",
            "blue": "#2878D0",
            "orange": "#E99A35",
            "red": "#DC2626",
            "grey": "#64748B",
        }

        bg = badge_bg_map.get(badge_color, "#F1F5F9")
        fg = badge_text_map.get(badge_color, "#475569")

        st.markdown(
            f"""
            <div style="background-color: #FFFFFF; border: 1px solid #E2E8F0; border-left: 4.5px solid {cat_border};
                        border-radius: 12px; padding: 18px 22px; margin-bottom: 16px;
                        box-shadow: 0 2px 8px rgba(20, 43, 74, 0.04);">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap;">
                    <div>
                        <span style="display: inline-block; background-color: {cat_bg}; color: {cat_border};
                                     font-size: 0.75rem; font-weight: 700; padding: 2px 8px; border-radius: 6px;
                                     text-transform: uppercase; letter-spacing: 0.5px;">
                            {meta.get('category', '')}
                        </span>
                        <h4 style="color: #142B4A; margin: 4px 0 6px 0; font-size: 1.15rem; font-weight: 700;">
                            {meta.get('name', key)}
                        </h4>
                    </div>
                    <div style="text-align: right;">
                        <span style="font-size: 1.55rem; font-weight: 800; color: #142B4A;">
                            {formatted_val}
                        </span>
                        <div style="margin-top: 4px;">
                            <span style="background-color: {bg}; color: {fg}; font-size: 0.75rem;
                                         font-weight: 700; padding: 3px 10px; border-radius: 12px;">
                                {status_label}
                            </span>
                        </div>
                    </div>
                </div>
                <div style="margin-top: 10px; padding-top: 10px; border-top: 1px dashed #E2E8F0;">
                    <div style="font-size: 0.82rem; color: #5A6E85; margin-bottom: 4px;">
                        <b>Formula:</b> <code style="background-color: #F8FAFC; padding: 2px 6px; border-radius: 4px; color: #142B4A; border: 1px solid #E2E8F0;">{meta.get('formula', '')}</code>
                        &bull; <b>Benchmark:</b> <span style="font-weight: 600; color: #142B4A;">{meta.get('benchmark', 'N/A')}</span>
                    </div>
                    <p style="color: #334155; font-size: 0.85rem; margin: 4px 0 0 0;">
                        {meta.get('explanation', '')}
                    </p>
                    <p style="color: {fg}; font-size: 0.85rem; margin: 6px 0 0 0; font-weight: 600;">
                        💡 <b>Analysis:</b> {interp_text}
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ------------------------------------------------------------------------
    # TAB 1: MASTER SUMMARY TABLE
    # ------------------------------------------------------------------------
    with tab_overview:
        st.markdown("### 📊 Master Ratio Summary Table")
        st.caption(f"Financial profile for {active_company.get('company_name', 'Company')} ({active_statement['financial_year']})")

        rows = []
        for key, meta in calculations.RATIO_METADATA.items():
            val = ratios.get(key)
            formatted = format_ratio_value(key, val)
            status, _, _ = calculations.interpret_ratio(key, val)
            rows.append({
                "Category": meta["category"],
                "Ratio Name": meta["name"],
                "Result": formatted,
                "Benchmark": meta["benchmark"],
                "Status": status,
                "Formula": meta["formula"],
            })

        df_summary = pd.DataFrame(rows)
        st.dataframe(df_summary, use_container_width=True, hide_index=True)

        st.markdown("---")
        st.markdown("#### Statement Figures Summary (in Indian Rupees)")
        f_col1, f_col2, f_col3, f_col4 = st.columns(4)
        with f_col1:
            st.markdown('<div class="kpi-card kpi-blue">', unsafe_allow_html=True)
            st.metric("Total Revenue", format_indian_currency(active_statement.get("revenue"), compact=True))
            st.markdown('</div>', unsafe_allow_html=True)
        with f_col2:
            st.markdown('<div class="kpi-card kpi-teal">', unsafe_allow_html=True)
            st.metric("Gross Profit", format_indian_currency(active_statement.get("gross_profit"), compact=True))
            st.markdown('</div>', unsafe_allow_html=True)
        with f_col3:
            st.markdown('<div class="kpi-card kpi-green">', unsafe_allow_html=True)
            st.metric("Net Income", format_indian_currency(active_statement.get("net_income"), compact=True))
            st.markdown('</div>', unsafe_allow_html=True)
        with f_col4:
            st.markdown('<div class="kpi-card kpi-amber">', unsafe_allow_html=True)
            st.metric("Free Cash Flow", format_indian_currency(active_statement.get("free_cash_flow"), compact=True))
            st.markdown('</div>', unsafe_allow_html=True)

    # ------------------------------------------------------------------------
    # TAB 2: LIQUIDITY RATIOS
    # ------------------------------------------------------------------------
    with tab_liq:
        st.markdown("### 💧 Liquidity Ratios")
        st.caption("Assesses the company's capability to honor short-term commitments using current liquid assets.")
        render_ratio_card("current_ratio")
        render_ratio_card("quick_ratio")
        render_ratio_card("cash_ratio")

    # ------------------------------------------------------------------------
    # TAB 3: PROFITABILITY RATIOS
    # ------------------------------------------------------------------------
    with tab_prof:
        st.markdown("### 📈 Profitability Ratios")
        st.caption("Evaluates margins and capital earning efficiency relative to revenue, assets, and equity.")
        render_ratio_card("gross_profit_margin")
        render_ratio_card("net_profit_margin")
        render_ratio_card("return_on_assets")
        render_ratio_card("return_on_equity")

    # ------------------------------------------------------------------------
    # TAB 4: SOLVENCY RATIOS
    # ------------------------------------------------------------------------
    with tab_solv:
        st.markdown("### 🛡️ Solvency Ratios")
        st.caption("Analyzes long-term financial stability, capital structure leverage, and debt interest coverage.")
        render_ratio_card("debt_to_equity")
        render_ratio_card("debt_ratio")
        render_ratio_card("interest_coverage")

    # ------------------------------------------------------------------------
    # TAB 5: EFFICIENCY RATIOS
    # ------------------------------------------------------------------------
    with tab_eff:
        st.markdown("### ⚙️ Efficiency Ratios")
        st.caption("Measures how swiftly inventory moves and how effectively total assets generate top-line turnover.")
        render_ratio_card("inventory_turnover")
        render_ratio_card("asset_turnover")

    # ------------------------------------------------------------------------
    # TAB 6: CASH FLOW RATIOS
    # ------------------------------------------------------------------------
    with tab_cf:
        st.markdown("### 💸 Cash Flow Ratios & Metrics")
        st.caption("Examines cash generation quality relative to short-term obligations and capital expenditures.")
        render_ratio_card("operating_cash_flow_ratio")
        render_ratio_card("free_cash_flow")
