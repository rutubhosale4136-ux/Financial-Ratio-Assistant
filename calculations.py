"""Financial ratio calculations engine.

College Project: Financial Statement Ratio Analysis Assistant
This module implements the 14 standard financial ratio formulas:
- Liquidity Ratios (Current Ratio, Quick Ratio, Cash Ratio)
- Profitability Ratios (Gross Profit Margin, Net Profit Margin, Return on Assets, Return on Equity)
- Solvency Ratios (Debt-to-Equity Ratio, Debt Ratio, Interest Coverage Ratio)
- Efficiency Ratios (Inventory Turnover, Asset Turnover)
- Cash Flow Ratios (Operating Cash Flow Ratio, Free Cash Flow)

Simplified Income Statement & Cash Flow Formulas:
1. Gross Profit = Revenue - Cost of Goods Sold
2. Operating Income (EBIT) = Gross Profit - Operating Expenses
3. Net Income = Operating Income - Interest Expense - Tax Expense
4. Free Cash Flow = Operating Cash Flow - Capital Expenditure

Strict Calculation Safeguards:
- Average Inventory = (Opening Inventory + Closing Inventory) / 2
- Average Total Assets = (Opening Total Assets + Closing Total Assets) / 2
- Division by Zero: Returns None (displayed as N/A in the UI)
- Missing opening/closing values: Returns None (displayed as N/A). Never silently replaces with closing balance.
"""

from typing import Any, Dict, Optional, Tuple


# ============================================================================
# Core Income Statement & Cash Flow Auto-Calculators
# ============================================================================

def compute_gross_profit(revenue: Optional[float], cost_of_goods_sold: Optional[float]) -> Optional[float]:
    """Gross Profit = Revenue - Cost of Goods Sold."""
    if revenue is None or cost_of_goods_sold is None:
        return None
    return float(revenue) - float(cost_of_goods_sold)


def compute_operating_income(gross_profit: Optional[float], operating_expenses: Optional[float]) -> Optional[float]:
    """Operating Income (EBIT) = Gross Profit - Operating Expenses."""
    if gross_profit is None or operating_expenses is None:
        return None
    return float(gross_profit) - float(operating_expenses)


def compute_net_income(
    operating_income: Optional[float],
    interest_expense: Optional[float],
    tax_expense: Optional[float],
) -> Optional[float]:
    """Net Income = Operating Income - Interest Expense - Tax Expense."""
    if operating_income is None:
        return None
    interest = float(interest_expense or 0.0)
    tax = float(tax_expense or 0.0)
    return float(operating_income) - interest - tax


def compute_free_cash_flow(
    operating_cash_flow: Optional[float],
    capital_expenditure: Optional[float],
) -> Optional[float]:
    """Free Cash Flow = Operating Cash Flow - Capital Expenditure."""
    if operating_cash_flow is None or capital_expenditure is None:
        return None
    return float(operating_cash_flow) - float(capital_expenditure)


# ============================================================================
# Average Calculations (Strict Verification)
# ============================================================================

def compute_average(opening: Optional[float], closing: Optional[float]) -> Optional[float]:
    """Calculate the simple average of opening and closing balances.

    Rule: Both opening and closing values must be provided and > 0.
    Missing balances are NEVER silently replaced with closing balances.
    """
    if opening is None or closing is None:
        return None
    try:
        op = float(opening)
        cl = float(closing)
        if op <= 0 or cl <= 0:
            return None
        return (op + cl) / 2.0
    except (ValueError, TypeError):
        return None


# ============================================================================
# Safe Division Helper
# ============================================================================

def _safe_divide(numerator: Optional[float], denominator: Optional[float], multiply_by: float = 1.0) -> Optional[float]:
    """Divide numerator by denominator safely, handling None and zero division."""
    if numerator is None or denominator is None:
        return None
    try:
        num = float(numerator)
        den = float(denominator)
        if den == 0.0:
            return None
        return round((num / den) * multiply_by, 4)
    except (ValueError, TypeError, ZeroDivisionError):
        return None


# ============================================================================
# 14 Financial Ratios Calculator
# ============================================================================

