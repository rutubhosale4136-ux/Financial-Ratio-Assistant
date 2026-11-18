"""Plotly charts for ratios, performance, and financial-year comparison.

College Project: Financial Statement Ratio Analysis Assistant
This module builds interactive Plotly charts adhering to the white and navy-blue
theme, formatted for Indian Rupees (₹).
"""

import pandas as pd
import plotly.graph_objects as go


NAVY_PRIMARY = "#2878D0"       # Royal Blue for Revenue
NAVY_LIGHT = "#3B82F6"
EMERALD_GREEN = "#20A46B"      # Vibrant Green for Net Profit
CORAL_RED = "#EF4444"
AMBER_YELLOW = "#E99A35"       # Amber for Net Margin Line
TEAL_ACCENT = "#13A89E"        # Teal
PURPLE_ACCENT = "#8064C8"      # Purple
DEEP_NAVY = "#142B4A"          # Deep Navy
CARD_BG = "#FFFFFF"
TEXT_COLOR = "#142B4A"
GRID_COLOR = "#EDF2F7"


def format_inr(value):
    """Format numeric value into Indian Rupee string for chart labels and tooltips."""
    if value is None:
        return "₹ 0"
    try:
        val = float(value)
    except (ValueError, TypeError):
        return "₹ 0"

    sign = "-" if val < 0 else ""
    abs_v = abs(val)

    if abs_v >= 10_000_000:
        return f"{sign}₹ {abs_v / 10_000_000:.2f} Cr"
    elif abs_v >= 100_000:
        return f"{sign}₹ {abs_v / 100_000:.2f} Lakh"
    elif abs_v >= 1_000:
        return f"{sign}₹ {abs_v:,.0f}"
    else:
        return f"{sign}₹ {abs_v:.2f}".rstrip("0").rstrip(".")


def create_performance_overview_chart(analyses_records):
    """Create a Plotly bar chart comparing Revenue and Net Profit across analyzed companies.

    Args:
        analyses_records: List of dictionaries from analysis_history or statements.

    Returns:
        go.Figure or None if no records exist.
    """
    if not analyses_records:
        return None

    df = pd.DataFrame(analyses_records)

    # Use company_name and financial_year for labels
    if "company_name" in df.columns and "financial_year" in df.columns:
        df["label"] = df["company_name"] + "<br>(" + df["financial_year"] + ")"
    elif "financial_year" in df.columns:
        df["label"] = df["financial_year"]
    else:
        df["label"] = [f"Record #{i+1}" for i in range(len(df))]

    revenue_col = "total_revenue" if "total_revenue" in df.columns else "revenue"
    profit_col = "net_profit" if "net_profit" in df.columns else "net_income"

    df["rev_val"] = df[revenue_col].fillna(0.0).astype(float)
    df["profit_val"] = df[profit_col].fillna(0.0).astype(float)

    # Hover templates with Indian formatting
    rev_formatted = [format_inr(v) for v in df["rev_val"]]
    profit_formatted = [format_inr(v) for v in df["profit_val"]]

    fig = go.Figure()

    # Revenue Bar
    fig.add_trace(
        go.Bar(
            x=df["label"],
            y=df["rev_val"],
            name="Total Revenue (₹)",
            marker_color=NAVY_PRIMARY,
            customdata=rev_formatted,
            hovertemplate="<b>%{x}</b><br>Revenue: %{customdata}<extra></extra>",
        )
    )

    # Net Profit Bar
    fig.add_trace(
        go.Bar(
            x=df["label"],
            y=df["profit_val"],
            name="Net Profit (₹)",
            marker_color=EMERALD_GREEN,
            customdata=profit_formatted,
            hovertemplate="<b>%{x}</b><br>Net Profit: %{customdata}<extra></extra>",
        )
    )

    fig.update_layout(
        barmode="group",
        plot_bgcolor=CARD_BG,
        paper_bgcolor=CARD_BG,
        margin=dict(l=20, r=20, t=30, b=40),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(color=TEXT_COLOR, size=12),
        ),
        xaxis=dict(
            title="",
            tickfont=dict(color=TEXT_COLOR, size=12),
            showgrid=False,
        ),
        yaxis=dict(
            title="Amount (₹)",
            tickfont=dict(color=TEXT_COLOR, size=11),
            showgrid=True,
            gridcolor=GRID_COLOR,
        ),
        height=340,
    )

    return fig


