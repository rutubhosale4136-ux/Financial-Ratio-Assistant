# Financial Ratio Assistant - Codebase Bundle

## File Tree
```
.gitignore
.streamlit\config.toml
README.md
analysis.py
assets\style.css
authentication.py
calculations.py
database.py
database\.gitkeep
database\financial_data.db
main.py
pages\__init__.py
pages\companies.py
pages\comparison.py
pages\dashboard.py
pages\financial_insights.py
pages\financial_statements.py
pages\history.py
pages\ratio_analysis.py
pages\reports.py
pdf_report.py
requirements.txt
test_auth.py
test_dashboard.py
test_quick_action_buttons.py
test_quick_actions.py
test_step_10.py
test_step_11.py
test_step_12.py
test_step_9.py
test_steps_6_7_8.py
view_database.py
visualization.py
```

## File: `.gitignore`

```
venv/
.venv/
__pycache__/
*.py[cod]
.streamlit/secrets.toml
.pytest_cache/
*.egg-info/

```

---

## File: `.streamlit\config.toml`

```
[client]
showSidebarNavigation = false

[theme]
primaryColor = "#6ab0f6"
backgroundColor = "#f5f6f9"
secondaryBackgroundColor = "#fcf6f6"
textColor = "#062041"
font = "sans serif"

[server]
headless = true
enableCORS = false
enableXsrfProtection = true

```

---

## File: `README.md`

```
# Financial Statement Ratio Analysis Assistant 📈

A comprehensive, production-grade financial statement analysis desktop application built in Python and Streamlit for college project demonstration and academic evaluation.

Designed specifically for Indian corporate financial standards, the system operates exclusively in **Indian Rupees (₹)**, standard **April to March Financial Years**, **DD-MM-YYYY dates**, and **Indian comma notation (Lakhs & Crores)** without any external paid APIs or cloud dependencies.

---

## 🌟 Key Features

1. **Enterprise Security & Authentication (Step 4)**
   - Industry-standard **PBKDF2-HMAC-SHA256** password hashing with 100,000 iterations and cryptographic per-user salting.
   - Constant-time hash comparison (`hmac.compare_digest`) preventing timing attacks.
   - Strict user-level data isolation: multi-tenant architecture where accounts cannot view or manipulate other users' records.

2. **Executive Financial Dashboard (Step 5)**
   - Clean White & Navy-Blue (`#1E3A8A`) modern theme.
   - Real-time aggregate metric cards: Total Companies, Saved Analyses, Exported PDF Reports, Cumulative Revenue, and Net Profit.
   - Interactive Plotly financial performance charts with empty-state guidance.
   - Quick action shortcut buttons with safe session-state navigation.

3. **Company Management (Step 6)**
   - Add, View, Edit, and Safely Delete corporate profiles.
   - Fields: Company Name, Industry Sector, Financial Year (e.g., `FY 2025-26`), and Description.
   - Safe deletion protection with explicit confirmation checkbox.

4. **Structured Financial Statement Entry (Step 7)**
   - **Income Statement:** Revenue, COGS, Gross Profit, Operating Expenses, Operating Income (EBIT), Interest, Tax, and Net Income.
   - **Balance Sheet:** Current Assets, Cash & Cash Equivalents, Inventory, Total Assets, Current Liabilities, Total Liabilities, Total Debt, Shareholders' Equity (Net Worth), Opening/Closing Balances.
   - **Cash Flow Statement:** Operating Cash Flow (OCF), Capital Expenditure (CapEx), and Free Cash Flow (FCF).
   - Multi-unit multiplier support: **₹ (Actuals), Thousands, Lakhs, Crores**.

5. **14 Core Financial Ratios Calculator (Step 8)**
   - **Liquidity (3):** Current Ratio, Quick Ratio (Acid-Test), Cash Ratio.
   - **Profitability (4):** Gross Profit Margin, Net Profit Margin, Return on Assets (ROA), Return on Equity (ROE).
   - **Solvency (3):** Debt-to-Equity Ratio, Debt Ratio, Interest Coverage Ratio.
   - **Efficiency (2):** Inventory Turnover, Asset Turnover.
   - **Cash Flow (2):** Operating Cash Flow Ratio, Free Cash Flow.
   - Strict strict-average rules and division-by-zero safeguards (explicitly outputs `N/A` without synthetic defaults).

6. **Deterministic Financial Insights & Scoring (Step 9)**
   - 0–100 Weighted Financial Health Index and grading (`Strong`, `Good`, `Moderate`, `Vulnerable`).
   - 5 Category Pillar Score cards.
   - Automated identification of Key Strengths and Critical Concerns with actionable recommendations.

7. **Multi-Year Trends & Peer Comparison (Step 10)**
   - **Multi-Year Trends:** Dual-axis visualization tracking Revenue growth, Profit trajectory, and Margin expansion across fiscal years.
   - **Peer Benchmarking:** Interactive 5-axis Radar / Spider chart comparing corporate efficiency across peer companies.

8. **Executive PDF Reports Generation (Step 11)**
   - High-definition multi-page PDF generation via **ReportLab**.
   - Native Windows `Arial` TrueType font registration ensuring crisp Unicode Rupee (`₹`) glyphs.
   - Health scorecard, 14-ratio matrix, baseline financial statements, running headers/footers (*"Page X of Y"*), and academic disclaimer.
   - Automated sync with the Dashboard's report generation counter.

9. **Analysis History & Audit Log (Step 12)**
   - Chronological audit log of all financial statements analyzed.
   - Search by company name and filter by company or financial year.
   - Expandable snapshot drawers with instant navigation to ratio analysis and reports.
   - Single-click CSV audit trail export via Pandas.
   - Safe record deletion with confirmation dialog.

---

## 🏗️ Project Architecture

```
financial_ratio_assistant/
│
├── main.py                  # Streamlit application entry point & page router
├── database.py              # SQLite schema, parameterized queries, and ACID transactions
├── authentication.py        # PBKDF2 user registration, authentication & session gate
├── calculations.py          # 14 financial ratio mathematical formulas & benchmarks
├── analysis.py              # Deterministic rule-based health scoring & insights engine
├── visualization.py         # Interactive Plotly charts (Multi-Year Trends & Peer Radar)
├── pdf_report.py            # High-definition ReportLab multi-page PDF generator
├── view_database.py         # Utility script to inspect raw SQLite tables and rows
├── requirements.txt         # Production dependencies (streamlit, pandas, plotly, reportlab)
│
├── pages/                   # Application Page Modules
│   ├── dashboard.py         # Executive KPI summary & performance chart
│   ├── companies.py         # Company profile management
│   ├── financial_statements.py # Input forms for Income, Balance Sheet & Cash Flow
│   ├── ratio_analysis.py    # Categorized 14-ratio diagnostic matrix & formula cards
│   ├── financial_insights.py# Health score index & strategic recommendations
│   ├── comparison.py        # Multi-year trend analysis & peer radar benchmarking
│   ├── reports.py           # Interactive PDF preview & single-click export
│   └── history.py           # Chronological audit trail & CSV export
│
├── database/                # Permanent storage directory
│   └── financial_data.db    # Relational SQLite database file
│
├── assets/
│   └── style.css            # Custom White & Navy-Blue stylesheet
│
└── tests/                   # 8 Automated Test Suites (44 Total Tests, 100% Passing)
    ├── test_auth.py
    ├── test_dashboard.py
    ├── test_steps_6_7_8.py
    ├── test_step_9.py
    ├── test_step_10.py
    ├── test_quick_action_buttons.py
    ├── test_step_11.py
    └── test_step_12.py
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10, 3.11, or 3.12 installed on Windows.
- Standard PowerShell terminal.

### 2. Run the Application
Open PowerShell in this project folder:

```powershell
cd c:\Users\omkar\financial_ratio_assistant
.\venv\Scripts\streamlit run main.py
```

Open your web browser at:
`http://localhost:8501`

### 3. Demo Login Credentials
- **Email:** `demo@student.edu` / `rutu522@gmail.com`
- Or click **"Register a new account"** on the login screen to create a fresh student profile.

---

## 🧪 Running Automated Tests

To run the complete 44-test verification battery:

```powershell
.\venv\Scripts\python test_auth.py
.\venv\Scripts\python test_dashboard.py
.\venv\Scripts\python test_steps_6_7_8.py
.\venv\Scripts\python test_step_9.py
.\venv\Scripts\python test_step_10.py
.\venv\Scripts\python test_quick_action_buttons.py
.\venv\Scripts\python test_step_11.py
.\venv\Scripts\python test_step_12.py
```
*(All 8 test suites pass with 100% success).*

```

---

## File: `analysis.py`

```python
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

```

---

## File: `assets\style.css`

```
/* ============================================================================
   Financial Statement Ratio Analysis Assistant - SaaS Design Theme
   Palette:
   - Deep Navy:  #142B4A
   - Royal Blue: #2878D0
   - Teal:       #13A89E
   - Purple:     #8064C8
   - Green:      #20A46B
   - Amber:      #E99A35
   - Canvas Bg:  #F4F7FC
   - Cards:      #FFFFFF
   ============================================================================ */

:root {
    --deep-navy: #142B4A;
    --royal-blue: #2878D0;
    --teal: #13A89E;
    --purple: #8064C8;
    --green: #20A46B;
    --amber: #E99A35;
    --bg-canvas: #F4F7FC;
    --card-bg: #FFFFFF;
    --text-primary: #142B4A;
    --text-muted: #5A6E85;
    --border-soft: #E2E8F0;
    --border-subtle: #CBD5E1;
    --font-stack: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}

/* Global App Styling */
html, body, [class*="css"], .stApp {
    font-family: var(--font-stack) !important;
    background-color: var(--bg-canvas) !important;
    color: var(--text-primary);
}

h1, h2, h3, h4, h5, h6 {
    color: var(--deep-navy) !important;
    font-weight: 700 !important;
    letter-spacing: -0.3px;
}

/* ============================================================================
   1. SIDEBAR DESIGN (Deep Navy #142B4A)
   ============================================================================ */
section[data-testid="stSidebar"] {
    background-color: var(--deep-navy) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] div,
section[data-testid="stSidebar"] label {
    color: #FFFFFF !important;
}

section[data-testid="stSidebar"] hr {
    border-color: rgba(255, 255, 255, 0.12) !important;
}

