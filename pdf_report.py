"""Professional PDF Report Generator using ReportLab.

College Project: Financial Statement Ratio Analysis Assistant
This module generates an executive-grade, multi-page financial analysis report:
- White and navy-blue color palette (#1E3A8A)
- Full Indian financial formatting (INR ₹, Indian comma grouping 3,2,2, Lakhs/Crores, DD-MM-YYYY)
- Safe font registration with Arial and Unicode Rupee (₹) symbol support
- 14 Financial Ratios grouped by Liquidity, Profitability, Solvency, Efficiency, and Cash Flow
- Health Scorecard with Category Pillar Scores (0-100)
- Highlighted Key Strengths and Critical Concerns
- Financial Statement Breakdown (Income Statement, Balance Sheet, Cash Flow)
- Dynamic two-pass NumberedCanvas with page numbering ("Page X of Y")
"""

import os
import io
from datetime import datetime
from typing import Any, Dict, List, Optional

from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

import calculations
import analysis


# ============================================================================
# Font Setup & Unicode Rupee Configuration
# ============================================================================

def _setup_fonts():
    """Register Arial TrueType fonts on Windows to support the Unicode ₹ symbol."""
    font_paths = {
        "Arial": "C:/Windows/Fonts/arial.ttf",
        "Arial-Bold": "C:/Windows/Fonts/arialbd.ttf",
        "Arial-Italic": "C:/Windows/Fonts/ariali.ttf",
        "Arial-BoldItalic": "C:/Windows/Fonts/arialbi.ttf",
    }
    can_use_arial = True
    for name, path in font_paths.items():
        if os.path.exists(path):
            try:
                pdfmetrics.registerFont(TTFont(name, path))
            except Exception:
                can_use_arial = False
                break
        else:
            can_use_arial = False
            break

    if can_use_arial:
        try:
            registerFontFamily(
                "Arial",
                normal="Arial",
                bold="Arial-Bold",
                italic="Arial-Italic",
                boldItalic="Arial-BoldItalic",
            )
            return "Arial", "Arial-Bold", "Arial-Italic", "₹"
        except Exception:
            pass

    return "Helvetica", "Helvetica-Bold", "Helvetica-Oblique", "Rs."


FONT_NORMAL, FONT_BOLD, FONT_ITALIC, CURRENCY_SYMBOL = _setup_fonts()


# ============================================================================
# Indian Financial Formatting Helpers
# ============================================================================

def format_inr(amount: Optional[float], compact: bool = False) -> str:
    """Format numeric values into Indian Rupee format with Indian comma grouping (3,2,2)."""
    if amount is None:
        return f"{CURRENCY_SYMBOL} 0"
    try:
        val = float(amount)
    except (ValueError, TypeError):
        return f"{CURRENCY_SYMBOL} 0"

    sign = "-" if val < 0 else ""
    abs_val = abs(val)

    if compact:
        if abs_val >= 10_000_000:
            return f"{sign}{CURRENCY_SYMBOL} {abs_val / 10_000_000:.2f} Cr"
        elif abs_val >= 100_000:
            return f"{sign}{CURRENCY_SYMBOL} {abs_val / 100_000:.2f} Lakh"

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
    return f"{sign}{CURRENCY_SYMBOL} {result}"


def format_ratio_val(key: str, val: Optional[float]) -> str:
    """Format ratio value based on unit (%, x, or currency)."""
    if val is None:
        return "N/A"
    meta = calculations.RATIO_METADATA.get(key, {})
    unit = meta.get("unit", "")
    if unit == "%":
        return f"{float(val):.2f}%"
    elif unit == "x":
        return f"{float(val):.2f}x"
    elif unit == "₹":
        return format_inr(val, compact=False)
    return f"{float(val):.2f}"


def format_date_display(date_str: Optional[str]) -> str:
    """Format date to Indian DD-MM-YYYY format."""
    if not date_str:
        return datetime.now().strftime("%d-%m-%Y")
    try:
        clean = str(date_str).strip().split(" ")[0]
        parts = clean.split("-")
        if len(parts) == 3 and len(parts[0]) == 4:
            return f"{parts[2]}-{parts[1]}-{parts[0]}"
        return str(date_str)
    except Exception:
        return str(date_str)


