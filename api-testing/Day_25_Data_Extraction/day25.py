import stripe
import os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")


def extract_charge_info(charge_id):
    try:
        print(f"🔍 Fetching details for ID: {charge_id}...")

        # 1. Retrieve data based on ID type
        if charge_id.startswith('pi_'):
            resource = stripe.PaymentIntent.retrieve(charge_id)
        else:
            resource = stripe.Charge.retrieve(charge_id)

        # 2. Convert Stripe object to a standard Python dictionary
        data = resource.to_dict()

        # 3. Data Extraction with safer access
        amount = data.get('amount', 0) / 100
        currency = data.get('currency', 'unknown').upper()
        status = data.get('status', 'unknown')

        # PaymentIntent and Charge store emails in different places
        email = data.get('receipt_email') or \
                data.get('billing_details', {}).get('email') or \
                "No email provided"

        print("\n" + "=" * 30)
        print("📊 EXTRACTED PAYMENT DATA")
        print("=" * 30)
        print(f"💰 Amount:   {amount} {currency}")
        print(f"🚦 Status:   {status}")
        print(f"📧 Customer: {email}")
        print(f"🆔 ID:       {charge_id}")
        print("=" * 30)

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    # Ensure you have the correct ID here
    MY_CHARGE_ID = "pi_3TQDDXJP62O0ob1e0PHTw8da"
    extract_charge_info(MY_CHARGE_ID)
