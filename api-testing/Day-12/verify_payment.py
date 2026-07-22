import sqlite3

def run_task():
    try:
        # 1. Connect to the SQL database file( creates 'payments.db' if it doesn't exist)
        conn = sqlite3.connect('payments.db')
        cursor = conn.cursor() # Cursor allows us to execute SQL commands

        # 2. Create the 'test_transactions' table if it is not already created
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS test_transactions (
                id INTEGER PRIMARY KEY,
                user_id TEXT,
                amount REAL,
                status TEXT
            )
        ''')

        # 3. Clear any existing records from previous runs to keep test data fresh
        cursor.execute("DELETE FROM test_transactions")
        # Prepare mock transaction data to insert into the table
        data = [
            (1, 'tester_01', 250.0, 'Success'),
            (2, 'tester_02', 100.0, 'Success'),
            (3, 'tester_01', 50.0, 'Success')
        ]
        # Insert multiple rows into the database at once using executemany
        cursor.executemany("INSERT INTO test_transactions VALUES (?,?,?,?)", data)
        # Save (commit)  the changes into the database file
        conn.commit()

        # 4. Fetch all rows from the table to process and print them
        cursor.execute("SELECT * FROM test_transactions")
        rows = cursor.fetchall()

        print("--- DATABASE CONTENT ---")
        total = 0
        for row in rows:
            # sqlite3 fetchall() returns eah record as  a tuple, so we access columns by index
            print(f"ID: {row[0]} | User: {row[1]} | Amount: {row[2]} USD | Status: {row[3]}")
            total += row[2]

        print("-" * 30)
        print(f"TOTAL CALCULATED: {total} USD")

    except sqlite3.Error as e:
        # Catch and print any SQLite specific database errors
        print(f"Error: {e}")
    finally:
        # Ensure the database connection is always  closed properly
        if conn:
            conn.close()

if __name__ == "__main__":
    run_task()