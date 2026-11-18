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