def calculate_all_ratios(data: Dict[str, Any]) -> Dict[str, Optional[float]]:
    """Calculate all 14 financial ratios from financial statement data.

    Returns:
        dict: Mapping of ratio names to float or None (N/A).
    """
    # Extract values safely
    rev = data.get("revenue")
    cogs = data.get("cost_of_goods_sold")
    gp = data.get("gross_profit")
    if gp is None and rev is not None and cogs is not None:
        gp = compute_gross_profit(rev, cogs)

    op_inc = data.get("operating_income")
    int_exp = data.get("interest_expense")
    net_inc = data.get("net_income")

    ca = data.get("current_assets")
    cash = data.get("cash_and_cash_equivalents")
    inv = data.get("inventory")
    ta = data.get("total_assets")
    cl = data.get("current_liabilities")
    tl = data.get("total_liabilities")
    debt = data.get("total_debt")
    equity = data.get("shareholders_equity")

    op_inv = data.get("opening_inventory")
    cl_inv = data.get("closing_inventory")
    avg_inv = compute_average(op_inv, cl_inv)

    op_ta = data.get("opening_total_assets")
    cl_ta = data.get("closing_total_assets")
    avg_ta = compute_average(op_ta, cl_ta)

    ocf = data.get("operating_cash_flow")
    capex = data.get("capital_expenditure")

    # 1. LIQUIDITY RATIOS
    current_ratio = _safe_divide(ca, cl)
    quick_assets = (float(ca) - float(inv)) if (ca is not None and inv is not None) else None
    quick_ratio = _safe_divide(quick_assets, cl)
    cash_ratio = _safe_divide(cash, cl)

    # 2. PROFITABILITY RATIOS (Multiplied by 100 for percentage)
    gross_profit_margin = _safe_divide(gp, rev, multiply_by=100.0)
    net_profit_margin = _safe_divide(net_inc, rev, multiply_by=100.0)
    return_on_assets = _safe_divide(net_inc, avg_ta, multiply_by=100.0)
    return_on_equity = _safe_divide(net_inc, equity, multiply_by=100.0)

    # 3. SOLVENCY RATIOS
    debt_to_equity = _safe_divide(debt, equity)
    debt_ratio = _safe_divide(tl, ta, multiply_by=100.0)  # percentage
    interest_coverage = _safe_divide(op_inc, int_exp)

    # 4. EFFICIENCY RATIOS
    inventory_turnover = _safe_divide(cogs, avg_inv)
    asset_turnover = _safe_divide(rev, avg_ta)

    # 5. CASH FLOW RATIOS
    operating_cash_flow_ratio = _safe_divide(ocf, cl)
    fcf = compute_free_cash_flow(ocf, capex)

    return {
        "current_ratio": current_ratio,
        "quick_ratio": quick_ratio,
        "cash_ratio": cash_ratio,
        "gross_profit_margin": gross_profit_margin,
        "net_profit_margin": net_profit_margin,
        "return_on_assets": return_on_assets,
        "return_on_equity": return_on_equity,
        "debt_to_equity": debt_to_equity,
        "debt_ratio": debt_ratio,
        "interest_coverage": interest_coverage,
        "inventory_turnover": inventory_turnover,
        "asset_turnover": asset_turnover,
        "operating_cash_flow_ratio": operating_cash_flow_ratio,
        "free_cash_flow": fcf,
    }


# ============================================================================
# Metadata & Plain-English Interpretation Rules
# ============================================================================

