import stripe
import os

# 1. Setup API Key from environment variables
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")


def retrieve_charge_details():
    try:
        # 2. Read the Charge ID from the text file
        with open("charge_id.txt", "r") as file:
            # .strip() removes any accidental spaces or new lines
            charge_id = file.read().strip()

        if not charge_id:
            print("❌ Error: charge_id.txt is empty!")
            return

        print(f"🔍 Fetching details for: {charge_id}...")

        # 3. Query Stripe API to get charge details
        # We use PaymentIntent because you created it in the dashboard
        payment_intent = stripe.PaymentIntent.retrieve(charge_id)

        # 4. Print the required details
        print("\n--- Charge Details Successfully Retrieved ---")
        print(f"ID:      {payment_intent.id}")
        print(f"Amount:  ${payment_intent.amount / 100} {payment_intent.currency.upper()}")
        print(f"Status:  {payment_intent.status}")
        # Convert timestamp to readable format isn't strictly required,
        # but the raw 'created' value is a unix timestamp.
        print(f"Created: {payment_intent.created} (Unix Timestamp)")
        print("--------------------------------------------")

    except FileNotFoundError:
        print("❌ Error: charge_id.txt file not found!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    retrieve_charge_details()