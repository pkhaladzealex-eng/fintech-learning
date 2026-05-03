import stripe
import os

stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")


charge_id = "ch_3TSMOwJP62O0ob1e0X1bJbEj"

try:

    charge = stripe.Charge.retrieve(charge_id)


    charge_details = {
        'ID': charge.id,
        'Amount': charge.amount / 100,
        'Status': charge.status,
        'Created': charge.created,
        'Currency': charge.currency.upper()
    }


    print("--- Charge Details Extracted ---")
    for key, value in charge_details.items():
        print(f'{key}: {value}')

except Exception as e:
    print(f'Error fetching charge: {e}')
