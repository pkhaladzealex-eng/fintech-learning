
import sqlite3
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def run_transaction_test(force_error=False):
    conn = None
    try:
        conn = sqlite3.connect(config.DATABASE_PATH)
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM charges")
        initial_count = cursor.fetchone()[0]
        print(f"Initial record count in database: {initial_count}")

        conn.execute("BEGIN TRANSACTION")
        print("\nDatabase transaction started (BEGIN TRANSACTION)...")

       
        cursor.execute("DELETE FROM charges")


        mock_data = [
            ('ch_57_test_1', 9900, 'succeeded'),
            ('ch_57_test_2', 15000, 'failed'),
        ]


        cursor.executemany("INSERT INTO charges (charge_id, amount_cents, status) VALUES (?, ?, ?)", mock_data)
        print("Fresh records successfully staged in-memory...")

        if force_error:
            print("Injecting intentional runtime failure (Force Error)...")

            cursor.execute("SELECT * FROM non_existent_table")

        conn.commit()
        print("Transaction successfully committed (COMMIT)!")

    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        print(f"Transaction collapsed! Error details: {e}")
        print("ROLLBACK executed: All mutations discarded. Database restored to baseline state!")

    finally:
        if conn:
            cursor.execute("SELECT COUNT(*) FROM charges")
            final_count = cursor.fetchone()[0]
            print(f"Final record count in database: {final_count}\n")
            conn.close()

if __name__ == "__main__":
    print("--- Test Case 1: Successful Transaction Pipeline (No Errors) ---")
    run_transaction_test(force_error=False)

    print("--- Test Case 2: Fault-Injected Transaction Pipeline (Rollback Verification) ---")
    run_transaction_test(force_error=True)
