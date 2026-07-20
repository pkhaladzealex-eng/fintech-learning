import os
import stripe

# 1. Fetch the Stripe API KEY from system environment variables
stripe.api_key = os.getenv('STRIPE_TEST_KEY')

# 2. Make sure the API KEY  is set before trying to make a charge
if not stripe.api_key:
    print("❌ Error: API key not found! Did you run 'export STRIPE_TEST_KEY=...'?")
else:
    try:
        # 3. Creating a charge in British Pounds  (GBP) using a test card
        charge = stripe.Charge.create(
            amount=4000, # 4000 = 40.00 GBP
            currency="gbp",
            source="tok_visa", # Standard Stripe Visa test token
            description="Practice charge in GBP"
        )

        # 4. Print transaction details after successful charge
        print("\n✅ Success! Charge Created:")
        print(f"ID:     {charge['id']}")
        print(f"Amount: {charge['amount'] / 100} {charge['currency'].upper()}")
        print(f"Status: {charge['status']}")

    except Exception as e:
        # 5. Catch any general errors during execution
        print(f"❌ API Error: {e}")
