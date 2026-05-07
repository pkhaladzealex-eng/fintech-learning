import stripe
import os
import sqlite3
try:

    stripe.api_key = os.environ.get('STRIPE_API_KEY')
    conn = None
    refund_id_to_fetch = "re_3TUX2FJP62O0ob1e1BEnijMc"
    refund_obj = stripe.Refund.retrieve(refund_id_to_fetch)

    conn = sqlite3.connect('/Users/alexpkhaladze/desktop/fintech-learning/global_data/fintech_main.db')
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS refunds (
    refund_id TEXT PRIMARY KEY,
    charge_id TEXT,

    amount INTEGER NOT NULL,
    status TEXT
    )""")
    conn.commit()

    formated_data = [(refund_obj.id, refund_obj.charge, refund_obj.amount, refund_obj.status)]
    cursor.executemany("INSERT INTO refunds (refund_id, charge_id, amount, status) VALUES (?,?,?,?)", formated_data)
    conn.commit()

    cursor.execute("SELECT * FROM refunds")
    rows = cursor.fetchall()
    for row in rows:
        print(f'Refund ID : [{row[0]}], Charge : [{row[1]}], Amount : [{row[2]}], Status : [{row[3]}]')

    cursor.execute("SELECT  SUM(amount) FROM refunds")
    totalAmount = cursor.fetchone()[0] or 0
    print(f'Total Amount : [{totalAmount / 100}] USD')

except stripe.error.StripeError as e:
    print(f"Stripe API Error: {e}")
except sqlite3.Error as e:
    print(f"Database Error: {e}")
except Exception as e:
    print(f"Unexpected Error: {e}")
finally:
    if 'conn' in locals():
        conn.close()



