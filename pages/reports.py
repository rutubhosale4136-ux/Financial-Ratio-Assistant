"""Financial Reports Page for Financial Statement Ratio Analysis Assistant.

College Project: Financial Statement Ratio Analysis Assistant
This page enables the logged-in user to:
1. Select an existing company and financial year.
2. Interactively preview the executive financial scorecard, pillar scores, and 14 ratios.
3. Generate and download a branded, multi-page PDF report in Indian Rupees (₹).
4. Automatically update the database report generation counter (reflected on Dashboard).
"""

import streamlit as st
import database
import calculations
import analysis
import pdf_report
from pages.dashboard import format_indian_currency, format_indian_date


def record_download_event(user_id: int, analysis_id: int):
    """Callback triggered when the user downloads the PDF report."""
    if analysis_id:
        try:
            database.mark_report_generated(user_id, analysis_id)
            st.session_state["last_downloaded_report"] = analysis_id
        except Exception:
            pass


def render_reports_page(current_user: dict):
    """Render the Reports Generation and Download page."""
    user_id = current_user["id"]

    # Header
    st.markdown(
        """
        <div style="margin-bottom: 20px;">
            <h2 style="color: #142B4A; font-weight: 700; margin-bottom: 4px;">📄 Executive Financial Reports</h2>
            <p style="color: #5A6E85; margin-top: 0; font-size: 0.95rem;">
                Generate, preview, and download formal multi-page PDF audit reports formatted in Indian Rupees (₹).
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 1. Fetch User Companies
    companies = database.list_companies(user_id)

    if not companies:
        st.markdown(
            """
            <div style="background-color: #FFFFFF; border: 1.5px dashed #CBD5E1;
                        border-radius: 12px; padding: 36px 24px; text-align: center; margin-top: 16px;">
                <div style="font-size: 2.5rem; margin-bottom: 12px;">🏢</div>
                <h3 style="color: #1E3A8A; margin-bottom: 8px;">No Companies Registered</h3>
                <p style="color: #64748B; max-width: 500px; margin: 0 auto 20px auto; font-size: 0.95rem;">
                    You need to register at least one company and enter its financial statements before generating PDF reports.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        col1, _, _ = st.columns([1.2, 1, 2])
        with col1:
            if st.button("➕ Go to Company Management", type="primary", use_container_width=True):
                st.session_state["nav_selection"] = "Company Management"
                st.rerun()
        return

    # 2. Company & Financial Year Selection
    col_sel1, col_sel2 = st.columns([1.5, 1.2])

    company_options = {c["id"]: f"{c['company_name']} ({c['industry']})" for c in companies}
    with col_sel1:
        selected_company_id = st.selectbox(
            "Select Company for Report",
            options=list(company_options.keys()),
            format_func=lambda cid: company_options[cid],
            key="report_company_select",
        )

    selected_company = next((c for c in companies if c["id"] == selected_company_id), companies[0])

    # Fetch statements for selected company
    statements = database.list_statements(user_id=user_id, company_id=selected_company_id)

    if not statements:
        st.warning(
            f"⚠️ No financial statements found for **{selected_company['company_name']}**. "
            "Please enter statement data before generating an audit report."
        )
        col1, _, _ = st.columns([1.2, 1, 2])
        with col1:
            if st.button("📑 Enter Financial Statements", type="primary", use_container_width=True):
                st.session_state["nav_selection"] = "Financial Statements"
                st.rerun()
        return

    fy_options = [s["financial_year"] for s in statements]
    with col_sel2:
        selected_fy = st.selectbox(
            "Select Financial Year",
            options=fy_options,
            key="report_fy_select",
        )

    active_statement = next((s for s in statements if s["financial_year"] == selected_fy), statements[0])

    # 3. Calculate Ratios and Health Evaluation
    ratios = calculations.calculate_all_ratios(active_statement)
    health = analysis.compute_comprehensive_financial_health(ratios)

    # 4. Find corresponding analysis_history record for report tracking
    analyses = database.list_analyses(user_id)
    matching_analyses = [
        a for a in analyses
        if a["company_id"] == selected_company_id and a["financial_year"] == selected_fy
    ]
    analysis_id = matching_analyses[0]["id"] if matching_analyses else None

    # Check if download notification is pending
    if st.session_state.get("last_downloaded_report") == analysis_id:
        st.success(
            "✅ **PDF Report downloaded successfully!** "
            "Your report generation counter has been updated on the Dashboard."
        )
        # Clear flag so message does not persist across page switches
        st.session_state.pop("last_downloaded_report", None)

    st.markdown("---")

    # =========================================================================
    # 5. LIVE REPORT PREVIEW
    # =========================================================================
    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, #142B4A 0%, #1D3D66 50%, #2878D0 100%);
                    color: white; border-radius: 12px; padding: 18px 22px; margin-bottom: 20px;
                    box-shadow: 0 4px 12px rgba(20, 43, 74, 0.1);">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <div>
                    <h3 style="margin: 0; color: white; font-size: 1.25rem; font-weight: 700;">
                        📋 Report Preview: {selected_company['company_name']}
                    </h3>
                    <div style="color: #93C5FD; font-size: 0.85rem; margin-top: 4px;">
                        Financial Year: <b>{selected_fy}</b> &bull; Industry: {selected_company['industry']} &bull; Currency: <b>INR (₹)</b>
                    </div>
                </div>
                <div style="text-align: right; margin-top: 6px;">
                    <span style="background-color: #2878D0; color: white; font-size: 0.8rem; font-weight: 600; padding: 4px 12px; border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.25);">
                        Status: Ready for Export
                    </span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Key Financial Metrics Row
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    with m_col1:
        st.markdown('<div class="kpi-card kpi-blue">', unsafe_allow_html=True)
        st.metric("Total Revenue", format_indian_currency(active_statement.get("revenue"), compact=True))
        st.markdown('</div>', unsafe_allow_html=True)
    with m_col2:
        st.markdown('<div class="kpi-card kpi-green">', unsafe_allow_html=True)
        st.metric("Net Profit", format_indian_currency(active_statement.get("net_income"), compact=True))
        st.markdown('</div>', unsafe_allow_html=True)
    with m_col3:
        st.markdown('<div class="kpi-card kpi-teal">', unsafe_allow_html=True)
        st.metric("Total Assets", format_indian_currency(active_statement.get("total_assets"), compact=True))
        st.markdown('</div>', unsafe_allow_html=True)
    with m_col4:
        st.markdown('<div class="kpi-card kpi-purple">', unsafe_allow_html=True)
        st.metric("Shareholders' Equity", format_indian_currency(active_statement.get("shareholders_equity"), compact=True))
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

    # Health Scorecard and Category Pillars
    score_col, pillar_col = st.columns([1, 1.8])

    overall_score = health.get("overall_score", 0.0)
    health_grade = health.get("health_grade", "Moderate")
    cat_scores = health.get("category_scores", {})

    with score_col:
        st.markdown(
            f"""
            <div style="background-color: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 10px;
                        padding: 20px; text-align: center; height: 100%;">
                <div style="font-size: 0.85rem; font-weight: 700; color: #64748B; text-transform: uppercase;">
                    Financial Health Index
                </div>
                <div style="font-size: 2.4rem; font-weight: 800; color: #1E3A8A; margin: 8px 0;">
                    {overall_score:.1f} <span style="font-size: 1rem; color: #94A3B8;">/ 100</span>
                </div>
                <div style="display: inline-block; background-color: #DCFCE7; color: #15803D;
                            font-size: 0.85rem; font-weight: 700; padding: 4px 12px; border-radius: 16px;">
                    {health_grade}
                </div>
                <p style="font-size: 0.75rem; color: #64748B; margin-top: 12px; margin-bottom: 0;">
                    Deterministic benchmark evaluation based on Indian corporate standards.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with pillar_col:
        st.markdown(
            """
            <div style="background-color: #FFFFFF; border: 1.5px solid #CBD5E1; border-radius: 10px; padding: 16px;">
                <div style="font-size: 0.85rem; font-weight: 700; color: #64748B; text-transform: uppercase; margin-bottom: 10px;">
                    Core Financial Pillar Performance
                </div>
            """,
            unsafe_allow_html=True,
        )
        p_cols = st.columns(5)
        pillars_meta = [
            ("💧 Liquidity", cat_scores.get("Liquidity", 0.0)),
            ("📈 Profitability", cat_scores.get("Profitability", 0.0)),
            ("🛡️ Solvency", cat_scores.get("Solvency", 0.0)),
            ("⚙️ Efficiency", cat_scores.get("Efficiency", 0.0)),
            ("💵 Cash Flow", cat_scores.get("Cash Flow", 0.0)),
        ]
        for col, (label, score) in zip(p_cols, pillars_meta):
            with col:
                st.metric(label, f"{score:.1f}")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)

    # Key Strengths & Concerns Preview
    strengths = health.get("strengths", [])[:3]
    concerns = health.get("concerns", [])[:3]

    str_col, con_col = st.columns(2)
    with str_col:
        st.markdown(
            """
            <div style="background-color: #F0FDF4; border: 1px solid #BBF7D0; border-radius: 8px; padding: 14px;">
                <div style="font-weight: 700; color: #15803D; font-size: 0.9rem; margin-bottom: 8px;">
                    🌟 Key Financial Strengths
                </div>
            """,
            unsafe_allow_html=True,
        )
        if strengths:
            for s in strengths:
                val_str = pdf_report.format_ratio_val(s["key"], s["value"])
                st.markdown(f"• **{s['name']} ({val_str}):** {s['headline']}")
        else:
            st.markdown("• Operational indicators stable.")
        st.markdown("</div>", unsafe_allow_html=True)

    with con_col:
        st.markdown(
            """
            <div style="background-color: #FEF2F2; border: 1px solid #FECACA; border-radius: 8px; padding: 14px;">
                <div style="font-weight: 700; color: #B91C1C; font-size: 0.9rem; margin-bottom: 8px;">
                    ⚠️ Critical Concerns & Watchlist
                </div>
            """,
            unsafe_allow_html=True,
        )
        if concerns:
            for c in concerns:
                val_str = pdf_report.format_ratio_val(c["key"], c["value"])
                st.markdown(f"• **{c['name']} ({val_str}):** {c['headline']}")
        else:
            st.markdown("• No critical vulnerabilities detected.")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)

    # Expandable 14-Ratio Details Table
    with st.expander("📊 View Complete 14-Ratio Diagnostic Table Preview", expanded=False):
        table_rows = []
        for key, meta in calculations.RATIO_METADATA.items():
            val = ratios.get(key)
            formatted = pdf_report.format_ratio_val(key, val)
            ev = health.get("all_evaluations", {}).get(key, {})
            table_rows.append({
                "Category": meta.get("category", ""),
                "Ratio / Metric": meta.get("name", key),
                "Formula": meta.get("formula", ""),
                "Result": formatted,
                "Benchmark": meta.get("benchmark", "N/A"),
                "Health Rating": ev.get("status", "N/A"),
            })
        st.dataframe(table_rows, use_container_width=True, hide_index=True)

    st.markdown("---")

    # =========================================================================
    # 6. PDF GENERATION AND DOWNLOAD BUTTON
    # =========================================================================
    clean_company_slug = "".join(c if c.isalnum() else "_" for c in selected_company["company_name"])
    clean_fy_slug = "".join(c if c.isalnum() else "_" for c in selected_fy)
    file_name = f"Financial_Report_{clean_company_slug}_{clean_fy_slug}.pdf"

    # Generate PDF bytes dynamically
    pdf_bytes = pdf_report.generate_pdf_report(
        company=selected_company,
        statement=active_statement,
        ratios=ratios,
        health_eval=health,
        user=current_user,
    )

    pdf_size_kb = len(pdf_bytes) / 1024.0

    dl_col1, dl_col2 = st.columns([1.5, 1])

    with dl_col1:
        st.markdown(
            f"""
            <div style="background-color: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 14px 18px;">
                <div style="font-weight: 700; color: #0F172A; font-size: 1rem;">
                    📄 Document Specifications
                </div>
                <div style="font-size: 0.85rem; color: #64748B; margin-top: 4px;">
                    &bull; <b>Format:</b> A4 Executive Multi-Page PDF &bull; <b>Size:</b> {pdf_size_kb:.1f} KB<br/>
                    &bull; <b>Font:</b> High-definition Arial with native Rupee (₹) glyphs<br/>
                    &bull; <b>Contents:</b> Cover Profile, Health Scorecard, 14 Ratios, Statement Breakdown & Academic Disclaimer
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with dl_col2:
        st.markdown("<div style='height: 6px;'></div>", unsafe_allow_html=True)
        st.download_button(
            label="📥 Download Executive PDF Report",
            data=pdf_bytes,
            file_name=file_name,
            mime="application/pdf",
            type="primary",
            use_container_width=True,
            on_click=record_download_event,
            args=(user_id, analysis_id),
            help="Download the formal analysis report in PDF format with Indian currency formatting.",
        )
