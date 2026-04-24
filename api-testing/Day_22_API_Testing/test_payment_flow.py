import stripe
import os

# Set the API key from environment variable
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

try:
    # 1. Create a PaymentIntent (This simulates a customer trying to pay $50.00)
    # Stripe uses cents, so 5000 = $50.00
    payment_intent = stripe.PaymentIntent.create(
        amount=5000,
        currency="usd",
        payment_method_types=["card"],
        description="Day 22 Automation Test"
    )

    # 2. Print the critical details for your report
    print("--- Payment Intent Created Successfully ---")
    print(f"Charge ID (PI): {payment_intent.id}")
    print(f"Amount: ${payment_intent.amount / 100}")
    print(f"Status: {payment_intent.status}")
    print(f"Client Secret: {payment_intent.client_secret}")
    print("------------------------------------------")

except Exception as e:
    print(f"❌ Error during payment creation: {e}")