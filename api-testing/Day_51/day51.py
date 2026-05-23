import stripe
import os

stripe.api_key = os.environ.get("STRIPE_API_KEY")
charge_id = "ch_3TZHd0JP62O0ob1e29DOOv37"
try:

    charge = stripe.Charge.retrieve(charge_id)
    print(charge)
except stripe.error.AuthenticationError as e:
    print(f'Authentication Error: {e}')
except stripe.error.InvalidRequestError as e:
    print(f'The requested resource was not found or parameters are invalid!: {e}')
except Exception as e:
    print(f'Something else went wrong: {e}')