RATIO_METADATA = {
    "current_ratio": {
        "category": "Liquidity",
        "name": "Current Ratio",
        "unit": "x",
        "formula": "Current Assets / Current Liabilities",
        "explanation": "Measures the company's ability to cover its short-term obligations due within one year using short-term assets.",
        "benchmark": "1.5x - 2.5x",
    },
    "quick_ratio": {
        "category": "Liquidity",
        "name": "Quick Ratio (Acid-Test)",
        "unit": "x",
        "formula": "(Current Assets - Inventory) / Current Liabilities",
        "explanation": "Evaluates instant liquidity by excluding inventory, which takes time to convert into cash.",
        "benchmark": "≥ 1.0x",
    },
    "cash_ratio": {
        "category": "Liquidity",
        "name": "Cash Ratio",
        "unit": "x",
        "formula": "Cash & Cash Equivalents / Current Liabilities",
        "explanation": "The most conservative liquidity ratio, measuring ability to pay off short-term debt immediately with cash.",
        "benchmark": "0.2x - 0.5x",
    },
    "gross_profit_margin": {
        "category": "Profitability",
        "name": "Gross Profit Margin",
        "unit": "%",
        "formula": "(Gross Profit / Revenue) × 100",
        "explanation": "Shows the percentage of revenue remaining after paying the direct costs of producing goods or services.",
        "benchmark": "≥ 20%",
    },
    "net_profit_margin": {
        "category": "Profitability",
        "name": "Net Profit Margin",
        "unit": "%",
        "formula": "(Net Income / Revenue) × 100",
        "explanation": "Indicates how much of each Rupee earned by the company translates into net bottom-line profit.",
        "benchmark": "≥ 10%",
    },
    "return_on_assets": {
        "category": "Profitability",
        "name": "Return on Assets (ROA)",
        "unit": "%",
        "formula": "(Net Income / Average Total Assets) × 100",
        "explanation": "Measures how efficiently management utilizes company assets to generate net earnings.",
        "benchmark": "≥ 5%",
    },
    "return_on_equity": {
        "category": "Profitability",
        "name": "Return on Equity (ROE)",
        "unit": "%",
        "formula": "(Net Income / Shareholders' Equity) × 100",
        "explanation": "Reflects the rate of return generated on the capital invested by shareholders.",
        "benchmark": "≥ 15%",
    },
    "debt_to_equity": {
        "category": "Solvency",
        "name": "Debt-to-Equity Ratio",
        "unit": "x",
        "formula": "Total Debt / Shareholders' Equity",
        "explanation": "Compares total borrowings against shareholders' equity to assess long-term financial leverage.",
        "benchmark": "≤ 1.5x",
    },
    "debt_ratio": {
        "category": "Solvency",
        "name": "Debt Ratio",
        "unit": "%",
        "formula": "(Total Liabilities / Total Assets) × 100",
        "explanation": "Indicates the proportion of company assets financed through debt obligations.",
        "benchmark": "≤ 50%",
    },
    "interest_coverage": {
        "category": "Solvency",
        "name": "Interest Coverage Ratio",
        "unit": "x",
        "formula": "Operating Income / Interest Expense",
        "explanation": "Measures how easily the company can pay interest on its outstanding debt from operating earnings.",
        "benchmark": "≥ 2.5x",
    },
    "inventory_turnover": {
        "category": "Efficiency",
        "name": "Inventory Turnover",
        "unit": "x",
        "formula": "Cost of Goods Sold / Average Inventory",
        "explanation": "Measures how many times inventory is sold and replaced over the financial year.",
        "benchmark": "4x - 8x",
    },
    "asset_turnover": {
        "category": "Efficiency",
        "name": "Asset Turnover Ratio",
        "unit": "x",
        "formula": "Revenue / Average Total Assets",
        "explanation": "Measures the efficiency with which a company deploys its assets to generate revenue.",
        "benchmark": "≥ 1.0x",
    },
    "operating_cash_flow_ratio": {
        "category": "Cash Flow",
        "name": "Operating Cash Flow Ratio",
        "unit": "x",
        "formula": "Operating Cash Flow / Current Liabilities",
        "explanation": "Assesses whether operating cash generation is sufficient to settle short-term obligations.",
        "benchmark": "≥ 1.0x",
    },
    "free_cash_flow": {
        "category": "Cash Flow",
        "name": "Free Cash Flow (FCF)",
        "unit": "₹",
        "formula": "Operating Cash Flow - Capital Expenditure",
        "explanation": "The cash remaining after funding operations and capital investments, available for growth, debt payoff, or dividends.",
        "benchmark": "> 0 (Positive)",
    },
}


