import os
import stripe
import sqlite3

# 1. Stripe Configuration
stripe.api_key = os.environ.get('STRIPE_API_KEY')

if not stripe.api_key:
    raise ValueError("STRIPE_API_KEY environment variable is not set!")

# 2. Database Connection
db_path = '/Users/alexpkhaladze/desktop/fintech-learning/global_data/fintech_main.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


def fetch_and_store_charges():
    print("--- Fetching Data from Stripe API ---")

    # Retrieve the last 5 charges
    charges = stripe.Charge.list(limit=5)

    for c in charges.data:
        charge_id = c.id
        amount = c.amount
        status = c.status

        # Matches your schema: charge_id, amount_cents, status
        cursor.execute("""
            INSERT OR IGNORE INTO charges (charge_id, amount_cents, status)
            VALUES (?, ?, ?)
        """, (charge_id, amount, status))

    conn.commit()
    print(f"Successfully processed and stored {len(charges.data)} charges.")


def calculate_statistics():
    print("\n--- Financial Statistics (Last 5 Charges) ---")

    cursor.execute("""
        SELECT amount_cents FROM charges 
        ORDER BY ROWID DESC LIMIT 5
    """)
    amounts = [row[0] for row in cursor.fetchall()]

    if not amounts:
        print("Error: No data found in database!")
        return

    total_revenue = sum(amounts)
    avg_charge = total_revenue / len(amounts)
    max_charge = max(amounts)
    min_charge = min(amounts)

    print(f"Total Revenue:       ${total_revenue / 100:.2f}")
    print(f"Average Charge:      ${avg_charge / 100:.2f}")
    print(f"Highest Charge:      ${max_charge / 100:.2f}")
    print(f"Lowest Charge:       ${min_charge / 100:.2f}")


if __name__ == "__main__":
    try:
        fetch_and_store_charges()
        calculate_statistics()
    except Exception as e:
        print(f"Execution Error: {e}")
    finally:
        conn.close()