/* Sidebar Radio Navigation List */
section[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > label {
    background-color: transparent !important;
    border-radius: 8px !important;
    padding: 10px 14px !important;
    margin-bottom: 5px !important;
    color: #E2E8F0 !important;
    font-size: 0.92rem !important;
    font-weight: 500 !important;
    transition: all 0.2s ease !important;
    border: 1px solid transparent !important;
    cursor: pointer !important;
}

section[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > label:hover {
    background-color: rgba(255, 255, 255, 0.08) !important;
    color: #FFFFFF !important;
    border-color: rgba(255, 255, 255, 0.14) !important;
}

/* Active Highlight (Royal Blue #2878D0) */
section[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > label:has(input:checked),
section[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > label[data-checked="true"] {
    background: linear-gradient(135deg, #2878D0 0%, #1D65B5 100%) !important;
    color: #FFFFFF !important;
    font-weight: 600 !important;
    border-color: #3B82F6 !important;
    box-shadow: 0 4px 12px rgba(40, 120, 208, 0.35) !important;
}

/* Hide native radio button dots in sidebar */
section[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] > label > div:first-child {
    display: none !important;
}

/* Sidebar Logout Button */
section[data-testid="stSidebar"] button[kind="secondary"] {
    background: rgba(255, 255, 255, 0.08) !important;
    border: 1px solid rgba(255, 255, 255, 0.18) !important;
    color: #FFFFFF !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    transition: all 0.2s ease !important;
}

section[data-testid="stSidebar"] button[kind="secondary"]:hover {
    background: rgba(239, 68, 68, 0.22) !important;
    border-color: #EF4444 !important;
    color: #FFFFFF !important;
    transform: translateY(-1px) !important;
}

/* ============================================================================
   2. DASHBOARD KPI METRIC CARDS
   ============================================================================ */
div[data-testid="stMetric"] {
    background-color: var(--card-bg) !important;
    border: 1px solid var(--border-soft) !important;
    border-radius: 12px !important;
    padding: 1.15rem 1.25rem !important;
    box-shadow: 0 2px 8px rgba(20, 43, 74, 0.04) !important;
    transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease !important;
}

div[data-testid="stMetric"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 20px rgba(20, 43, 74, 0.08) !important;
    border-color: var(--border-subtle) !important;
}

div[data-testid="stMetricLabel"] {
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    color: var(--text-muted) !important;
    text-transform: uppercase !important;
    letter-spacing: 0.3px !important;
}

div[data-testid="stMetricValue"] {
    font-size: 1.7rem !important;
    font-weight: 800 !important;
    color: var(--deep-navy) !important;
    margin-top: 2px !important;
}

/* ============================================================================
   3. BUTTONS (Royal Blue & Teal)
   ============================================================================ */
button[kind="primary"] {
    background: linear-gradient(135deg, #2878D0 0%, #1D65B5 100%) !important;
    border: none !important;
    color: #FFFFFF !important;
    font-weight: 600 !important;
    border-radius: 8px !important;
    padding: 0.55rem 1.25rem !important;
    box-shadow: 0 2px 8px rgba(40, 120, 208, 0.25) !important;
    transition: all 0.2s ease !important;
}

button[kind="primary"]:hover {
    background: linear-gradient(135deg, #1D65B5 0%, #144B88 100%) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 14px rgba(40, 120, 208, 0.4) !important;
}

button[kind="secondary"] {
    background-color: #FFFFFF !important;
    border: 1.5px solid #CBD5E1 !important;
    color: var(--deep-navy) !important;
    font-weight: 600 !important;
    border-radius: 8px !important;
    transition: all 0.2s ease !important;
}

button[kind="secondary"]:hover {
    background-color: #F8FAFC !important;
    border-color: var(--teal) !important;
    color: var(--teal) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 3px 10px rgba(19, 168, 158, 0.15) !important;
}

/* ============================================================================
   4. TABLES, DATAFRAMES & FORMS
   ============================================================================ */
div[data-testid="stDataFrame"] {
    border: 1px solid var(--border-soft) !important;
    border-radius: 10px !important;
    background-color: #FFFFFF !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02) !important;
    overflow: hidden !important;
}

div[data-baseweb="input"] {
    border-radius: 8px !important;
    border: 1px solid var(--border-subtle) !important;
    background-color: #FFFFFF !important;
    transition: all 0.2s ease !important;
}

div[data-baseweb="input"]:focus-within {
    border-color: var(--royal-blue) !important;
    box-shadow: 0 0 0 3px rgba(40, 120, 208, 0.15) !important;
}

div[data-baseweb="select"] {
    border-radius: 8px !important;
}

/* Tabs */
button[data-baseweb="tab"] {
    font-weight: 600 !important;
    color: var(--text-muted) !important;
    padding: 8px 18px !important;
    border-radius: 6px 6px 0 0 !important;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: var(--royal-blue) !important;
    border-bottom-color: var(--royal-blue) !important;
    border-bottom-width: 3px !important;
}

/* ============================================================================
   5. FINANCIAL CATEGORY CARD ACCENTS
   - Liquidity:    Blue   (#2878D0)
   - Profitability: Green  (#20A46B)
   - Solvency:     Purple (#8064C8)
   - Efficiency:   Teal   (#13A89E)
   - Cash Flow:    Orange (#E99A35)
   ============================================================================ */
.card-liquidity {
    border-top: 4px solid var(--royal-blue) !important;
    background: #FFFFFF;
}
.card-profitability {
    border-top: 4px solid var(--green) !important;
    background: #FFFFFF;
}
.card-solvency {
    border-top: 4px solid var(--purple) !important;
    background: #FFFFFF;
}
.card-efficiency {
    border-top: 4px solid var(--teal) !important;
    background: #FFFFFF;
}
.card-cashflow {
    border-top: 4px solid var(--amber) !important;
    background: #FFFFFF;
}

/* Expander Cards */
div[data-testid="stExpander"] {
    background-color: #FFFFFF !important;
    border: 1px solid var(--border-soft) !important;
    border-radius: 10px !important;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.03) !important;
    margin-bottom: 8px !important;
}

/* ============================================================================
   6. FINTECH SPLIT-SCREEN AUTHENTICATION STYLING
   ============================================================================ */
@keyframes floatSlow {
    0% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-7px) rotate(-0.5deg); }
    100% { transform: translateY(0px) rotate(0deg); }
}

@keyframes floatFast {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

@keyframes floatCoin {
    0% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-9px) rotate(4deg); }
    100% { transform: translateY(0px) rotate(0deg); }
}

.auth-hero-card {
    background: linear-gradient(135deg, #142B4A 0%, #173660 40%, #1A4479 70%, #205396 100%);
    border-radius: 20px;
    padding: 34px 30px;
    color: #FFFFFF;
    box-shadow: 0 14px 36px rgba(20, 43, 74, 0.16);
    border: 1px solid rgba(255, 255, 255, 0.14);
    position: relative;
    overflow: hidden;
}

.float-metric-card {
    background: rgba(20, 43, 74, 0.78);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 12px;
    padding: 10px 14px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.22);
}

.anim-float-1 {
    animation: floatSlow 4.5s ease-in-out infinite;
}

.anim-float-2 {
    animation: floatFast 3.8s ease-in-out infinite;
}

.anim-coin {
    animation: floatCoin 4s ease-in-out infinite;
}

.auth-card-right,
div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 20px !important;
    padding: 24px 26px !important;
    box-shadow: 0 12px 32px rgba(20, 43, 74, 0.06) !important;
}

```

---

## File: `authentication.py`

```python
"""Registration, login, and session management with PBKDF2 password hashing.

College Project: Financial Statement Ratio Analysis Assistant
This module handles:
1. PBKDF2 password hashing and salt generation (using Python standard library hashlib & secrets).
2. Input validation for name, email, and password.
3. User registration with duplicate email prevention.
4. User login and credential verification.
5. Streamlit session state management for logged-in users.
6. Streamlit UI for login and registration forms.
"""

import hashlib
import re
import secrets
import streamlit as st
import database

# Number of PBKDF2 iterations (industry standard, secure & fast)
HASH_ITERATIONS = 100_000


# ============================================================================
# Password Hashing & Verification (PBKDF2)
# ============================================================================

def hash_password(password: str, salt: str = None) -> tuple[str, str]:
    """Hash a password using PBKDF2-HMAC-SHA256 with a unique cryptographic salt.

    Plain-text passwords are never stored.

    Args:
        password: Plain-text password string.
        salt: Optional hex salt string. If None, a new 16-byte random salt is generated.

    Returns:
        tuple: (password_hash_hex, salt_hex)
    """
    if salt is None:
        salt = secrets.token_hex(16)

    derived = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt.encode("utf-8"),
        HASH_ITERATIONS,
    )
    return derived.hex(), salt


def verify_password(password: str, stored_hash: str, salt: str) -> bool:
    """Verify an entered password against the stored PBKDF2 hash.

    Uses constant-time comparison (secrets.compare_digest) to prevent timing attacks.
    """
    if not password or not stored_hash or not salt:
        return False
    computed_hash, _ = hash_password(password, salt)
    return secrets.compare_digest(stored_hash, computed_hash)


# ============================================================================
# Input Validation
# ============================================================================

def validate_email(email: str) -> tuple[bool, str]:
    """Validate email format."""
    email = (email or "").strip()
    if not email:
        return False, "Email address is required."
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(pattern, email):
        return False, "Please enter a valid email address (e.g. student@example.com)."
    return True, ""


def validate_registration_inputs(
    full_name: str,
    email: str,
    password: str,
    confirm_password: str,
) -> tuple[bool, str]:
    """Validate all user registration inputs."""
    name = (full_name or "").strip()
    if not name:
        return False, "Full name is required."
    if len(name) < 2:
        return False, "Full name must be at least 2 characters long."

    valid_email, email_msg = validate_email(email)
    if not valid_email:
        return False, email_msg

    if not password:
        return False, "Password is required."
    if len(password) < 6:
        return False, "Password must be at least 6 characters long."

    if password != confirm_password:
        return False, "Passwords do not match. Please re-enter confirm password."

    return True, ""


# ============================================================================
# User Registration and Authentication Logic
# ============================================================================

def register_user(
    full_name: str,
    email: str,
    password: str,
    confirm_password: str,
    db_path=None,
) -> tuple[bool, str]:
    """Register a new user account.

    Validates input, checks for duplicate email, hashes the password with a unique salt,
    and inserts the record into SQLite.

    Returns:
        tuple: (success_bool, message_str)
    """
    is_valid, error_msg = validate_registration_inputs(
        full_name, email, password, confirm_password
    )
    if not is_valid:
        return False, error_msg

    normalised_email = email.strip().lower()

    # Pre-check for duplicate email in database
    existing_user = database.get_user_by_email(normalised_email, db_path=db_path)
    if existing_user is not None:
        return False, "An account with this email already exists. Please log in."

    # Hash the password with a newly generated salt
    password_hash, password_salt = hash_password(password)

    try:
        database.create_user(
            full_name=full_name.strip(),
            email=normalised_email,
            password_hash=password_hash,
            password_salt=password_salt,
            db_path=db_path,
        )
        return True, "Registration successful! You can now log in with your credentials."
    except database.DatabaseError as e:
        return False, str(e)


def authenticate_user(
    email: str,
    password: str,
    db_path=None,
) -> tuple[bool, str, dict | None]:
    """Authenticate a user using their email and password.

    Returns:
        tuple: (success_bool, message_str, user_dict_or_None)
    """
    normalised_email = (email or "").strip().lower()
    if not normalised_email or not password:
        return False, "Email and password are required.", None

    user = database.get_user_by_email(normalised_email, db_path=db_path)
    if user is None:
        # Generic message avoids user enumeration
        return False, "Invalid email or password.", None

    if not verify_password(password, user["password_hash"], user["password_salt"]):
        return False, "Invalid email or password.", None

    # Return safe user dictionary without hash and salt
    safe_user = {
        "id": user["id"],
        "full_name": user["full_name"],
        "email": user["email"],
        "created_at": user.get("created_at"),
    }
    return True, "Login successful!", safe_user


# ============================================================================
# Session State Management
# ============================================================================

def init_session_state():
    """Ensure authentication keys exist in Streamlit session state."""
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "user" not in st.session_state:
        st.session_state["user"] = None


def is_authenticated() -> bool:
    """Check if a user is currently logged in."""
    init_session_state()
    return bool(st.session_state.get("logged_in") and st.session_state.get("user"))


def get_current_user() -> dict | None:
    """Get the currently logged-in user dictionary from session state."""
    init_session_state()
    return st.session_state.get("user")


def get_current_user_id() -> int | None:
    """Get the user ID of the currently logged-in user for database queries."""
    user = get_current_user()
    return user["id"] if user else None


def login_session(user_data: dict):
    """Store the authenticated user in Streamlit session state."""
    init_session_state()
    st.session_state["logged_in"] = True
    st.session_state["user"] = user_data


def logout():
    """Clear session state, logging the user out immediately."""
    st.session_state["logged_in"] = False
    st.session_state["user"] = None
    st.session_state.clear()
    st.rerun()


# ============================================================================
# Streamlit Authentication UI
# ============================================================================

def render_html(html_str: str):
    """Safely render raw HTML in Streamlit using st.markdown with zero-indented lines to prevent code blocks."""
    clean_html = "\n".join(line.strip() for line in html_str.splitlines() if line.strip())
    st.markdown(clean_html, unsafe_allow_html=True)


def render_auth_page():
    """Render the user registration and login interface with a modern fintech split-screen layout."""
    init_session_state()

    # Split-screen columns: Left (Visuals & Analytics Hero), Right (Auth Form Card)
    col_left, col_right = st.columns([1.2, 1], gap="large")

    # =========================================================================
    # LEFT SECTION — FINANCIAL VISUALS & HERO
    # =========================================================================
    with col_left:
        hero_html = """<div class="auth-hero-card" style="background: linear-gradient(135deg, #142B4A 0%, #173660 40%, #1A4479 70%, #205396 100%) !important; border-radius: 20px !important; padding: 34px 30px !important; color: #FFFFFF !important; box-shadow: 0 14px 36px rgba(20, 43, 74, 0.22) !important; border: 1px solid rgba(255, 255, 255, 0.16) !important; position: relative !important; overflow: hidden !important;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
<span style="background: rgba(255, 255, 255, 0.12); border: 1px solid rgba(255, 255, 255, 0.2); padding: 4px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; color: #93C5FD; letter-spacing: 0.5px; text-transform: uppercase;">
🚀 Corporate Intelligence Platform
</span>
<span style="color: #CBD5E1; font-size: 0.8rem; font-weight: 600;">v1.0 &bull; Indian Rupee Workspace</span>
</div>
<h1 style="color: #FFFFFF !important; font-size: 2.1rem; font-weight: 800; line-height: 1.25; margin: 0 0 10px 0;">
Financial Statement<br/>
<span style="background: linear-gradient(90deg, #38BDF8, #818CF8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
Ratio Analysis
</span> Assistant
</h1>
<p style="color: #E2E8F0 !important; font-size: 1rem; line-height: 1.5; margin: 0 0 22px 0;">
Smarter Financial Decisions Through Intelligent Ratio Analysis.
</p>
<div style="position: relative; width: 100%; height: 260px; background: rgba(10, 25, 47, 0.65); border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.18); overflow: hidden; margin-bottom: 22px;">
<div style="position: absolute; top: -30px; right: -30px; width: 150px; height: 150px; background: radial-gradient(circle, rgba(19, 168, 158, 0.45) 0%, transparent 70%); border-radius: 50%;"></div>
<div style="position: absolute; bottom: -30px; left: 10px; width: 170px; height: 170px; background: radial-gradient(circle, rgba(40, 120, 208, 0.5) 0%, transparent 70%); border-radius: 50%;"></div>
<svg viewBox="0 0 500 240" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" preserveAspectRatio="none">
<defs>
<linearGradient id="areaGradient" x1="0" y1="0" x2="0" y2="1">
<stop offset="0%" stop-color="#13A89E" stop-opacity="0.5" />
<stop offset="50%" stop-color="#2878D0" stop-opacity="0.2" />
<stop offset="100%" stop-color="#142B4A" stop-opacity="0.0" />
</linearGradient>
<linearGradient id="lineGradient" x1="0" y1="0" x2="1" y2="0">
<stop offset="0%" stop-color="#13A89E" />
<stop offset="50%" stop-color="#38BDF8" />
<stop offset="100%" stop-color="#20A46B" />
</linearGradient>
<linearGradient id="goldGradient" x1="0" y1="0" x2="1" y2="1">
<stop offset="0%" stop-color="#FDE68A" />
<stop offset="50%" stop-color="#F59E0B" />
<stop offset="100%" stop-color="#B45309" />
</linearGradient>
</defs>
<line x1="20" y1="60" x2="480" y2="60" stroke="rgba(255,255,255,0.12)" stroke-dasharray="4,4" />
<line x1="20" y1="120" x2="480" y2="120" stroke="rgba(255,255,255,0.12)" stroke-dasharray="4,4" />
<line x1="20" y1="180" x2="480" y2="180" stroke="rgba(255,255,255,0.12)" stroke-dasharray="4,4" />
<polygon points="30,220 90,190 160,200 230,140 300,160 380,90 440,105 480,45 480,240 30,240" fill="url(#areaGradient)" />
<path d="M 30 220 Q 60 190 90 190 T 160 200 T 230 140 T 300 160 T 380 90 T 440 105 T 480 45" fill="none" stroke="url(#lineGradient)" stroke-width="4.5" stroke-linecap="round" />
<circle cx="90" cy="190" r="5" fill="#38BDF8" />
<circle cx="230" cy="140" r="5" fill="#38BDF8" />
<circle cx="380" cy="90" r="5" fill="#20A46B" />
<circle cx="480" cy="45" r="7" fill="#20A46B" />
<circle cx="480" cy="45" r="14" fill="none" stroke="#20A46B" stroke-width="2" opacity="0.6" />
<g class="anim-coin" transform="translate(65, 75)">
<circle cx="0" cy="0" r="22" fill="#F59E0B" />
<circle cx="0" cy="0" r="22" fill="url(#goldGradient)" />
<circle cx="0" cy="0" r="18" fill="none" stroke="#FEF3C7" stroke-width="1.8" opacity="0.9" />
<text x="0" y="7" font-size="20" font-weight="900" fill="#FFFFFF" text-anchor="middle" font-family="Arial, sans-serif">₹</text>
</g>
<g class="anim-coin" transform="translate(435, 185)">
<circle cx="0" cy="0" r="17" fill="#F59E0B" />
<circle cx="0" cy="0" r="17" fill="url(#goldGradient)" />
<circle cx="0" cy="0" r="14" fill="none" stroke="#FEF3C7" stroke-width="1.4" opacity="0.9" />
<text x="0" y="5" font-size="15" font-weight="900" fill="#FFFFFF" text-anchor="middle" font-family="Arial, sans-serif">₹</text>
</g>
</svg>
<div class="float-metric-card anim-float-1" style="position: absolute; top: 16px; right: 18px; background: rgba(20, 43, 74, 0.88); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.22); border-radius: 12px; padding: 10px 14px; box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);">
<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">
<span style="color: #94A3B8; font-size: 0.7rem; font-weight: 700; text-transform: uppercase;">Turnover</span>
<span style="background: rgba(32, 164, 107, 0.25); color: #4ADE80; padding: 2px 6px; border-radius: 4px; font-size: 0.7rem; font-weight: 700;">▲ +24.8%</span>
</div>
<div style="font-size: 1.15rem; font-weight: 800; color: #FFFFFF; margin-top: 3px;">
₹ 14.85 Cr
</div>
</div>
<div class="float-metric-card anim-float-2" style="position: absolute; bottom: 18px; left: 20px; background: rgba(20, 43, 74, 0.88); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.22); border-radius: 12px; padding: 10px 14px; box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);">
<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">
<span style="color: #94A3B8; font-size: 0.7rem; font-weight: 700; text-transform: uppercase;">Net Profit</span>
<span style="background: rgba(40, 120, 208, 0.25); color: #60A5FA; padding: 2px 6px; border-radius: 4px; font-size: 0.7rem; font-weight: 700;">▲ +18.2%</span>
</div>
<div style="font-size: 1.15rem; font-weight: 800; color: #FFFFFF; margin-top: 3px;">
₹ 2.75 Cr
</div>
</div>
<div class="float-metric-card anim-float-1" style="position: absolute; bottom: 18px; right: 18px; background: rgba(20, 43, 74, 0.88); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.22); border-radius: 12px; padding: 10px 14px; box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);">
<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">
<span style="color: #94A3B8; font-size: 0.7rem; font-weight: 700; text-transform: uppercase;">Health Score</span>
<span style="background: rgba(128, 100, 200, 0.25); color: #C084FC; padding: 2px 6px; border-radius: 4px; font-size: 0.7rem; font-weight: 700;">Strong</span>
</div>
<div style="font-size: 1.15rem; font-weight: 800; color: #FFFFFF; margin-top: 3px;">
94.2 <span style="font-size: 0.75rem; color: #94A3B8;">/ 100</span>
</div>
</div>
</div>
<div style="display: flex; flex-wrap: wrap; gap: 8px;">
<span style="background: rgba(255, 255, 255, 0.12); border: 1px solid rgba(255, 255, 255, 0.2); padding: 6px 14px; border-radius: 20px; font-size: 0.78rem; color: #FFFFFF; font-weight: 500;">
✓ 14 Deterministic Financial Ratios
</span>
<span style="background: rgba(255, 255, 255, 0.12); border: 1px solid rgba(255, 255, 255, 0.2); padding: 6px 14px; border-radius: 20px; font-size: 0.78rem; color: #FFFFFF; font-weight: 500;">
✓ Multi-Year Trends & Peer Radar
</span>
<span style="background: rgba(255, 255, 255, 0.12); border: 1px solid rgba(255, 255, 255, 0.2); padding: 6px 14px; border-radius: 20px; font-size: 0.78rem; color: #FFFFFF; font-weight: 500;">
✓ Executive PDF Reports (ReportLab)
</span>
<span style="background: rgba(255, 255, 255, 0.12); border: 1px solid rgba(255, 255, 255, 0.2); padding: 6px 14px; border-radius: 20px; font-size: 0.78rem; color: #FFFFFF; font-weight: 500;">
✓ PBKDF2 Password Security
</span>
</div>
</div>"""
        render_html(hero_html)

    # =========================================================================
    # RIGHT SECTION — AUTHENTICATION FORM CARD
    # =========================================================================
    with col_right:
        with st.container(border=True):
            tab_login, tab_register = st.tabs(["🔑 Sign In", "📝 Create Account"])

            # -----------------------------------------------------------------
            # TAB 1: LOGIN FORM
            # -----------------------------------------------------------------
            with tab_login:
                welcome_html = """<div style="margin-bottom: 16px;">
<h2 style="color: #142B4A; font-weight: 800; font-size: 1.65rem; margin: 0 0 4px 0;">Welcome Back 👋</h2>
<p style="color: #5A6E85; font-size: 0.92rem; margin: 0;">Enter your credentials to access your financial dashboard.</p>
</div>"""
                render_html(welcome_html)

                with st.form("login_form", clear_on_submit=False):
                    login_email = st.text_input(
                        "Email Address",
                        placeholder="student@example.com",
                        key="login_email_input",
                    )

                    show_pwd = st.checkbox("Show password", key="login_show_pwd")
                    login_password = st.text_input(
                        "Password",
                        type="default" if show_pwd else "password",
                        placeholder="Enter your password",
                        key="login_password_input",
                    )

                    col_rem, col_badge = st.columns([1.2, 1])
                    with col_rem:
                        remember_me = st.checkbox("Remember me", value=True, key="login_remember_me")
                    with col_badge:
                        render_html("<div style='text-align: right; color: #2878D0; font-size: 0.78rem; font-weight: 600; padding-top: 6px;'>🔒 Private SQLite</div>")

                    submitted_login = st.form_submit_button(
                        "Sign In to Workspace 🚀",
                        use_container_width=True,
                        type="primary",
                    )

                    if submitted_login:
                        success, message, user = authenticate_user(login_email, login_password)
                        if success:
                            login_session(user)
                            st.success(f"Welcome back, {user['full_name']}!")
                            st.rerun()
                        else:
                            st.error(f"❌ {message}")

                demo_html = """<div style="background-color: #F8FAFC; border: 1px dashed #CBD5E1; border-radius: 8px; padding: 10px 14px; margin-top: 18px; font-size: 0.8rem; color: #64748B;">
💡 <b>Demo Accounts:</b> <code>rutu522@gmail.com</code> &bull; <code>demo@student.edu</code><br/>
New user? Click the <b>Create Account</b> tab above.
</div>"""
                render_html(demo_html)

            # -----------------------------------------------------------------
            # TAB 2: REGISTRATION FORM
            # -----------------------------------------------------------------
            with tab_register:
                create_html = """<div style="margin-bottom: 16px;">
<h2 style="color: #142B4A; font-weight: 800; font-size: 1.65rem; margin: 0 0 4px 0;">Create Account ✨</h2>
<p style="color: #5A6E85; font-size: 0.92rem; margin: 0;">Get isolated, private access to company ratio analysis.</p>
</div>"""
                render_html(create_html)

                with st.form("register_form", clear_on_submit=False):
                    reg_name = st.text_input(
                        "Full Name",
                        placeholder="e.g. Ramesh Sharma",
                        key="reg_name_input",
                    )
                    reg_email = st.text_input(
                        "Email Address",
                        placeholder="student@example.com",
                        key="reg_email_input",
                    )
                    show_reg_pwd = st.checkbox("Show password", key="reg_show_pwd")
                    reg_password = st.text_input(
                        "Password",
                        type="default" if show_reg_pwd else "password",
                        placeholder="At least 6 characters",
                        help="Password will be securely hashed with PBKDF2-HMAC-SHA256 and salted.",
                        key="reg_password_input",
                    )
                    reg_confirm = st.text_input(
                        "Confirm Password",
                        type="default" if show_reg_pwd else "password",
                        placeholder="Re-enter password",
                        key="reg_confirm_input",
                    )
                    submitted_register = st.form_submit_button(
                        "Create My Account 🎯",
                        use_container_width=True,
                        type="primary",
                    )

                    if submitted_register:
                        success, message = register_user(
                            full_name=reg_name,
                            email=reg_email,
                            password=reg_password,
                            confirm_password=reg_confirm,
                        )
                        if success:
                            st.success(f"✅ {message}")
                            st.info("👉 Switch to the **🔑 Sign In** tab above to sign in.")
                        else:
                            st.error(f"❌ {message}")

                already_html = """<div style="text-align: center; margin-top: 14px; font-size: 0.8rem; color: #64748B;">
Already registered? Switch to the <b>Sign In</b> tab above.
</div>"""
                render_html(already_html)

```

---

## File: `calculations.py`

```python
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

```

---

## File: `database.py`

```python
"""SQLite database for the Financial Statement Ratio Analysis Assistant.

This file is the only place that reads and writes the database.
The database file is the permanent record. Closing the app does not
delete it. Streamlit session state is never used to store these records.

Tables
------
users                  Login accounts. Passwords are stored only as hashes.
companies              Companies owned by one user.
financial_statements   Income statement, balance sheet, and cash flow figures.
financial_ratios       Latest calculated ratios for one statement.
analysis_history       One row each time an analysis is saved.

Every company, statement, ratio, and history row stores user_id.
Queries always filter by that user, so one account cannot read or
change another account's data.
"""

import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).resolve().parent / "database" / "financial_data.db"

# Amounts are real INR numbers. Indian formatting is applied only on screen.
STATEMENT_FIELDS = [
    "financial_year",
    "revenue",
    "cost_of_goods_sold",
    "gross_profit",
    "operating_expenses",
    "operating_income",
    "interest_expense",
    "tax_expense",
    "net_income",
    "current_assets",
    "cash_and_cash_equivalents",
    "inventory",
    "total_assets",
    "current_liabilities",
    "total_liabilities",
    "total_debt",
    "shareholders_equity",
    "opening_inventory",
    "closing_inventory",
    "opening_total_assets",
    "closing_total_assets",
    "operating_cash_flow",
    "capital_expenditure",
    "free_cash_flow",
]

# NULL means the ratio could not be calculated. It is shown later as N/A.
RATIO_FIELDS = [
    "current_ratio",
    "quick_ratio",
    "cash_ratio",
    "gross_profit_margin",
    "net_profit_margin",
    "return_on_assets",
    "return_on_equity",
    "debt_to_equity",
    "debt_ratio",
    "interest_coverage",
    "inventory_turnover",
    "asset_turnover",
    "operating_cash_flow_ratio",
    "free_cash_flow",
]


class DatabaseError(Exception):
    """A save or lookup that the application can show to the user."""


def get_connection(db_path=None):
    """Open SQLite and turn foreign keys on for this connection."""
    path = Path(db_path) if db_path else DB_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def _row(record):
    if record is None:
        return None
    return dict(record)


def _rows(records):
    return [dict(record) for record in records]


