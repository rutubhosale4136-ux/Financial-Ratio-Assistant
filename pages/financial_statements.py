"""Financial Statement Input Module.

College Project: Financial Statement Ratio Analysis Assistant
This module implements Step 7:
- Company and Financial Year selection
- Denomination conversion (Rupees, Thousands, Lakhs, Crores) to actual INR
- Three structured sections: Income Statement, Balance Sheet, Cash Flow Statement
- Automated calculation of Gross Profit, Operating Income, Net Income, and Free Cash Flow
- Real-time mathematical validation & negative figure support
- Automated ratio calculation and SQLite persistence in a single transaction
"""

import streamlit as st
import database
import calculations
from pages.dashboard import format_indian_currency


# Denomination multipliers
UNIT_MULTIPLIERS = {
    "Actual Rupees (₹ 1)": 1.0,
    "Thousands (₹ '000)": 1_000.0,
    "Lakhs (₹ Lakh) [1,00,000]": 100_000.0,
    "Crores (₹ Cr) [1,00,00,000]": 10_000_000.0,
}

INDIAN_FINANCIAL_YEARS = [
    "FY 2026-27",
    "FY 2025-26",
    "FY 2024-25",
    "FY 2023-24",
    "FY 2022-23",
    "FY 2021-22",
    "Custom",
]


