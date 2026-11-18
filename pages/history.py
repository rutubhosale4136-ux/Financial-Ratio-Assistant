"""Analysis History and Audit Log Page for Financial Statement Ratio Analysis Assistant.

College Project: Financial Statement Ratio Analysis Assistant
This page enables the logged-in user to:
1. Review a chronological audit log of all financial statements analyzed.
2. Filter analyses by company name, financial year, and search keywords.
3. Inspect detailed historical snapshots (ratios, revenue, profit, report count).
4. Jump directly to Ratio Analysis or Reports with one click.
5. Safely delete historical audit entries with confirmation (preserving statements & companies).
6. Export the full audit history to CSV for external records or college submission.
"""

from typing import Optional
import pandas as pd
import streamlit as st

import database
import calculations
import analysis
from pages.dashboard import format_indian_currency, format_indian_date


def render_history_page(current_user: dict, on_navigate_callback=None):
    """Render the Analysis History and Audit Trail page."""
    user_id = current_user["id"]

    # Header
    st.markdown(
        """
        <div style="margin-bottom: 20px;">
            <h2 style="color: #142B4A; margin-bottom: 4px; font-weight: 700;">🕒 Analysis History & Audit Trail</h2>
            <p style="color: #5A6E85; margin-top: 0; font-size: 0.95rem;">
                Chronological log of saved financial statements, ratio calculations, and exported PDF reports.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 1. Fetch History Records
    history_records = database.list_analyses(user_id)

    # Empty State: No History Recorded
    if not history_records:
        st.markdown(
            """
            <div style="background-color: #FFFFFF; border: 1.5px dashed #CBD5E1;
                        border-radius: 12px; padding: 40px 24px; text-align: center; margin-top: 16px;">
                <div style="font-size: 2.5rem; margin-bottom: 12px;">🕒</div>
                <h3 style="color: #1E3A8A; margin-bottom: 8px;">No Analysis History Recorded Yet</h3>
                <p style="color: #64748B; max-width: 520px; margin: 0 auto 24px auto; font-size: 0.95rem;">
                    Whenever you save a financial statement or compute financial ratios, a permanent timestamped
                    audit log is automatically archived here for your records.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        col1, _, _ = st.columns([1.3, 1, 2])
        with col1:
            if st.button("📑 Enter Financial Statements", type="primary", use_container_width=True):
                if on_navigate_callback:
                    on_navigate_callback("Financial Statements")
                else:
                    st.session_state["nav_selection"] = "Financial Statements"
                    st.rerun()
        return

    # 2. Executive KPI Summary Cards
    total_analyses = len(history_records)
    total_reports_exported = sum(r.get("report_generated", 0) for r in history_records)
    unique_companies = len(set(r.get("company_name", "") for r in history_records))
    cumulative_revenue = sum(r.get("total_revenue", 0.0) or 0.0 for r in history_records)

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1:
        st.markdown('<div class="kpi-card kpi-blue">', unsafe_allow_html=True)
        st.metric("Total Analyses Logged", f"{total_analyses}")
        st.markdown('</div>', unsafe_allow_html=True)
    with kpi2:
        st.markdown('<div class="kpi-card kpi-purple">', unsafe_allow_html=True)
        st.metric("Reports Exported", f"{total_reports_exported}")
        st.markdown('</div>', unsafe_allow_html=True)
    with kpi3:
        st.markdown('<div class="kpi-card kpi-teal">', unsafe_allow_html=True)
        st.metric("Companies Analyzed", f"{unique_companies}")
        st.markdown('</div>', unsafe_allow_html=True)
    with kpi4:
        st.markdown('<div class="kpi-card kpi-green">', unsafe_allow_html=True)
        st.metric("Cumulative Revenue", format_indian_currency(cumulative_revenue, compact=True))
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

    # 3. Search & Filter Controls Toolbar
    st.markdown(
        """
        <div style="font-size: 0.85rem; font-weight: 700; color: #475569; text-transform: uppercase; margin-bottom: 6px;">
            Filter & Search Audit Records
        </div>
        """,
        unsafe_allow_html=True,
    )

    filter_c1, filter_c2, filter_c3 = st.columns([1.5, 1.2, 1.2])

    company_names = sorted(list(set(r.get("company_name", "") for r in history_records if r.get("company_name"))))
    fy_names = sorted(list(set(r.get("financial_year", "") for r in history_records if r.get("financial_year"))), reverse=True)

    with filter_c1:
        search_query = st.text_input("🔍 Search by Company Name", placeholder="e.g. Tata, Apex, Lala...", key="history_search").strip().lower()

    with filter_c2:
        selected_company_filter = st.selectbox(
            "Filter by Company",
            options=["All Companies"] + company_names,
            key="history_comp_filter",
        )

    with filter_c3:
        selected_fy_filter = st.selectbox(
            "Filter by Financial Year",
            options=["All Financial Years"] + fy_names,
            key="history_fy_filter",
        )

    # Apply Filters
    filtered_records = []
    for r in history_records:
        c_name = str(r.get("company_name", "")).lower()
        fy = str(r.get("financial_year", ""))

        if search_query and search_query not in c_name:
            continue
        if selected_company_filter != "All Companies" and r.get("company_name") != selected_company_filter:
            continue
        if selected_fy_filter != "All Financial Years" and fy != selected_fy_filter:
            continue

        filtered_records.append(r)

    st.markdown("---")

    # Filter Result Count & CSV Export Button
    head_left, head_right = st.columns([2, 1])
    with head_left:
        st.markdown(
            f"<p style='color: #475569; font-weight: 600; font-size: 0.95rem; margin-top: 6px;'>"
            f"Showing <b>{len(filtered_records)}</b> of <b>{total_analyses}</b> audit records"
            f"</p>",
            unsafe_allow_html=True,
        )

    with head_right:
        if filtered_records:
            export_rows = []
            for r in filtered_records:
                export_rows.append({
                    "Log ID": r.get("id"),
                    "Company Name": r.get("company_name"),
                    "Financial Year": r.get("financial_year"),
                    "Analysis Date": r.get("analysis_date"),
                    "Total Revenue (INR)": r.get("total_revenue"),
                    "Net Profit (INR)": r.get("net_profit"),
                    "Ratios Calculated": r.get("ratios_calculated"),
                    "PDF Reports Exported": r.get("report_generated"),
                })
            df_export = pd.DataFrame(export_rows)
            csv_data = df_export.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Export Audit Log (CSV)",
                data=csv_data,
                file_name=f"Financial_Analysis_History_User_{user_id}.csv",
                mime="text/csv",
                use_container_width=True,
                help="Download full filtered history as a CSV spreadsheet.",
            )

    if not filtered_records:
        st.info("ℹ️ No historical records match your search and filter criteria. Try clearing the filter.")
        return

    # 4. Chronological Audit Log Cards
    for record in filtered_records:
        rec_id = record["id"]
        c_name = record.get("company_name", "Unknown")
        fy = record.get("financial_year", "N/A")
        analysis_dt = format_indian_date(record.get("analysis_date"))
        rev = record.get("total_revenue")
        profit = record.get("net_profit")
        ratios_count = record.get("ratios_calculated", 14)
        rep_count = record.get("report_generated", 0)
        stmt_id = record.get("statement_id")

        with st.expander(
            f"📌 Log #{rec_id} &bull; **{c_name}** &bull; {fy} &bull; Date: {analysis_dt} &bull; (Reports: {rep_count})",
            expanded=False,
        ):
            c_top1, c_top2, c_top3, c_top4 = st.columns(4)
            with c_top1:
                st.metric("Total Revenue", format_indian_currency(rev, compact=True))
            with c_top2:
                st.metric("Net Profit", format_indian_currency(profit, compact=True))
            with c_top3:
                st.metric("Ratios Evaluated", f"{ratios_count} / 14")
            with c_top4:
                st.metric("PDF Reports", f"{rep_count} Downloaded")

            st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

            # Retrieve statement details if available
            statement = database.get_statement(user_id=user_id, statement_id=stmt_id) if stmt_id else None

            if statement:
                # Calculate live health snapshot
                ratios = calculations.calculate_all_ratios(statement)
                health = analysis.compute_comprehensive_financial_health(ratios)
                score = health.get("overall_score", 0.0)
                grade = health.get("health_grade", "Moderate")

                st.markdown(
                    f"""
                    <div style="background-color: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px;
                                padding: 12px 16px; margin: 8px 0 14px 0;">
                        <div style="font-size: 0.8rem; font-weight: 700; color: #64748B; text-transform: uppercase;">
                            Archived Health Score
                        </div>
                        <div style="font-size: 1.25rem; font-weight: 800; color: #1E3A8A; margin: 4px 0;">
                            {score:.1f} / 100 &mdash; <span style="font-size: 0.95rem; color: #15803D;">{grade}</span>
                        </div>
                        <div style="font-size: 0.8rem; color: #64748B;">
                            <b>Gross Profit:</b> {format_indian_currency(statement.get('gross_profit'))} &bull;
                            <b>Operating Income:</b> {format_indian_currency(statement.get('operating_income'))} &bull;
                            <b>Total Assets:</b> {format_indian_currency(statement.get('total_assets'))}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            # Action Buttons Row
            btn_col1, btn_col2, btn_col3 = st.columns([1.2, 1.2, 1.5])

            with btn_col1:
                if st.button("📈 View Ratio Analysis", key=f"hist_ratios_{rec_id}", use_container_width=True):
                    if on_navigate_callback:
                        on_navigate_callback("Ratio Analysis")
                    else:
                        st.session_state["nav_selection"] = "Ratio Analysis"
                        st.rerun()

            with btn_col2:
                if st.button("📄 Export PDF Report", key=f"hist_pdf_{rec_id}", use_container_width=True):
                    if on_navigate_callback:
                        on_navigate_callback("Reports")
                    else:
                        st.session_state["nav_selection"] = "Reports"
                        st.rerun()

            with btn_col3:
                # Safe Delete with explicit confirmation
                with st.popover("🗑️ Delete Audit Entry", use_container_width=True):
                    st.markdown(f"**Delete Audit Entry #{rec_id}?**")
                    st.caption(
                        "This deletes this audit record from your history timeline. "
                        "The underlying company and financial statements remain safe."
                    )
                    confirm_delete = st.checkbox(
                        "Yes, remove this audit entry",
                        key=f"confirm_del_{rec_id}",
                    )
                    if st.button(
                        "Confirm Deletion",
                        key=f"do_del_{rec_id}",
                        type="primary",
                        disabled=not confirm_delete,
                        use_container_width=True,
                    ):
                        success = database.delete_analysis(user_id=user_id, analysis_id=rec_id)
                        if success:
                            st.success(f"Audit log #{rec_id} successfully deleted.")
                            st.rerun()
                        else:
                            st.error("Failed to delete audit record.")