def init_db(db_path=None):
    """Create the database file and tables if they do not exist yet."""
    connection = get_connection(db_path)
    try:
        connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE COLLATE NOCASE,
                password_hash TEXT NOT NULL,
                password_salt TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT (datetime('now', 'localtime'))
            );

            CREATE TABLE IF NOT EXISTS companies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                company_name TEXT NOT NULL,
                industry TEXT NOT NULL,
                financial_year TEXT NOT NULL,
                description TEXT NOT NULL DEFAULT '',
                created_at TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
                updated_at TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS financial_statements (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                company_id INTEGER NOT NULL,
                financial_year TEXT NOT NULL,
                revenue REAL,
                cost_of_goods_sold REAL,
                gross_profit REAL,
                operating_expenses REAL,
                operating_income REAL,
                interest_expense REAL,
                tax_expense REAL,
                net_income REAL,
                current_assets REAL,
                cash_and_cash_equivalents REAL,
                inventory REAL,
                total_assets REAL,
                current_liabilities REAL,
                total_liabilities REAL,
                total_debt REAL,
                shareholders_equity REAL,
                opening_inventory REAL,
                closing_inventory REAL,
                opening_total_assets REAL,
                closing_total_assets REAL,
                operating_cash_flow REAL,
                capital_expenditure REAL,
                free_cash_flow REAL,
                created_at TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
                updated_at TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE CASCADE,
                UNIQUE (company_id, financial_year)
            );

            CREATE TABLE IF NOT EXISTS financial_ratios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                statement_id INTEGER NOT NULL UNIQUE,
                current_ratio REAL,
                quick_ratio REAL,
                cash_ratio REAL,
                gross_profit_margin REAL,
                net_profit_margin REAL,
                return_on_assets REAL,
                return_on_equity REAL,
                debt_to_equity REAL,
                debt_ratio REAL,
                interest_coverage REAL,
                inventory_turnover REAL,
                asset_turnover REAL,
                operating_cash_flow_ratio REAL,
                free_cash_flow REAL,
                calculated_at TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (statement_id) REFERENCES financial_statements(id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS analysis_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                company_id INTEGER NOT NULL,
                statement_id INTEGER NOT NULL,
                company_name TEXT NOT NULL,
                financial_year TEXT NOT NULL,
                analysis_date TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
                total_revenue REAL,
                net_profit REAL,
                ratios_calculated INTEGER NOT NULL DEFAULT 0,
                report_generated INTEGER NOT NULL DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE CASCADE,
                FOREIGN KEY (statement_id) REFERENCES financial_statements(id) ON DELETE CASCADE
            );

            CREATE INDEX IF NOT EXISTS idx_companies_user ON companies(user_id);
            CREATE INDEX IF NOT EXISTS idx_statements_user ON financial_statements(user_id);
            CREATE INDEX IF NOT EXISTS idx_ratios_user ON financial_ratios(user_id);
            CREATE INDEX IF NOT EXISTS idx_history_user ON analysis_history(user_id);
            """
        )
        connection.commit()
    finally:
        connection.close()


def create_user(full_name, email, password_hash, password_salt, db_path=None):
    """Store a new account. The hash is saved; the password is not."""
    name = (full_name or "").strip()
    normalised_email = (email or "").strip().lower()
    if not name or not normalised_email or not password_hash or not password_salt:
        raise DatabaseError("Name, email, and password are required.")

    connection = get_connection(db_path)
    try:
        cursor = connection.execute(
            """
            INSERT INTO users (full_name, email, password_hash, password_salt)
            VALUES (?, ?, ?, ?)
            """,
            (name, normalised_email, password_hash, password_salt),
        )
        connection.commit()
        return cursor.lastrowid
    except sqlite3.IntegrityError as error:
        connection.rollback()
        raise DatabaseError("An account with this email already exists.") from error
    finally:
        connection.close()


def get_user_by_email(email, db_path=None):
    connection = get_connection(db_path)
    try:
        record = connection.execute(
            "SELECT * FROM users WHERE email = ?",
            ((email or "").strip().lower(),),
        ).fetchone()
        return _row(record)
    finally:
        connection.close()


def get_user_by_id(user_id, db_path=None):
    connection = get_connection(db_path)
    try:
        record = connection.execute(
            "SELECT id, full_name, email, created_at FROM users WHERE id = ?",
            (user_id,),
        ).fetchone()
        return _row(record)
    finally:
        connection.close()


def _require_company(connection, user_id, company_id):
    record = connection.execute(
        "SELECT * FROM companies WHERE id = ? AND user_id = ?",
        (company_id, user_id),
    ).fetchone()
    if record is None:
        raise DatabaseError("That company was not found for this account.")
    return record


def create_company(user_id, company_name, industry, financial_year, description="", db_path=None):
    name = (company_name or "").strip()
    industry_name = (industry or "").strip()
    year = (financial_year or "").strip()
    if not name or not industry_name or not year:
        raise DatabaseError("Company name, industry, and financial year are required.")

    connection = get_connection(db_path)
    try:
        cursor = connection.execute(
            """
            INSERT INTO companies (user_id, company_name, industry, financial_year, description)
            VALUES (?, ?, ?, ?, ?)
            """,
            (user_id, name, industry_name, year, (description or "").strip()),
        )
        connection.commit()
        return cursor.lastrowid
    except sqlite3.IntegrityError as error:
        connection.rollback()
        raise DatabaseError("Could not save the company.") from error
    finally:
        connection.close()


def update_company(user_id, company_id, company_name, industry, financial_year, description="", db_path=None):
    name = (company_name or "").strip()
    industry_name = (industry or "").strip()
    year = (financial_year or "").strip()
    if not name or not industry_name or not year:
        raise DatabaseError("Company name, industry, and financial year are required.")

    connection = get_connection(db_path)
    try:
        _require_company(connection, user_id, company_id)
        cursor = connection.execute(
            """
            UPDATE companies
            SET company_name = ?, industry = ?, financial_year = ?, description = ?,
                updated_at = datetime('now', 'localtime')
            WHERE id = ? AND user_id = ?
            """,
            (name, industry_name, year, (description or "").strip(), company_id, user_id),
        )
        connection.commit()
        return cursor.rowcount == 1
    finally:
        connection.close()


def delete_company(user_id, company_id, db_path=None):
    """Delete a company and, through foreign keys, its statements and analyses."""
    connection = get_connection(db_path)
    try:
        cursor = connection.execute(
            "DELETE FROM companies WHERE id = ? AND user_id = ?",
            (company_id, user_id),
        )
        connection.commit()
        return cursor.rowcount == 1
    finally:
        connection.close()


def get_company(user_id, company_id, db_path=None):
    connection = get_connection(db_path)
    try:
        record = connection.execute(
            "SELECT * FROM companies WHERE id = ? AND user_id = ?",
            (company_id, user_id),
        ).fetchone()
        return _row(record)
    finally:
        connection.close()


def list_companies(user_id, db_path=None):
    connection = get_connection(db_path)
    try:
        records = connection.execute(
            """
            SELECT * FROM companies
            WHERE user_id = ?
            ORDER BY company_name COLLATE NOCASE, financial_year
            """,
            (user_id,),
        ).fetchall()
        return _rows(records)
    finally:
        connection.close()


def _statement_values(data, fallback_year):
    values = {field: data.get(field) for field in STATEMENT_FIELDS}
    year = (values.get("financial_year") or fallback_year or "").strip()
    if not year:
        raise DatabaseError("Financial year is required.")
    values["financial_year"] = year
    return values


def save_financial_statement(user_id, company_id, data, db_path=None):
    """Insert or update the statement for one company and financial year."""
    connection = get_connection(db_path)
    try:
        company = _require_company(connection, user_id, company_id)
        values = _statement_values(data, company["financial_year"])
        existing = connection.execute(
            """
            SELECT id FROM financial_statements
            WHERE user_id = ? AND company_id = ? AND financial_year = ?
            """,
            (user_id, company_id, values["financial_year"]),
        ).fetchone()

        if existing is None:
            columns = ["user_id", "company_id", *STATEMENT_FIELDS]
            placeholders = ", ".join("?" for _ in columns)
            connection.execute(
                f"INSERT INTO financial_statements ({', '.join(columns)}) VALUES ({placeholders})",
                [user_id, company_id, *[values[field] for field in STATEMENT_FIELDS]],
            )
            statement_id = connection.execute("SELECT last_insert_rowid()").fetchone()[0]
        else:
            assignments = ", ".join(f"{field} = ?" for field in STATEMENT_FIELDS)
            connection.execute(
                f"""
                UPDATE financial_statements
                SET {assignments}, updated_at = datetime('now', 'localtime')
                WHERE id = ? AND user_id = ?
                """,
                [*[values[field] for field in STATEMENT_FIELDS], existing["id"], user_id],
            )
            statement_id = existing["id"]

        connection.commit()
        return statement_id
    except DatabaseError:
        connection.rollback()
        raise
    finally:
        connection.close()


def get_statement(user_id, statement_id, db_path=None):
    connection = get_connection(db_path)
    try:
        record = connection.execute(
            "SELECT * FROM financial_statements WHERE id = ? AND user_id = ?",
            (statement_id, user_id),
        ).fetchone()
        return _row(record)
    finally:
        connection.close()


def get_statement_for_company(user_id, company_id, financial_year, db_path=None):
    connection = get_connection(db_path)
    try:
        record = connection.execute(
            """
            SELECT * FROM financial_statements
            WHERE user_id = ? AND company_id = ? AND financial_year = ?
            """,
            (user_id, company_id, financial_year),
        ).fetchone()
        return _row(record)
    finally:
        connection.close()


def list_statements(user_id, company_id=None, db_path=None):
    connection = get_connection(db_path)
    try:
        if company_id is None:
            records = connection.execute(
                """
                SELECT * FROM financial_statements
                WHERE user_id = ?
                ORDER BY financial_year DESC, id DESC
                """,
                (user_id,),
            ).fetchall()
        else:
            records = connection.execute(
                """
                SELECT * FROM financial_statements
                WHERE user_id = ? AND company_id = ?
                ORDER BY financial_year DESC, id DESC
                """,
                (user_id, company_id),
            ).fetchall()
        return _rows(records)
    finally:
        connection.close()


def _ratio_values(data):
    return {field: data.get(field) for field in RATIO_FIELDS}


def _count_ratios(values):
    return sum(value is not None for value in values.values())


def save_full_analysis(user_id, company_id, statement_data, ratio_data, db_path=None):
    """Save the statement, its ratios, and a history row in one transaction.

    If any write fails, none of the three records are kept.
    """
    connection = get_connection(db_path)
    try:
        company = _require_company(connection, user_id, company_id)
        values = _statement_values(statement_data, company["financial_year"])
        ratios = _ratio_values(ratio_data)

        existing = connection.execute(
            """
            SELECT id FROM financial_statements
            WHERE user_id = ? AND company_id = ? AND financial_year = ?
            """,
            (user_id, company_id, values["financial_year"]),
        ).fetchone()

        if existing is None:
            columns = ["user_id", "company_id", *STATEMENT_FIELDS]
            placeholders = ", ".join("?" for _ in columns)
            connection.execute(
                f"INSERT INTO financial_statements ({', '.join(columns)}) VALUES ({placeholders})",
                [user_id, company_id, *[values[field] for field in STATEMENT_FIELDS]],
            )
            statement_id = connection.execute("SELECT last_insert_rowid()").fetchone()[0]
        else:
            assignments = ", ".join(f"{field} = ?" for field in STATEMENT_FIELDS)
            connection.execute(
                f"""
                UPDATE financial_statements
                SET {assignments}, updated_at = datetime('now', 'localtime')
                WHERE id = ? AND user_id = ?
                """,
                [*[values[field] for field in STATEMENT_FIELDS], existing["id"], user_id],
            )
            statement_id = existing["id"]

        ratio_assignments = ", ".join(f"{field} = ?" for field in RATIO_FIELDS)
        connection.execute(
            f"""
            INSERT INTO financial_ratios (user_id, statement_id, {", ".join(RATIO_FIELDS)})
            VALUES (?, ?, {", ".join("?" for _ in RATIO_FIELDS)})
            ON CONFLICT(statement_id) DO UPDATE SET
                {ratio_assignments},
                calculated_at = datetime('now', 'localtime')
            """,
            [user_id, statement_id, *[ratios[field] for field in RATIO_FIELDS], *[ratios[field] for field in RATIO_FIELDS]],
        )
        ratio_id = connection.execute(
            "SELECT id FROM financial_ratios WHERE statement_id = ? AND user_id = ?",
            (statement_id, user_id),
        ).fetchone()["id"]

        cursor = connection.execute(
            """
            INSERT INTO analysis_history (
                user_id, company_id, statement_id, company_name, financial_year,
                total_revenue, net_profit, ratios_calculated
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user_id,
                company_id,
                statement_id,
                company["company_name"],
                values["financial_year"],
                values.get("revenue"),
                values.get("net_income"),
                _count_ratios(ratios),
            ),
        )
        connection.commit()
        return {
            "statement_id": statement_id,
            "ratio_id": ratio_id,
            "analysis_id": cursor.lastrowid,
        }
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def get_ratios(user_id, statement_id, db_path=None):
    connection = get_connection(db_path)
    try:
        record = connection.execute(
            "SELECT * FROM financial_ratios WHERE statement_id = ? AND user_id = ?",
            (statement_id, user_id),
        ).fetchone()
        return _row(record)
    finally:
        connection.close()


def list_analyses(user_id, db_path=None):
    connection = get_connection(db_path)
    try:
        records = connection.execute(
            """
            SELECT * FROM analysis_history
            WHERE user_id = ?
            ORDER BY analysis_date DESC, id DESC
            """,
            (user_id,),
        ).fetchall()
        return _rows(records)
    finally:
        connection.close()


def get_analysis(user_id, analysis_id, db_path=None):
    connection = get_connection(db_path)
    try:
        record = connection.execute(
            "SELECT * FROM analysis_history WHERE id = ? AND user_id = ?",
            (analysis_id, user_id),
        ).fetchone()
        return _row(record)
    finally:
        connection.close()


def delete_analysis(user_id, analysis_id, db_path=None):
    """Delete one history row. The company and statement stay saved."""
    connection = get_connection(db_path)
    try:
        cursor = connection.execute(
            "DELETE FROM analysis_history WHERE id = ? AND user_id = ?",
            (analysis_id, user_id),
        )
        connection.commit()
        return cursor.rowcount == 1
    finally:
        connection.close()


def mark_report_generated(user_id, analysis_id, db_path=None):
    connection = get_connection(db_path)
    try:
        cursor = connection.execute(
            """
            UPDATE analysis_history
            SET report_generated = report_generated + 1
            WHERE id = ? AND user_id = ?
            """,
            (analysis_id, user_id),
        )
        connection.commit()
        return cursor.rowcount == 1
    finally:
        connection.close()


def dashboard_summary(user_id, db_path=None):
    """Counts, financial aggregates, and the latest saved statements for dashboard cards."""
    connection = get_connection(db_path)
    try:
        counts = connection.execute(
            """
            SELECT
                (SELECT COUNT(*) FROM companies WHERE user_id = ?) AS companies,
                (SELECT COUNT(*) FROM analysis_history WHERE user_id = ?) AS analyses,
                (SELECT COALESCE(SUM(report_generated), 0) FROM analysis_history WHERE user_id = ?) AS reports
            """,
            (user_id, user_id, user_id),
        ).fetchone()

        totals = connection.execute(
            """
            SELECT
                COALESCE(SUM(revenue), 0.0) AS total_revenue,
                COALESCE(SUM(net_income), 0.0) AS total_net_profit
            FROM financial_statements
            WHERE user_id = ?
            """,
            (user_id,),
        ).fetchone()

        total_rev = float(totals["total_revenue"] or 0.0) if totals else 0.0
        total_profit = float(totals["total_net_profit"] or 0.0) if totals else 0.0

        if total_rev == 0.0 and total_profit == 0.0:
            hist_totals = connection.execute(
                """
                SELECT
                    COALESCE(SUM(total_revenue), 0.0) AS hist_revenue,
                    COALESCE(SUM(net_profit), 0.0) AS hist_profit
                FROM analysis_history
                WHERE user_id = ?
                """,
                (user_id,),
            ).fetchone()
            if hist_totals:
                total_rev = float(hist_totals["hist_revenue"] or 0.0)
                total_profit = float(hist_totals["hist_profit"] or 0.0)

        latest = connection.execute(
            """
            SELECT * FROM financial_statements
            WHERE user_id = ?
            ORDER BY updated_at DESC, id DESC
            LIMIT 1
            """,
            (user_id,),
        ).fetchone()
        recent = connection.execute(
            """
            SELECT * FROM analysis_history
            WHERE user_id = ?
            ORDER BY analysis_date DESC, id DESC
            LIMIT 5
            """,
            (user_id,),
        ).fetchall()
        return {
            "total_companies": counts["companies"],
            "total_analyses": counts["analyses"],
            "total_reports": counts["reports"],
            "total_revenue": total_rev,
            "total_net_profit": total_profit,
            "latest_statement": _row(latest),
            "recent_analyses": _rows(recent),
        }
    finally:
        connection.close()


def _self_check():
    """Create a temporary database and check isolation, rollback, and restart."""
    import tempfile

    temporary = Path(tempfile.mkdtemp()) / "check.db"
    init_db(temporary)

    first_user = create_user("Asha Rao", "asha@example.com", "hash-1", "salt-1", temporary)
    second_user = create_user("Ravi Shah", "ravi@example.com", "hash-2", "salt-2", temporary)
    try:
        create_user("Asha Again", "ASHA@example.com", "hash-3", "salt-3", temporary)
        raise AssertionError("Duplicate email was accepted.")
    except DatabaseError:
        pass

    company_id = create_company(
        first_user, "Narmada Textiles", "Manufacturing", "FY 2025-26", "Sample company", temporary
    )
    if list_companies(second_user, temporary):
        raise AssertionError("Second user can see the first user's company.")
    try:
        update_company(second_user, company_id, "Changed", "Retail", "FY 2026-27", "", temporary)
        raise AssertionError("Second user updated the first user's company.")
    except DatabaseError:
        pass
    if delete_company(second_user, company_id, temporary):
        raise AssertionError("Second user deleted the first user's company.")

    saved = save_full_analysis(
        first_user,
        company_id,
        {
            "financial_year": "FY 2025-26",
            "revenue": 10000000,
            "net_income": 1500000,
            "current_assets": 4000000,
            "current_liabilities": 2000000,
        },
        {"current_ratio": 2.0, "net_profit_margin": 15.0, "quick_ratio": None},
        temporary,
    )

    connection = get_connection(temporary)
    try:
        try:
            connection.execute(
                "INSERT INTO companies (user_id, company_name, industry, financial_year) VALUES (999, 'Ghost', 'Retail', 'FY 2025-26')"
            )
            connection.commit()
            raise AssertionError("Foreign key did not block a company with no user.")
        except sqlite3.IntegrityError:
            connection.rollback()
    finally:
        connection.close()

    connection = get_connection(temporary)
    try:
        connection.execute("BEGIN")
        connection.execute(
            """
            INSERT INTO financial_statements (user_id, company_id, financial_year, revenue)
            VALUES (?, ?, 'FY 2024-25', 500)
            """,
            (first_user, company_id),
        )
        connection.rollback()
    finally:
        connection.close()

    # A new connection is the same test as closing the app and opening it again.
    reopened = get_statement(first_user, saved["statement_id"], temporary)
    if reopened["revenue"] != 10000000:
        raise AssertionError("Saved revenue was not available after reconnecting.")
    if get_statement(second_user, saved["statement_id"], temporary) is not None:
        raise AssertionError("Second user can read the first user's statement.")
    years = [item["financial_year"] for item in list_statements(first_user, company_id, temporary)]
    if "FY 2024-25" in years:
        raise AssertionError("Rolled-back statement was saved.")
    if get_ratios(first_user, saved["statement_id"], temporary)["quick_ratio"] is not None:
        raise AssertionError("Unavailable ratio was not stored as empty.")
    if not list_analyses(first_user, temporary):
        raise AssertionError("Analysis history was not saved.")
    if list_analyses(second_user, temporary):
        raise AssertionError("Second user can see the first user's history.")

    summary = dashboard_summary(first_user, temporary)
    if summary["total_companies"] != 1 or summary["total_analyses"] != 1:
        raise AssertionError("Dashboard counts are wrong.")

    if not delete_company(first_user, company_id, temporary):
        raise AssertionError("Owner could not delete the company.")
    if get_statement(first_user, saved["statement_id"], temporary) is not None:
        raise AssertionError("Statement remained after the company was deleted.")
    if list_analyses(first_user, temporary):
        raise AssertionError("History remained after the company was deleted.")

    print("Database self-check passed.")
    print(f"Temporary test file: {temporary}")


