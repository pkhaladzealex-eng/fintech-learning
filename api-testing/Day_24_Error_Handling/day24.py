import stripe
import os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

def create_declined_charge():
    print("🚀 Attempting to create a charge with a declined card...")
    try:
        charge = stripe.Charge.create(
            amount=5000,
            currency="usd",
            source="tok_chargeDeclined",
            description="Testing declined card scenario for Day 24"
        )
        print("✅ Success? This shouldn't happen!")
    except stripe.error.CardError as e:
        body = e.json_body
        err = body.get('error', {})
        print("\n❌ CARD DECLINED BY API (Caught expected error)")
        print(f"HTTP Status:  {e.http_status}")
        print(f"Error Code:   {err.get('code')}")
        print(f"Decline Code: {err.get('decline_code')}")
        print(f"Message:      {err.get('message')}")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    create_declined_charge()
