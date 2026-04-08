import os
import stripe

stripe.api_key = os.getenv('STRIPE_TEST_KEY')

if not stripe.api_key:
    print("❌ Error: API key not found!")
else:
    try:
        # tok_chargeDeclined
        charge = stripe.Charge.create(
            amount=2500,
            currency="usd",
            source="tok_chargeDeclined",  # changed
            description="Testing a declined card"
        )
        print("✅ Success! (Wait, this should have failed...)")

    except stripe.error.CardError as e:
        print(f"❌ Card Declined: {e.user_message}")
    except stripe.error.StripeError as e:
        print(f"❌ Stripe Error: {e.user_message}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")