import json
from datetime import datetime

real_webhook_payload = """  {
"id": "evt_3TZdacJP62O0ob1e15DusHJ5",
  "object": {
    "id": "pi_3TZdacJP62O0ob1e1XNhVOnq",
    "object": "payment_intent",
    "amount": 4900,
    "amount_capturable": 0,
    "amount_details": {
      "tip": {}
    },
    "amount_received": 0,
    "application": null,
    "application_fee_amount": null,
    "automatic_payment_methods": null,
    "canceled_at": null,
    "cancellation_reason": null,
    "capture_method": "automatic",
    "client_secret": "pi_3TZdacJP62O0ob1e1XNhVOnq_secret_Pvzz9Bis91JYf51JpJCqF8Ezf",
    "confirmation_method": "automatic",
    "created": 1779396790,
    "currency": "usd",
    "customer": null,
    "customer_account": null,
    "description": "Test day 49",
    "excluded_payment_method_types": null,
    "last_payment_error": {
      "advice_code": "try_again_later",
      "charge": "ch_3TZdacJP62O0ob1e1xjus5Ai",
      "code": "card_declined",
      "decline_code": "generic_decline",
      "doc_url": "https://stripe.com/docs/error-codes/card-declined",
      "message": "Your card was declined.",
      "network_decline_code": "01",
      "payment_method": {
        "id": "pm_1TZdabJP62O0ob1epegvkgYo",
        "object": "payment_method",
        "allow_redisplay": "unspecified",
        "billing_details": {
          "address": {
            "city": null,
            "country": null,
            "line1": null,
            "line2": null,
            "postal_code": "10000",
            "state": null
          },
          "email": null,
          "name": null,
          "phone": null,
          "tax_id": null
        },
        "card": {
          "brand": "visa",
          "checks": {
            "address_line1_check": null,
            "address_postal_code_check": "pass",
            "cvc_check": "pass"
          },
          "country": "US",
          "display_brand": "visa",
          "exp_month": 12,
          "exp_year": 2034,
          "fingerprint": "ZyOo1is0VTEWEiDw",
          "funding": "credit",
          "generated_from": null,
          "last4": "0002",
          "networks": {
            "available": [
              "visa"
            ],
            "preferred": null
          },
          "regulated_status": "unregulated",
          "three_d_secure_usage": {
            "supported": true
          },
          "wallet": null
        },
        "created": 1779396790,
        "customer": null,
        "customer_account": null,
        "livemode": false,
        "metadata": {},
        "radar_options": {},
        "shared_payment_granted_token": null,
        "type": "card"
      },
      "type": "card_error"
    },
    "latest_charge": "ch_3TZdacJP62O0ob1e1xjus5Ai",
    "livemode": false,
    "managed_payments": {
      "enabled": false
    },
    "metadata": {},
    "next_action": null,
    "on_behalf_of": null,
    "payment_method": null,
    "payment_method_configuration_details": null,
    "payment_method_options": {
      "card": {
        "installments": null,
        "mandate_options": null,
        "network": null,
        "request_three_d_secure": "automatic"
      }
    },
    "payment_method_types": [
      "card"
    ],
    "processing": null,
    "receipt_email": null,
    "review": null,
    "setup_future_usage": null,
    "shared_payment_granted_token": null,
    "shipping": null,
    "source": null,
    "statement_descriptor": "Test Day 49",
    "statement_descriptor_suffix": null,
    "status": "requires_payment_method",
    "transfer_data": null,
    "transfer_group": null
  },
  "previous_attributes": null
} 
"""
def process_failed_webhook(payload):
    event = json.loads(payload) # Get the core data object from the webhook
    stripe_obj = event["object"]
    payment_error = stripe_obj["last_payment_error"] # Extract the payment error details

    # Extract timestamp and convert to human-readable format
    timestamp = stripe_obj["created"]
    readable_date = datetime.fromtimestamp(timestamp)

    if payment_error:
        print(f'Event ID: {event["id"]}')
        print(f'Charge ID: {payment_error["charge"]}')
        print(f'Failure Reason: {payment_error["code"]}')
        print(f'Failure Message: {payment_error["message"]}')
        print(f'Timestamp: {readable_date}')
    else:
        print("No error details found")
process_failed_webhook(real_webhook_payload)



