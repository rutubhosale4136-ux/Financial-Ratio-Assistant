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