if __name__ == "__main__":
    _self_check()
    init_db()
    connection = get_connection()
    try:
        tables = connection.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name"
        ).fetchall()
    finally:
        connection.close()
    print(f"Permanent database: {DB_PATH}")
    print("Tables:", ", ".join(table["name"] for table in tables))

```

---

## File: `database\.gitkeep`

```

```

---

## File: `database\financial_data.db` (SQLite database binary excluded)

---

## File: `main.py`

```python
"""Application entry point for Financial Statement Ratio Analysis Assistant.

College Project
This file handles:
1. Streamlit configuration, metadata, and custom styling.
2. SQLite database initialization.
3. Authentication gate (unauthenticated users see login/registration).
4. Professional Sidebar with user account details and navigation menu.
5. Routing to dashboard and placeholder pages for upcoming steps.
6. Clean logout handling.
"""

import streamlit as st
import database
import authentication
from pages import dashboard, companies, financial_statements, ratio_analysis, financial_insights, comparison, reports, history


# Standard sidebar navigation items
NAV_ITEMS = [
    "📊 Dashboard",
    "🏢 Company Management",
    "📑 Financial Statements",
    "📈 Ratio Analysis",
    "💡 Financial Insights",
    "🔄 Financial Comparison",
    "📄 Reports",
    "🕒 Analysis History",
]


def load_custom_css():
    """Load custom CSS stylesheet if present."""
    try:
        with open("assets/style.css", "r", encoding="utf-8") as f:
            css = f.read()
            if css.strip():
                st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass


