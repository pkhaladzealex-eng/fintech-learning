import sqlite3
import os
import stripe

stripe.api_key=os.environ.get("STRIPE_API_KEY")
conn = None
try:
    stripe.Charge.create(
        amount=5000,
        currency="usd",
        source="tok_chargeDeclined",
        description="Declined Card Test"

    )
except stripe.error.CardError as e:
    body = e.json_body
    err = body.get('error', {})
    error_message = err.get('message')
    print(f"Stripe Error Message: {error_message}")
    failed_charge_id = err.get('charge')

    conn = sqlite3.connect('/Users/alexpkhaladze/desktop/fintech-learning/global_data/fintech_main.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO charges (charge_id, amount, status) Values (?, ?, ?)", (failed_charge_id, 50.00, 'failed'))
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM charges WHERE LOWER(status) = 'succeeded'")
    total_succeeded = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*)  FROM charges WHERE LOWER(status) = 'failed'")
    total_failed = cursor.fetchone()[0]
    print(f"✅ Successful charges: {total_succeeded}")
    print(f"❌ Failed charges: {total_failed}")
finally:
    if conn:
        conn.close()