def render_statements_page(user: dict):
    """Render the Financial Statement Input screen for the logged-in user."""
    user_id = user["id"]

    st.markdown(
        """
        <div style="margin-bottom: 20px;">
            <h1 style="color: #142B4A; font-weight: 700; margin-bottom: 4px;">
                📑 Financial Statement Input
            </h1>
            <p style="color: #5A6E85; font-size: 1rem; margin: 0;">
                Record and update Balance Sheets, Income Statements, and Cash Flow figures in Indian Rupees (₹).
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 1. Ensure user has registered at least one company
    companies = database.list_companies(user_id)
    if not companies:
        st.warning(
            "⚠️ **No Companies Found:** You must register a company first before entering financial statements."
        )
        if st.button("🏢 Go to Company Management", type="primary"):
            st.session_state["nav_selection"] = "Company Management"
            st.rerun()
        return

    # 2. Company & Financial Year Selection Controls
    st.markdown("### 1. Select Target Company & Financial Year")
    col_c, col_fy, col_unit = st.columns([1.5, 1, 1.2])

    with col_c:
        comp_map = {f"{c['company_name']} ({c['industry']})": c for c in companies}
        selected_comp_label = st.selectbox("Select Company *", list(comp_map.keys()))
        target_company = comp_map[selected_comp_label]
        company_id = target_company["id"]

    with col_fy:
        default_fy = target_company["financial_year"]
        fy_idx = INDIAN_FINANCIAL_YEARS.index(default_fy) if default_fy in INDIAN_FINANCIAL_YEARS else 1
        fy_choice = st.selectbox("Financial Year (Apr-Mar) *", INDIAN_FINANCIAL_YEARS, index=fy_idx)
        if fy_choice == "Custom":
            final_fy = st.text_input("Enter FY (e.g. FY 2027-28)", placeholder="FY 2027-28").strip()
        else:
            final_fy = fy_choice

    with col_unit:
        chosen_unit = st.selectbox(
            "Input Denomination *",
            list(UNIT_MULTIPLIERS.keys()),
            index=2,  # Defaults to Lakhs (₹ Lakh)
            help="Choose how you prefer to enter numbers. All amounts are converted to exact numeric INR before saving.",
        )
        multiplier = UNIT_MULTIPLIERS[chosen_unit]

    # Check if a statement already exists for this Company + FY
    existing_stmt = database.get_statement_for_company(user_id, company_id, final_fy)
    if existing_stmt:
        st.info(
            f"ℹ️ **Existing Statement Detected:** Found saved records for **{target_company['company_name']}** ({final_fy}). "
            f"Values have been pre-filled below for editing."
        )
    else:
        st.caption(f"Creating a new statement for **{target_company['company_name']}** for **{final_fy}**.")

    # Helper function to get default pre-filled value converted to chosen denomination
    def get_val(field_name: str, fallback: float = 0.0) -> float:
        if existing_stmt and existing_stmt.get(field_name) is not None:
            # Convert stored INR back into selected display unit
            return float(existing_stmt[field_name]) / multiplier
        return fallback

    # ========================================================================
    # STATEMENT INPUT FORM
    # ========================================================================
    with st.form("financial_statement_form"):
        # --------------------------------------------------------------------
        # SECTION A: INCOME STATEMENT
        # --------------------------------------------------------------------
        st.markdown("---")
        st.markdown("### A. Income Statement")
        st.caption("Figures reflect operational revenue and expenditures for the 12-month fiscal year.")

        i_col1, i_col2 = st.columns(2)
        with i_col1:
            revenue_input = st.number_input(
                f"Revenue / Sales ({chosen_unit.split(' ')[0]}) *",
                value=get_val("revenue", 100.0),
                step=1.0,
                format="%.2f",
                help="Total gross sales and operating turnover in the chosen unit.",
            )
            cogs_input = st.number_input(
                f"Cost of Goods Sold (COGS) ({chosen_unit.split(' ')[0]}) *",
                value=get_val("cost_of_goods_sold", 60.0),
                step=1.0,
                format="%.2f",
                help="Direct cost of producing goods or services sold.",
            )
            opex_input = st.number_input(
                f"Operating Expenses (OpEx) ({chosen_unit.split(' ')[0]}) *",
                value=get_val("operating_expenses", 15.0),
                step=1.0,
                format="%.2f",
                help="Selling, general, and administrative (SG&A) operational expenses.",
            )

        with i_col2:
            interest_input = st.number_input(
                f"Interest Expense ({chosen_unit.split(' ')[0]})",
                value=get_val("interest_expense", 5.0),
                step=0.5,
                format="%.2f",
                help="Interest on short and long-term debt obligations.",
            )
            tax_input = st.number_input(
                f"Tax Expense ({chosen_unit.split(' ')[0]})",
                value=get_val("tax_expense", 5.0),
                step=0.5,
                format="%.2f",
                help="Corporate income tax provisions for the financial year.",
            )

        # --------------------------------------------------------------------
        # SECTION B: BALANCE SHEET
        # --------------------------------------------------------------------
        st.markdown("---")
        st.markdown("### B. Balance Sheet")
        st.caption("Asset, liability, and equity positions as of March 31.")

        b_col1, b_col2 = st.columns(2)
        with b_col1:
            st.markdown("##### 📦 Assets")
            ca_input = st.number_input(
                f"Current Assets ({chosen_unit.split(' ')[0]}) *",
                value=get_val("current_assets", 30.0),
                step=1.0,
                format="%.2f",
            )
            cash_input = st.number_input(
                f"Cash & Cash Equivalents ({chosen_unit.split(' ')[0]}) *",
                value=get_val("cash_and_cash_equivalents", 10.0),
                step=1.0,
                format="%.2f",
            )
            inv_input = st.number_input(
                f"Inventory ({chosen_unit.split(' ')[0]}) *",
                value=get_val("inventory", 12.0),
                step=1.0,
                format="%.2f",
            )
            ta_input = st.number_input(
                f"Total Assets ({chosen_unit.split(' ')[0]}) *",
                value=get_val("total_assets", 80.0),
                step=1.0,
                format="%.2f",
            )

        with b_col2:
            st.markdown("##### 💳 Liabilities & Equity")
            cl_input = st.number_input(
                f"Current Liabilities ({chosen_unit.split(' ')[0]}) *",
                value=get_val("current_liabilities", 15.0),
                step=1.0,
                format="%.2f",
            )
            tl_input = st.number_input(
                f"Total Liabilities ({chosen_unit.split(' ')[0]}) *",
                value=get_val("total_liabilities", 35.0),
                step=1.0,
                format="%.2f",
            )
            debt_input = st.number_input(
                f"Total Debt ({chosen_unit.split(' ')[0]}) *",
                value=get_val("total_debt", 20.0),
                step=1.0,
                format="%.2f",
                help="Short-term borrowings + long-term debt.",
            )
            equity_input = st.number_input(
                f"Shareholders' Equity ({chosen_unit.split(' ')[0]}) *",
                value=get_val("shareholders_equity", 45.0),
                step=1.0,
                format="%.2f",
            )

        st.markdown("##### 📅 Opening & Closing Balances (For Accurate Average Ratios)")
        st.caption("Required for strict Return on Assets (ROA), Asset Turnover, and Inventory Turnover.")
        avg_col1, avg_col2 = st.columns(2)
        with avg_col1:
            op_inv_input = st.number_input(
                f"Opening Inventory ({chosen_unit.split(' ')[0]})",
                value=get_val("opening_inventory", 10.0),
                step=1.0,
                format="%.2f",
            )
            cl_inv_input = st.number_input(
                f"Closing Inventory ({chosen_unit.split(' ')[0]})",
                value=get_val("closing_inventory", 14.0),
                step=1.0,
                format="%.2f",
            )
        with avg_col2:
            op_ta_input = st.number_input(
                f"Opening Total Assets ({chosen_unit.split(' ')[0]})",
                value=get_val("opening_total_assets", 70.0),
                step=1.0,
                format="%.2f",
            )
            cl_ta_input = st.number_input(
                f"Closing Total Assets ({chosen_unit.split(' ')[0]})",
                value=get_val("closing_total_assets", 90.0),
                step=1.0,
                format="%.2f",
            )

        # --------------------------------------------------------------------
        # SECTION C: CASH FLOW STATEMENT
        # --------------------------------------------------------------------
        st.markdown("---")
        st.markdown("### C. Cash Flow Statement")
        st.caption("Cash generated from operational activities and capital investments.")

        cf_col1, cf_col2 = st.columns(2)
        with cf_col1:
            ocf_input = st.number_input(
                f"Operating Cash Flow (OCF) ({chosen_unit.split(' ')[0]}) *",
                value=get_val("operating_cash_flow", 22.0),
                step=1.0,
                format="%.2f",
                help="Cash flow from primary operations. Negative values permitted.",
            )
        with cf_col2:
            capex_input = st.number_input(
                f"Capital Expenditure (CapEx) ({chosen_unit.split(' ')[0]}) *",
                value=get_val("capital_expenditure", 7.0),
                step=1.0,
                format="%.2f",
                help="Investments in fixed assets, plant, property, and equipment.",
            )

        st.markdown("---")
        submitted = st.form_submit_button("💾 Save & Calculate Financial Ratios", use_container_width=True, type="primary")

    # ========================================================================
    # FORM SUBMISSION PROCESSING
    # ========================================================================
    if submitted:
        if not final_fy:
            st.error("❌ Please provide a valid Financial Year.")
            return

        # 1. Convert all inputs into actual INR numbers
        actual_revenue = float(revenue_input) * multiplier
        actual_cogs = float(cogs_input) * multiplier
        actual_opex = float(opex_input) * multiplier
        actual_interest = float(interest_input) * multiplier
        actual_tax = float(tax_input) * multiplier

        # Compute Core Income Statement values
        actual_gross_profit = calculations.compute_gross_profit(actual_revenue, actual_cogs)
        actual_operating_income = calculations.compute_operating_income(actual_gross_profit, actual_opex)
        actual_net_income = calculations.compute_net_income(actual_operating_income, actual_interest, actual_tax)

        # Balance Sheet actual INR values
        actual_ca = float(ca_input) * multiplier
        actual_cash = float(cash_input) * multiplier
        actual_inv = float(inv_input) * multiplier
        actual_ta = float(ta_input) * multiplier

        actual_cl = float(cl_input) * multiplier
        actual_tl = float(tl_input) * multiplier
        actual_debt = float(debt_input) * multiplier
        actual_equity = float(equity_input) * multiplier

        actual_op_inv = float(op_inv_input) * multiplier if op_inv_input > 0 else None
        actual_cl_inv = float(cl_inv_input) * multiplier if cl_inv_input > 0 else None
        actual_op_ta = float(op_ta_input) * multiplier if op_ta_input > 0 else None
        actual_cl_ta = float(cl_ta_input) * multiplier if cl_ta_input > 0 else None

        # Cash Flow actual INR values
        actual_ocf = float(ocf_input) * multiplier
        actual_capex = float(capex_input) * multiplier
        actual_fcf = calculations.compute_free_cash_flow(actual_ocf, actual_capex)

        # 2. Logical Validation Checks (Warnings for potential inconsistencies)
        validation_warnings = []
        if actual_revenue <= 0:
            validation_warnings.append("Revenue is zero or negative. Please verify turnover figures.")
        if actual_cash > actual_ca:
            validation_warnings.append("Cash & Cash Equivalents exceeds Current Assets.")
        if actual_inv > actual_ca:
            validation_warnings.append("Inventory exceeds Current Assets.")
        if actual_ca > actual_ta:
            validation_warnings.append("Current Assets exceeds Total Assets.")
        if actual_cl > actual_tl:
            validation_warnings.append("Current Liabilities exceeds Total Liabilities.")

        for warning in validation_warnings:
            st.warning(f"⚠️ **Note:** {warning}")

        # 3. Assemble statement data dictionary
        statement_data = {
            "financial_year": final_fy,
            "revenue": actual_revenue,
            "cost_of_goods_sold": actual_cogs,
            "gross_profit": actual_gross_profit,
            "operating_expenses": actual_opex,
            "operating_income": actual_operating_income,
            "interest_expense": actual_interest,
            "tax_expense": actual_tax,
            "net_income": actual_net_income,
            "current_assets": actual_ca,
            "cash_and_cash_equivalents": actual_cash,
            "inventory": actual_inv,
            "total_assets": actual_ta,
            "current_liabilities": actual_cl,
            "total_liabilities": actual_tl,
            "total_debt": actual_debt,
            "shareholders_equity": actual_equity,
            "opening_inventory": actual_op_inv,
            "closing_inventory": actual_cl_inv,
            "opening_total_assets": actual_op_ta,
            "closing_total_assets": actual_cl_ta,
            "operating_cash_flow": actual_ocf,
            "capital_expenditure": actual_capex,
            "free_cash_flow": actual_fcf,
        }

        # 4. Calculate all 14 ratios
        calculated_ratios = calculations.calculate_all_ratios(statement_data)

        # 5. Save in SQLite via unified transaction
        try:
            save_result = database.save_full_analysis(
                user_id=user_id,
                company_id=company_id,
                statement_data=statement_data,
                ratio_data=calculated_ratios,
            )

            st.success(
                f"✅ **Financial Statement Saved Successfully!**\n\n"
                f"- **Company:** {target_company['company_name']} ({final_fy})\n"
                f"- **Revenue:** {format_indian_currency(actual_revenue)}\n"
                f"- **Gross Profit:** {format_indian_currency(actual_gross_profit)}\n"
                f"- **Net Income:** {format_indian_currency(actual_net_income)}\n"
                f"- **Free Cash Flow:** {format_indian_currency(actual_fcf)}\n"
                f"- **Statement ID:** `#{save_result['statement_id']}` &bull; Analysis ID: `#{save_result['analysis_id']}`"
            )

            col_btn1, col_btn2 = st.columns([1, 1])
            with col_btn1:
                if st.button("📈 View Financial Ratio Analysis", type="primary"):
                    st.session_state["nav_selection"] = "Ratio Analysis"
                    st.session_state["selected_analysis_company"] = company_id
                    st.session_state["selected_analysis_fy"] = final_fy
                    st.rerun()
            with col_btn2:
                if st.button("📊 Return to Dashboard"):
                    st.session_state["nav_selection"] = "Dashboard"
                    st.rerun()

        except database.DatabaseError as e:
            st.error(f"❌ Database Error: {e}")
        except Exception as e:
            st.error(f"❌ An error occurred while saving: {e}")
