import os
import stripe

# ვკითხულობთ გასაღებს, რომელიც წეღან export-ით დავაყენეთ
stripe.api_key = os.getenv('STRIPE_TEST_KEY')

if not stripe.api_key:
    print("❌ Error: API key not found! Did you run 'export STRIPE_TEST_KEY=...'?")
else:
    try:
        # ვქმნით სატესტო "Charge"-ს
        charge = stripe.Charge.create(
            amount=2500,        # ეს არის 25.00 USD (ცენტებში იწერება)
            currency="usd",
            source="tok_visa",  # სპეციალური ტესტ-ტოკენი Stripe-ისგან
            description="My first Python Stripe test"
        )

        # პასუხის დაბეჭდვა
        print("\n✅ Success! Charge Created:")
        print(f"ID:     {charge['id']}")
        print(f"Amount: {charge['amount'] / 100} {charge['currency'].upper()}")
        print(f"Status: {charge['status']}")

    except Exception as e:
        print(f"❌ API Error: {e}")