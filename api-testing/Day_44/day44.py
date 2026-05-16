import os
import stripe
import sqlite3

# 1. Stripe Configuration
stripe.api_key = os.environ.get('STRIPE_API_KEY')

# 2. Database Connection
db_path = '/Users/alexpkhaladze/desktop/fintech-learning/global_data/fintech_main.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


def create_two_charges():
    print("Processing 2 Automated Charges for Customer")


    cursor.execute("SELECT stripe_customer_id, name FROM customers ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()

    if not row:
        print("Error: No customers found in database.")
        return

    target_id = row[0]
    customer_name = row[1]
    print(f"Selected Customer: {customer_name} ({target_id})")


    amounts_to_charge = [1500, 2000]

    for amount in amounts_to_charge:
        try:
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency="usd",
                customer=target_id,
                payment_method="pm_card_visa",
                confirm=True,
                off_session=True,
                description="Day 44 Multi-Charge Test"
            )

            charge_id = intent.latest_charge


            cursor.execute("""
                INSERT INTO charges (charge_id, amount_cents, status, customer_id)
                VALUES (?, ?, ?, ?)
            """, (charge_id, amount, intent.status, target_id))

            print(f"Success! Charge {charge_id} created (${amount / 100:.2f})")

        except Exception as e:
            print(f"Stripe Error: {e}")

    conn.commit()


def show_customer_total_spent():
    print("\nCustomer Report & Total Spent (SQL Aggregation)")


    cursor.execute("SELECT stripe_customer_id, name, email FROM customers ORDER BY id DESC LIMIT 1")
    cust = cursor.fetchone()
    target_id = cust[0]
    name = cust[1]
    email = cust[2]


    query = """
        SELECT COUNT(ch.charge_id), SUM(ch.amount_cents)
        FROM charges ch
        WHERE ch.customer_id = ?
    """
    cursor.execute(query, (target_id,))
    result = cursor.fetchone()

    total_charges = result[0]

    total_cents = result[1] if result[1] is not None else 0

    print(f"Customer Name: {name}")
    print(f"Email:         {email}")
    print(f"Stripe ID:     {target_id}")
    print("-" * 50)
    print(f"Total Charges: {total_charges} transaction(s)")
    print(f"Total Spent:   ${total_cents / 100:.2f}")


if __name__ == "__main__":
    create_two_charges()
    show_customer_total_spent()
    conn.close()