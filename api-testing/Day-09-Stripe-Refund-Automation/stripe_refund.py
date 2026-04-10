import stripe
import os


stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

try:

    payment = stripe.Charge.create(
        amount=5000,
        currency="usd",
        source="tok_visa",
        description="Test payment for refund exercise"
    )

    charge_id = payment.id
    print(f"Successfully created charge! ID: {charge_id}")


    refund = stripe.Refund.create(
        charge=charge_id
    )

    print(f"Refund Status: {refund.status}")
    print(f"Refund ID: {refund.id}")

except Exception as e:
    
    print(f"An error occurred: {e}")