def interpret_ratio(key: str, value: Optional[float]) -> Tuple[str, str, str]:
    """Provide rule-based financial interpretation.

    Returns:
        tuple: (status_label, badge_color, interpretation_text)
    """
    if value is None:
        return (
            "Not Available",
            "grey",
            "Unable to calculate ratio due to missing inputs or zero denominator (e.g. no debt or zero interest expense).",
        )

    try:
        val = float(value)
    except (ValueError, TypeError):
        return (
            "Not Available",
            "grey",
            "Unable to calculate ratio due to missing inputs or zero denominator (e.g. no debt or zero interest expense).",
        )

    if key == "current_ratio":
        if val >= 2.0:
            return ("Strong", "green", "Strong short-term liquidity position. Comfortable buffer for obligations.")
        elif val >= 1.2:
            return ("Adequate", "blue", "Adequate liquidity. Current assets exceed short-term debt.")
        else:
            return ("Needs Attention", "red", "Current assets are below current liabilities; potential liquidity strain.")

    elif key == "quick_ratio":
        if val >= 1.0:
            return ("Healthy", "green", "Healthy acid-test ratio. Can settle short-term debt without selling inventory.")
        elif val >= 0.7:
            return ("Moderate", "orange", "Moderate quick liquidity; partly relies on inventory turnover.")
        else:
            return ("Needs Attention", "red", "Weak quick ratio. Instant obligations may require external financing.")

    elif key == "cash_ratio":
        if val >= 0.5:
            return ("Very Strong", "green", "Substantial cash reserves relative to short-term obligations.")
        elif val >= 0.2:
            return ("Adequate", "blue", "Normal cash buffer for operational and debt service needs.")
        else:
            return ("Low", "orange", "Minimal cash buffer; dependent on incoming receivables and daily sales.")

    elif key == "gross_profit_margin":
        if val >= 35.0:
            return ("High", "green", "Excellent gross profitability, reflecting strong pricing power or cost efficiency.")
        elif val >= 15.0:
            return ("Moderate", "blue", "Standard gross margin for manufacturing/trade operations.")
        else:
            return ("Low", "red", "Thin gross margin; vulnerable to raw material cost increases.")

    elif key == "net_profit_margin":
        if val >= 15.0:
            return ("High", "green", "Strong bottom-line profitability after all operating, interest, and tax expenses.")
        elif val >= 5.0:
            return ("Healthy", "blue", "Healthy and sustainable net margin.")
        elif val >= 0.0:
            return ("Thin", "orange", "Low profitability; limited cushion against downturns.")
        else:
            return ("Operating at a Loss", "red", "Negative net profit. Expenses exceed total revenue.")

    elif key == "return_on_assets":
        if val >= 10.0:
            return ("Strong", "green", "Superior asset productivity and operational management.")
        elif val >= 5.0:
            return ("Moderate", "blue", "Acceptable return on asset base.")
        else:
            return ("Needs Attention", "red", "Low asset return. Capital deployed is underperforming.")

    elif key == "return_on_equity":
        if val >= 20.0:
            return ("Excellent", "green", "Outstanding return on shareholders' invested capital.")
        elif val >= 10.0:
            return ("Good", "blue", "Satisfactory equity returns.")
        else:
            return ("Low", "red", "Subdued return for equity investors.")

    elif key == "debt_to_equity":
        if val <= 1.0:
            return ("Conservative", "green", "Conservative leverage. Equity capital comfortably exceeds total debt.")
        elif val <= 2.0:
            return ("Moderate", "blue", "Moderate debt leverage within customary industry levels.")
        else:
            return ("High Leverage", "red", "High debt-to-equity ratio; heightened financial risk in high-interest environments.")

    elif key == "debt_ratio":
        if val <= 40.0:
            return ("Low Debt", "green", "Low proportion of assets financed by liabilities; strong solvency cushion.")
        elif val <= 65.0:
            return ("Moderate Debt", "blue", "Balanced capital structure.")
        else:
            return ("High Debt", "red", "More than 65% of assets funded by debt; aggressive capital structure.")

    elif key == "interest_coverage":
        if val >= 3.0:
            return ("Comfortable", "green", "Operating profits easily service interest charges.")
        elif val >= 1.5:
            return ("Fair", "orange", "Adequate interest coverage, though vulnerable to earnings drops.")
        else:
            return ("At Risk", "red", "Operating earnings struggle to service interest payments.")

    elif key == "inventory_turnover":
        if val >= 6.0:
            return ("Rapid", "green", "Rapid inventory movement with minimal unsold stock risk.")
        elif val >= 3.0:
            return ("Moderate", "blue", "Standard inventory turnover.")
        else:
            return ("Slow Moving", "orange", "Slow inventory turnover; risk of holding excess or obsolete stock.")

    elif key == "asset_turnover":
        if val >= 1.5:
            return ("High Efficiency", "green", "High revenue generation per Rupee of invested assets.")
        elif val >= 0.8:
            return ("Moderate", "blue", "Typical capital turnover.")
        else:
            return ("Low Turnover", "orange", "Sluggish asset efficiency; underutilized capacity.")

    elif key == "operating_cash_flow_ratio":
        if val >= 1.2:
            return ("Strong", "green", "Operating cash flows comfortably exceed short-term obligations.")
        elif val >= 0.8:
            return ("Adequate", "blue", "Cash generated from core business covers immediate liabilities.")
        else:
            return ("Weak", "red", "Operations not generating enough cash to satisfy short-term liabilities.")

    elif key == "free_cash_flow":
        if val > 0:
            return ("Positive Cash Flow", "green", "Company generates excess cash after capital expenditures.")
        elif val == 0:
            return ("Break-Even", "blue", "Operating cash covers capital expenditures exactly.")
        else:
            return ("Negative Cash Flow", "red", "Capital expenditures exceed operating cash generation.")

    return ("Neutral", "grey", "Ratio computed.")