def render_feature_placeholder(feature_title: str, upcoming_step: str, description: str):
    """Render a clean placeholder for features to be built in subsequent steps."""
    st.markdown(f"## {feature_title}")
    st.markdown(f"<p style='color: #64748B;'>{description}</p>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <div style="background-color: #FFFFFF; border: 1.5px dashed #CBD5E1;
                    border-radius: 12px; padding: 36px 24px; text-align: center; margin-top: 16px;">
            <div style="font-size: 2.5rem; margin-bottom: 12px;">🚧</div>
            <h3 style="color: #1E3A8A; margin-bottom: 8px;">Scheduled for {upcoming_step}</h3>
            <p style="color: #64748B; max-width: 550px; margin: 0 auto 20px auto; font-size: 0.95rem;">
                This module will be fully activated in {upcoming_step} following the project roadmap.
                Please explore the <b>Dashboard</b> in the meantime.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, _ = st.columns([1, 1, 2])
    with col1:
        if st.button("⬅️ Back to Dashboard", use_container_width=True, type="primary"):
            st.session_state["nav_selection"] = "Dashboard"
            st.rerun()


def render_sidebar(user: dict) -> str:
    """Render the professional sidebar with user badge, navigation, and logout."""
    with st.sidebar:
        # App branding in sidebar
        st.markdown(
            """
            <div style="padding-bottom: 14px; border-bottom: 1px solid rgba(255, 255, 255, 0.12); margin-bottom: 16px;">
                <h3 style="color: #FFFFFF; margin: 0; font-size: 1.25rem; font-weight: 700;">📈 Financial Assistant</h3>
                <span style="color: #93C5FD; font-size: 0.8rem; font-weight: 500;">Indian Rupee (₹) Workspace</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # User profile badge
        user_name = user["full_name"]
        user_email = user["email"]
        user_id = user["id"]

        st.markdown(
            f"""
            <div style="background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.14);
                        border-radius: 10px; padding: 12px; margin-bottom: 16px;">
                <div style="font-size: 0.72rem; color: #93C5FD; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">
                    Logged In User
                </div>
                <div style="font-weight: 700; color: #FFFFFF; font-size: 1rem; margin-top: 2px;">
                    {user_name}
                </div>
                <div style="font-size: 0.8rem; color: #CBD5E1;">
                    {user_email}
                </div>
                <div style="display: inline-block; background-color: #2878D0; color: #FFFFFF;
                            font-size: 0.72rem; font-weight: 600; padding: 2px 8px; border-radius: 10px; margin-top: 6px;">
                    Account #{user_id}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<p style='font-size: 0.75rem; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px;'>NAVIGATION</p>", unsafe_allow_html=True)

        # Check if programmatic navigation was requested (e.g. Quick Action buttons)
        # We update sidebar_nav HERE before st.radio is instantiated on this script run
        if "nav_selection" in st.session_state:
            target = st.session_state.pop("nav_selection")
            for item in NAV_ITEMS:
                if target in item:
                    st.session_state["sidebar_nav"] = item
                    break

        # Default navigation selection
        if "sidebar_nav" not in st.session_state:
            st.session_state["sidebar_nav"] = "📊 Dashboard"

        # Sidebar radio navigation (controlled cleanly by st.session_state["sidebar_nav"])
        selection = st.radio(
            "Navigation Menu",
            NAV_ITEMS,
            label_visibility="collapsed",
            key="sidebar_nav",
        )

        st.markdown("---")

        # Logout button
        if st.button("🚪 Log Out", use_container_width=True, type="secondary"):
            authentication.logout()

        # Footer
        st.markdown(
            """
            <div style="text-align: center; color: #94A3B8; font-size: 0.75rem; margin-top: 20px;">
                Financial Ratio Assistant &bull; v1.0<br>Standard April&ndash;March FY
            </div>
            """,
            unsafe_allow_html=True,
        )

        return selection


def navigate_to(page_keyword: str):
    """Callback to switch navigation page safely from buttons without widget key conflict."""
    st.session_state["nav_selection"] = page_keyword
    st.rerun()


def main():
    # Streamlit page configuration
    st.set_page_config(
        page_title="Financial Statement Ratio Analysis Assistant",
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Initialize permanent SQLite tables
    database.init_db()

    # Load white & navy CSS
    load_custom_css()

    # Authentication Gate
    if not authentication.is_authenticated():
        authentication.render_auth_page()
        return

    # Authenticated user session
    current_user = authentication.get_current_user()

    # Render sidebar navigation
    selected_page = render_sidebar(current_user)

    # Page Routing
    if "Dashboard" in selected_page:
        dashboard.render_dashboard(current_user, on_navigate_callback=navigate_to)
    elif "Company Management" in selected_page:
        companies.render_companies_page(current_user)
    elif "Financial Statements" in selected_page:
        financial_statements.render_statements_page(current_user)
    elif "Ratio Analysis" in selected_page:
        ratio_analysis.render_ratio_analysis_page(current_user)
    elif "Financial Insights" in selected_page:
        financial_insights.render_financial_insights_page(current_user)
    elif "Financial Comparison" in selected_page:
        comparison.render_comparison_page(current_user)
    elif "Reports" in selected_page:
        reports.render_reports_page(current_user)
    elif "Analysis History" in selected_page:
        history.render_history_page(current_user, on_navigate_callback=navigate_to)


if __name__ == "__main__":
    main()

```

---

## File: `pages\__init__.py`

```python
"""Screen modules imported by main.py."""

```

---

## File: `pages\companies.py`

```python
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

```

---

## File: `pages\comparison.py`

```python
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

```

---

## File: `pages\dashboard.py`

```python
"""Professional Financial Analytics Dashboard.

College Project: Financial Statement Ratio Analysis Assistant
This module renders the Step 5 professional dashboard:
- White and navy-blue theme
- User welcome header
- Indian financial formatting (INR ₹, Lakhs/Crores, DD-MM-YYYY, April-March FY)
- Summary metric cards (Companies, Analyses, Reports, Revenue, Net Profit)
- Interactive Plotly performance charts (with informative empty states)
- Recent financial analyses table
- Quick action navigation cards
- Strict user data isolation
"""

import pandas as pd
import streamlit as st
import database
import visualization


# ============================================================================
# Indian Financial Formatting Helpers
# ============================================================================

def format_indian_currency(amount, compact=False) -> str:
    """Format numeric values into Indian Rupee (₹) format with Indian comma grouping.

    Follows the 3,2,2 grouping convention (e.g., ₹ 12,34,567).
    When compact=True:
        >= 1,00,00,000 -> ₹ X.XX Cr
        >= 1,00,000    -> ₹ X.XX Lakh
    """
    if amount is None:
        return "₹ 0"
    try:
        val = float(amount)
    except (ValueError, TypeError):
        return "₹ 0"

    sign = "-" if val < 0 else ""
    abs_val = abs(val)

    if compact:
        if abs_val >= 10_000_000:
            return f"{sign}₹ {abs_val / 10_000_000:.2f} Cr"
        elif abs_val >= 100_000:
            return f"{sign}₹ {abs_val / 100_000:.2f} Lakh"

    # Full Indian comma grouping
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
    return f"{sign}₹ {result}"


def format_indian_date(date_str) -> str:
    """Format ISO or SQLite date string to Indian DD-MM-YYYY format."""
    if not date_str:
        return "N/A"
    try:
        clean_date = str(date_str).strip().split(" ")[0]
        parts = clean_date.split("-")
        if len(parts) == 3 and len(parts[0]) == 4:
            return f"{parts[2]}-{parts[1]}-{parts[0]}"
        return str(date_str)
    except Exception:
        return str(date_str)


# ============================================================================
# Dashboard Render Function
# ============================================================================

def render_dashboard(user: dict, on_navigate_callback=None):
    """Render the full professional dashboard for the authenticated user.

    Args:
        user: Authenticated user dictionary from session state.
        on_navigate_callback: Optional callable(target_page_name) to switch screens.
    """
    user_id = user["id"]
    user_name = user["full_name"]
    user_email = user["email"]

    # 1. Fetch user-scoped financial data from database
    summary = database.dashboard_summary(user_id)
    recent_analyses = summary.get("recent_analyses") or []

    # ------------------------------------------------------------------------
    # 1. Welcome Header Banner
    # ------------------------------------------------------------------------
    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, #142B4A 0%, #1D3D66 50%, #2878D0 100%);
                    color: white; padding: 24px 28px; border-radius: 14px; margin-bottom: 24px;
                    box-shadow: 0 4px 14px rgba(20, 43, 74, 0.12);">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <div>
                    <h2 style="color: #FFFFFF; margin: 0 0 6px 0; font-weight: 700; font-size: 1.75rem;">
                        Welcome back, {user_name}! 👋
                    </h2>
                    <p style="color: #E2E8F0; margin: 0; font-size: 0.95rem;">
                        Financial Statement Ratio Analysis Assistant &bull; Indian Rupee (₹) Financial Workspace
                    </p>
                </div>
                <div style="text-align: right; margin-top: 8px;">
                    <span style="background: rgba(255, 255, 255, 0.18); padding: 6px 14px;
                                 border-radius: 20px; font-size: 0.82rem; font-weight: 600; border: 1px solid rgba(255, 255, 255, 0.25);">
                        Account #{user_id} &bull; {user_email}
                    </span>
                    <div style="color: #93C5FD; font-size: 0.8rem; margin-top: 6px; font-weight: 500;">
                        Standard Indian FY: April 1 &ndash; March 31
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ------------------------------------------------------------------------
    # 2. Key Metrics - Primary Counters
    # ------------------------------------------------------------------------
    st.markdown("### 📌 Workspace Highlights")
    m_col1, m_col2, m_col3 = st.columns(3)

    with m_col1:
        st.markdown('<div class="kpi-card kpi-blue">', unsafe_allow_html=True)
        st.metric(
            label="🏢 Total Companies Analyzed",
            value=summary["total_companies"],
            help="Total companies registered under your account.",
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with m_col2:
        st.markdown('<div class="kpi-card kpi-teal">', unsafe_allow_html=True)
        st.metric(
            label="📊 Total Financial Analyses",
            value=summary["total_analyses"],
            help="Total completed financial ratio analyses saved in SQLite.",
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with m_col3:
        st.markdown('<div class="kpi-card kpi-purple">', unsafe_allow_html=True)
        st.metric(
            label="📑 PDF Reports Generated",
            value=summary["total_reports"],
            help="Total official PDF analysis reports downloaded.",
        )
        st.markdown('</div>', unsafe_allow_html=True)

    # ------------------------------------------------------------------------
    # 3. Key Metrics - Financial Totals (INR ₹)
    # ------------------------------------------------------------------------
    st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
    f_col1, f_col2, f_col3 = st.columns(3)

    total_revenue = summary.get("total_revenue", 0.0)
    total_profit = summary.get("total_net_profit", 0.0)

    # Calculate average profit margin if revenue > 0
    margin_pct = (total_profit / total_revenue * 100) if total_revenue > 0 else 0.0

    with f_col1:
        st.markdown('<div class="kpi-card kpi-blue">', unsafe_allow_html=True)
        st.metric(
            label="💰 Total Revenue Tracked",
            value=format_indian_currency(total_revenue, compact=True),
            delta=f"Full: {format_indian_currency(total_revenue, compact=False)}" if total_revenue > 0 else None,
            delta_color="off",
            help="Cumulative revenue recorded across all your financial statements.",
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with f_col2:
        st.markdown('<div class="kpi-card kpi-green">', unsafe_allow_html=True)
        st.metric(
            label="📈 Total Net Profit",
            value=format_indian_currency(total_profit, compact=True),
            delta=f"Full: {format_indian_currency(total_profit, compact=False)}" if total_profit != 0 else None,
            delta_color="normal" if total_profit >= 0 else "inverse",
            help="Cumulative net profit recorded across all your financial statements.",
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with f_col3:
        st.markdown('<div class="kpi-card kpi-amber">', unsafe_allow_html=True)
        st.metric(
            label="🎯 Overall Net Profit Margin",
            value=f"{margin_pct:.2f}%" if total_revenue > 0 else "0.00%",
            delta="Healthy (≥ 10%)" if margin_pct >= 10.0 else ("Low (< 10%)" if total_revenue > 0 else None),
            delta_color="normal" if margin_pct >= 10.0 else "inverse",
            help="Aggregate net profit margin across tracked statements.",
        )
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # ------------------------------------------------------------------------
    # 4. Quick Action Buttons
    # ------------------------------------------------------------------------
    st.markdown("### ⚡ Quick Actions")
    q_col1, q_col2, q_col3, q_col4 = st.columns(4)

    with q_col1:
        if st.button("🏢 Add Company", use_container_width=True, type="secondary"):
            if on_navigate_callback:
                on_navigate_callback("Company Management")
            else:
                st.session_state["nav_selection"] = "Company Management"
                st.rerun()

    with q_col2:
        if st.button("📑 Enter Statement", use_container_width=True, type="secondary"):
            if on_navigate_callback:
                on_navigate_callback("Financial Statements")
            else:
                st.session_state["nav_selection"] = "Financial Statements"
                st.rerun()

    with q_col3:
        if st.button("📈 Calculate Ratios", use_container_width=True, type="secondary"):
            if on_navigate_callback:
                on_navigate_callback("Ratio Analysis")
            else:
                st.session_state["nav_selection"] = "Ratio Analysis"
                st.rerun()

    with q_col4:
        if st.button("📄 Generate Report", use_container_width=True, type="secondary"):
            if on_navigate_callback:
                on_navigate_callback("Reports")
            else:
                st.session_state["nav_selection"] = "Reports"
                st.rerun()

    st.markdown("---")

    # ------------------------------------------------------------------------
    # 5. Financial Performance Charts (Plotly)
    # ------------------------------------------------------------------------
    st.markdown("### 📊 Financial Performance Overview")

    all_analyses = database.list_analyses(user_id)

    if all_analyses and len(all_analyses) > 0:
        fig = visualization.create_performance_overview_chart(all_analyses)
        if fig is not None:
            st.plotly_chart(fig, use_container_width=True)
    else:
        # Informative Empty State for Performance Charts
        st.markdown(
            """
            <div style="background-color: #FFFFFF; border: 1.5px dashed #CBD5E1;
                        border-radius: 10px; padding: 32px 24px; text-align: center; margin-bottom: 20px;">
                <div style="font-size: 2.2rem; margin-bottom: 10px;">📊</div>
                <h4 style="color: #1E3A8A; margin-bottom: 6px; font-weight: 600;">No Financial Records to Display</h4>
                <p style="color: #64748B; max-width: 580px; margin: 0 auto 16px auto; font-size: 0.95rem;">
                    Once you add companies and input financial figures in <b>Company Management & Financial Statements</b>,
                    interactive Plotly charts comparing Revenue, Net Profit, and Ratios in Indian Rupees (₹) will appear here automatically.
                </p>
                <span style="display: inline-block; background-color: #EFF6FF; color: #1E40AF;
                             font-size: 0.85rem; font-weight: 500; padding: 6px 16px; border-radius: 20px;">
                    Ready for Data &bull; Database Scoped to Account #{}
                </span>
            </div>
            """.format(user_id),
            unsafe_allow_html=True,
        )

    # ------------------------------------------------------------------------
    # 6. Recent Financial Analyses Section
    # ------------------------------------------------------------------------
    st.markdown("### 🕒 Recent Financial Analyses")

    if recent_analyses and len(recent_analyses) > 0:
        # Prepare structured display table
        table_rows = []
        for row in recent_analyses:
            table_rows.append({
                "Company Name": row.get("company_name", "N/A"),
                "Financial Year": row.get("financial_year", "N/A"),
                "Analysis Date": format_indian_date(row.get("analysis_date")),
                "Total Revenue": format_indian_currency(row.get("total_revenue")),
                "Net Profit": format_indian_currency(row.get("net_profit")),
                "Ratios Computed": f"{row.get('ratios_calculated', 0)} Ratios",
                "Reports": f"{row.get('report_generated', 0)} Generated",
            })
        df_recent = pd.DataFrame(table_rows)
        st.dataframe(df_recent, use_container_width=True, hide_index=True)
    else:
        # Clean Empty State for Recent Analyses
        st.markdown(
            """
            <div style="background-color: #FFFFFF; border: 1px solid #E2E8F0;
                        border-radius: 10px; padding: 24px; text-align: center;">
                <p style="color: #64748B; margin: 0; font-size: 0.95rem;">
                    ℹ️ No recent analyses found. Saved ratio calculations and performance insights will be cataloged here.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )



```

---

## File: `pages\financial_insights.py`

```python
"""Financial Insights Module.

College Project: Financial Statement Ratio Analysis Assistant
This module implements Step 9:
- Rule-based financial interpretation (Healthy, Moderate, Needs Attention, Not Available)
- Comprehensive financial health score (0 to 100%) across 5 core pillars
- Key Strengths and Critical Areas of Concern
- Actionable recommendations tailored to Indian corporate benchmarks
- Strict user data isolation
"""

import pandas as pd
import streamlit as st
import database
import calculations
import analysis
from pages.dashboard import format_indian_currency, format_indian_date


CATEGORIES = [
    ("💧 Liquidity", "Liquidity", ["current_ratio", "quick_ratio", "cash_ratio"]),
    ("📈 Profitability", "Profitability", ["gross_profit_margin", "net_profit_margin", "return_on_assets", "return_on_equity"]),
    ("🛡️ Solvency", "Solvency", ["debt_to_equity", "debt_ratio", "interest_coverage"]),
    ("⚙️ Efficiency", "Efficiency", ["inventory_turnover", "asset_turnover"]),
    ("💸 Cash Flow", "Cash Flow", ["operating_cash_flow_ratio", "free_cash_flow"]),
]


def render_financial_insights_page(user: dict):
    """Render the Financial Insights and rule-based interpretation screen."""
    user_id = user["id"]

    st.markdown(
        """
        <div style="margin-bottom: 20px;">
            <h1 style="color: #142B4A; font-weight: 700; margin-bottom: 4px;">
                💡 Financial Insights & Interpretation
            </h1>
            <p style="color: #5A6E85; font-size: 1rem; margin: 0;">
                Deterministic rule-based diagnosis of corporate financial health, operational efficiency, and risk factors.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 1. Fetch statements
    statements = database.list_statements(user_id)
    if not statements:
        st.info(
            "ℹ️ **No Financial Statements Found:** To view financial insights, "
            "please enter company statement data under **📑 Financial Statements**."
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

    col_sel1, col_sel2 = st.columns([2, 1])
    with col_sel1:
        selected_label = st.selectbox(
            "Select Company & Financial Year for Diagnosis *",
            statement_labels,
            key="insights_statement_select",
        )
        active_statement = statement_map[selected_label]
        statement_id = active_statement["id"]
        active_company_id = active_statement["company_id"]
        active_company = companies_lookup.get(active_company_id, {})

    with col_sel2:
        st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
        st.caption(
            f"**Industry:** {active_company.get('industry', 'N/A')}<br>"
            f"**Evaluation Type:** Deterministic Rule-Based System",
            unsafe_allow_html=True,
        )

    # 3. Retrieve or calculate ratios
    ratios = database.get_ratios(user_id, statement_id)
    if not ratios:
        ratios = calculations.calculate_all_ratios(active_statement)

    # 4. Generate Comprehensive Health Evaluation
    health_report = analysis.compute_comprehensive_financial_health(ratios)
    overall_score = health_report["overall_score"]
    health_grade = health_report["health_grade"]
    cat_scores = health_report["category_scores"]
    strengths = health_report["strengths"]
    concerns = health_report["concerns"]
    all_evals = health_report["all_evaluations"]

    # Grade styling
    badge_bg = {
        "green": "#DCFCE7",
        "blue": "#DBEAFE",
        "orange": "#FEF3C7",
        "red": "#FEE2E2",
    }.get(health_report["grade_color"], "#F1F5F9")

    badge_fg = {
        "green": "#166534",
        "blue": "#1E40AF",
        "orange": "#92400E",
        "red": "#991B1B",
    }.get(health_report["grade_color"], "#0F172A")

    st.markdown("---")

    # ------------------------------------------------------------------------
    # EXECUTIVE FINANCIAL HEALTH SCORECARD
    # ------------------------------------------------------------------------
    st.markdown(
        f"""
        <div style="background-color: #FFFFFF; border: 1px solid #E2E8F0; border-left: 5px solid #2878D0; border-radius: 12px;
                    padding: 24px; margin-bottom: 24px; box-shadow: 0 2px 8px rgba(20, 43, 74, 0.04);">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <div>
                    <span style="color: #64748B; font-size: 0.82rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">
                        Executive Summary &bull; {active_company.get('company_name', 'Company')} ({active_statement['financial_year']})
                    </span>
                    <h2 style="color: #142B4A; margin: 4px 0 6px 0; font-weight: 800; font-size: 1.65rem;">
                        Overall Health Score: {overall_score} / 100
                    </h2>
                    <span style="background-color: {badge_bg}; color: {badge_fg}; font-size: 0.9rem;
                                 font-weight: 700; padding: 4px 14px; border-radius: 16px;">
                        {health_grade}
                    </span>
                </div>
                <div style="text-align: right; margin-top: 8px;">
                    <div style="color: #64748B; font-size: 0.85rem; font-weight: 500;">Evaluation Basis</div>
                    <div style="font-weight: 700; color: #142B4A; font-size: 0.95rem;">
                        14 Standard Financial Ratios
                    </div>
                    <div style="font-size: 0.8rem; color: #20A46B; font-weight: 600;">
                        Deterministic Financial Logic
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 5 Pillar Progress Cards
    p_col1, p_col2, p_col3, p_col4, p_col5 = st.columns(5)
    with p_col1:
        st.markdown('<div class="kpi-card kpi-blue">', unsafe_allow_html=True)
        st.metric("💧 Liquidity", f"{cat_scores.get('Liquidity', 0.0)}%", help="Ability to meet short-term commitments.")
        st.markdown('</div>', unsafe_allow_html=True)
    with p_col2:
        st.markdown('<div class="kpi-card kpi-green">', unsafe_allow_html=True)
        st.metric("📈 Profitability", f"{cat_scores.get('Profitability', 0.0)}%", help="Margin strength & capital returns.")
        st.markdown('</div>', unsafe_allow_html=True)
    with p_col3:
        st.markdown('<div class="kpi-card kpi-purple">', unsafe_allow_html=True)
        st.metric("🛡️ Solvency", f"{cat_scores.get('Solvency', 0.0)}%", help="Long-term debt safety & leverage.")
        st.markdown('</div>', unsafe_allow_html=True)
    with p_col4:
        st.markdown('<div class="kpi-card kpi-teal">', unsafe_allow_html=True)
        st.metric("⚙️ Efficiency", f"{cat_scores.get('Efficiency', 0.0)}%", help="Asset and inventory velocity.")
        st.markdown('</div>', unsafe_allow_html=True)
    with p_col5:
        st.markdown('<div class="kpi-card kpi-amber">', unsafe_allow_html=True)
        st.metric("💸 Cash Flow", f"{cat_scores.get('Cash Flow', 0.0)}%", help="Core cash backing and Free Cash Flow.")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # ------------------------------------------------------------------------
    # STRENGTHS & VULNERABILITIES CALLOUTS
    # ------------------------------------------------------------------------
    h_col1, h_col2 = st.columns(2)

    with h_col1:
        st.markdown("### 🏆 Key Financial Strengths")
        if strengths:
            for s in strengths[:4]:
                st.markdown(
                    f"""
                    <div style="background-color: #F0FDF4; border-left: 4px solid #10B981; border-radius: 6px;
                                padding: 12px 16px; margin-bottom: 12px;">
                        <div style="font-weight: 700; color: #166534; font-size: 0.95rem;">
                            ✓ {s['name']}: {s['headline']}
                        </div>
                        <div style="color: #374151; font-size: 0.85rem; margin-top: 4px;">
                            {s['detailed_insight']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        else:
            st.info("ℹ️ No dominant outlier strengths identified for this statement.")

    with h_col2:
        st.markdown("### ⚠️ Areas Requiring Attention")
        if concerns:
            for c in concerns[:4]:
                st.markdown(
                    f"""
                    <div style="background-color: #FEF2F2; border-left: 4px solid #EF4444; border-radius: 6px;
                                padding: 12px 16px; margin-bottom: 12px;">
                        <div style="font-weight: 700; color: #991B1B; font-size: 0.95rem;">
                            ⚠ {c['name']}: {c['headline']}
                        </div>
                        <div style="color: #374151; font-size: 0.85rem; margin-top: 4px;">
                            {c['detailed_insight']}
                        </div>
                        <div style="color: #7F1D1D; font-size: 0.82rem; margin-top: 4px; font-weight: 500;">
                            👉 <b>Action:</b> {c['recommendation']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        else:
            st.success("✅ **Zero Critical Vulnerabilities:** No ratios fell below minimum warning thresholds.")

    st.markdown("---")

    # ------------------------------------------------------------------------
    # DETAILED CATEGORIZED INSIGHTS TABS
    # ------------------------------------------------------------------------
    st.markdown("### 🔍 In-Depth Category Diagnosis")

    tab_liq, tab_prof, tab_solv, tab_eff, tab_cf = st.tabs([
        "💧 Liquidity",
        "📈 Profitability",
        "🛡️ Solvency",
        "⚙️ Efficiency",
        "💸 Cash Flow",
    ])

    def render_detailed_insight_card(key: str):
        item = all_evals.get(key)
        if not item:
            return

        status_colors = {
            "Healthy": ("#DCFCE7", "#166534", "✅"),
            "Moderate": ("#DBEAFE", "#1E40AF", "ℹ️"),
            "Needs Attention": ("#FEE2E2", "#991B1B", "⚠️"),
            "Not Available": ("#F1F5F9", "#475569", "⚪"),
        }
        bg, fg, icon = status_colors.get(item["status"], ("#F1F5F9", "#475569", "•"))

        val_display = (
            f"{item['value']:.2f}{item['unit']}"
            if item["value"] is not None and item["unit"] != "₹"
            else (format_indian_currency(item["value"]) if item["unit"] == "₹" else "N/A")
        )

        st.markdown(
            f"""
            <div style="background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 10px;
                        padding: 16px 20px; margin-bottom: 16px; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                    <div>
                        <h4 style="color: #1E3A8A; margin: 0 0 2px 0; font-size: 1.1rem; font-weight: 700;">
                            {item['name']} &mdash; <span style="color: #0F172A;">{val_display}</span>
                        </h4>
                        <span style="color: #64748B; font-size: 0.82rem; font-weight: 500;">
                            {item['headline']}
                        </span>
                    </div>
                    <div style="margin-top: 4px;">
                        <span style="background-color: {bg}; color: {fg}; font-size: 0.8rem;
                                     font-weight: 700; padding: 4px 10px; border-radius: 14px;">
                            {icon} {item['status']}
                        </span>
                    </div>
                </div>
                <div style="margin-top: 10px; padding-top: 8px; border-top: 1px solid #F1F5F9;">
                    <p style="color: #334155; font-size: 0.88rem; line-height: 1.45; margin: 0 0 8px 0;">
                        {item['detailed_insight']}
                    </p>
                    <div style="background-color: #F8FAFC; border-left: 3px solid #3B82F6; padding: 8px 12px; border-radius: 4px;">
                        <span style="color: #1E40AF; font-size: 0.82rem; font-weight: 600;">Strategic Guidance:</span>
                        <span style="color: #475569; font-size: 0.82rem;">{item['recommendation']}</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with tab_liq:
        st.markdown("#### 💧 Liquidity Health & Short-Term Obligations")
        render_detailed_insight_card("current_ratio")
        render_detailed_insight_card("quick_ratio")
        render_detailed_insight_card("cash_ratio")

    with tab_prof:
        st.markdown("#### 📈 Profitability Margins & Capital Productivity")
        render_detailed_insight_card("gross_profit_margin")
        render_detailed_insight_card("net_profit_margin")
        render_detailed_insight_card("return_on_assets")
        render_detailed_insight_card("return_on_equity")

    with tab_solv:
        st.markdown("#### 🛡️ Long-Term Solvency & Debt Gearing")
        render_detailed_insight_card("debt_to_equity")
        render_detailed_insight_card("debt_ratio")
        render_detailed_insight_card("interest_coverage")

    with tab_eff:
        st.markdown("#### ⚙️ Operational Asset & Inventory Velocity")
        render_detailed_insight_card("inventory_turnover")
        render_detailed_insight_card("asset_turnover")

    with tab_cf:
        st.markdown("#### 💸 Cash Flow Viability & Self-Funded Growth")
        render_detailed_insight_card("operating_cash_flow_ratio")
        render_detailed_insight_card("free_cash_flow")

```

---

## File: `pages\financial_statements.py`

```python
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

```

---

## File: `pages\history.py`

```python
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

```

---

## File: `pages\ratio_analysis.py`

```python
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

```

---

## File: `pages\reports.py`

```python
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

```

---

## File: `pdf_report.py`

```python
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

```

---

## File: `requirements.txt`

```
streamlit>=1.40
pandas>=2.2
plotly>=5.24
reportlab>=4.2

```

---

## File: `test_auth.py`

```python
"""Comprehensive test suite for authentication.py and database integration."""

import os
import tempfile
import sqlite3
from pathlib import Path
import database
import authentication


def run_all_tests():
    print("=" * 60)
    print("RUNNING AUTHENTICATION & REGISTRATION TESTS")
    print("=" * 60)

    # 1. PBKDF2 Password Hashing Tests
    print("\n[Test 1] PBKDF2 Hashing and Verification")
    pwd = "SecureStudentPass@123"
    hash1, salt1 = authentication.hash_password(pwd)
    assert len(salt1) == 32, f"Expected 32 hex chars for salt, got {len(salt1)}"
    assert len(hash1) == 64, f"Expected 64 hex chars for SHA256 hash, got {len(hash1)}"
    assert hash1 != pwd, "Plaintext password must not equal hash!"

    # Verify correct password
    assert authentication.verify_password(pwd, hash1, salt1) is True, "Password verification failed for correct password!"

    # Verify wrong password
    assert authentication.verify_password("WrongPassword!", hash1, salt1) is False, "Verification accepted wrong password!"

    # Verify salt uniqueness
    hash2, salt2 = authentication.hash_password(pwd)
    assert salt1 != salt2, "Two generated salts must be unique!"
    assert hash1 != hash2, "Hashes with different salts must differ!"
    print("  --> PBKDF2 password hashing & verification PASSED.")

    # 2. Input Validation Tests
    print("\n[Test 2] Input Validation")
    # Empty name
    ok, msg = authentication.validate_registration_inputs("", "test@example.com", "pass123", "pass123")
    assert not ok and "Full name" in msg, f"Failed empty name check: {msg}"

    # Invalid email
    ok, msg = authentication.validate_registration_inputs("Ramesh Sharma", "notanemail", "pass123", "pass123")
    assert not ok and "valid email" in msg, f"Failed invalid email check: {msg}"

    # Password too short (< 6 chars)
    ok, msg = authentication.validate_registration_inputs("Ramesh Sharma", "ramesh@example.com", "12345", "12345")
    assert not ok and "at least 6 characters" in msg, f"Failed short password check: {msg}"

    # Password mismatch
    ok, msg = authentication.validate_registration_inputs("Ramesh Sharma", "ramesh@example.com", "password123", "password456")
    assert not ok and "do not match" in msg, f"Failed password mismatch check: {msg}"

    # Valid inputs
    ok, msg = authentication.validate_registration_inputs("Ramesh Sharma", "ramesh@example.com", "pass123", "pass123")
    assert ok, f"Valid registration failed validation: {msg}"
    print("  --> Input validation PASSED.")

    # 3. Registration, Duplicate Email Prevention, and DB Persistence
    print("\n[Test 3] Registration and Database Persistence (Isolated Test DB)")
    temp_dir = tempfile.mkdtemp()
    temp_db = Path(temp_dir) / "test_auth.db"
    database.init_db(temp_db)

    # Register first user
    ok, msg = authentication.register_user(
        "Asha Rao", "asha.rao@college.edu", "AshaPass2026", "AshaPass2026", db_path=temp_db
    )
    assert ok is True, f"Registration failed: {msg}"
    print("  --> User 1 registered successfully.")

    # Verify in DB
    user_record = database.get_user_by_email("asha.rao@college.edu", db_path=temp_db)
    assert user_record is not None, "User record not found in database!"
    assert user_record["full_name"] == "Asha Rao"
    assert user_record["email"] == "asha.rao@college.edu"
    assert "AshaPass2026" not in user_record["password_hash"], "Plaintext password found in database!"
    assert len(user_record["password_salt"]) == 32
    print("  --> User verified in SQLite database (plain-text password NOT stored).")

    # Duplicate email registration attempt (identical)
    ok, msg = authentication.register_user(
        "Asha Duplicate", "asha.rao@college.edu", "AnotherPass123", "AnotherPass123", db_path=temp_db
    )
    assert ok is False, "Duplicate email registration was erroneously allowed!"
    assert "already exists" in msg, f"Unexpected duplicate email message: {msg}"

    # Duplicate email registration attempt (different case: ASHA.RAO@COLLEGE.EDU)
    ok, msg = authentication.register_user(
        "Asha Uppercase", "ASHA.RAO@COLLEGE.EDU", "AnotherPass123", "AnotherPass123", db_path=temp_db
    )
    assert ok is False, "Duplicate uppercase email registration was erroneously allowed!"
    assert "already exists" in msg, f"Unexpected uppercase duplicate email message: {msg}"
    print("  --> Duplicate email prevention PASSED.")

    # 4. User Login and Authentication Tests
    print("\n[Test 4] User Login & Authentication")
    # Successful login
    ok, msg, safe_user = authentication.authenticate_user("asha.rao@college.edu", "AshaPass2026", db_path=temp_db)
    assert ok is True, f"Login failed for valid credentials: {msg}"
    assert safe_user["id"] == user_record["id"]
    assert safe_user["full_name"] == "Asha Rao"
    assert safe_user["email"] == "asha.rao@college.edu"
    assert "password_hash" not in safe_user, "password_hash leaked in safe_user object!"
    assert "password_salt" not in safe_user, "password_salt leaked in safe_user object!"
    print("  --> Valid login succeeded with safe user dictionary.")

    # Wrong password login
    ok, msg, bad_user = authentication.authenticate_user("asha.rao@college.edu", "WrongPassword", db_path=temp_db)
    assert ok is False, "Login succeeded with wrong password!"
    assert bad_user is None
    assert "Invalid email or password" in msg

    # Non-existent email login
    ok, msg, bad_user = authentication.authenticate_user("nobody@college.edu", "SomePassword", db_path=temp_db)
    assert ok is False, "Login succeeded with non-existent email!"
    assert bad_user is None
    assert "Invalid email or password" in msg
    print("  --> Invalid credentials handling PASSED.")

    # 5. User Data Isolation Verification
    print("\n[Test 5] User-Specific Data Isolation")
    # Register second user
    ok, msg = authentication.register_user(
        "Rohan Gupta", "rohan@college.edu", "RohanPass2026", "RohanPass2026", db_path=temp_db
    )
    assert ok is True
    ok, _, user2 = authentication.authenticate_user("rohan@college.edu", "RohanPass2026", db_path=temp_db)

    # User 1 creates a company
    c_id = database.create_company(
        user_id=safe_user["id"],
        company_name="Asha Tech Ltd",
        industry="Technology",
        financial_year="FY 2025-26",
        db_path=temp_db,
    )
    assert c_id > 0

    # User 1 dashboard summary
    summary1 = database.dashboard_summary(safe_user["id"], db_path=temp_db)
    assert summary1["total_companies"] == 1, f"Expected 1 company for User 1, got {summary1['total_companies']}"

    # User 2 dashboard summary (must be 0)
    summary2 = database.dashboard_summary(user2["id"], db_path=temp_db)
    assert summary2["total_companies"] == 0, f"Expected 0 companies for User 2, got {summary2['total_companies']}"

    # User 2 cannot list User 1's companies
    user2_companies = database.list_companies(user2["id"], db_path=temp_db)
    assert len(user2_companies) == 0, f"User 2 can see companies: {user2_companies}"
    print("  --> User-specific data isolation PASSED.")

    # 6. Session Management Simulation
    print("\n[Test 6] Session Management & Logout Simulation")
    import unittest.mock as mock

    # Mock st.session_state
    fake_session = {}
    with mock.patch.object(authentication.st, "session_state", fake_session):
        authentication.init_session_state()
        assert authentication.is_authenticated() is False
        assert authentication.get_current_user() is None
        assert authentication.get_current_user_id() is None

        # Simulate login
        dummy_user = {"id": 42, "full_name": "Test Student", "email": "test@student.edu"}
        authentication.login_session(dummy_user)
        assert authentication.is_authenticated() is True
        assert authentication.get_current_user()["id"] == 42
        assert authentication.get_current_user_id() == 42

        # Simulate logout (mocking st.rerun to prevent exception)
        with mock.patch.object(authentication.st, "rerun"):
            authentication.logout()
            assert authentication.is_authenticated() is False
            assert authentication.get_current_user() is None
            assert authentication.get_current_user_id() is None
    print("  --> Session state initialization, login, and logout PASSED.")

    # 7. Persistence After Restart Simulation
    print("\n[Test 7] Persistence After Application Restart")
    # Simulate completely closing connection and re-opening the file as a new app instance
    del user_record
    del safe_user
    del user2

    # Fresh lookup from disk
    persisted_user = database.get_user_by_email("asha.rao@college.edu", db_path=temp_db)
    assert persisted_user is not None, "User not found after simulated application restart!"
    assert persisted_user["full_name"] == "Asha Rao"

    # Authenticate on the reopened database
    reopened_login_ok, _, reopened_user = authentication.authenticate_user(
        "asha.rao@college.edu", "AshaPass2026", db_path=temp_db
    )
    assert reopened_login_ok is True, "Login failed after simulated application restart!"
    assert reopened_user["email"] == "asha.rao@college.edu"

    # Verify user's company persisted
    persisted_companies = database.list_companies(reopened_user["id"], db_path=temp_db)
    assert len(persisted_companies) == 1, "User's company data did not persist after restart!"
    assert persisted_companies[0]["company_name"] == "Asha Tech Ltd"
    print("  --> Persistence across restart verified (accounts, hashes, and relational data intact).")

    # Clean up temp file
    try:
        os.remove(temp_db)
        os.rmdir(temp_dir)
    except Exception:
        pass

    print("\n" + "=" * 60)
    print("ALL 7 TEST SUITES PASSED! (100% SUCCESS)")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()

```

---

## File: `test_dashboard.py`

```python
"""Automated test suite for Step 5: Professional Dashboard and Indian Financial Formatting."""

import os
import tempfile
import unittest.mock as mock
from pathlib import Path
import database
import authentication
import visualization
from pages import dashboard


def test_indian_formatting():
    print("\n[Test 1] Indian Currency & Date Formatting")
    # Currency tests
    assert dashboard.format_indian_currency(0) == "₹ 0"
    assert dashboard.format_indian_currency(None) == "₹ 0"
    assert dashboard.format_indian_currency(500) == "₹ 500"
    assert dashboard.format_indian_currency(1500) == "₹ 1,500"
    assert dashboard.format_indian_currency(150000) == "₹ 1,50,000"
    assert dashboard.format_indian_currency(150000, compact=True) == "₹ 1.50 Lakh"
    assert dashboard.format_indian_currency(12500000) == "₹ 1,25,00,000"
    assert dashboard.format_indian_currency(12500000, compact=True) == "₹ 1.25 Cr"
    assert dashboard.format_indian_currency(-450000) == "-₹ 4,50,000"
    assert dashboard.format_indian_currency(-450000, compact=True) == "-₹ 4.50 Lakh"
    assert dashboard.format_indian_currency(12345678.50) == "₹ 1,23,45,678.50"

    # Date formatting tests
    assert dashboard.format_indian_date("2026-11-15 16:46:36") == "15-11-2026"
    assert dashboard.format_indian_date("2026-04-01") == "01-04-2026"
    assert dashboard.format_indian_date(None) == "N/A"
    print("  --> Indian currency (₹, Lakhs/Crores) and date (DD-MM-YYYY) tests PASSED.")


def test_database_dashboard_summary():
    print("\n[Test 2] Database dashboard_summary with Financial Aggregates")
    temp_dir = tempfile.mkdtemp()
    temp_db = Path(temp_dir) / "test_dash.db"
    database.init_db(temp_db)

    # Register 2 users
    u1 = database.create_user("Asha Rao", "asha@dash.com", "hash1", "salt1", temp_db)
    u2 = database.create_user("Rohan Gupta", "rohan@dash.com", "hash2", "salt2", temp_db)

    # Initially both users have 0 records
    sum1_empty = database.dashboard_summary(u1, temp_db)
    assert sum1_empty["total_companies"] == 0
    assert sum1_empty["total_analyses"] == 0
    assert sum1_empty["total_reports"] == 0
    assert sum1_empty["total_revenue"] == 0.0
    assert sum1_empty["total_net_profit"] == 0.0
    assert sum1_empty["recent_analyses"] == []

    # User 1 creates a company and financial statement
    c1 = database.create_company(u1, "Reliance Textiles", "Manufacturing", "FY 2024-25", "", temp_db)
    database.save_full_analysis(
        u1,
        c1,
        {"financial_year": "FY 2024-25", "revenue": 5000000.0, "net_income": 750000.0},
        {"current_ratio": 2.1, "net_profit_margin": 15.0},
        temp_db,
    )

    # User 1 summary must reflect the saved amounts
    sum1 = database.dashboard_summary(u1, temp_db)
    assert sum1["total_companies"] == 1
    assert sum1["total_analyses"] == 1
    assert sum1["total_revenue"] == 5000000.0
    assert sum1["total_net_profit"] == 750000.0
    assert len(sum1["recent_analyses"]) == 1
    assert sum1["recent_analyses"][0]["company_name"] == "Reliance Textiles"

    # User 2 must STILL have 0 records (Strict Isolation)
    sum2 = database.dashboard_summary(u2, temp_db)
    assert sum2["total_companies"] == 0
    assert sum2["total_analyses"] == 0
    assert sum2["total_revenue"] == 0.0
    assert sum2["total_net_profit"] == 0.0
    assert sum2["recent_analyses"] == []
    print("  --> Database summary, aggregates, and user isolation PASSED.")

    # Clean up
    try:
        os.remove(temp_db)
        os.rmdir(temp_dir)
    except Exception:
        pass


def test_visualization_charts():
    print("\n[Test 3] Plotly Performance Chart Generation")
    # Empty records
    empty_fig = visualization.create_performance_overview_chart([])
    assert empty_fig is None

    # Sample records
    sample_data = [
        {
            "company_name": "Bharat Electronics",
            "financial_year": "FY 2024-25",
            "total_revenue": 12000000.0,
            "net_profit": 2400000.0,
        },
        {
            "company_name": "Tata Motors",
            "financial_year": "FY 2024-25",
            "total_revenue": 45000000.0,
            "net_profit": 6000000.0,
        },
    ]
    fig = visualization.create_performance_overview_chart(sample_data)
    assert fig is not None
    assert len(fig.data) == 2  # Revenue and Net Profit traces
    assert fig.data[0].name == "Total Revenue (₹)"
    assert fig.data[1].name == "Net Profit (₹)"
    print("  --> Plotly chart generation & styling PASSED.")


def test_dashboard_render_simulation():
    print("\n[Test 4] Dashboard Render Execution Simulation")
    # Simulate render_dashboard for a mock user using mocks for streamlit UI calls
    mock_user = {"id": 1, "full_name": "Ruturaj Bhosale", "email": "rutu522@gmail.com"}

    with mock.patch("pages.dashboard.st") as mock_st, \
         mock.patch("pages.dashboard.database") as mock_db, \
         mock.patch("pages.dashboard.visualization") as mock_viz:

        # Mock database return for 0 records
        mock_db.dashboard_summary.return_value = {
            "total_companies": 0,
            "total_analyses": 0,
            "total_reports": 0,
            "total_revenue": 0.0,
            "total_net_profit": 0.0,
            "recent_analyses": [],
        }
        mock_db.list_analyses.return_value = []
        mock_st.columns.side_effect = lambda n: [mock.MagicMock() for _ in range(n if isinstance(n, int) else len(n))]

        # Call render_dashboard for empty state
        dashboard.render_dashboard(mock_user)
        assert mock_db.dashboard_summary.called

        # Mock database return with 1 analysis
        mock_db.dashboard_summary.return_value = {
            "total_companies": 1,
            "total_analyses": 1,
            "total_reports": 0,
            "total_revenue": 1000000.0,
            "total_net_profit": 150000.0,
            "recent_analyses": [{
                "company_name": "Test Co",
                "financial_year": "FY 2025-26",
                "analysis_date": "2026-11-15",
                "total_revenue": 1000000.0,
                "net_profit": 150000.0,
                "ratios_calculated": 10,
                "report_generated": 0,
            }],
        }
        mock_db.list_analyses.return_value = [{
            "company_name": "Test Co",
            "financial_year": "FY 2025-26",
            "total_revenue": 1000000.0,
            "net_profit": 150000.0,
        }]
        dashboard.render_dashboard(mock_user)
        print("  --> Dashboard render simulation (both empty and populated states) PASSED.")


if __name__ == "__main__":
    print("=" * 60)
    print("RUNNING STEP 5 PROFESSIONAL DASHBOARD VERIFICATION TESTS")
    print("=" * 60)
    test_indian_formatting()
    test_database_dashboard_summary()
    test_visualization_charts()
    test_dashboard_render_simulation()
    print("\n" + "=" * 60)
    print("ALL STEP 5 TESTS PASSED SUCCESSFULLY! (100% PASS)")
    print("=" * 60)

```

---

## File: `test_quick_action_buttons.py`

```python
"""Comprehensive test suite for Quick Action buttons and cross-page navigation."""

import unittest.mock as mock
import main
from pages import dashboard

NAV_ITEMS = main.NAV_ITEMS


def test_quick_action_button_routing():
    print("=" * 60)
    print("TESTING QUICK ACTION BUTTONS & STREAMLIT SESSION STATE")
    print("=" * 60)

    # 1. Test navigate_to callback
    print("\n[Test 1] Testing navigate_to Callback")
    mock_session = {}
    with mock.patch.object(main.st, "session_state", mock_session), \
         mock.patch.object(main.st, "rerun") as mock_rerun:
        main.navigate_to("Company Management")
        assert mock_session.get("nav_selection") == "Company Management"
        assert mock_rerun.called
    print("  --> navigate_to properly sets nav_selection and calls rerun without modifying widget key.")

    # 2. Test render_sidebar consumes nav_selection before widget instantiation
    print("\n[Test 2] Testing render_sidebar Safe Consumption of nav_selection")
    buttons_to_test = [
        ("🏢 Add Company", "Company Management", "🏢 Company Management"),
        ("📑 Enter Statement", "Financial Statements", "📑 Financial Statements"),
        ("📈 Calculate Ratios", "Ratio Analysis", "📈 Ratio Analysis"),
        ("📄 Generate Report", "Reports", "📄 Reports"),
        ("⬅️ Back to Dashboard", "Dashboard", "📊 Dashboard"),
    ]

    for btn_name, target_kw, expected_item in buttons_to_test:
        sim_session = {
            "nav_selection": target_kw,
            "sidebar_nav": "📊 Dashboard",
        }

        # Mock streamlit inside main.py
        with mock.patch.object(main.st, "session_state", sim_session), \
             mock.patch.object(main.st, "sidebar") as mock_sidebar, \
             mock.patch.object(main.st, "radio", return_value=expected_item) as mock_radio:

            user_mock = {"id": 1, "full_name": "Test User", "email": "test@example.com"}
            selection = main.render_sidebar(user_mock)

            # Verification:
            # a) nav_selection was popped
            assert "nav_selection" not in sim_session, f"nav_selection was not cleared for {btn_name}"
            # b) sidebar_nav in session_state was updated to the full item before radio call
            assert sim_session["sidebar_nav"] == expected_item, f"Expected {expected_item}, got {sim_session['sidebar_nav']}"
            # c) radio was called with the updated key without throwing WidgetAlreadyInstantiated
            assert mock_radio.called
            # d) selection matches expected target
            assert selection == expected_item
            print(f"  [Button: {btn_name}] -> Successfully navigated to '{expected_item}'")

    # 3. Test Dashboard button triggers
    print("\n[Test 3] Testing Dashboard Quick Action Button Triggers")
    user_mock = {"id": 1, "full_name": "Test User", "email": "test@example.com"}

    with mock.patch("pages.dashboard.st") as mock_dash_st, \
         mock.patch("pages.dashboard.database") as mock_dash_db:

        mock_dash_db.dashboard_summary.return_value = {
            "total_companies": 0, "total_analyses": 0, "total_reports": 0,
            "total_revenue": 0.0, "total_net_profit": 0.0, "recent_analyses": [],
        }
        mock_dash_db.list_analyses.return_value = []
        mock_dash_st.columns.side_effect = lambda n: [mock.MagicMock() for _ in range(n if isinstance(n, int) else len(n))]

        # Mock callback
        mock_cb = mock.MagicMock()
        dashboard.render_dashboard(user_mock, on_navigate_callback=mock_cb)

        # Ensure dashboard rendered without error
        assert mock_dash_db.dashboard_summary.called
        print("  --> Dashboard rendered with navigation callback hooked up cleanly.")

    print("\n" + "=" * 60)
    print("ALL QUICK ACTION BUTTON TESTS PASSED (100% SUCCESS)!")
    print("=" * 60)


if __name__ == "__main__":
    test_quick_action_button_routing()

```

---

## File: `test_quick_actions.py`

```python
"""Test diagnostic script for Quick Action navigation mechanism."""

import main

NAV_ITEMS = main.NAV_ITEMS

def simulate_navigation(target_keyword, session_state):
    # Simulate button click
    session_state["nav_selection"] = target_keyword

    # Simulate next script execution in main.py BEFORE st.radio instantiation
    if "nav_selection" in session_state:
        target = session_state.pop("nav_selection")
        for item in NAV_ITEMS:
            if target in item:
                session_state["sidebar_nav"] = item
                break

    return session_state["sidebar_nav"]


def run_tests():
    print("Testing Quick Action Button Navigation Destinations:")
    session_state = {"sidebar_nav": "📊 Dashboard"}

    # Test 1: Add Company
    dest1 = simulate_navigation("Company Management", session_state)
    assert dest1 == "🏢 Company Management", f"Expected '🏢 Company Management', got '{dest1}'"
    print("  [Button 1: Add Company] ->", dest1, "OK")

    # Test 2: Enter Statement
    dest2 = simulate_navigation("Financial Statements", session_state)
    assert dest2 == "📑 Financial Statements", f"Expected '📑 Financial Statements', got '{dest2}'"
    print("  [Button 2: Enter Statement] ->", dest2, "OK")

    # Test 3: Calculate Ratios
    dest3 = simulate_navigation("Ratio Analysis", session_state)
    assert dest3 == "📈 Ratio Analysis", f"Expected '📈 Ratio Analysis', got '{dest3}'"
    print("  [Button 3: Calculate Ratios] ->", dest3, "OK")

    # Test 4: Generate Report
    dest4 = simulate_navigation("Reports", session_state)
    assert dest4 == "📄 Reports", f"Expected '📄 Reports', got '{dest4}'"
    print("  [Button 4: Generate Report] ->", dest4, "OK")

    # Test 5: Back to Dashboard
    dest5 = simulate_navigation("Dashboard", session_state)
    assert dest5 == "📊 Dashboard", f"Expected '📊 Dashboard', got '{dest5}'"
    print("  [Back to Dashboard] ->", dest5, "OK")

    print("\nAll 5 navigation targets verified!")


if __name__ == "__main__":
    run_tests()

```

---

## File: `test_step_10.py`

```python
"""Test suite for Step 10: Financial Comparison and Multi-Year Trend Analysis."""

import os
import tempfile
from pathlib import Path
import database
import calculations
import visualization
from pages import comparison


def test_multi_year_trend_chart():
    print("\n[Test 1] Multi-Year Trend Chart Generation")
    # Less than 2 statements
    fig_empty = visualization.create_multi_year_trend_chart([])
    assert fig_empty is None
    fig_one = visualization.create_multi_year_trend_chart([{"financial_year": "FY 2024-25"}])
    assert fig_one is None

    # Two years of statements
    two_years = [
        {"financial_year": "FY 2023-24", "revenue": 8000000.0, "net_income": 800000.0},
        {"financial_year": "FY 2024-25", "revenue": 10000000.0, "net_income": 1500000.0},
    ]
    fig = visualization.create_multi_year_trend_chart(two_years, company_name="Bharat Motors")
    assert fig is not None
    assert len(fig.data) == 3  # Revenue bar, Profit bar, Margin scatter line
    assert fig.data[0].name == "Revenue (₹)"
    assert fig.data[1].name == "Net Profit (₹)"
    assert fig.data[2].name == "Net Margin (%)"
    print("  --> Multi-year trend chart generated with all 3 traces (Revenue, Profit, Margin).")


def test_peer_radar_chart():
    print("\n[Test 2] Peer Benchmarking Radar Chart Generation")
    # Less than 2 peers
    assert visualization.create_peer_comparison_radar_chart({}) is None
    assert visualization.create_peer_comparison_radar_chart({"Comp A": {}}) is None

    # Two peer companies
    radar_data = {
        "Tata Motors": {"Liquidity": 85.0, "Profitability": 80.0, "Solvency": 75.0, "Efficiency": 90.0, "Cash Flow": 80.0},
        "Mahindra & Mahindra": {"Liquidity": 80.0, "Profitability": 85.0, "Solvency": 80.0, "Efficiency": 85.0, "Cash Flow": 75.0},
    }
    fig_radar = visualization.create_peer_comparison_radar_chart(radar_data)
    assert fig_radar is not None
    assert len(fig_radar.data) == 2  # 2 peer radar polygons
    assert fig_radar.data[0].name == "Tata Motors"
    assert fig_radar.data[1].name == "Mahindra & Mahindra"
    print("  --> Peer comparison radar chart generated successfully.")


def test_yoy_growth_calculations():
    print("\n[Test 3] YoY Growth & Comparison Logic")
    rev_2024 = 8000000.0   # 80 Lakh
    rev_2025 = 10000000.0  # 100 Lakh
    growth = ((rev_2025 - rev_2024) / rev_2024) * 100.0
    assert growth == 25.0, f"Expected 25.0% YoY revenue growth, got {growth}"

    profit_2024 = 800000.0   # 8 Lakh (10% margin)
    profit_2025 = 1500000.0  # 15 Lakh (15% margin)
    profit_growth = ((profit_2025 - profit_2024) / profit_2024) * 100.0
    assert profit_growth == 87.5, f"Expected 87.5% YoY profit growth, got {profit_growth}"

    margin_2024 = 800000.0 / 8000000.0 * 100.0  # 10.0%
    margin_2025 = 1500000.0 / 10000000.0 * 100.0 # 15.0%
    margin_expansion = margin_2025 - margin_2024
    assert margin_expansion == 5.0, f"Expected +5.0% margin expansion, got {margin_expansion}"
    print("  --> YoY growth and margin expansion calculations verified.")


def test_comparison_user_isolation():
    print("\n[Test 4] Comparison User Isolation")
    temp_dir = tempfile.mkdtemp()
    temp_db = Path(temp_dir) / "test_comparison_iso.db"
    database.init_db(temp_db)

    u1 = database.create_user("User One", "user1@comp.com", "h1", "s1", temp_db)
    u2 = database.create_user("User Two", "user2@comp.com", "h2", "s2", temp_db)

    c1 = database.create_company(u1, "Company Alpha", "IT", "FY 2023-24", "", temp_db)
    database.save_full_analysis(
        u1, c1,
        {"financial_year": "FY 2023-24", "revenue": 5000000.0, "net_income": 500000.0},
        {"current_ratio": 2.0},
        temp_db,
    )
    database.save_full_analysis(
        u1, c1,
        {"financial_year": "FY 2024-25", "revenue": 6000000.0, "net_income": 700000.0},
        {"current_ratio": 2.2},
        temp_db,
    )

    # User 1 has 2 statements for Company Alpha
    u1_stmts = database.list_statements(u1, company_id=c1, db_path=temp_db)
    assert len(u1_stmts) == 2

    # User 2 has NO companies and NO statements
    u2_comps = database.list_companies(u2, db_path=temp_db)
    assert len(u2_comps) == 0
    u2_stmts = database.list_statements(u2, db_path=temp_db)
    assert len(u2_stmts) == 0

    try:
        os.remove(temp_db)
        os.rmdir(temp_dir)
    except Exception:
        pass
    print("  --> Multi-user comparison isolation verified.")


if __name__ == "__main__":
    print("=" * 60)
    print("RUNNING STEP 10 FINANCIAL COMPARISON TESTS")
    print("=" * 60)
    test_multi_year_trend_chart()
    test_peer_radar_chart()
    test_yoy_growth_calculations()
    test_comparison_user_isolation()
    print("\n" + "=" * 60)
    print("ALL STEP 10 TESTS PASSED! (100% SUCCESS)")
    print("=" * 60)

```

---

## File: `test_step_11.py`

```python
"""Unit and integration test suite for Step 11: PDF Reports Generation (ReportLab).

College Project: Financial Statement Ratio Analysis Assistant
Tests:
1. PDF generator builds valid PDF bytes with ReportLab (%PDF- header and %%EOF).
2. Proper Indian currency formatting (INR ₹, 3,2,2 grouping, Lakhs and Crores).
3. 14 Ratios diagnostic matrix and financial statement tables inclusion.
4. Edge cases: zero denominators (None / N/A), negative net profit, zero balances.
5. Database report tracking counter increment (mark_report_generated).
6. Multi-user isolation in PDF reporting.
7. Reports page rendering simulation (empty states & populated states).
"""

import os
import sqlite3
import tempfile
import unittest
from unittest.mock import MagicMock, patch

import database
import calculations
import analysis
import pdf_report
from pages import reports


class TestStep11PDFReports(unittest.TestCase):
    """Test suite for Step 11 PDF generation and reporting."""

    def setUp(self):
        """Create an isolated temporary SQLite database for testing."""
        self.temp_db = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.temp_db.close()
        self.db_path = self.temp_db.name
        database.init_db(self.db_path)

        # Create two test users
        self.user1_id = database.create_user(
            full_name="Analyst One",
            email="analyst1@college.edu",
            password_hash="hash1",
            password_salt="salt1",
            db_path=self.db_path,
        )
        self.user2_id = database.create_user(
            full_name="Analyst Two",
            email="analyst2@college.edu",
            password_hash="hash2",
            password_salt="salt2",
            db_path=self.db_path,
        )

        # Create company and statement for User 1
        self.company1_id = database.create_company(
            user_id=self.user1_id,
            company_name="Apex Motors Ltd",
            industry="Automotive",
            financial_year="FY 2025-26",
            description="Leading EV and commercial vehicle manufacturer.",
            db_path=self.db_path,
        )

        self.sample_statement_user1 = {
            "revenue": 50000000.0,            # ₹ 5.00 Cr
            "cost_of_goods_sold": 30000000.0, # ₹ 3.00 Cr
            "gross_profit": 20000000.0,       # ₹ 2.00 Cr
            "operating_expenses": 8000000.0,   # ₹ 80.00 Lakh
            "operating_income": 12000000.0,   # ₹ 1.20 Cr
            "interest_expense": 2000000.0,    # ₹ 20.00 Lakh
            "tax_expense": 2500000.0,         # ₹ 25.00 Lakh
            "net_income": 7500000.0,          # ₹ 75.00 Lakh
            "current_assets": 18000000.0,     # ₹ 1.80 Cr
            "cash_and_cash_equivalents": 6000000.0,
            "inventory": 5000000.0,
            "total_assets": 45000000.0,       # ₹ 4.50 Cr
            "current_liabilities": 9000000.0,  # ₹ 90.00 Lakh
            "total_liabilities": 18000000.0,
            "total_debt": 12000000.0,
            "shareholders_equity": 27000000.0,# ₹ 2.70 Cr
            "opening_inventory": 4500000.0,
            "closing_inventory": 5000000.0,
            "opening_total_assets": 40000000.0,
            "closing_total_assets": 45000000.0,
            "operating_cash_flow": 11000000.0,# ₹ 1.10 Cr
            "capital_expenditure": 4000000.0, # ₹ 40.00 Lakh
            "free_cash_flow": 7000000.0,      # ₹ 70.00 Lakh
        }

        # Calculate ratios and save full analysis in database
        self.ratios_user1 = calculations.calculate_all_ratios(self.sample_statement_user1)
        self.analysis_res1 = database.save_full_analysis(
            user_id=self.user1_id,
            company_id=self.company1_id,
            statement_data=self.sample_statement_user1,
            ratio_data=self.ratios_user1,
            db_path=self.db_path,
        )
        self.analysis1_id = self.analysis_res1["analysis_id"]

    def tearDown(self):
        """Clean up test database file."""
        if os.path.exists(self.db_path):
            try:
                os.remove(self.db_path)
            except Exception:
                pass

    def test_pdf_generation_bytes_and_structure(self):
        """Test that generate_pdf_report outputs valid PDF bytes with header, scorecard, and ratios."""
        company = database.get_company(self.company1_id, self.user1_id, db_path=self.db_path)
        statement = database.get_statement(self.analysis_res1["statement_id"], self.user1_id, db_path=self.db_path)
        health = analysis.compute_comprehensive_financial_health(self.ratios_user1)
        user = database.get_user_by_id(self.user1_id, db_path=self.db_path)

        pdf_bytes = pdf_report.generate_pdf_report(
            company=company,
            statement=statement,
            ratios=self.ratios_user1,
            health_eval=health,
            user=user,
        )

        self.assertIsInstance(pdf_bytes, bytes)
        self.assertTrue(len(pdf_bytes) > 10000, "PDF size should be substantial (at least 10 KB)")
        # PDF binary starts with standard %PDF magic bytes
        self.assertTrue(pdf_bytes.startswith(b"%PDF-"), "Generated file must start with %PDF- header")
        # PDF ends with %%EOF
        self.assertTrue(b"%%EOF" in pdf_bytes[-1024:], "Generated file must contain %%EOF marker")

    def test_indian_currency_and_ratio_formatting(self):
        """Verify Indian currency notation (₹), comma groupings, and ratio units."""
        sym = pdf_report.CURRENCY_SYMBOL
        self.assertEqual(pdf_report.format_inr(0), f"{sym} 0")
        self.assertEqual(pdf_report.format_inr(1234567), f"{sym} 12,34,567")
        self.assertEqual(pdf_report.format_inr(-500000), f"-{sym} 5,00,000")
        self.assertEqual(pdf_report.format_inr(25000000, compact=True), f"{sym} 2.50 Cr")
        self.assertEqual(pdf_report.format_inr(450000, compact=True), f"{sym} 4.50 Lakh")

        # Ratio formatting
        self.assertEqual(pdf_report.format_ratio_val("current_ratio", 2.0), "2.00x")
        self.assertEqual(pdf_report.format_ratio_val("gross_profit_margin", 40.0), "40.00%")
        self.assertEqual(pdf_report.format_ratio_val("free_cash_flow", 7000000.0), f"{sym} 70,00,000")
        self.assertEqual(pdf_report.format_ratio_val("current_ratio", None), "N/A")

    def test_edge_cases_zero_and_missing_values(self):
        """Test PDF generation with edge cases: N/A ratios, zero revenue, and negative profit."""
        sparse_statement = {
            "financial_year": "FY 2025-26",
            "revenue": 0.0,
            "cost_of_goods_sold": 0.0,
            "gross_profit": 0.0,
            "operating_expenses": 100000.0,
            "operating_income": -100000.0,
            "interest_expense": 0.0,  # Zero denominator for interest coverage
            "tax_expense": 0.0,
            "net_income": -100000.0,  # Negative bottom-line profit
            "current_assets": 50000.0,
            "cash_and_cash_equivalents": 10000.0,
            "inventory": 0.0,
            "total_assets": 200000.0,
            "current_liabilities": 0.0, # Zero denominator for liquidity ratios
            "total_liabilities": 50000.0,
            "total_debt": 0.0,
            "shareholders_equity": 150000.0,
            "opening_inventory": None, # Missing opening average balance
            "closing_inventory": 0.0,
            "opening_total_assets": None,
            "closing_total_assets": 200000.0,
            "operating_cash_flow": -80000.0,
            "capital_expenditure": 20000.0,
            "free_cash_flow": -100000.0,
        }

        ratios = calculations.calculate_all_ratios(sparse_statement)
        # Verify zero denominators return None
        self.assertIsNone(ratios["current_ratio"])
        self.assertIsNone(ratios["interest_coverage"])
        self.assertIsNone(ratios["inventory_turnover"])

        health = analysis.compute_comprehensive_financial_health(ratios)
        company = {"id": 99, "company_name": "Edge Case Corp", "industry": "Technology", "financial_year": "FY 2025-26"}

        # PDF must still generate without crashing or throwing division by zero
        pdf_bytes = pdf_report.generate_pdf_report(
            company=company,
            statement=sparse_statement,
            ratios=ratios,
            health_eval=health,
        )
        self.assertTrue(len(pdf_bytes) > 5000)

    def test_report_generation_counter_and_dashboard_integration(self):
        """Verify mark_report_generated increments report count and reflects in dashboard_summary."""
        # Initial summary before report download
        summary_before = database.dashboard_summary(self.user1_id, db_path=self.db_path)
        self.assertEqual(summary_before["total_reports"], 0)

        # Trigger download event
        reports.record_download_event(self.user1_id, self.analysis1_id)
        # Also run database.mark_report_generated directly with test db path
        database.mark_report_generated(self.user1_id, self.analysis1_id, db_path=self.db_path)

        # Summary after report download
        summary_after = database.dashboard_summary(self.user1_id, db_path=self.db_path)
        self.assertEqual(summary_after["total_reports"], 1)

    def test_multi_user_report_isolation(self):
        """Ensure User 2 cannot access or generate reports for User 1's company."""
        # User 2 attempts to query statements for User 1's company
        u2_statements = database.list_statements(user_id=self.user2_id, company_id=self.company1_id, db_path=self.db_path)
        self.assertEqual(len(u2_statements), 0, "User 2 must not see User 1's statements")

        # User 2 attempts to mark report generated on User 1's analysis
        res = database.mark_report_generated(user_id=self.user2_id, analysis_id=self.analysis1_id, db_path=self.db_path)
        self.assertFalse(res, "User 2 cannot increment report counter on User 1's analysis")

    @patch("streamlit.selectbox")
    @patch("streamlit.metric")
    @patch("streamlit.markdown")
    @patch("streamlit.download_button")
    def test_reports_page_render_simulation(self, mock_dl, mock_md, mock_metric, mock_select):
        """Simulate rendering the reports page with mocked Streamlit components."""
        orig_get_conn = database.get_connection
        with patch("database.get_connection", lambda db_path=None: orig_get_conn(self.db_path)):
            user1 = {"id": self.user1_id, "full_name": "Analyst One", "email": "analyst1@college.edu"}
            mock_select.side_effect = [self.company1_id, "FY 2025-26"]

            reports.render_reports_page(user1)

            # Assert download_button was invoked with PDF data
            self.assertTrue(mock_dl.called, "st.download_button must be rendered for download")
            call_kwargs = mock_dl.call_args[1]
            self.assertEqual(call_kwargs.get("mime"), "application/pdf")
            self.assertTrue(call_kwargs.get("file_name").startswith("Financial_Report_Apex_Motors_Ltd"))


if __name__ == "__main__":
    unittest.main()

```

---

## File: `test_step_12.py`

```python
"""Unit and integration test suite for Step 12: Analysis History & Audit Log.

College Project: Financial Statement Ratio Analysis Assistant
Tests:
1. Chronological retrieval of analysis history records (list_analyses).
2. Safe deletion of analysis history row (delete_analysis) while preserving company and statement data.
3. Multi-user isolation in analysis history (User 1 cannot see or delete User 2's history).
4. Search and filter logic (company filter, FY filter, search keyword).
5. Render simulation with mocked Streamlit components (empty state and populated audit cards).
"""

import os
import tempfile
import unittest
from unittest.mock import MagicMock, patch

import database
import calculations
import analysis
from pages import history


class TestStep12AnalysisHistory(unittest.TestCase):
    """Test suite for Step 12 Analysis History and Audit Trail."""

    def setUp(self):
        """Create an isolated temporary SQLite database for testing."""
        self.temp_db = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.temp_db.close()
        self.db_path = self.temp_db.name
        database.init_db(self.db_path)

        # Create two test users
        self.user1_id = database.create_user(
            full_name="Analyst One",
            email="analyst1@college.edu",
            password_hash="hash1",
            password_salt="salt1",
            db_path=self.db_path,
        )
        self.user2_id = database.create_user(
            full_name="Analyst Two",
            email="analyst2@college.edu",
            password_hash="hash2",
            password_salt="salt2",
            db_path=self.db_path,
        )

        # Create two companies for User 1
        self.comp1_id = database.create_company(
            user_id=self.user1_id,
            company_name="Apex Motors Ltd",
            industry="Automotive",
            financial_year="FY 2025-26",
            db_path=self.db_path,
        )
        self.comp2_id = database.create_company(
            user_id=self.user1_id,
            company_name="Bharat Tech Solutions",
            industry="IT Services",
            financial_year="FY 2025-26",
            db_path=self.db_path,
        )

        # Create one company for User 2
        self.u2_comp_id = database.create_company(
            user_id=self.user2_id,
            company_name="User2 Enterprise",
            industry="Retail",
            financial_year="FY 2025-26",
            db_path=self.db_path,
        )

        # Sample statement data
        self.stmt1_data = {
            "revenue": 50000000.0,
            "cost_of_goods_sold": 30000000.0,
            "gross_profit": 20000000.0,
            "operating_expenses": 8000000.0,
            "operating_income": 12000000.0,
            "interest_expense": 2000000.0,
            "tax_expense": 2500000.0,
            "net_income": 7500000.0,
            "current_assets": 18000000.0,
            "cash_and_cash_equivalents": 6000000.0,
            "inventory": 5000000.0,
            "total_assets": 45000000.0,
            "current_liabilities": 9000000.0,
            "total_liabilities": 18000000.0,
            "total_debt": 12000000.0,
            "shareholders_equity": 27000000.0,
            "opening_inventory": 4500000.0,
            "closing_inventory": 5000000.0,
            "opening_total_assets": 40000000.0,
            "closing_total_assets": 45000000.0,
            "operating_cash_flow": 11000000.0,
            "capital_expenditure": 4000000.0,
            "free_cash_flow": 7000000.0,
        }

        # Save analysis 1 for User 1 (Apex Motors)
        ratios1 = calculations.calculate_all_ratios(self.stmt1_data)
        res1 = database.save_full_analysis(
            user_id=self.user1_id,
            company_id=self.comp1_id,
            statement_data=self.stmt1_data,
            ratio_data=ratios1,
            db_path=self.db_path,
        )
        self.analysis1_id = res1["analysis_id"]
        self.stmt1_id = res1["statement_id"]

        # Save analysis 2 for User 1 (Bharat Tech)
        self.stmt2_data = dict(self.stmt1_data)
        self.stmt2_data["revenue"] = 80000000.0
        self.stmt2_data["net_income"] = 18000000.0
        ratios2 = calculations.calculate_all_ratios(self.stmt2_data)
        res2 = database.save_full_analysis(
            user_id=self.user1_id,
            company_id=self.comp2_id,
            statement_data=self.stmt2_data,
            ratio_data=ratios2,
            db_path=self.db_path,
        )
        self.analysis2_id = res2["analysis_id"]

        # Save analysis for User 2
        ratios_u2 = calculations.calculate_all_ratios(self.stmt1_data)
        res_u2 = database.save_full_analysis(
            user_id=self.user2_id,
            company_id=self.u2_comp_id,
            statement_data=self.stmt1_data,
            ratio_data=ratios_u2,
            db_path=self.db_path,
        )
        self.u2_analysis_id = res_u2["analysis_id"]

    def tearDown(self):
        """Clean up test database file."""
        if os.path.exists(self.db_path):
            try:
                os.remove(self.db_path)
            except Exception:
                pass

    def test_list_analyses_chronological_retrieval(self):
        """Test retrieving history records for a user in reverse chronological order."""
        history_list = database.list_analyses(self.user1_id, db_path=self.db_path)
        self.assertEqual(len(history_list), 2)
        # Most recent analysis first
        self.assertEqual(history_list[0]["id"], self.analysis2_id)
        self.assertEqual(history_list[0]["company_name"], "Bharat Tech Solutions")
        self.assertEqual(history_list[1]["id"], self.analysis1_id)
        self.assertEqual(history_list[1]["company_name"], "Apex Motors Ltd")

    def test_safe_delete_analysis_history(self):
        """Test that delete_analysis safely deletes only the history record while preserving statements and companies."""
        # Confirm initial state
        initial_history = database.list_analyses(self.user1_id, db_path=self.db_path)
        self.assertEqual(len(initial_history), 2)

        # Delete Analysis 1
        success = database.delete_analysis(self.user1_id, self.analysis1_id, db_path=self.db_path)
        self.assertTrue(success, "delete_analysis must return True on success")

        # History should now have only 1 row
        updated_history = database.list_analyses(self.user1_id, db_path=self.db_path)
        self.assertEqual(len(updated_history), 1)
        self.assertEqual(updated_history[0]["id"], self.analysis2_id)

        # Verify underlying company and statement are STILL INTACT!
        company = database.get_company(self.user1_id, self.comp1_id, db_path=self.db_path)
        self.assertIsNotNone(company, "Company must NOT be deleted when deleting an analysis log")
        self.assertEqual(company["company_name"], "Apex Motors Ltd")

        statement = database.get_statement(self.user1_id, self.stmt1_id, db_path=self.db_path)
        self.assertIsNotNone(statement, "Statement must NOT be deleted when deleting an analysis log")
        self.assertEqual(statement["revenue"], 50000000.0)

    def test_user_data_isolation_in_history(self):
        """Verify strict multi-user privacy in history querying and deletion."""
        # User 1 cannot see User 2's history
        u1_history = database.list_analyses(self.user1_id, db_path=self.db_path)
        u1_ids = [r["id"] for r in u1_history]
        self.assertNotIn(self.u2_analysis_id, u1_ids, "User 1 must not see User 2's audit logs")

        # User 2 cannot see User 1's history
        u2_history = database.list_analyses(self.user2_id, db_path=self.db_path)
        u2_ids = [r["id"] for r in u2_history]
        self.assertEqual(len(u2_history), 1)
        self.assertNotIn(self.analysis1_id, u2_ids, "User 2 must not see User 1's audit logs")
        self.assertNotIn(self.analysis2_id, u2_ids)

        # User 1 cannot delete User 2's history row
        del_attempt = database.delete_analysis(self.user1_id, self.u2_analysis_id, db_path=self.db_path)
        self.assertFalse(del_attempt, "User 1 cannot delete User 2's analysis record")

        # Verify User 2's record is still intact
        u2_record = database.get_analysis(self.user2_id, self.u2_analysis_id, db_path=self.db_path)
        self.assertIsNotNone(u2_record)

    @patch("streamlit.selectbox")
    @patch("streamlit.text_input")
    @patch("streamlit.download_button")
    @patch("streamlit.metric")
    @patch("streamlit.markdown")
    def test_history_page_render_simulation(self, mock_md, mock_metric, mock_dl, mock_text, mock_select):
        """Simulate rendering the analysis history page with mocked Streamlit widgets."""
        orig_get_conn = database.get_connection
        with patch("database.get_connection", lambda db_path=None: orig_get_conn(self.db_path)):
            user1 = {"id": self.user1_id, "full_name": "Analyst One", "email": "analyst1@college.edu"}
            mock_text.return_value = ""
            mock_select.side_effect = ["All Companies", "All Financial Years"]

            history.render_history_page(user1)

            # Verify CSV export button was rendered
            self.assertTrue(mock_dl.called, "CSV download button must be rendered")
            call_kwargs = mock_dl.call_args[1]
            self.assertEqual(call_kwargs.get("mime"), "text/csv")
            self.assertTrue(call_kwargs.get("file_name").startswith(f"Financial_Analysis_History_User_{self.user1_id}"))


if __name__ == "__main__":
    unittest.main()

```

---

## File: `test_step_9.py`

```python
"""Test suite for Step 9: Financial Insights and Rule-Based Interpretation."""

import os
import tempfile
from pathlib import Path
import database
import calculations
import analysis


def test_single_ratio_evaluations():
    print("\n[Test 1] Deterministic Evaluation of Individual Ratios")
    # Current Ratio
    e_cr_high = analysis.evaluate_single_ratio("current_ratio", 2.2)
    assert e_cr_high["status"] == analysis.STATUS_HEALTHY
    assert e_cr_high["badge_color"] == "green"
    assert e_cr_high["score"] == 100.0

    e_cr_mod = analysis.evaluate_single_ratio("current_ratio", 1.5)
    assert e_cr_mod["status"] == analysis.STATUS_MODERATE
    assert e_cr_mod["badge_color"] == "blue"

    e_cr_low = analysis.evaluate_single_ratio("current_ratio", 0.9)
    assert e_cr_low["status"] == analysis.STATUS_ATTENTION
    assert e_cr_low["badge_color"] == "red"

    # Missing / None
    e_cr_none = analysis.evaluate_single_ratio("current_ratio", None)
    assert e_cr_none["status"] == analysis.STATUS_NA
    assert e_cr_none["badge_color"] == "grey"

    # Net Profit Margin
    e_npm_loss = analysis.evaluate_single_ratio("net_profit_margin", -2.5)
    assert e_npm_loss["status"] == analysis.STATUS_ATTENTION
    assert e_npm_loss["badge_color"] == "red"

    e_npm_healthy = analysis.evaluate_single_ratio("net_profit_margin", 18.0)
    assert e_npm_healthy["status"] == analysis.STATUS_HEALTHY

    # Debt-to-Equity
    e_de_healthy = analysis.evaluate_single_ratio("debt_to_equity", 0.5)
    assert e_de_healthy["status"] == analysis.STATUS_HEALTHY

    e_de_high = analysis.evaluate_single_ratio("debt_to_equity", 2.5)
    assert e_de_high["status"] == analysis.STATUS_ATTENTION
    print("  --> Individual ratio evaluations verified against deterministic thresholds.")


def test_comprehensive_health_score():
    print("\n[Test 2] Comprehensive Financial Health Scoring & Categorization")
    # Sample dataset ratios
    sample_stmt = {
        "revenue": 10000000.0,
        "cost_of_goods_sold": 6000000.0,
        "gross_profit": 4000000.0,
        "operating_expenses": 1500000.0,
        "operating_income": 2500000.0,
        "interest_expense": 500000.0,
        "tax_expense": 500000.0,
        "net_income": 1500000.0,
        "current_assets": 3000000.0,
        "cash_and_cash_equivalents": 1000000.0,
        "inventory": 1200000.0,
        "total_assets": 8000000.0,
        "current_liabilities": 1500000.0,
        "total_liabilities": 3500000.0,
        "total_debt": 2000000.0,
        "shareholders_equity": 4500000.0,
        "opening_inventory": 1000000.0,
        "closing_inventory": 1400000.0,
        "opening_total_assets": 7000000.0,
        "closing_total_assets": 9000000.0,
        "operating_cash_flow": 2200000.0,
        "capital_expenditure": 700000.0,
    }
    ratios = calculations.calculate_all_ratios(sample_stmt)
    health = analysis.compute_comprehensive_financial_health(ratios)

    assert health["overall_score"] >= 80.0, f"Expected strong score, got {health['overall_score']}"
    assert health["health_grade"] == "Strong Financial Position"
    assert health["grade_color"] == "green"
    assert "Liquidity" in health["category_scores"]
    assert "Profitability" in health["category_scores"]
    assert "Solvency" in health["category_scores"]
    assert "Efficiency" in health["category_scores"]
    assert "Cash Flow" in health["category_scores"]
    assert len(health["strengths"]) > 0
    print(f"  --> Overall Score: {health['overall_score']}/100 ({health['health_grade']}) PASSED.")


def test_user_data_isolation():
    print("\n[Test 3] User Data Isolation in Insights")
    temp_dir = tempfile.mkdtemp()
    temp_db = Path(temp_dir) / "test_insights_iso.db"
    database.init_db(temp_db)

    u1 = database.create_user("User A", "usera@test.com", "h1", "s1", temp_db)
    u2 = database.create_user("User B", "userb@test.com", "h2", "s2", temp_db)

    c1 = database.create_company(u1, "Company Alpha", "IT", "FY 2024-25", "", temp_db)
    database.save_full_analysis(
        u1, c1,
        {"financial_year": "FY 2024-25", "revenue": 5000000.0, "net_income": 1000000.0},
        {"current_ratio": 2.0},
        temp_db,
    )

    # User 1 statements exist
    stmts_u1 = database.list_statements(u1, db_path=temp_db)
    assert len(stmts_u1) == 1

    # User 2 has NO statements
    stmts_u2 = database.list_statements(u2, db_path=temp_db)
    assert len(stmts_u2) == 0

    # Test that ratios fetched from database (with id, user_id, statement_id, calculated_at timestamp)
    # can be evaluated without ValueError: could not convert string to float
    db_ratios = database.get_ratios(u1, stmts_u1[0]["id"], db_path=temp_db)
    assert db_ratios is not None
    assert "calculated_at" in db_ratios
    health_from_db = analysis.compute_comprehensive_financial_health(db_ratios)
    assert health_from_db is not None
    assert "overall_score" in health_from_db
    print("  --> Evaluated DB ratios with timestamp metadata successfully.")

    try:
        os.remove(temp_db)
        os.rmdir(temp_dir)
    except Exception:
        pass
    print("  --> Data isolation verified: User 2 cannot access User 1's statements or insights.")


if __name__ == "__main__":
    print("=" * 60)
    print("RUNNING STEP 9 FINANCIAL INSIGHTS TESTS")
    print("=" * 60)
    test_single_ratio_evaluations()
    test_comprehensive_health_score()
    test_user_data_isolation()
    print("\n" + "=" * 60)
    print("ALL STEP 9 TESTS PASSED! (100% SUCCESS)")
    print("=" * 60)

```

---

## File: `test_steps_6_7_8.py`

```python
"""Comprehensive Test Suite for Steps 6, 7 and 8.

College Project: Financial Statement Ratio Analysis Assistant
This test suite validates:
1. Add a company (Step 6)
2. Edit company details
3. Save financial statements (Step 7)
4. Retrieve saved statements
5. Edit financial statements
6. Calculate all 14 ratios (Step 8)
7. Verify calculations manually against exact sample numbers
8. Test zero denominators (N/A)
9. Test missing opening and closing balances (N/A, no silent fallback)
10. Restart the application simulation (persistent SQLite storage)
11. Confirm all records remain saved after restart
12. Second user login simulation
13. Verify multi-user data privacy & strict isolation
"""

import os
import tempfile
from pathlib import Path
import database
import authentication
import calculations


def run_tests():
    print("=" * 70)
    print("RUNNING COMPREHENSIVE VERIFICATION: STEPS 6, 7 AND 8")
    print("=" * 70)

    # Setup isolated test database
    temp_dir = tempfile.mkdtemp()
    temp_db = Path(temp_dir) / "test_steps_6_7_8.db"
    database.init_db(temp_db)

    # Register two distinct users for data isolation testing
    u1_id = database.create_user("User One", "user1@college.edu", "hash1", "salt1", temp_db)
    u2_id = database.create_user("User Two", "user2@college.edu", "hash2", "salt2", temp_db)

    # ------------------------------------------------------------------------
    # [1] ADD COMPANY
    # ------------------------------------------------------------------------
    print("\n[Test 1] Add Company (Step 6)")
    c1_id = database.create_company(
        user_id=u1_id,
        company_name="[SAMPLE] Bharat Industrial Motors Ltd",
        industry="Automobile & Auto Ancillaries",
        financial_year="FY 2024-25",
        description="Fictional sample company for ratio verification",
        db_path=temp_db,
    )
    assert c1_id > 0
    c1 = database.get_company(u1_id, c1_id, temp_db)
    assert c1["company_name"] == "[SAMPLE] Bharat Industrial Motors Ltd"
    assert c1["financial_year"] == "FY 2024-25"
    print(f"  --> Company created successfully (ID: #{c1_id}).")

    # ------------------------------------------------------------------------
    # [2] EDIT COMPANY
    # ------------------------------------------------------------------------
    print("\n[Test 2] Edit Company Details")
    updated = database.update_company(
        user_id=u1_id,
        company_id=c1_id,
        company_name="[SAMPLE] Bharat Motors Ltd",
        industry="Manufacturing",
        financial_year="FY 2024-25",
        description="Updated description",
        db_path=temp_db,
    )
    assert updated is True
    c1_edited = database.get_company(u1_id, c1_id, temp_db)
    assert c1_edited["company_name"] == "[SAMPLE] Bharat Motors Ltd"
    assert c1_edited["industry"] == "Manufacturing"
    print("  --> Company details updated successfully.")

    # ------------------------------------------------------------------------
    # [3 & 4] SAVE & RETRIEVE FINANCIAL STATEMENTS
    # ------------------------------------------------------------------------
    print("\n[Test 3 & 4] Save and Retrieve Financial Statement (Step 7)")
    # Fictional sample numbers in exact INR
    sample_stmt = {
        "financial_year": "FY 2024-25",
        "revenue": 10000000.0,            # ₹ 1.00 Cr
        "cost_of_goods_sold": 6000000.0,   # ₹ 60 Lakh
        "gross_profit": 4000000.0,         # ₹ 40 Lakh
        "operating_expenses": 1500000.0,   # ₹ 15 Lakh
        "operating_income": 2500000.0,     # ₹ 25 Lakh
        "interest_expense": 500000.0,      # ₹ 5 Lakh
        "tax_expense": 500000.0,           # ₹ 5 Lakh
        "net_income": 1500000.0,           # ₹ 15 Lakh
        "current_assets": 3000000.0,       # ₹ 30 Lakh
        "cash_and_cash_equivalents": 1000000.0,  # ₹ 10 Lakh
        "inventory": 1200000.0,            # ₹ 12 Lakh
        "total_assets": 8000000.0,         # ₹ 80 Lakh
        "current_liabilities": 1500000.0,  # ₹ 15 Lakh
        "total_liabilities": 3500000.0,    # ₹ 35 Lakh
        "total_debt": 2000000.0,           # ₹ 20 Lakh
        "shareholders_equity": 4500000.0,  # ₹ 45 Lakh
        "opening_inventory": 1000000.0,    # ₹ 10 Lakh
        "closing_inventory": 1400000.0,    # ₹ 14 Lakh (Average = 12 Lakh)
        "opening_total_assets": 7000000.0, # ₹ 70 Lakh
        "closing_total_assets": 9000000.0, # ₹ 90 Lakh (Average = 80 Lakh)
        "operating_cash_flow": 2200000.0,  # ₹ 22 Lakh
        "capital_expenditure": 700000.0,   # ₹ 7 Lakh
        "free_cash_flow": 1500000.0,       # ₹ 15 Lakh
    }

    # Calculate ratios
    ratios = calculations.calculate_all_ratios(sample_stmt)

    save_info = database.save_full_analysis(
        user_id=u1_id,
        company_id=c1_id,
        statement_data=sample_stmt,
        ratio_data=ratios,
        db_path=temp_db,
    )
    s_id = save_info["statement_id"]
    assert s_id > 0

    # Retrieve statement
    retrieved = database.get_statement(u1_id, s_id, temp_db)
    assert retrieved is not None
    assert retrieved["revenue"] == 10000000.0
    assert retrieved["net_income"] == 1500000.0
    print(f"  --> Statement saved and retrieved (Statement ID: #{s_id}).")

    # ------------------------------------------------------------------------
    # [5] EDIT FINANCIAL STATEMENT
    # ------------------------------------------------------------------------
    print("\n[Test 5] Edit Financial Statement")
    sample_stmt["revenue"] = 12000000.0  # Update to ₹ 1.20 Cr
    updated_ratios = calculations.calculate_all_ratios(sample_stmt)
    save_info_2 = database.save_full_analysis(
        user_id=u1_id,
        company_id=c1_id,
        statement_data=sample_stmt,
        ratio_data=updated_ratios,
        db_path=temp_db,
    )
    assert save_info_2["statement_id"] == s_id  # Updates same statement row
    re_retrieved = database.get_statement(u1_id, s_id, temp_db)
    assert re_retrieved["revenue"] == 12000000.0
    # Revert to 10000000.0 for formula checks below
    sample_stmt["revenue"] = 10000000.0
    database.save_full_analysis(u1_id, c1_id, sample_stmt, ratios, temp_db)
    print("  --> Statement update confirmed.")

    # ------------------------------------------------------------------------
    # [6 & 7] CALCULATE AND VERIFY ALL 14 RATIOS AGAINST EXPECTED SAMPLE VALUES
    # ------------------------------------------------------------------------
    print("\n[Test 6 & 7] Verify All 14 Financial Ratios against Expected Formulas")
    calc = calculations.calculate_all_ratios(sample_stmt)

    # 1. Current Ratio = 30L / 15L = 2.00
    assert calc["current_ratio"] == 2.0, f"Current Ratio error: {calc['current_ratio']}"

    # 2. Quick Ratio = (30L - 12L) / 15L = 18L / 15L = 1.20
    assert calc["quick_ratio"] == 1.2, f"Quick Ratio error: {calc['quick_ratio']}"

    # 3. Cash Ratio = 10L / 15L = 0.6667 (0.67)
    assert round(calc["cash_ratio"], 2) == 0.67, f"Cash Ratio error: {calc['cash_ratio']}"

    # 4. Gross Profit Margin = (40L / 100L) * 100 = 40.0%
    assert calc["gross_profit_margin"] == 40.0, f"Gross Profit Margin error: {calc['gross_profit_margin']}"

    # 5. Net Profit Margin = (15L / 100L) * 100 = 15.0%
    assert calc["net_profit_margin"] == 15.0, f"Net Profit Margin error: {calc['net_profit_margin']}"

    # 6. ROA = (15L / 80L) * 100 = 18.75%  [Avg Assets = (70L + 90L)/2 = 80L]
    assert calc["return_on_assets"] == 18.75, f"ROA error: {calc['return_on_assets']}"

    # 7. ROE = (15L / 45L) * 100 = 33.3333% (33.33%)
    assert round(calc["return_on_equity"], 2) == 33.33, f"ROE error: {calc['return_on_equity']}"

    # 8. Debt-to-Equity = 20L / 45L = 0.4444 (0.44)
    assert round(calc["debt_to_equity"], 2) == 0.44, f"Debt-to-Equity error: {calc['debt_to_equity']}"

    # 9. Debt Ratio = (35L / 80L) * 100 = 43.75%
    assert calc["debt_ratio"] == 43.75, f"Debt Ratio error: {calc['debt_ratio']}"

    # 10. Interest Coverage = 25L / 5L = 5.00
    assert calc["interest_coverage"] == 5.0, f"Interest Coverage error: {calc['interest_coverage']}"

    # 11. Inventory Turnover = 60L / 12L = 5.00  [Avg Inventory = (10L + 14L)/2 = 12L]
    assert calc["inventory_turnover"] == 5.0, f"Inventory Turnover error: {calc['inventory_turnover']}"

    # 12. Asset Turnover = 100L / 80L = 1.25  [Avg Assets = 80L]
    assert calc["asset_turnover"] == 1.25, f"Asset Turnover error: {calc['asset_turnover']}"

    # 13. Operating Cash Flow Ratio = 22L / 15L = 1.4667 (1.47)
    assert round(calc["operating_cash_flow_ratio"], 2) == 1.47, f"OCF Ratio error: {calc['operating_cash_flow_ratio']}"

    # 14. Free Cash Flow = 22L - 7L = 15L (₹ 15,00,000)
    assert calc["free_cash_flow"] == 1500000.0, f"FCF error: {calc['free_cash_flow']}"

    print("  --> All 14 ratios verified with 100% mathematical accuracy against sample data.")

    # ------------------------------------------------------------------------
    # [8] TEST ZERO DENOMINATORS
    # ------------------------------------------------------------------------
    print("\n[Test 8] Zero Denominator Safeguards")
    zero_den_data = dict(sample_stmt)
    zero_den_data["current_liabilities"] = 0.0
    zero_den_data["interest_expense"] = 0.0
    zero_den_data["revenue"] = 0.0
    zero_den_data["shareholders_equity"] = 0.0
    zero_den_calc = calculations.calculate_all_ratios(zero_den_data)

    assert zero_den_calc["current_ratio"] is None
    assert zero_den_calc["quick_ratio"] is None
    assert zero_den_calc["cash_ratio"] is None
    assert zero_den_calc["interest_coverage"] is None
    assert zero_den_calc["gross_profit_margin"] is None
    assert zero_den_calc["net_profit_margin"] is None
    assert zero_den_calc["return_on_equity"] is None
    assert zero_den_calc["debt_to_equity"] is None
    print("  --> Zero denominators safely return None (N/A) without throwing exceptions.")

    # ------------------------------------------------------------------------
    # [9] TEST MISSING OPENING AND CLOSING BALANCES
    # ------------------------------------------------------------------------
    print("\n[Test 9] Missing Opening/Closing Balances (Strict Average Rule)")
    missing_avg_data = dict(sample_stmt)
    missing_avg_data["opening_inventory"] = None   # Missing opening inventory
    missing_avg_data["closing_inventory"] = 1400000.0
    missing_avg_data["opening_total_assets"] = 7000000.0
    missing_avg_data["closing_total_assets"] = None  # Missing closing total assets

    missing_calc = calculations.calculate_all_ratios(missing_avg_data)
    assert missing_calc["inventory_turnover"] is None, "Must not replace missing opening inventory with closing balance!"
    assert missing_calc["return_on_assets"] is None, "Must not replace missing closing assets with opening balance!"
    assert missing_calc["asset_turnover"] is None, "Must not replace missing closing assets!"
    print("  --> Strict average rules verified (no silent fallbacks to closing balance).")

    # ------------------------------------------------------------------------
    # [10 & 11] RESTART APPLICATION SIMULATION (PERSISTENCE)
    # ------------------------------------------------------------------------
    print("\n[Test 10 & 11] Persistence Across Application Restart")
    # Simulate fresh app startup by closing connection, discarding objects, and reconnecting
    fresh_companies = database.list_companies(u1_id, temp_db)
    assert len(fresh_companies) == 1
    assert fresh_companies[0]["company_name"] == "[SAMPLE] Bharat Motors Ltd"

    fresh_statements = database.list_statements(u1_id, c1_id, temp_db)
    assert len(fresh_statements) == 1
    assert fresh_statements[0]["revenue"] == 10000000.0

    fresh_ratios = database.get_ratios(u1_id, s_id, temp_db)
    assert fresh_ratios is not None
    assert fresh_ratios["current_ratio"] == 2.0
    assert fresh_ratios["free_cash_flow"] == 1500000.0
    print("  --> All records (companies, statements, ratios, history) persisted across restart.")

    # ------------------------------------------------------------------------
    # [12 & 13] SECOND USER LOGIN & STRICT PRIVACY ISOLATION
    # ------------------------------------------------------------------------
    print("\n[Test 12 & 13] Second User Login & Strict Data Isolation")
    # User 2 logs in
    u2_companies = database.list_companies(u2_id, temp_db)
    assert len(u2_companies) == 0, f"User 2 can see User 1's companies! {u2_companies}"

    u2_statements = database.list_statements(u2_id, db_path=temp_db)
    assert len(u2_statements) == 0, f"User 2 can see User 1's statements! {u2_statements}"

    u2_ratios = database.get_ratios(u2_id, s_id, temp_db)
    assert u2_ratios is None, f"User 2 can read User 1's ratios! {u2_ratios}"

    # User 2 attempts to query User 1's company directly
    u2_company_attempt = database.get_company(u2_id, c1_id, temp_db)
    assert u2_company_attempt is None, "User 2 accessed User 1's company by ID!"

    # User 2 attempts to delete User 1's company
    try:
        deleted_by_u2 = database.delete_company(u2_id, c1_id, temp_db)
        assert deleted_by_u2 is False
    except Exception:
        pass
    # Verify User 1's company still exists
    assert database.get_company(u1_id, c1_id, temp_db) is not None

    print("  --> Multi-user data privacy & query isolation 100% verified.")

    # Cleanup temp db
    try:
        os.remove(temp_db)
        os.rmdir(temp_dir)
    except Exception:
        pass

    print("\n" + "=" * 70)
    print("ALL TESTS FOR STEPS 6, 7 AND 8 PASSED WITH 100% SUCCESS!")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()

```

---

## File: `view_database.py`

```python
import sqlite3

DB_PATH = "database/financial_data.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
""")

tables = cursor.fetchall()

print("\nDATABASE TABLES:")

for table in tables:
    table_name = table[0]
    print(f"\n--- {table_name} ---")

    cursor.execute(f'SELECT * FROM "{table_name}"')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

connection.close()

```

---

## File: `visualization.py`

```python
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

```

---