def create_multi_year_trend_chart(statements_list, company_name: str = ""):
    """Create a Plotly trend chart showing Revenue, Net Profit, and Profit Margin over Financial Years.

    Args:
        statements_list: List of statement dicts sorted chronologically by financial_year.
        company_name: Company name string.

    Returns:
        go.Figure or None.
    """
    if not statements_list or len(statements_list) < 2:
        return None

    years = [s["financial_year"] for s in statements_list]
    revs = [float(s.get("revenue") or 0.0) for s in statements_list]
    profits = [float(s.get("net_income") or 0.0) for s in statements_list]
    margins = [
        round((p / r * 100), 2) if r > 0 else 0.0
        for p, r in zip(profits, revs)
    ]

    rev_labels = [format_inr(v) for v in revs]
    profit_labels = [format_inr(v) for v in profits]

    fig = go.Figure()

    # Revenue Bar
    fig.add_trace(
        go.Bar(
            x=years,
            y=revs,
            name="Revenue (₹)",
            marker_color=NAVY_PRIMARY,
            customdata=rev_labels,
            hovertemplate="<b>%{x}</b><br>Revenue: %{customdata}<extra></extra>",
            yaxis="y1",
        )
    )

    # Net Profit Bar
    fig.add_trace(
        go.Bar(
            x=years,
            y=profits,
            name="Net Profit (₹)",
            marker_color=EMERALD_GREEN,
            customdata=profit_labels,
            hovertemplate="<b>%{x}</b><br>Net Profit: %{customdata}<extra></extra>",
            yaxis="y1",
        )
    )

    # Profit Margin Line
    fig.add_trace(
        go.Scatter(
            x=years,
            y=margins,
            name="Net Margin (%)",
            mode="lines+markers+text",
            text=[f"{m:.1f}%" for m in margins],
            textposition="top center",
            line=dict(color=AMBER_YELLOW, width=3),
            marker=dict(size=8, color=AMBER_YELLOW),
            hovertemplate="<b>%{x}</b><br>Net Margin: %{y:.2f}%<extra></extra>",
            yaxis="y2",
        )
    )

    fig.update_layout(
        title=f"Multi-Year Performance Trend: {company_name}" if company_name else "Multi-Year Performance Trend",
        barmode="group",
        plot_bgcolor=CARD_BG,
        paper_bgcolor=CARD_BG,
        margin=dict(l=20, r=20, t=50, b=40),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(color=TEXT_COLOR, size=11),
        ),
        xaxis=dict(
            title="Financial Year (April &ndash; March)",
            tickfont=dict(color=TEXT_COLOR, size=12),
            showgrid=False,
        ),
        yaxis=dict(
            title="Amount in Indian Rupees (₹)",
            tickfont=dict(color=TEXT_COLOR, size=11),
            showgrid=True,
            gridcolor=GRID_COLOR,
        ),
        yaxis2=dict(
            title="Net Margin (%)",
            tickfont=dict(color=AMBER_YELLOW, size=11),
            overlaying="y",
            side="right",
            showgrid=False,
        ),
        height=380,
    )

    return fig


def create_peer_comparison_radar_chart(categories_scores_by_company: dict):
    """Create a radar chart comparing 5 financial pillars between companies.

    Args:
        categories_scores_by_company: dict mapping company_name -> dict of category -> score (0-100).

    Returns:
        go.Figure or None.
    """
    if not categories_scores_by_company or len(categories_scores_by_company) < 2:
        return None

    categories = ["Liquidity", "Profitability", "Solvency", "Efficiency", "Cash Flow"]
    # Close the radar loop
    radar_cats = categories + [categories[0]]

    colors = ["#2878D0", "#20A46B", "#8064C8", "#13A89E", "#E99A35"]

    fig = go.Figure()

    for idx, (comp_name, scores) in enumerate(categories_scores_by_company.items()):
        values = [scores.get(c, 0.0) for c in categories]
        values.append(values[0])  # close loop

        color = colors[idx % len(colors)]
        fig.add_trace(
            go.Scatterpolar(
                r=values,
                theta=radar_cats,
                fill="toself",
                name=comp_name,
                line=dict(color=color, width=2),
                opacity=0.6,
            )
        )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(size=10, color=TEXT_COLOR),
                gridcolor=GRID_COLOR,
            ),
            angularaxis=dict(
                tickfont=dict(size=12, color=TEXT_COLOR, family="sans-serif"),
                gridcolor=GRID_COLOR,
            ),
            bgcolor=CARD_BG,
        ),
        paper_bgcolor=CARD_BG,
        margin=dict(l=40, r=40, t=30, b=30),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.15,
            xanchor="center",
            x=0.5,
            font=dict(color=TEXT_COLOR, size=11),
        ),
        height=380,
    )

    return fig
