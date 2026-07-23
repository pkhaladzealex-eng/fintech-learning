import stripe
import os

# 1. Fetch the Stripe secret API key from system environment variables
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")


def create_declined_charge():
    print("🚀 Attempting to create a charge with a declined card...")
    try:
        # 2. Try to create a $50 charge using Stripe's specific test token for declined cards
        charge = stripe.Charge.create(
            amount=5000,  # $50.00 in cents
            currency="usd",
            source="tok_chargeDeclined",  # Forces Stripe to reject this card
            description="Testing declined card scenario for Day 24"
        )
        # This print should not execute since the charge is expected to fail
        print("✅ Success? This shouldn't happen!")

    except stripe.error.CardError as e:
        # 3. Extract the full JSON response payload returned by Stripe API
        body = e.json_body
        err = body.get('error', {})  # Safely get the 'error' dictionary

        # 4. Print detailed error fields (HTTP status, error codes, and message)
        print("\n❌ CARD DECLINED BY API (Caught expected error)")
        print(f"HTTP Status:  {e.http_status}")
        print(f"Error Code:   {err.get('code')}")
        print(f"Decline Code: {err.get('decline_code')}")
        print(f"Message:      {err.get('message')}")

    except Exception as e:
        # 5. Catch any other non-card or network level errors
        print(f"⚠️ An unexpected error occurred: {e}")


if __name__ == "__main__":
    create_declined_charge()