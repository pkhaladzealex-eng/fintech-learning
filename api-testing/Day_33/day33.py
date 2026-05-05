import stripe
import sqlite3
import os

def run_task():
    try:
        stripe.api_key = os.environ.get("STRIPE_API_KEY")
        
        # Fetching charges via Stripe API
        charge1 = stripe.Charge.retrieve("ch_3TTlJHJP62O0ob1e0R3E4KTz")
        charge2 = stripe.Charge.retrieve("ch_3TTlJeJP62O0ob1e2YztVXyQ")

        charges_to_insert = [charge1, charge2]

        # Connecting to database
        conn = sqlite3.connect('/Users/alexpkhaladze/desktop/fintech-learning/global_data/fintech_main.db')
        cursor = conn.cursor()

        formated_data = []
        for row in charges_to_insert:
            formated_data.append((row.id, row.amount / 100, row.status))

        # Inserting data
        cursor.executemany("INSERT INTO charges (charge_id, amount, status) VALUES (?,?,?)", formated_data)
        conn.commit()

        # Querying database
        cursor.execute("SELECT * FROM charges")
        rows = cursor.fetchall()

        print("--- DATABASE CONTENT ---")
        for row in rows:
            print(f"id: {row[0]}, amount: {row[1]}, status: {row[2]}")

        # Calculating Sum and Average
        cursor.execute("SELECT SUM(amount) FROM charges")
        total_sum = cursor.fetchone()[0]
        cursor.execute("SELECT AVG(amount) FROM charges")
        avg_amount = cursor.fetchone()[0]

        print(f"--- TOTAL AMOUNT: {total_sum} ---")
        print(f"--- AVERAGE AMOUNT: {avg_amount} ---")
        
    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    run_task()
