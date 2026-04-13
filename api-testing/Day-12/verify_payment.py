import sqlite3

def run_task():
    try:
        # 1. Create/Connect to database file
        conn = sqlite3.connect('payments.db')
        cursor = conn.cursor()

        # 2. Create the table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS test_transactions (
                id INTEGER PRIMARY KEY,
                user_id TEXT,
                amount REAL,
                status TEXT
            )
        ''')

        # 3. Insert fresh data
        cursor.execute("DELETE FROM test_transactions") # Clear old data
        data = [
            (1, 'tester_01', 250.0, 'Success'),
            (2, 'tester_02', 100.0, 'Success'),
            (3, 'tester_01', 50.0, 'Success')
        ]
        cursor.executemany("INSERT INTO test_transactions VALUES (?,?,?,?)", data)
        conn.commit()

        # 4. Query and Print
        cursor.execute("SELECT * FROM test_transactions")
        rows = cursor.fetchall()

        print("--- DATABASE CONTENT ---")
        total = 0
        for row in rows:
            print(f"ID: {row[0]} | User: {row[1]} | Amount: {row[2]} USD | Status: {row[3]}")
            total += row[2]

        print("-" * 30)
        print(f"TOTAL CALCULATED: {total} USD")

    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    run_task()