"""Company Management Module.

College Project: Financial Statement Ratio Analysis Assistant
This module implements Step 6:
- Add Company
- View Companies (in a professional table)
- Edit Company
- Delete Company with explicit confirmation safeguards
- Strict user-level data isolation
"""

import pandas as pd
import streamlit as st
import database
from pages.dashboard import format_indian_date


# Standard Indian Industry Sectors
INDIAN_INDUSTRIES = [
    "Manufacturing",
    "Information Technology & Software",
    "Banking & Financial Services (BFSI)",
    "Pharmaceuticals & Healthcare",
    "FMCG & Consumer Goods",
    "Automobile & Auto Ancillaries",
    "Energy, Oil & Power",
    "Textiles & Apparel",
    "Real Estate & Infrastructure",
    "Telecommunications",
    "Chemicals & Petrochemicals",
    "Steel & Metallurgy",
    "Agriculture & Agrochemicals",
    "Logistics & Supply Chain",
    "Retail & E-Commerce",
    "Other / Diversified",
]

# Standard Indian Financial Years (April to March)
INDIAN_FINANCIAL_YEARS = [
    "FY 2026-27",
    "FY 2025-26",
    "FY 2024-25",
    "FY 2023-24",
    "FY 2022-23",
    "FY 2021-22",
    "Custom Financial Year",
]


