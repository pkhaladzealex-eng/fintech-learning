import os
import stripe

# 1. Get the Stripe API key from the environment variables
stripe.api_key = os.getenv('STRIPE_TEST_KEY')

# 2. Chek if the API key is actually set before making any requests
if not stripe.api_key:
    print("❌ Error: API key not found!")
else:
    try:
        # 3. Create a charge using 'tok_chargeDeclined' to simulate a card that gets rejected
        charge = stripe.Charge.create(
            amount=2500,
            currency="usd",
            source="tok_chargeDeclined",  # Special Stripe token to force a decline error
            description="Testing a declined card"
        )
        # If the code reaches this line, something went wrong because this card  must FAIL
        print("✅ Success! (Wait, this should have failed...)")

    except stripe.error.CardError as e:
        # 4. Catch specific card issues (like insufficient funds, wrong PIN, or declined cards)
        print(f"❌ Card Declined: {e.user_message}")

    except stripe.error.StripeError as e:
        # 5. Catch other Stripe-related API issues (like network failure or wrong setup)
        print(f"❌ Stripe Error: {e.user_message}")
        # 6. Catch any other unexpected Python errors
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")