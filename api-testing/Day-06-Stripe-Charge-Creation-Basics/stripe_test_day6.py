import os
import stripe

# 1. Get the Stripe API key from the environment variables
stripe.api_key = os.getenv('STRIPE_TEST_KEY')

# 2. Check if the API key is actually set before making any requests
if not stripe.api_key:
    print("❌ Error: API key not found! Did you run 'export STRIPE_TEST_KEY=...'?")
else:
    try:
        # 3. Creating a real test transaction on Stipe using their mock Visa card
        charge = stripe.Charge.create(
            amount=2500, # $25.00 (Stripe uses cents)
            currency="usd",
            source="tok_visa", # Stripe's official test card token
            description="My first Python Stripe test"
        )

        # 4. If successful, print the main transaction details to the console
        print("\n✅ Success! Charge Created:")
        print(f"ID:     {charge['id']}")
        print(f"Amount: {charge['amount'] / 100} {charge['currency'].upper()}")
        print(f"Status: {charge['status']}")

    except Exception as e:
        # 5. Catch and print any API or network errors safely
        print(f"❌ API Error: {e}")