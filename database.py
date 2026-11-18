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
