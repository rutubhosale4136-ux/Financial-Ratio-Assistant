"""Rule-based financial interpretation engine.

College Project: Financial Statement Ratio Analysis Assistant
This is a deterministic, rule-based financial analysis system (not an LLM/generative model).
It assigns ratings (Healthy, Moderate, Needs Attention, Not Available), computes a 0-100
overall financial health score, and provides actionable insights based on established
Indian financial standards.
"""

from typing import Any, Dict, List, Optional, Tuple
import calculations


STATUS_HEALTHY = "Healthy"
STATUS_MODERATE = "Moderate"
STATUS_ATTENTION = "Needs Attention"
STATUS_NA = "Not Available"


def evaluate_single_ratio(key: str, value: Optional[float]) -> Dict[str, Any]:
    """Evaluate a single ratio against deterministic benchmarks.

    Returns:
        dict: {
            "key": str,
            "name": str,
            "value": float | None,
            "unit": str,
            "status": str ("Healthy", "Moderate", "Needs Attention", "Not Available"),
            "badge_color": str ("green", "blue", "orange", "red", "grey"),
            "score": float (0.0 to 100.0),
            "headline": str,
            "detailed_insight": str,
            "recommendation": str,
        }
    """
    meta = calculations.RATIO_METADATA.get(key, {})
    name = meta.get("name", key)
    unit = meta.get("unit", "")

    if value is None:
        return {
            "key": key,
            "name": name,
            "value": None,
            "unit": unit,
            "status": STATUS_NA,
            "badge_color": "grey",
            "score": 0.0,
            "headline": "Data Not Available",
            "detailed_insight": "This metric cannot be calculated due to zero or unrecorded statement inputs (e.g. no debt, missing opening/closing balances).",
            "recommendation": "Provide the necessary financial statement lines to unlock this analysis.",
        }

    try:
        val = float(value)
    except (ValueError, TypeError):
        return {
            "key": key,
            "name": name,
            "value": None,
            "unit": unit,
            "status": STATUS_NA,
            "badge_color": "grey",
            "score": 0.0,
            "headline": "Data Not Available",
            "detailed_insight": "This metric cannot be calculated due to zero or unrecorded statement inputs (e.g. no debt, missing opening/closing balances).",
            "recommendation": "Provide the necessary financial statement lines to unlock this analysis.",
        }

    # 1. LIQUIDITY RATIOS
    if key == "current_ratio":
        if val >= 2.0:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_HEALTHY, "badge_color": "green", "score": 100.0,
                "headline": "Robust Short-Term Liquidity Buffer",
                "detailed_insight": f"Current assets exceed short-term liabilities by {val:.2f}x. The enterprise possesses ample working capital to absorb operational delays without liquidity strain.",
                "recommendation": "Maintain optimal liquidity while ensuring excess idle cash is deployed into short-term liquid funds or productive business assets.",
            }
        elif val >= 1.2:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_MODERATE, "badge_color": "blue", "score": 75.0,
                "headline": "Adequate Working Capital Buffer",
                "detailed_insight": f"At {val:.2f}x, current assets cover obligations due within 12 months, though the safety cushion is moderate.",
                "recommendation": "Accelerate customer receivables collection and align supplier credit terms to prevent temporary cash bottlenecks.",
            }
        else:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_ATTENTION, "badge_color": "red", "score": 35.0,
                "headline": "Deficit Working Capital Position",
                "detailed_insight": f"Current ratio of {val:.2f}x indicates current liabilities surpass short-term assets. High risk of liquidity stress.",
                "recommendation": "Urgent attention required: renegotiate short-term vendor credit, establish an emergency overdraft/CC limit, or inject long-term equity.",
            }

    elif key == "quick_ratio":
        if val >= 1.0:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_HEALTHY, "badge_color": "green", "score": 100.0,
                "headline": "Exceptional Acid-Test Solvency",
                "detailed_insight": f"Quick ratio stands at {val:.2f}x. The business can satisfy 100% of its immediate obligations without needing to liquidate inventory.",
                "recommendation": "Strong position. Continue monitoring trade receivables aging to maintain high collection velocity.",
            }
        elif val >= 0.7:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_MODERATE, "badge_color": "blue", "score": 70.0,
                "headline": "Fair Quick Liquidity",
                "detailed_insight": f"At {val:.2f}x, quick assets partially cover liabilities. Settle obligations relying moderately on fresh inventory sales.",
                "recommendation": "Review slow-moving inventory to convert inactive stocks into readily available bank balances.",
            }
        else:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_ATTENTION, "badge_color": "red", "score": 30.0,
                "headline": "Excessive Inventory Dependency",
                "detailed_insight": f"Quick ratio of {val:.2f}x exposes the firm to severe liquidity squeezes if customer orders stall or inventory cycles slow down.",
                "recommendation": "Reduce holding stock levels, offer prompt cash discounts to speed up receivables, and secure working capital credit.",
            }

    elif key == "cash_ratio":
        if val >= 0.4:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_HEALTHY, "badge_color": "green", "score": 100.0,
                "headline": "Superior Immediate Cash Reserves",
                "detailed_insight": f"Cash reserves cover {val:.2f}x of current liabilities immediately without relying on receivables or inventory.",
                "recommendation": "Explore deploying non-operational cash balances into risk-free Indian overnight or liquid mutual funds.",
            }
        elif val >= 0.15:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_MODERATE, "badge_color": "blue", "score": 70.0,
                "headline": "Normal Operating Cash Float",
                "detailed_insight": f"Cash ratio is {val:.2f}x, reflecting standard treasury management where cash is continuously reinvested.",
                "recommendation": "Maintain a rolling 30-day cash flow forecast to avoid overdraft utilization.",
            }
        else:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_ATTENTION, "badge_color": "orange", "score": 40.0,
                "headline": "Tight Ready Cash Cushion",
                "detailed_insight": f"Low cash ratio of {val:.2f}x leaves little immediate cushion for unpredicted statutory or operational obligations.",
                "recommendation": "Strengthen minimum bank float balances and arrange standby bank credit facilities.",
            }

    # 2. PROFITABILITY RATIOS
    elif key == "gross_profit_margin":
        if val >= 35.0:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_HEALTHY, "badge_color": "green", "score": 100.0,
                "headline": "High Pricing Power & Cost Efficiency",
                "detailed_insight": f"Gross profit margin of {val:.2f}% indicates strong value addition, effective raw material procurement, and pricing leverage.",
                "recommendation": "Leverage healthy margins to reinvest in research, market expansion, and production automation.",
            }
        elif val >= 15.0:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_MODERATE, "badge_color": "blue", "score": 75.0,
                "headline": "Standard Industry Gross Margin",
                "detailed_insight": f"Gross margin of {val:.2f}% is typical for competitive manufacturing and trading segments in India.",
                "recommendation": "Seek bulk purchasing economies or optimize transport logistics to widen gross margins by 2-3%.",
            }
        else:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_ATTENTION, "badge_color": "red", "score": 35.0,
                "headline": "Thin Gross Margin Exposure",
                "detailed_insight": f"Gross margin of {val:.2f}% leaves insufficient margin to absorb overheads, interest, and taxes.",
                "recommendation": "Conduct thorough bill-of-materials cost audit, renegotiate supplier contracts, and consider selective price adjustments.",
            }

    elif key == "net_profit_margin":
        if val >= 15.0:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_HEALTHY, "badge_color": "green", "score": 100.0,
                "headline": "Outstanding Bottom-Line Profitability",
                "detailed_insight": f"Generating {val:.2f}% net income from turnover indicates superior overhead containment and efficient financial gearing.",
                "recommendation": "Sustain operational discipline and reward shareholders through dividend payouts or growth reserves.",
            }
        elif val >= 5.0:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_MODERATE, "badge_color": "blue", "score": 75.0,
                "headline": "Healthy Net Profit Generation",
                "detailed_insight": f"Net profit margin of {val:.2f}% delivers positive net value to shareholders.",
                "recommendation": "Benchmark operating expenses against industry leaders to eliminate non-productive overheads.",
            }
        elif val >= 0.0:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_ATTENTION, "badge_color": "orange", "score": 45.0,
                "headline": "Narrow Bottom-Line Cushion",
                "detailed_insight": f"Thin net margin of {val:.2f}% makes the business vulnerable to unexpected expense spikes or turnover dips.",
                "recommendation": "Review debt service interest rates and implement administrative expenditure controls.",
            }
        else:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_ATTENTION, "badge_color": "red", "score": 10.0,
                "headline": "Operating at a Net Loss",
                "detailed_insight": f"Negative net margin of {val:.2f}% signifies that total expenses exceed business turnover.",
                "recommendation": "Implement turnaround strategy: discontinue loss-making product lines and restructure interest costs.",
            }

    elif key == "return_on_assets":
        if val >= 10.0:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_HEALTHY, "badge_color": "green", "score": 100.0,
                "headline": "Superior Asset Productivity",
                "detailed_insight": f"Generating ₹{val:.2f} of net profit for every ₹100 of total assets employed indicates elite capital efficiency.",
                "recommendation": "Document best operational practices across business divisions to preserve asset productivity.",
            }
        elif val >= 4.0:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_MODERATE, "badge_color": "blue", "score": 70.0,
                "headline": "Moderate Capital Efficiency",
                "detailed_insight": f"ROA of {val:.2f}% is in line with capital-intensive industries.",
                "recommendation": "Identify underutilized fixed machinery or idle facilities to boost revenue per asset unit.",
            }
        else:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_ATTENTION, "badge_color": "red", "score": 30.0,
                "headline": "Underperforming Asset Base",
                "detailed_insight": f"ROA of {val:.2f}% reveals low earnings generation relative to the total scale of assets deployed.",
                "recommendation": "Divest obsolete machinery or non-core assets to reduce capital drag.",
            }

    elif key == "return_on_equity":
        if val >= 18.0:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_HEALTHY, "badge_color": "green", "score": 100.0,
                "headline": "Superior Return for Shareholders",
                "detailed_insight": f"ROE of {val:.2f}% significantly outperforms prevailing Indian risk-free return benchmarks (RBI repo rate ~6.5%).",
                "recommendation": "Maintain capital allocation discipline to protect high equity returns.",
            }
        elif val >= 8.0:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_MODERATE, "badge_color": "blue", "score": 70.0,
                "headline": "Acceptable Equity Return",
                "detailed_insight": f"At {val:.2f}%, return on equity exceeds the cost of capital moderately.",
                "recommendation": "Improve net profit margins to lift overall equity returns into double digits.",
            }
        else:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_ATTENTION, "badge_color": "red", "score": 25.0,
                "headline": "Subdued Return on Equity",
                "detailed_insight": f"ROE of {val:.2f}% represents unsatisfactory wealth creation for equity stakeholders.",
                "recommendation": "Focus on margin expansion and revenue growth before raising additional equity capital.",
            }

    # 3. SOLVENCY RATIOS
    elif key == "debt_to_equity":
        if val <= 0.8:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_HEALTHY, "badge_color": "green", "score": 100.0,
                "headline": "Conservative Financial Leverage",
                "detailed_insight": f"Debt-to-Equity of {val:.2f}x demonstrates strong equity backing with low reliance on bank debt.",
                "recommendation": "Strong balance sheet provides borrowing headroom for future strategic acquisitions or capacity expansions.",
            }
        elif val <= 1.8:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_MODERATE, "badge_color": "blue", "score": 75.0,
                "headline": "Balanced Capital Structure",
                "detailed_insight": f"D/E ratio of {val:.2f}x is well within prudent Indian banking norms.",
                "recommendation": "Ensure operating cash flows remain consistent to service debt obligations comfortably.",
            }
        else:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_ATTENTION, "badge_color": "red", "score": 35.0,
                "headline": "Elevated Debt Leverage Risk",
                "detailed_insight": f"High D/E of {val:.2f}x indicates debt heavily outweighs equity, amplifying financial vulnerability during interest rate hikes.",
                "recommendation": "Prioritize deleveraging: apply operating cash flow toward paying down principal debt balances.",
            }

    elif key == "debt_ratio":
        if val <= 40.0:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_HEALTHY, "badge_color": "green", "score": 100.0,
                "headline": "Strong Solvency Position",
                "detailed_insight": f"Only {val:.2f}% of assets are funded via external liabilities. Strong long-term solvency cushion.",
                "recommendation": "Maintain prudent capital preservation while exploring growth opportunities.",
            }
        elif val <= 65.0:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_MODERATE, "badge_color": "blue", "score": 70.0,
                "headline": "Moderate Liability Exposure",
                "detailed_insight": f"External liabilities finance {val:.2f}% of company assets.",
                "recommendation": "Monitor debt repayment schedules to ensure debt maturity is staggered across future financial years.",
            }
        else:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_ATTENTION, "badge_color": "red", "score": 30.0,
                "headline": "High Liability Risk",
                "detailed_insight": f"Over {val:.2f}% of total assets are financed by creditors and lenders.",
                "recommendation": "Cap external borrowing and improve retained earnings to build equity reserves.",
            }

    elif key == "interest_coverage":
        if val >= 4.0:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_HEALTHY, "badge_color": "green", "score": 100.0,
                "headline": "Comfortable Interest Servicing Ability",
                "detailed_insight": f"Operating earnings cover interest costs by {val:.2f}x, meeting credit rating benchmarks for investment-grade status.",
                "recommendation": "Maintain credit rating profile to negotiate lower borrowing spreads from banks.",
            }
        elif val >= 1.8:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_MODERATE, "badge_color": "blue", "score": 70.0,
                "headline": "Adequate Debt Service Coverage",
                "detailed_insight": f"Operating income covers interest by {val:.2f}x, meeting basic debt-service requirements.",
                "recommendation": "Refinance high-cost debt into lower-interest corporate facilities where available.",
            }
        else:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_ATTENTION, "badge_color": "red", "score": 25.0,
                "headline": "Distressed Debt Service Capacity",
                "detailed_insight": f"Critical interest coverage of {val:.2f}x signals earnings are barely sufficient to service bank interest.",
                "recommendation": "Approach lenders for loan restructuring, moratorium, or debt-to-equity conversion.",
            }

    # 4. EFFICIENCY RATIOS
    elif key == "inventory_turnover":
        if val >= 5.0:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_HEALTHY, "badge_color": "green", "score": 100.0,
                "headline": "Swift Stock Circulation",
                "detailed_insight": f"Inventory turns over {val:.2f}x annually (~{365/val:.0f} days holding period), indicating lean inventory management.",
                "recommendation": "Maintain just-in-time replenishment while avoiding stockouts during seasonal demand peaks.",
            }
        elif val >= 2.5:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_MODERATE, "badge_color": "blue", "score": 70.0,
                "headline": "Standard Inventory Velocity",
                "detailed_insight": f"Inventory turns over {val:.2f}x annually (~{365/val:.0f} days holding period).",
                "recommendation": "Review aged stocks to accelerate turnover cycles.",
            }
        else:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_ATTENTION, "badge_color": "red", "score": 35.0,
                "headline": "Sluggish Inventory Turnover",
                "detailed_insight": f"Slow turnover of {val:.2f}x indicates inventory sits idle for ~{365/val:.0f} days, locking up valuable working capital.",
                "recommendation": "Discount stagnant SKUs, improve demand forecasting, and reduce minimum batch sizes.",
            }

    elif key == "asset_turnover":
        if val >= 1.2:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_HEALTHY, "badge_color": "green", "score": 100.0,
                "headline": "High Capital Utilization Efficiency",
                "detailed_insight": f"Asset turnover of {val:.2f}x demonstrates that the enterprise generates strong revenue relative to assets employed.",
                "recommendation": "Scale operational capacity to sustain revenue momentum.",
            }
        elif val >= 0.7:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_MODERATE, "badge_color": "blue", "score": 70.0,
                "headline": "Moderate Asset Utilization",
                "detailed_insight": f"Asset turnover of {val:.2f}x is normal for manufacturing plants with heavy equipment investments.",
                "recommendation": "Improve plant utilization rates and explore multi-shift operations.",
            }
        else:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_ATTENTION, "badge_color": "red", "score": 35.0,
                "headline": "Sluggish Capital Turnover",
                "detailed_insight": f"Low turnover of {val:.2f}x indicates capital is under-generating top-line sales.",
                "recommendation": "Evaluate operational bottlenecks or sub-contract underutilized machinery capacity.",
            }

    # 5. CASH FLOW RATIOS
    elif key == "operating_cash_flow_ratio":
        if val >= 1.2:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_HEALTHY, "badge_color": "green", "score": 100.0,
                "headline": "Strong Cash Coverage of Obligations",
                "detailed_insight": f"Operating cash flow covers current liabilities by {val:.2f}x, reflecting genuine cash-backed earnings.",
                "recommendation": "Strong position allows self-funding of strategic growth initiatives.",
            }
        elif val >= 0.7:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_MODERATE, "badge_color": "blue", "score": 70.0,
                "headline": "Adequate Operating Cash Generation",
                "detailed_insight": f"At {val:.2f}x, core cash generation provides adequate support for short-term liabilities.",
                "recommendation": "Tighten customer credit terms to convert paper profits into bank deposits faster.",
            }
        else:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_ATTENTION, "badge_color": "red", "score": 30.0,
                "headline": "Cash Flow Deficit Vulnerability",
                "detailed_insight": f"OCF ratio of {val:.2f}x reveals core operations do not produce enough cash to service short-term debts.",
                "recommendation": "Investigate working capital leakage, reduce debtor days, and manage supplier payment cycles.",
            }

    elif key == "free_cash_flow":
        if val > 0:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_HEALTHY, "badge_color": "green", "score": 100.0,
                "headline": "Positive Free Cash Flow Generation",
                "detailed_insight": f"Positive FCF indicates the company generated surplus cash after funding all operating costs and capital investments.",
                "recommendation": "Deploy surplus cash toward debt reduction, dividend distribution, or strategic reserve funds.",
            }
        elif val == 0:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_MODERATE, "badge_color": "blue", "score": 60.0,
                "headline": "Break-Even Free Cash Flow",
                "detailed_insight": "Operating cash flows exactly matched capital expenditures, leaving zero net cash surplus.",
                "recommendation": "Ensure future CapEx investments yield clear incremental revenue.",
            }
        else:
            return {
                "key": key, "name": name, "value": val, "unit": unit,
                "status": STATUS_ATTENTION, "badge_color": "red", "score": 35.0,
                "headline": "Negative Free Cash Flow",
                "detailed_insight": "Capital expenditure exceeded operating cash generated, requiring external borrowings or equity funding.",
                "recommendation": "Pause non-essential capital investments until operating cash generation recovers.",
            }

    return {
        "key": key, "name": name, "value": val, "unit": unit,
        "status": STATUS_MODERATE, "badge_color": "blue", "score": 60.0,
        "headline": "Neutral Metric",
        "detailed_insight": f"Calculated value is {val:.2f}.",
        "recommendation": "Maintain ongoing tracking.",
    }


