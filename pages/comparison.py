"""Financial Comparison Module.

College Project: Financial Statement Ratio Analysis Assistant
This module implements Step 10:
- Multi-Year Comparison (Same Company across Financial Years)
- Peer Benchmarking (Cross-Company Comparison)
- Year-over-Year (YoY) Growth Metrics & Trend Visualizations
- 5-Pillar Financial Health Radar Comparison
- Side-by-Side Financial Ratios Matrix
- Strict User Data Isolation & Indian Financial Formatting (₹, Lakhs/Crores)
"""

import pandas as pd
import streamlit as st
import database
import calculations
import analysis
import visualization
from pages.dashboard import format_indian_currency, format_indian_date


def render_comparison_page(user: dict):
    """Render the Financial Comparison and Multi-Year Trend screen."""
    user_id = user["id"]

    st.markdown(
        """
        <div style="margin-bottom: 20px;">
            <h1 style="color: #142B4A; font-weight: 700; margin-bottom: 4px;">
                🔄 Financial Comparison & Trend Analysis
            </h1>
            <p style="color: #5A6E85; font-size: 1rem; margin: 0;">
                Track multi-year financial trends (YoY) and benchmark performance across peer companies.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 1. Fetch user companies and statements
    companies = database.list_companies(user_id)
    statements = database.list_statements(user_id)

    if not companies or not statements:
        st.info(
            "ℹ️ **Insufficient Data for Comparison:** You need at least one registered company "
            "with financial statements to run comparisons. Visit **📑 Financial Statements** to record figures."
        )
        if st.button("📑 Enter Financial Statements", type="primary"):
            st.session_state["nav_selection"] = "Financial Statements"
            st.rerun()
        return

    # Tabs for Comparison Modes
    tab_multi_year, tab_peer = st.tabs([
        "📅 Multi-Year Trend (Same Company)",
        "🏢 Peer Benchmarking (Company vs Company)",
    ])

    # ========================================================================
    # TAB 1: MULTI-YEAR COMPARISON
    # ========================================================================
    with tab_multi_year:
        st.markdown("### 📅 Multi-Year Financial Performance Trend")
        st.caption("Evaluate how a company's revenue, margins, liquidity, and solvency evolve across consecutive financial years.")

        # Select company
        comp_map = {c["company_name"]: c for c in companies}
        selected_comp_name = st.selectbox(
            "Select Company for Multi-Year Evaluation *",
            list(comp_map.keys()),
            key="comp_multi_year_select",
        )
        selected_company = comp_map[selected_comp_name]
        company_id = selected_company["id"]

        # Fetch all statements for this company
        company_statements = database.list_statements(user_id, company_id=company_id)

        if len(company_statements) < 2:
            st.warning(
                f"⚠️ **Only {len(company_statements)} Financial Year Found for {selected_comp_name}:**\n\n"
                f"Multi-year trend analysis requires at least **2 financial years** of data. "
                f"Add statement figures for a second financial year (e.g. FY 2023-24 and FY 2024-25) to unlock trend tracking."
            )
            if st.button("➕ Add Another Financial Year Statement", type="primary"):
                st.session_state["nav_selection"] = "Financial Statements"
                st.rerun()
        else:
            # Sort statements chronologically by financial_year
            sorted_stmts = sorted(company_statements, key=lambda x: str(x["financial_year"]))

            # Render Multi-Year Trend Chart
            fig_trend = visualization.create_multi_year_trend_chart(sorted_stmts, company_name=selected_comp_name)
            if fig_trend:
                st.plotly_chart(fig_trend, use_container_width=True)

            # Year-over-Year (YoY) Growth Metrics
            st.markdown("#### 📈 Year-over-Year (YoY) Growth Metrics")

            latest_stmt = sorted_stmts[-1]
            prev_stmt = sorted_stmts[-2]

            rev_curr = float(latest_stmt.get("revenue") or 0.0)
            rev_prev = float(prev_stmt.get("revenue") or 0.0)
            rev_growth = ((rev_curr - rev_prev) / rev_prev * 100) if rev_prev > 0 else 0.0

            prof_curr = float(latest_stmt.get("net_income") or 0.0)
            prof_prev = float(prev_stmt.get("net_income") or 0.0)
            prof_growth = ((prof_curr - prof_prev) / abs(prof_prev) * 100) if prof_prev != 0 else 0.0

            margin_curr = (prof_curr / rev_curr * 100) if rev_curr > 0 else 0.0
            margin_prev = (prof_prev / rev_prev * 100) if rev_prev > 0 else 0.0
            margin_expansion = margin_curr - margin_prev

            g_col1, g_col2, g_col3 = st.columns(3)
            with g_col1:
                st.metric(
                    label=f"Turnover Growth ({prev_stmt['financial_year']} → {latest_stmt['financial_year']})",
                    value=format_indian_currency(rev_curr, compact=True),
                    delta=f"{rev_growth:+.2f}% YoY",
                    delta_color="normal",
                )
            with g_col2:
                st.metric(
                    label=f"Net Profit Growth ({prev_stmt['financial_year']} → {latest_stmt['financial_year']})",
                    value=format_indian_currency(prof_curr, compact=True),
                    delta=f"{prof_growth:+.2f}% YoY",
                    delta_color="normal",
                )
            with g_col3:
                st.metric(
                    label=f"Margin Expansion ({latest_stmt['financial_year']})",
                    value=f"{margin_curr:.2f}%",
                    delta=f"{margin_expansion:+.2f}% pts YoY",
                    delta_color="normal",
                )

            st.markdown("---")

            # Side-by-Side Ratios Comparison Table
            st.markdown("#### 📊 Multi-Year Ratio Comparison Matrix")

            # Collect ratios for all sorted statements
            year_ratios = {}
            for s in sorted_stmts:
                r = database.get_ratios(user_id, s["id"])
                if not r:
                    r = calculations.calculate_all_ratios(s)
                year_ratios[s["financial_year"]] = r

            matrix_rows = []
            for r_key, meta in calculations.RATIO_METADATA.items():
                unit = meta.get("unit", "")
                row = {
                    "Category": meta["category"],
                    "Ratio Name": meta["name"],
                    "Benchmark": meta["benchmark"],
                }

                for yr in sorted_stmts:
                    val = year_ratios[yr["financial_year"]].get(r_key)
                    if val is None:
                        row[yr["financial_year"]] = "N/A"
                    elif unit == "%":
                        row[yr["financial_year"]] = f"{float(val):.2f}%"
                    elif unit == "x":
                        row[yr["financial_year"]] = f"{float(val):.2f}x"
                    elif unit == "₹":
                        row[yr["financial_year"]] = format_indian_currency(val, compact=True)
                    else:
                        row[yr["financial_year"]] = f"{float(val):.2f}"

                matrix_rows.append(row)

            df_matrix = pd.DataFrame(matrix_rows)
            st.dataframe(df_matrix, use_container_width=True, hide_index=True)

    # ========================================================================
    # TAB 2: PEER BENCHMARKING (COMPANY VS COMPANY)
    # ========================================================================
    with tab_peer:
        st.markdown("### 🏢 Cross-Company Peer Benchmarking")
        st.caption("Compare financial metrics, liquidity health, and operational ratios between competing enterprises.")

        if len(companies) < 2:
            st.warning(
                f"⚠️ **Only {len(companies)} Company Found:** "
                "Peer benchmarking requires at least **2 registered companies**. "
                "Go to **🏢 Company Management** to register a second enterprise."
            )
            if st.button("🏢 Add Another Company", type="primary"):
                st.session_state["nav_selection"] = "Company Management"
                st.rerun()
        else:
            # Multi-select peer companies
            all_comp_names = [c["company_name"] for c in companies]
            selected_peers = st.multiselect(
                "Select Companies to Compare (2 or more) *",
                all_comp_names,
                default=all_comp_names[:2],
            )

            if len(selected_peers) < 2:
                st.info("ℹ️ Please select at least 2 companies to compare.")
            else:
                # Find statements for selected peers
                peer_data = {}
                peer_radar_scores = {}

                for c_name in selected_peers:
                    c_obj = next(c for c in companies if c["company_name"] == c_name)
                    c_stmts = database.list_statements(user_id, company_id=c_obj["id"])
                    if c_stmts:
                        latest_s = c_stmts[0]  # latest statement
                        s_ratios = database.get_ratios(user_id, latest_s["id"])
                        if not s_ratios:
                            s_ratios = calculations.calculate_all_ratios(latest_s)

                        health = analysis.compute_comprehensive_financial_health(s_ratios)
                        peer_data[c_name] = {
                            "statement": latest_s,
                            "ratios": s_ratios,
                            "health": health,
                        }
                        peer_radar_scores[c_name] = health["category_scores"]

                if len(peer_data) < 2:
                    st.warning("⚠️ Some of the selected companies do not have saved financial statements yet.")
                else:
                    # 1. 5-Pillar Radar Benchmark Chart
                    st.markdown("#### 🎯 5-Pillar Financial Health Radar Benchmark")
                    fig_radar = visualization.create_peer_comparison_radar_chart(peer_radar_scores)
                    if fig_radar:
                        st.plotly_chart(fig_radar, use_container_width=True)

                    # 2. Executive Health Summary Cards
                    st.markdown("#### 🏆 Overall Health Score Comparison")
                    score_cols = st.columns(len(peer_data))
                    for col, (c_name, p_info) in zip(score_cols, peer_data.items()):
                        with col:
                            h_score = p_info["health"]["overall_score"]
                            h_grade = p_info["health"]["health_grade"]
                            st.metric(
                                label=c_name,
                                value=f"{h_score} / 100",
                                delta=h_grade,
                                delta_color="normal" if h_score >= 65.0 else "inverse",
                            )

                    st.markdown("---")

                    # 3. Side-by-Side Peer Comparison Table
                    st.markdown("#### 📋 Peer Financial Ratio Benchmark Matrix")

                    peer_rows = []
                    for r_key, meta in calculations.RATIO_METADATA.items():
                        unit = meta.get("unit", "")
                        row = {
                            "Category": meta["category"],
                            "Ratio Name": meta["name"],
                            "Benchmark": meta["benchmark"],
                        }

                        for c_name, p_info in peer_data.items():
                            val = p_info["ratios"].get(r_key)
                            col_header = f"{c_name} ({p_info['statement']['financial_year']})"
                            if val is None:
                                row[col_header] = "N/A"
                            elif unit == "%":
                                row[col_header] = f"{float(val):.2f}%"
                            elif unit == "x":
                                row[col_header] = f"{float(val):.2f}x"
                            elif unit == "₹":
                                row[col_header] = format_indian_currency(val, compact=True)
                            else:
                                row[col_header] = f"{float(val):.2f}"

                        peer_rows.append(row)

                    df_peer = pd.DataFrame(peer_rows)
                    st.dataframe(df_peer, use_container_width=True, hide_index=True)
