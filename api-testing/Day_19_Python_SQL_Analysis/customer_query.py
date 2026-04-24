import sqlite3
import os

# Define the path to the database (it sits in payment-setup folder)
db_path = "../../payment-setup/Day-18-sql/fintech_qa.db"


def run_customer_analysis():
    # Connect to the SQLite database
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        print("--- Fintech QA: Customer Payment Analysis ---")

        # 1. Querying 'name' and 'payment_method' (NOT card_type)
        cursor.execute("SELECT name, payment_method FROM customers")
        customers = cursor.fetchall()

        # 2. Iterate through results and print details
        for row in customers:
            print(f"Customer: {row[0]} | Payment Method: {row[1]}")

        # 3. Use SQL aggregate function to count total records
        cursor.execute("SELECT COUNT(*) FROM customers")
        total_count = cursor.fetchone()[0]

        print("-" * 45)
        print(f"Total verified customers in DB: {total_count}")

    except sqlite3.Error as e:
        # Catch and display any SQL-related errors
        print(f"Database error: {e}")
    finally:
        # Securely close the connection
        if conn:
            conn.close()


if __name__ == "__main__":
    run_customer_analysis()