def compute_comprehensive_financial_health(ratios: Dict[str, Optional[float]]) -> Dict[str, Any]:
    """Compute overall financial score (0-100) and categorized strengths/weaknesses.

    Returns:
        dict: {
            "overall_score": float (0 to 100),
            "health_grade": str,
            "grade_color": str,
            "category_scores": dict,
            "strengths": list of dicts,
            "concerns": list of dicts,
            "all_evaluations": dict,
        }
    """
    evaluations = {}
    # Filter out database metadata columns (e.g. id, user_id, statement_id, calculated_at)
    for key, val in ratios.items():
        if key in ("id", "user_id", "statement_id", "calculated_at", "created_at", "updated_at"):
            continue
        if key not in calculations.RATIO_METADATA:
            continue
        evaluations[key] = evaluate_single_ratio(key, val)

    # Ensure all defined ratios have an evaluation (defaulting to STATUS_NA if not present)
    for key in calculations.RATIO_METADATA:
        if key not in evaluations:
            evaluations[key] = evaluate_single_ratio(key, None)

    # Category definitions with weights
    weights = {
        "Liquidity": (["current_ratio", "quick_ratio", "cash_ratio"], 0.25),
        "Profitability": (["gross_profit_margin", "net_profit_margin", "return_on_assets", "return_on_equity"], 0.30),
        "Solvency": (["debt_to_equity", "debt_ratio", "interest_coverage"], 0.20),
        "Efficiency": (["inventory_turnover", "asset_turnover"], 0.15),
        "Cash Flow": (["operating_cash_flow_ratio", "free_cash_flow"], 0.10),
    }

    category_scores = {}
    weighted_total = 0.0
    active_weight_sum = 0.0

    for cat_name, (keys, cat_weight) in weights.items():
        scores = [evaluations[k]["score"] for k in keys if evaluations[k]["status"] != STATUS_NA]
        if scores:
            cat_avg = sum(scores) / len(scores)
            category_scores[cat_name] = round(cat_avg, 1)
            weighted_total += cat_avg * cat_weight
            active_weight_sum += cat_weight
        else:
            category_scores[cat_name] = 0.0

    final_score = round(weighted_total / active_weight_sum, 1) if active_weight_sum > 0 else 0.0

    if final_score >= 80.0:
        health_grade = "Strong Financial Position"
        grade_color = "green"
    elif final_score >= 65.0:
        health_grade = "Good / Stable Financial Health"
        grade_color = "blue"
    elif final_score >= 50.0:
        health_grade = "Moderate / Watchlist"
        grade_color = "orange"
    else:
        health_grade = "Vulnerable / High Financial Risk"
        grade_color = "red"

    # Identify Key Strengths and Critical Concerns
    strengths = [e for e in evaluations.values() if e["status"] == STATUS_HEALTHY and e["score"] >= 90.0]
    concerns = [e for e in evaluations.values() if e["status"] == STATUS_ATTENTION]

    return {
        "overall_score": final_score,
        "health_grade": health_grade,
        "grade_color": grade_color,
        "category_scores": category_scores,
        "strengths": strengths,
        "concerns": concerns,
        "all_evaluations": evaluations,
    }
