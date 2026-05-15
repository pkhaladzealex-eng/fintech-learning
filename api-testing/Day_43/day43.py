import os
import stripe
import sqlite3


stripe.api_key = os.environ.get('STRIPE_API_KEY')


db_path = '/Users/alexpkhaladze/desktop/fintech-learning/global_data/fintech_main.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


def create_linked_charge():
    print("---  Creating Simple Linked PaymentIntent ---")


    cursor.execute("SELECT stripe_customer_id FROM customers ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()

    if not row:
        print(" Error: No customers found in database. Run day42.py first.")
        return

    target_customer_id = row[0]
    print(f"Targeting Customer ID from Database: {target_customer_id}")

    try:

        intent = stripe.PaymentIntent.create(
            amount=4300,
            currency="usd",
            customer=target_customer_id,
            payment_method="pm_card_visa",
            confirm=True,
            off_session=True
        )

        charge_id = intent.latest_charge


        cursor.execute("""
            INSERT INTO charges (charge_id, amount_cents, status, customer_id)
            VALUES (?, ?, ?, ?)
        """, (charge_id, intent.amount, intent.status, target_customer_id))

        conn.commit()
        print(f"✅ Success! Created charge {charge_id}")

    except Exception as e:
        print(f" Stripe Error: {e}")


def query_customer_charges():
    print("\n---  Customer Details & Linked Charges (SQL JOIN) ---")


    query = """
        SELECT c.id, c.name, c.email, ch.charge_id, ch.amount_cents, ch.status
        FROM customers c
        INNER JOIN charges ch ON c.stripe_customer_id = ch.customer_id
        ORDER BY ch.ROWID DESC LIMIT 5
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    print(f"{'ID':<3} | {'Name':<15} | {'Email':<20} | {'Charge ID':<24} | {'Amount':<8} | {'Status'}")
    print("-" * 90)
    for row in rows:
        amount_usd = f"${row[4] / 100:.2f}"
        print(f"{row[0]:<3} | {row[1]:<15} | {row[2]:<20} | {row[3]:<24} | {amount_usd:<8} | {row[5]}")


if __name__ == "__main__":
    create_linked_charge()
    query_customer_charges()
    conn.close()