def render_companies_page(user: dict):
    """Render the Company Management interface for the authenticated user."""
    user_id = user["id"]

    st.markdown(
        """
        <div style="margin-bottom: 20px;">
            <h1 style="color: #142B4A; font-weight: 700; margin-bottom: 4px;">
                🏢 Company Management
            </h1>
            <p style="color: #5A6E85; font-size: 1rem; margin: 0;">
                Register, edit, view, and organize your companies for Indian financial statement analysis.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    tab_view, tab_add, tab_edit, tab_delete = st.tabs([
        "📋 View Companies",
        "➕ Add New Company",
        "✏️ Edit Company",
        "🗑️ Delete Company",
    ])

    # ========================================================================
    # TAB 1: VIEW COMPANIES
    # ========================================================================
    with tab_view:
        st.markdown("### Registered Companies")
        st.caption("Companies registered under your account. Each account's portfolio is strictly private.")

        companies = database.list_companies(user_id)

        if not companies:
            st.info("ℹ️ No companies registered yet. Switch to the **'➕ Add New Company'** tab to add your first company.")
        else:
            # Prepare formatted display table
            table_data = []
            for idx, c in enumerate(companies, start=1):
                table_data.append({
                    "#": idx,
                    "Company Name": c["company_name"],
                    "Industry": c["industry"],
                    "Financial Year (Apr-Mar)": c["financial_year"],
                    "Description": c["description"] or "None provided",
                    "Created On": format_indian_date(c["created_at"]),
                    "Company ID": f"#{c['id']}",
                })

            df_companies = pd.DataFrame(table_data)
            st.dataframe(df_companies, use_container_width=True, hide_index=True)

            st.markdown(f"**Total Registered Companies:** `{len(companies)}`")

    # ========================================================================
    # TAB 2: ADD NEW COMPANY
    # ========================================================================
    with tab_add:
        st.markdown("### Register a New Company")
        st.caption("Add an Indian enterprise to analyze its financial statements.")

        with st.form("add_company_form", clear_on_submit=True):
            col_name, col_ind = st.columns([1.5, 1])
            with col_name:
                company_name = st.text_input(
                    "Company Name *",
                    placeholder="e.g. Bharat Industrial Motors Ltd",
                    help="Official registered name of the company.",
                )
            with col_ind:
                industry = st.selectbox(
                    "Industry Sector *",
                    INDIAN_INDUSTRIES,
                    help="Select the primary business sector.",
                )

            col_fy, col_custom = st.columns([1, 1.5])
            with col_fy:
                fy_selection = st.selectbox(
                    "Primary Financial Year (Apr-Mar) *",
                    INDIAN_FINANCIAL_YEARS,
                    index=1,  # Defaults to FY 2025-26
                    help="Standard Indian accounting year running April 1 to March 31.",
                )
            with col_custom:
                custom_fy = ""
                if fy_selection == "Custom Financial Year":
                    custom_fy = st.text_input(
                        "Enter Custom Financial Year (e.g. FY 2027-28) *",
                        placeholder="FY 2027-28",
                    )

            description = st.text_area(
                "Company Description / Notes (Optional)",
                placeholder="Brief summary of operations, stock ticker, or business segment...",
                help="Optional context for your financial records.",
            )

            submitted = st.form_submit_button("➕ Save Company", use_container_width=True, type="primary")

            if submitted:
                # Validation
                name_clean = (company_name or "").strip()
                final_fy = custom_fy.strip() if fy_selection == "Custom Financial Year" else fy_selection

                if not name_clean:
                    st.error("❌ Company name is required.")
                elif not final_fy:
                    st.error("❌ Financial year is required.")
                else:
                    try:
                        new_id = database.create_company(
                            user_id=user_id,
                            company_name=name_clean,
                            industry=industry,
                            financial_year=final_fy,
                            description=description.strip(),
                        )
                        st.success(f"✅ Company **{name_clean}** successfully registered! (ID: `#{new_id}`)")
                        st.info("👉 You can now enter its financial statements under **📑 Financial Statements**.")
                        st.rerun()
                    except database.DatabaseError as e:
                        st.error(f"❌ {e}")

    # ========================================================================
    # TAB 3: EDIT COMPANY
    # ========================================================================
    with tab_edit:
        st.markdown("### Update Company Information")
        st.caption("Edit company details. Existing statements and analyses remain intact.")

        companies = database.list_companies(user_id)

        if not companies:
            st.info("ℹ️ No companies available to edit. Please add a company first.")
        else:
            company_map = {f"{c['company_name']} ({c['financial_year']}) [ID #{c['id']}]": c for c in companies}
            selected_label = st.selectbox("Select Company to Edit", list(company_map.keys()))
            selected_comp = company_map[selected_label]

            with st.form("edit_company_form"):
                e_col1, e_col2 = st.columns([1.5, 1])
                with e_col1:
                    edit_name = st.text_input(
                        "Company Name *",
                        value=selected_comp["company_name"],
                    )
                with e_col2:
                    current_ind_idx = (
                        INDIAN_INDUSTRIES.index(selected_comp["industry"])
                        if selected_comp["industry"] in INDIAN_INDUSTRIES else 0
                    )
                    edit_industry = st.selectbox(
                        "Industry Sector *",
                        INDIAN_INDUSTRIES,
                        index=current_ind_idx,
                    )

                e_fy_col1, e_fy_col2 = st.columns([1, 1.5])
                with e_fy_col1:
                    current_fy = selected_comp["financial_year"]
                    fy_index = (
                        INDIAN_FINANCIAL_YEARS.index(current_fy)
                        if current_fy in INDIAN_FINANCIAL_YEARS else len(INDIAN_FINANCIAL_YEARS) - 1
                    )
                    edit_fy_sel = st.selectbox(
                        "Financial Year *",
                        INDIAN_FINANCIAL_YEARS,
                        index=fy_index,
                    )
                with e_fy_col2:
                    edit_custom_fy = ""
                    if edit_fy_sel == "Custom Financial Year":
                        edit_custom_fy = st.text_input(
                            "Enter Custom Financial Year *",
                            value=current_fy if current_fy not in INDIAN_FINANCIAL_YEARS else "",
                        )

                edit_description = st.text_area(
                    "Description / Notes",
                    value=selected_comp["description"] or "",
                )

                update_submitted = st.form_submit_button("💾 Update Company Details", use_container_width=True, type="primary")

                if update_submitted:
                    e_name_clean = (edit_name or "").strip()
                    e_final_fy = edit_custom_fy.strip() if edit_fy_sel == "Custom Financial Year" else edit_fy_sel

                    if not e_name_clean:
                        st.error("❌ Company name cannot be empty.")
                    elif not e_final_fy:
                        st.error("❌ Financial year cannot be empty.")
                    else:
                        try:
                            ok = database.update_company(
                                user_id=user_id,
                                company_id=selected_comp["id"],
                                company_name=e_name_clean,
                                industry=edit_industry,
                                financial_year=e_final_fy,
                                description=edit_description.strip(),
                            )
                            if ok:
                                st.success(f"✅ Company **{e_name_clean}** updated successfully!")
                                st.rerun()
                            else:
                                st.error("❌ Failed to update company.")
                        except database.DatabaseError as e:
                            st.error(f"❌ {e}")

    # ========================================================================
    # TAB 4: DELETE COMPANY (SAFE DELETION WITH EXPLICIT CONFIRMATION)
    # ========================================================================
    with tab_delete:
        st.markdown("### Delete Company")
        st.caption("Safely remove a company. Requires explicit confirmation to prevent accidental data loss.")

        companies = database.list_companies(user_id)

        if not companies:
            st.info("ℹ️ No companies available to delete.")
        else:
            del_company_map = {f"{c['company_name']} ({c['financial_year']}) [ID #{c['id']}]": c for c in companies}
            del_selected_label = st.selectbox(
                "Select Company to Delete",
                list(del_company_map.keys()),
                key="del_company_select",
            )
            del_comp = del_company_map[del_selected_label]
            company_id = del_comp["id"]

            # Inspect linked records
            statements = database.list_statements(user_id, company_id)
            analyses = [a for a in database.list_analyses(user_id) if a["company_id"] == company_id]

            st.warning(
                f"⚠️ **Attention:** Deleting **{del_comp['company_name']}** will remove:\n"
                f"- **{len(statements)}** saved financial statements\n"
                f"- **{len(analyses)}** associated ratio analyses and history records\n\n"
                f"*Historical financial analyses are not deleted automatically without your explicit consent.*"
            )

            # Safeguard confirmation
            confirm_check = st.checkbox(
                f"I explicitly confirm that I want to delete '{del_comp['company_name']}' and its {len(statements)} associated statement(s).",
                key="delete_confirm_checkbox",
            )

            if st.button("🗑️ Permanently Delete Company", type="primary", disabled=not confirm_check):
                try:
                    deleted = database.delete_company(user_id, company_id)
                    if deleted:
                        st.success(f"✅ Company **{del_comp['company_name']}** was deleted.")
                        st.rerun()
                    else:
                        st.error("❌ Could not delete the company.")
                except database.DatabaseError as e:
                    st.error(f"❌ {e}")
