import os
import stripe

# 1. Fetch the Stripe API KEY  from  system environment variables
stripe.api_key = os.getenv('STRIPE_TEST_KEY')

# 2. Check if API KEY exists before proceeding with the API call
if not stripe.api_key:
    print("❌ Error: API key not found!")
else:
    try:
        # 3. Try to charge a declined test  card with the British Pounds
        charge = stripe.Charge.create(
            amount=3500, #3500 cents = 35.00 GBP
            currency="gbp",
            source="tok_chargeDeclined",
            description="Testing a declined card" # Stripe test token that forces a card decline
        )
        # This line should never run because the card above is meant to  fail
        print("✅ Success! (Wait, this should have failed...)")

    except stripe.error.CardError as e:
        # 4.Handle card specific failures (like a declined card or wrong cvc)
        print(f"❌ Card Declined: {e.user_message}")
    except stripe.error.StripeError as e:
        # 5. Handle general Stripe errors ( like authentification issues)
        print(f"❌ Stripe Error: {e.user_message}")
    except Exception as e:
        # 6. Catch any other unexpected system errors
        print(f"❌ Unexpected Error: {e}")