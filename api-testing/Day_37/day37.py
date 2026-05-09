import os
import stripe
import sqlite3

from charset_normalizer import api

try:
    stripe.api_key = os.environ.get('STRIPE_API_KEY')

    charge_to_fetch = "pi_3TUX2FJP62O0ob1e1vyKvdOz"
    refund_to_fetch = "re_3TUX2FJP62O0ob1e1BEnijMc"

    payment_intent = stripe.PaymentIntent.retrieve(charge_to_fetch)
    charge_obj = stripe.Charge.retrieve(payment_intent.latest_charge)
    refund_obj= stripe.Refund.retrieve(refund_to_fetch)

    print(f'Fetched Charge: {charge_obj.id} - {charge_obj.amount} ')
    print(f'Fetched Refund: {refund_obj.id} -{refund_obj.amount}')

    conn = sqlite3.connect("/Users/alexpkhaladze/Desktop/fintech-learning/global_data/fintech_main.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS charges (
    charge_id  TEXT PRIMARY KEY,
    amount_cents INTEGER,
    status TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP)
    """)
    conn.commit()

    cursor.execute("""CREATE TABLE IF NOT EXISTS refunds (
    refund_id  TEXT PRIMARY KEY,
    charge_id TEXT,
    amount INTEGER NOT NULL,
    status TEXT)
     """)
    conn.commit()

    cursor.execute("INSERT OR IGNORE INTO charges (charge_id, amount_cents, status) VALUES (?, ?, ?)",(charge_obj.id, charge_obj.amount, charge_obj.status))
    conn.commit()
    cursor.execute("INSERT OR IGNORE INTO refunds (refund_id, charge_id, amount, status) VALUES (?, ?, ?, ?)",(refund_obj.id, refund_obj.charge, refund_obj.amount, refund_obj.status))
    conn.commit()


    query = """
    SELECT c.amount_cents, r.amount 
    FROM charges c
    JOIN refunds r ON c.charge_id = r.charge_id
    WHERE c.charge_id = ?
    """

    cursor.execute(query, (charge_obj.id,))
    result = cursor.fetchone()

    if result:
        charge_amt = result[0]
        refund_amt = result[1]
        net_amt = (charge_amt - refund_amt) / 100

        print("--- Financial Report ---")
        print(f"Original Charge: {charge_amt / 100: .2f} USD")
        print(f"Refunded Amount: {refund_amt / 100: .2f} USD")
        print(f"Net Revenue: {net_amt} USD")

except Exception as e:
    print(f'Error fetching data: {e}')






