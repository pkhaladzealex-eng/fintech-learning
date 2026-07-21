import stripe
import os

# 1. Fetch the secret API key from system environment variables
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

try:
    # 2. Step 1: Create a successful charge ($50.00) to refund later
    payment = stripe.Charge.create(
        amount=5000, # 5000 cents = 50.00$
        currency="usd",
        source="tok_visa", # Standard Test Visa token
        description="Test payment for refund exercise"
    )
    # 3. Extract  and print  the unique charge ID returned by Stripe
    charge_id = payment.id
    print(f"Successfully created charge! ID: {charge_id}")

    # 4. Step 2: Issue a full refund  for the created charge using its ID
    refund = stripe.Refund.create(
        charge=charge_id # Linking the  refund to the specific charge above
    )
    # 5. Print the refund  result details
    print(f"Refund Status: {refund.status}")
    print(f"Refund ID: {refund.id}")

except Exception as e:
    # 6. Catch and log any API or execution errors
    print(f"An error occurred: {e}")