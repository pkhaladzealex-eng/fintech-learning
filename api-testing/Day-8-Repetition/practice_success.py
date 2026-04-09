import os
import stripe


stripe.api_key = os.getenv('STRIPE_TEST_KEY')

if not stripe.api_key:
    print("❌ Error: API key not found! Did you run 'export STRIPE_TEST_KEY=...'?")
else:
    try:

        charge = stripe.Charge.create(
            amount=4000,
            currency="gbp",
            source="tok_visa",
            description="Practice charge in GBP"
        )


        print("\n✅ Success! Charge Created:")
        print(f"ID:     {charge['id']}")
        print(f"Amount: {charge['amount'] / 100} {charge['currency'].upper()}")
        print(f"Status: {charge['status']}")

    except Exception as e:
        print(f"❌ API Error: {e}")
