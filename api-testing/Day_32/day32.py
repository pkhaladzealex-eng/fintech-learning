import sqlite3


def run_task():
    try:
        # 1. Create/Connect to database file
        conn = sqlite3.connect('/Users/alexpkhaladze/Desktop/fintech-learning/global_data/fintech_main.db')
        cursor = conn.cursor()



        # 3. Insert fresh data
        cursor.execute("DELETE FROM charges") # Clear old data
        data = [
            ('ch_3TSjofJP62O0ob1e1eaWGA20', 10.00, 'Succeeded'),
            ('ch_3TSG3VJP62O0ob1e0jRUmmVP', 25.00, 'failed'),
            ('ch_3TSFzTJP62O0ob1e05zgZnMx', 35.00, 'succeeded')
        ]
        cursor.executemany("INSERT INTO charges (charge_id, amount, status) VALUES (?, ?, ?)", data)
        conn.commit()

        # 4. Query and Print
        cursor.execute("SELECT * FROM charges")
        rows = cursor.fetchall()

        print("--- DATABASE CONTENT ---")
        total = 0
        for row in rows:
            print(f"ID: {row[0]} | Amount: {row[1]} | Status: {row[2]} | Date: {row[3]}")
            total += row[1]

        print("-" * 30)
        print(f"TOTAL CALCULATED: {total} USD")

    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    run_task()