# ============================================================================
# Two-Pass Numbered Canvas for Running Headers and Footers
# ============================================================================

class NumberedCanvas(Canvas):
    """Two-pass canvas that dynamically calculates total pages and renders running headers/footers."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []
        self.doc_company_name = "Enterprise"
        self.doc_financial_year = "FY 2025-26"

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count: int):
        self.saveState()
        page_w, page_h = A4

        # Running Header on page 2 and onwards
        if self._pageNumber > 1:
            self.setFont(FONT_NORMAL, 8)
            self.setFillColor(colors.HexColor("#64748B"))
            self.drawString(36, page_h - 26, f"{self.doc_company_name} • {self.doc_financial_year}")
            self.drawRightString(page_w - 36, page_h - 26, "Financial Statement Ratio Analysis Report")
            self.setStrokeColor(colors.HexColor("#E2E8F0"))
            self.setLineWidth(0.6)
            self.line(36, page_h - 32, page_w - 36, page_h - 32)

        # Running Footer on all pages
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.6)
        self.line(36, 35, page_w - 36, 35)

        self.setFont(FONT_NORMAL, 7.5)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawString(
            36, 22,
            f"Financial Statement Ratio Analysis Assistant • Indian Rupee ({CURRENCY_SYMBOL}) Workspace • Academic Report"
        )
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(page_w - 36, 22, page_str)

        self.restoreState()


# ============================================================================
# PDF Document Builder
# ============================================================================

def generate_pdf_report(
    company: Dict[str, Any],
    statement: Dict[str, Any],
    ratios: Dict[str, Optional[float]],
    health_eval: Dict[str, Any],
    user: Optional[Dict[str, Any]] = None,
    output_path: Optional[str] = None,
) -> bytes:
    """Generate a multi-page executive financial analysis PDF report.

    Args:
        company: Company metadata dict.
        statement: Financial statement figures dict.
        ratios: 14 calculated financial ratios dict.
        health_eval: Comprehensive financial health diagnostic dict.
        user: Logged-in user account dict (optional).
        output_path: Optional file path to write to disk.

    Returns:
        bytes: Raw PDF bytes.
    """
    buffer = io.BytesIO()
    target = output_path if output_path else buffer

    doc = SimpleDocTemplate(
        target,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=45,
    )

    company_name = company.get("company_name", company.get("name", "Unknown Company"))
    industry = company.get("industry", "Not Specified")
    financial_year = company.get("financial_year", statement.get("financial_year", "FY 2025-26"))
    user_name = user.get("full_name", "Academic Analyst") if user else "Academic Analyst"
    analysis_date = format_date_display(statement.get("updated_at", company.get("created_at")))
    gen_time_str = datetime.now().strftime("%d-%m-%Y %H:%M IST")

    # Typography Stylesheet
    base_styles = getSampleStyleSheet()

    styles = {
        "HeaderTitle": ParagraphStyle(
            "HeaderTitle",
            parent=base_styles["Normal"],
            fontName=FONT_BOLD,
            fontSize=15,
            leading=18,
            textColor=colors.white,
        ),
        "HeaderSub": ParagraphStyle(
            "HeaderSub",
            parent=base_styles["Normal"],
            fontName=FONT_NORMAL,
            fontSize=8.5,
            leading=11,
            textColor=colors.HexColor("#93C5FD"),
        ),
        "HeaderMeta": ParagraphStyle(
            "HeaderMeta",
            parent=base_styles["Normal"],
            fontName=FONT_NORMAL,
            fontSize=8,
            leading=11,
            alignment=2,  # Right align
            textColor=colors.HexColor("#E2E8F0"),
        ),
        "SectionHeading": ParagraphStyle(
            "SectionHeading",
            parent=base_styles["Normal"],
            fontName=FONT_BOLD,
            fontSize=12,
            leading=15,
            textColor=colors.HexColor("#142B4A"),
            spaceBefore=12,
            spaceAfter=6,
        ),
        "SubHeading": ParagraphStyle(
            "SubHeading",
            parent=base_styles["Normal"],
            fontName=FONT_BOLD,
            fontSize=9.5,
            leading=12,
            textColor=colors.HexColor("#0F172A"),
        ),
        "BodyDark": ParagraphStyle(
            "BodyDark",
            parent=base_styles["Normal"],
            fontName=FONT_NORMAL,
            fontSize=8.5,
            leading=11,
            textColor=colors.HexColor("#0F172A"),
        ),
        "BodyMuted": ParagraphStyle(
            "BodyMuted",
            parent=base_styles["Normal"],
            fontName=FONT_NORMAL,
            fontSize=8,
            leading=10,
            textColor=colors.HexColor("#64748B"),
        ),
        "TableCell": ParagraphStyle(
            "TableCell",
            parent=base_styles["Normal"],
            fontName=FONT_NORMAL,
            fontSize=8,
            leading=10.5,
            textColor=colors.HexColor("#0F172A"),
        ),
        "TableCellBold": ParagraphStyle(
            "TableCellBold",
            parent=base_styles["Normal"],
            fontName=FONT_BOLD,
            fontSize=8,
            leading=10.5,
            textColor=colors.HexColor("#0F172A"),
        ),
        "TableCellCode": ParagraphStyle(
            "TableCellCode",
            parent=base_styles["Normal"],
            fontName=FONT_NORMAL,
            fontSize=7.5,
            leading=9.5,
            textColor=colors.HexColor("#475569"),
        ),
        "CategoryBanner": ParagraphStyle(
            "CategoryBanner",
            parent=base_styles["Normal"],
            fontName=FONT_BOLD,
            fontSize=8.5,
            leading=11,
            textColor=colors.HexColor("#142B4A"),
        ),
        "BadgeHealthy": ParagraphStyle(
            "BadgeHealthy",
            parent=base_styles["Normal"],
            fontName=FONT_BOLD,
            fontSize=7.5,
            leading=9,
            alignment=1,  # Center
            textColor=colors.HexColor("#15803D"),
        ),
        "BadgeModerate": ParagraphStyle(
            "BadgeModerate",
            parent=base_styles["Normal"],
            fontName=FONT_BOLD,
            fontSize=7.5,
            leading=9,
            alignment=1,
            textColor=colors.HexColor("#2563EB"),
        ),
        "BadgeAttention": ParagraphStyle(
            "BadgeAttention",
            parent=base_styles["Normal"],
            fontName=FONT_BOLD,
            fontSize=7.5,
            leading=9,
            alignment=1,
            textColor=colors.HexColor("#DC2626"),
        ),
        "BadgeNA": ParagraphStyle(
            "BadgeNA",
            parent=base_styles["Normal"],
            fontName=FONT_BOLD,
            fontSize=7.5,
            leading=9,
            alignment=1,
            textColor=colors.HexColor("#64748B"),
        ),
        "ScoreBig": ParagraphStyle(
            "ScoreBig",
            parent=base_styles["Normal"],
            fontName=FONT_BOLD,
            fontSize=22,
            leading=25,
            alignment=1,
            textColor=colors.HexColor("#142B4A"),
        ),
        "ScoreGrade": ParagraphStyle(
            "ScoreGrade",
            parent=base_styles["Normal"],
            fontName=FONT_BOLD,
            fontSize=9.5,
            leading=12,
            alignment=1,
            textColor=colors.HexColor("#15803D") if health_eval.get("grade_color") == "green" else colors.HexColor("#2563EB"),
        ),
        "CalloutTitle": ParagraphStyle(
            "CalloutTitle",
            parent=base_styles["Normal"],
            fontName=FONT_BOLD,
            fontSize=8.5,
            leading=11,
            textColor=colors.HexColor("#0F172A"),
        ),
        "CalloutBullet": ParagraphStyle(
            "CalloutBullet",
            parent=base_styles["Normal"],
            fontName=FONT_NORMAL,
            fontSize=7.8,
            leading=10,
            textColor=colors.HexColor("#334155"),
        ),
    }

    story = []
    page_usable_width = 523.27  # A4 width (595.27) - 2 * 36 margin

    # =========================================================================
    # 1. TOP HEADER BANNER (Deep Navy #1E3A8A)
    # =========================================================================
    header_content = [
        [
            Paragraph("<b>FINANCIAL STATEMENT RATIO ANALYSIS REPORT</b>", styles["HeaderTitle"]),
            Paragraph(f"<b>Report Ref:</b> FSRA-{company.get('id', 1)}-{str(financial_year).replace(' ', '')}<br/><b>Generated:</b> {gen_time_str}", styles["HeaderMeta"]),
        ],
        [
            Paragraph("Automated Solvency, Liquidity, Profitability & Efficiency Diagnostic", styles["HeaderSub"]),
            Paragraph(f"<b>Prepared For:</b> {user_name}", styles["HeaderMeta"]),
        ],
    ]
    header_table = Table(header_content, colWidths=[330, 193.27])
    header_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#142B4A")),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 10))

    # =========================================================================
    # 2. COMPANY & ASSESSMENT METADATA CARD (4 Columns)
    # =========================================================================
    profile_data = [
        [
            Paragraph("<b>Company Name</b>", styles["TableCellBold"]),
            Paragraph(company_name, styles["TableCell"]),
            Paragraph("<b>Financial Year</b>", styles["TableCellBold"]),
            Paragraph(f"<b>{financial_year}</b>", styles["TableCellBold"]),
        ],
        [
            Paragraph("<b>Industry Sector</b>", styles["TableCellBold"]),
            Paragraph(industry, styles["TableCell"]),
            Paragraph("<b>Assessment Date</b>", styles["TableCellBold"]),
            Paragraph(analysis_date, styles["TableCell"]),
        ],
        [
            Paragraph("<b>Total Revenue</b>", styles["TableCellBold"]),
            Paragraph(format_inr(statement.get("revenue"), compact=False), styles["TableCell"]),
            Paragraph("<b>Net Profit</b>", styles["TableCellBold"]),
            Paragraph(format_inr(statement.get("net_income"), compact=False), styles["TableCellBold"]),
        ],
        [
            Paragraph("<b>Total Assets</b>", styles["TableCellBold"]),
            Paragraph(format_inr(statement.get("total_assets"), compact=False), styles["TableCell"]),
            Paragraph("<b>Net Worth / Equity</b>", styles["TableCellBold"]),
            Paragraph(format_inr(statement.get("shareholders_equity"), compact=False), styles["TableCell"]),
        ],
    ]
    profile_table = Table(profile_data, colWidths=[110, 151.6, 110, 151.6])
    profile_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
        ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#E2E8F0")),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ("TOPPADDING", (0, 0), (-1, -1), 4.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(profile_table)
    story.append(Spacer(1, 10))

    # =========================================================================
    # 3. EXECUTIVE FINANCIAL HEALTH SCORECARD & PILLAR RATINGS
    # =========================================================================
    overall_score = health_eval.get("overall_score", 0.0)
    health_grade = health_eval.get("health_grade", "Moderate")
    cat_scores = health_eval.get("category_scores", {})

    scorecard_left = [
        [Paragraph("FINANCIAL HEALTH INDEX", styles["SubHeading"])],
        [Spacer(1, 2)],
        [Paragraph(f"{overall_score:.1f} <font size=10 color='#64748B'>/ 100</font>", styles["ScoreBig"])],
        [Paragraph(f"<b>{health_grade.upper()}</b>", styles["ScoreGrade"])],
        [Spacer(1, 2)],
        [Paragraph(f"<font size=7 color='#64748B'>Evaluated across 14 financial metrics under Indian financial standards.</font>", styles["TableCell"])],
    ]
    table_score_left = Table(scorecard_left, colWidths=[185])
    table_score_left.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))

    # Right side: 5 Pillar Mini-Grid
    pillar_rows = [
        [
            Paragraph("<b>Category Pillar</b>", styles["TableCellBold"]),
            Paragraph("<b>Score</b>", styles["TableCellBold"]),
            Paragraph("<b>Status Rating</b>", styles["TableCellBold"]),
        ],
        [
            Paragraph("💧 <b>Liquidity</b>", styles["TableCell"]),
            Paragraph(f"<b>{cat_scores.get('Liquidity', 0.0):.1f} / 100</b>", styles["TableCellBold"]),
            Paragraph("Healthy" if cat_scores.get('Liquidity', 0) >= 80 else ("Moderate" if cat_scores.get('Liquidity', 0) >= 60 else "Attention"), styles["BadgeHealthy"] if cat_scores.get('Liquidity', 0) >= 80 else styles["BadgeModerate"]),
        ],
        [
            Paragraph("📈 <b>Profitability</b>", styles["TableCell"]),
            Paragraph(f"<b>{cat_scores.get('Profitability', 0.0):.1f} / 100</b>", styles["TableCellBold"]),
            Paragraph("Healthy" if cat_scores.get('Profitability', 0) >= 80 else ("Moderate" if cat_scores.get('Profitability', 0) >= 60 else "Attention"), styles["BadgeHealthy"] if cat_scores.get('Profitability', 0) >= 80 else styles["BadgeModerate"]),
        ],
        [
            Paragraph("🛡️ <b>Solvency</b>", styles["TableCell"]),
            Paragraph(f"<b>{cat_scores.get('Solvency', 0.0):.1f} / 100</b>", styles["TableCellBold"]),
            Paragraph("Healthy" if cat_scores.get('Solvency', 0) >= 80 else ("Moderate" if cat_scores.get('Solvency', 0) >= 60 else "Attention"), styles["BadgeHealthy"] if cat_scores.get('Solvency', 0) >= 80 else styles["BadgeModerate"]),
        ],
        [
            Paragraph("⚙️ <b>Efficiency</b>", styles["TableCell"]),
            Paragraph(f"<b>{cat_scores.get('Efficiency', 0.0):.1f} / 100</b>", styles["TableCellBold"]),
            Paragraph("Healthy" if cat_scores.get('Efficiency', 0) >= 80 else ("Moderate" if cat_scores.get('Efficiency', 0) >= 60 else "Attention"), styles["BadgeHealthy"] if cat_scores.get('Efficiency', 0) >= 80 else styles["BadgeModerate"]),
        ],
        [
            Paragraph("💵 <b>Cash Flow</b>", styles["TableCell"]),
            Paragraph(f"<b>{cat_scores.get('Cash Flow', 0.0):.1f} / 100</b>", styles["TableCellBold"]),
            Paragraph("Healthy" if cat_scores.get('Cash Flow', 0) >= 80 else ("Moderate" if cat_scores.get('Cash Flow', 0) >= 60 else "Attention"), styles["BadgeHealthy"] if cat_scores.get('Cash Flow', 0) >= 80 else styles["BadgeModerate"]),
        ],
    ]
    table_score_right = Table(pillar_rows, colWidths=[130, 95, 95])
    table_score_right.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EFF6FF")),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))

    scorecard_container = [
        [table_score_left, table_score_right]
    ]
    scorecard_table = Table(scorecard_container, colWidths=[195, 328.27])
    scorecard_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FFFFFF")),
        ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#CBD5E1")),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(scorecard_table)
    story.append(Spacer(1, 10))

    # =========================================================================
    # 4. KEY STRENGTHS & CRITICAL CONCERNS CALLOUTS
    # =========================================================================
    strengths = health_eval.get("strengths", [])[:3]
    concerns = health_eval.get("concerns", [])[:3]

    strength_flowables = [
        Paragraph("<b>🌟 KEY FINANCIAL STRENGTHS</b>", styles["CalloutTitle"]),
        Spacer(1, 4),
    ]
    if strengths:
        for s in strengths:
            val_txt = format_ratio_val(s["key"], s["value"])
            strength_flowables.append(
                Paragraph(f"• <b>{s['name']} ({val_txt}):</b> {s['headline']}. {s['detailed_insight']}", styles["CalloutBullet"])
            )
            strength_flowables.append(Spacer(1, 3))
    else:
        strength_flowables.append(
            Paragraph("• Moderate operational indicators maintained across current financial year.", styles["CalloutBullet"])
        )

    concern_flowables = [
        Paragraph("<b>⚠️ CRITICAL CONCERNS & WATCHLIST</b>", styles["CalloutTitle"]),
        Spacer(1, 4),
    ]
    if concerns:
        for c in concerns:
            val_txt = format_ratio_val(c["key"], c["value"])
            concern_flowables.append(
                Paragraph(f"• <b>{c['name']} ({val_txt}):</b> {c['headline']}. {c['recommendation']}", styles["CalloutBullet"])
            )
            concern_flowables.append(Spacer(1, 3))
    else:
        concern_flowables.append(
            Paragraph("• No critical vulnerabilities detected. All ratios meet or exceed established benchmarks.", styles["CalloutBullet"])
        )

    callout_data = [[strength_flowables, concern_flowables]]
    callout_table = Table(callout_data, colWidths=[256, 267.27])
    callout_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), colors.HexColor("#F0FDF4")),  # Light green
        ("BACKGROUND", (1, 0), (1, 0), colors.HexColor("#FEF2F2")),  # Light red
        ("BOX", (0, 0), (0, 0), 1, colors.HexColor("#BBF7D0")),
        ("BOX", (1, 0), (1, 0), 1, colors.HexColor("#FECACA")),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(callout_table)

    # Page Break to ensure Clean 14-Ratio Diagnostic Table fits on Page 2
    story.append(PageBreak())

    # =========================================================================
    # 5. COMPREHENSIVE 14-RATIO DIAGNOSTIC TABLE (Grouped by Category)
    # =========================================================================
    story.append(Paragraph("<b>Comprehensive 14-Ratio Analysis Matrix</b>", styles["SectionHeading"]))
    story.append(Paragraph(
        "Ratios are benchmarked against standard Indian corporate accounting norms. Values marked N/A indicate unrecorded balance inputs or zero denominators.",
        styles["BodyMuted"]
    ))
    story.append(Spacer(1, 6))

    ratio_table_data = [
        [
            Paragraph("<b>Ratio / Metric</b>", styles["TableCellBold"]),
            Paragraph("<b>Standard Formula</b>", styles["TableCellBold"]),
            Paragraph("<b>Result</b>", styles["TableCellBold"]),
            Paragraph("<b>Benchmark</b>", styles["TableCellBold"]),
            Paragraph("<b>Status Rating</b>", styles["TableCellBold"]),
        ]
    ]

    categories_order = [
        ("Liquidity Ratios", ["current_ratio", "quick_ratio", "cash_ratio"]),
        ("Profitability Ratios", ["gross_profit_margin", "net_profit_margin", "return_on_assets", "return_on_equity"]),
        ("Solvency & Leverage Ratios", ["debt_to_equity", "debt_ratio", "interest_coverage"]),
        ("Efficiency & Turnover Ratios", ["inventory_turnover", "asset_turnover"]),
        ("Cash Flow Adequacy Ratios", ["operating_cash_flow_ratio", "free_cash_flow"]),
    ]

    all_evals = health_eval.get("all_evaluations", {})
    row_styles = [
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#142B4A")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("TOPPADDING", (0, 0), (-1, 0), 5),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 5),
        ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#CBD5E1")),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]

    current_row_idx = 1
    for cat_title, keys in categories_order:
        # Category Section Row spanning all columns
        ratio_table_data.append([
            Paragraph(f"<b>{cat_title.upper()}</b>", styles["CategoryBanner"]),
            "", "", "", ""
        ])
        row_styles.extend([
            ("SPAN", (0, current_row_idx), (-1, current_row_idx)),
            ("BACKGROUND", (0, current_row_idx), (-1, current_row_idx), colors.HexColor("#EFF6FF")),
            ("TOPPADDING", (0, current_row_idx), (-1, current_row_idx), 4),
            ("BOTTOMPADDING", (0, current_row_idx), (-1, current_row_idx), 4),
        ])
        current_row_idx += 1

        for k in keys:
            meta = calculations.RATIO_METADATA.get(k, {})
            name = meta.get("name", k)
            formula = meta.get("formula", "")
            benchmark = meta.get("benchmark", "N/A")
            raw_val = ratios.get(k)
            formatted_val = format_ratio_val(k, raw_val)

            ev = all_evals.get(k, {})
            status_text = ev.get("status", "N/A")

            if status_text == "Healthy":
                badge_style = styles["BadgeHealthy"]
            elif status_text == "Moderate":
                badge_style = styles["BadgeModerate"]
            elif status_text == "Needs Attention":
                badge_style = styles["BadgeAttention"]
            else:
                badge_style = styles["BadgeNA"]

            ratio_table_data.append([
                Paragraph(f"<b>{name}</b>", styles["TableCellBold"]),
                Paragraph(formula, styles["TableCellCode"]),
                Paragraph(f"<b>{formatted_val}</b>", styles["TableCellBold"]),
                Paragraph(benchmark, styles["TableCell"]),
                Paragraph(status_text, badge_style),
            ])

            # Alternating subtle row background
            if current_row_idx % 2 == 0:
                row_styles.append(("BACKGROUND", (0, current_row_idx), (-1, current_row_idx), colors.HexColor("#F8FAFC")))

            row_styles.extend([
                ("TOPPADDING", (0, current_row_idx), (-1, current_row_idx), 3.5),
                ("BOTTOMPADDING", (0, current_row_idx), (-1, current_row_idx), 3.5),
            ])
            current_row_idx += 1

    ratio_table = Table(ratio_table_data, colWidths=[125, 140, 85, 85, 88.27])
    ratio_table.setStyle(TableStyle(row_styles))
    story.append(ratio_table)

    # Page Break to ensure Clean Financial Statements Breakdown on Page 3
    story.append(PageBreak())

    # =========================================================================
    # 6. FINANCIAL STATEMENTS BASELINE BREAKDOWN (All values in ₹)
    # =========================================================================
    story.append(Paragraph("<b>Financial Statements Baseline Breakdown</b>", styles["SectionHeading"]))
    story.append(Paragraph(
        f"Verified input figures recorded in SQLite for {company_name} ({financial_year}). All amounts in Indian Rupees ({CURRENCY_SYMBOL}).",
        styles["BodyMuted"]
    ))
    story.append(Spacer(1, 6))

    # Income Statement Table
    inc_data = [
        [Paragraph("<b>Income Statement Line Item</b>", styles["TableCellBold"]), Paragraph("<b>Amount (INR)</b>", styles["TableCellBold"])],
        [Paragraph("Revenue / Top-Line Turnover", styles["TableCell"]), Paragraph(format_inr(statement.get("revenue")), styles["TableCell"])],
        [Paragraph("Cost of Goods Sold (COGS)", styles["TableCell"]), Paragraph(format_inr(statement.get("cost_of_goods_sold")), styles["TableCell"])],
        [Paragraph("<b>Gross Profit</b>", styles["TableCellBold"]), Paragraph(f"<b>{format_inr(statement.get('gross_profit'))}</b>", styles["TableCellBold"])],
        [Paragraph("Operating Expenses (OpEx)", styles["TableCell"]), Paragraph(format_inr(statement.get("operating_expenses")), styles["TableCell"])],
        [Paragraph("<b>Operating Income (EBIT)</b>", styles["TableCellBold"]), Paragraph(f"<b>{format_inr(statement.get('operating_income'))}</b>", styles["TableCellBold"])],
        [Paragraph("Interest Expense", styles["TableCell"]), Paragraph(format_inr(statement.get("interest_expense")), styles["TableCell"])],
        [Paragraph("Tax Expense", styles["TableCell"]), Paragraph(format_inr(statement.get("tax_expense")), styles["TableCell"])],
        [Paragraph("<b>Net Income (Bottom-Line Profit)</b>", styles["TableCellBold"]), Paragraph(f"<b>{format_inr(statement.get('net_income'))}</b>", styles["TableCellBold"])],
    ]
    t_inc = Table(inc_data, colWidths=[250, 273.27])
    t_inc.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EFF6FF")),
        ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#CBD5E1")),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(Paragraph("<b>1. Income Statement Summary</b>", styles["SubHeading"]))
    story.append(Spacer(1, 3))
    story.append(t_inc)
    story.append(Spacer(1, 8))

    # Balance Sheet Table
    bs_data = [
        [Paragraph("<b>Balance Sheet Line Item</b>", styles["TableCellBold"]), Paragraph("<b>Amount (INR)</b>", styles["TableCellBold"])],
        [Paragraph("Current Assets (Total)", styles["TableCell"]), Paragraph(format_inr(statement.get("current_assets")), styles["TableCell"])],
        [Paragraph("• Cash & Cash Equivalents", styles["TableCell"]), Paragraph(format_inr(statement.get("cash_and_cash_equivalents")), styles["TableCell"])],
        [Paragraph("• Closing Inventory", styles["TableCell"]), Paragraph(format_inr(statement.get("inventory")), styles["TableCell"])],
        [Paragraph("<b>Total Assets</b>", styles["TableCellBold"]), Paragraph(f"<b>{format_inr(statement.get('total_assets'))}</b>", styles["TableCellBold"])],
        [Paragraph("Current Liabilities", styles["TableCell"]), Paragraph(format_inr(statement.get("current_liabilities")), styles["TableCell"])],
        [Paragraph("Total Liabilities", styles["TableCell"]), Paragraph(format_inr(statement.get("total_liabilities")), styles["TableCell"])],
        [Paragraph("Total Borrowings / Debt", styles["TableCell"]), Paragraph(format_inr(statement.get("total_debt")), styles["TableCell"])],
        [Paragraph("<b>Shareholders' Equity (Net Worth)</b>", styles["TableCellBold"]), Paragraph(f"<b>{format_inr(statement.get('shareholders_equity'))}</b>", styles["TableCellBold"])],
    ]
    t_bs = Table(bs_data, colWidths=[250, 273.27])
    t_bs.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EFF6FF")),
        ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#CBD5E1")),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(Paragraph("<b>2. Balance Sheet Summary</b>", styles["SubHeading"]))
    story.append(Spacer(1, 3))
    story.append(t_bs)
    story.append(Spacer(1, 8))

    # Cash Flow Statement Table
    cf_data = [
        [Paragraph("<b>Cash Flow Line Item</b>", styles["TableCellBold"]), Paragraph("<b>Amount (INR)</b>", styles["TableCellBold"])],
        [Paragraph("Operating Cash Flow (OCF)", styles["TableCell"]), Paragraph(format_inr(statement.get("operating_cash_flow")), styles["TableCell"])],
        [Paragraph("Capital Expenditure (CapEx)", styles["TableCell"]), Paragraph(format_inr(statement.get("capital_expenditure")), styles["TableCell"])],
        [Paragraph("<b>Free Cash Flow (FCF = OCF - CapEx)</b>", styles["TableCellBold"]), Paragraph(f"<b>{format_inr(statement.get('free_cash_flow'))}</b>", styles["TableCellBold"])],
    ]
    t_cf = Table(cf_data, colWidths=[250, 273.27])
    t_cf.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EFF6FF")),
        ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#CBD5E1")),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(Paragraph("<b>3. Cash Flow Summary</b>", styles["SubHeading"]))
    story.append(Spacer(1, 3))
    story.append(t_cf)
    story.append(Spacer(1, 10))

    # =========================================================================
    # 7. STATUTORY & ACADEMIC DISCLAIMER BOX
    # =========================================================================
    disclaimer_text = (
        "<b>ACADEMIC & STATUTORY DISCLAIMER:</b><br/>"
        "This report was automatically synthesized by the <i>Financial Statement Ratio Analysis Assistant</i>. "
        "It is designed solely for college coursework, academic evaluation, and financial analysis simulations. "
        "All ratios are computed using deterministic formulas in accordance with standard Indian corporate accounting standards. "
        "Undefined mathematical outcomes (division by zero) are explicitly presented as 'N/A' without synthetic substitutions. "
        "This document does not constitute formal auditing, investment advice, or credit rating certification."
    )
    disc_table = Table([[Paragraph(disclaimer_text, styles["TableCell"])]], colWidths=[page_usable_width])
    disc_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F1F5F9")),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(disc_table)

    # =========================================================================
    # Build Document with NumberedCanvas
    # =========================================================================
    def canvas_maker(*args, **kwargs):
        c = NumberedCanvas(*args, **kwargs)
        c.doc_company_name = company_name
        c.doc_financial_year = financial_year
        return c

    doc.build(story, canvasmaker=canvas_maker)

    if output_path:
        with open(output_path, "rb") as f:
            return f.read()
    else:
        buffer.seek(0)
        return buffer.getvalue()
