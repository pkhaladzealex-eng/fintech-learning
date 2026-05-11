import os
import stripe

stripe.api_key = os.environ.get('STRIPE_API_KEY')

if stripe.api_key is None:
    raise ValueError('Stripe API key is required.')
    print(f"API KEY Validated!")
try:
    stripe.Charge.create(
        amount=7800,
        currency='USD',
        source='tok_visa',
        description="Day 39 Charge"
    )
    print(f"Charge created successfully!")
except stripe.error.StripeError as e:
    print(f"Stripe Error: {e}")
