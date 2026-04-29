import sqlite3
import os


def process_database_payments():
    # Path to  main database
    db_path = '../../global_data/fintech_main.db'

    if not os.path.exists(db_path):
        print(f"Error: Database not found at {db_path}")
        return

    try:
        # Establish connection
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        # Query records
        query = "SELECT stripe_charge_id, amount, status FROM payments"
        cursor.execute(query)
        rows = cursor.fetchall()

        print("--- Database Query Results ---")
        total_paid = 0.0

        for row in rows:
            charge_id = row[0]
            amount = row[1]
            status = row[2]

            print(f"ID: {charge_id} | Amount: {amount} | Status: {status}")

            # Aggregate total amount
            total_paid += amount

        print("------------------------------")
        print(f"Total Portfolio Value: {total_paid}")

        connection.close()

    except sqlite3.Error as e:
        print(f"Database error: {e}")


if __name__ == "__main__":
    process_database_payments()