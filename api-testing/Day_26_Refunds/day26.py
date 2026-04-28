import stripe
import os

# API Key setup
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

def create_refund(target_id):
    try:
        print(f"🔄 Initiating refund for: {target_id}...")

        # 1. API Call to create a refund (Universal Logic)
        if target_id.startswith('ch_'):
            resource = stripe.Refund.create(charge=target_id, reason="requested_by_customer")
        else:
            resource = stripe.Refund.create(payment_intent=target_id, reason="requested_by_customer")

        # 2. Convert to Dictionary for safe data extraction
        # This fixes the 'Error: get' issue
        data = resource.to_dict()

        # 3. Extract details safely
        refund_id = data.get('id')
        amount = data.get('amount', 0) / 100
        status = data.get('status')
        reason = data.get('reason')
        currency = data.get('currency', 'usd').upper()


        print(" REFUND SUCCESSFULLY CREATED")

        print(f" Refund ID: {refund_id}")
        print(f" Amount:    {amount} {currency}")
        print(f" Status:    {status}")
        print(f" Reason:    {reason}")


    except Exception as e:
        print(f"❌ Refund Error: {e}")

if __name__ == "__main__":

    TARGET_PAYMENT_ID = "ch_3TQZqhJP62O0ob1e0Pk740Bq"
    create_refund(TARGET_PAYMENT_ID)