import logging
import json
from datetime import datetime

filename='payment_logs.txt'
level=logging.INFO
format='%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(filename=filename, level=level, format=format)

real_webhook_payload = """ 
{   "id" : "evt_3TZHd0JP62O0ob1e21gtPULX",
  "object": {
    "id": "pi_3TZHd0JP62O0ob1e2UpdqomF",
    "object": "payment_intent",
    "amount": 4800,
    "amount_capturable": 0,
    "amount_details": {
      "tip": {}
    },
    "amount_received": 4800,
    "application": null,
    "application_fee_amount": null,
    "automatic_payment_methods": null,
    "canceled_at": null,
    "cancellation_reason": null,
    "capture_method": "automatic",
    "client_secret": "pi_3TZHd0JP62O0ob1e2UpdqomF_secret_KE1PCLXCNzChRzQ3mYfdBE2pr",
    "confirmation_method": "automatic",
    "created": 1779312370,
    "currency": "usd",
    "customer": "cus_UGdk3M75wDH1Wz",
    "customer_account": null,
    "description": "Test day 48",
    "excluded_payment_method_types": null,
    "last_payment_error": null,
    "latest_charge": "ch_3TZHd0JP62O0ob1e29DOOv37",
    "livemode": false,
    "managed_payments": {
      "enabled": false
    },
    "metadata": {},
    "next_action": null,
    "on_behalf_of": null,
    "payment_method": "pm_1TI6USJP62O0ob1e5guLwh9e",
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
    "receipt_email": "qaengineeralexander+mark@gmail.com",
    "review": null,
    "setup_future_usage": null,
    "shared_payment_granted_token": null,
    "shipping": null,
    "source": null,
    "statement_descriptor": "Test Day 48",
    "statement_descriptor_suffix": null,
    "status": "succeeded",
    "transfer_data": null,
    "transfer_group": null
  },
  "previous_attributes": null
}
"""

def parse_and_validate_webhook_with_logging(payload):
    logging.info("Webhook received")
    event = json.loads(payload)

    if 'id' not in event or 'object' not in event:
        logging.error("Validation failed: missing top level keys")
        return
    stripe_obj = event['object']
    if not all(k in stripe_obj for k in ['id','amount', 'customer', 'created']):
        logging.error('Validation failed: missing inner object keys')
        return

    charge_id = stripe_obj['id']
    logging.info(f' Charge ID Extracted: {charge_id}')
    timestamp = stripe_obj['created']
    readable_date = datetime.fromtimestamp(timestamp)
    logging.info(f'Timestamp parsed: {readable_date}')

    print(f'Event ID: {event["id"]}')
    print(f'Amount: {stripe_obj["amount"] / 100:.2f}{stripe_obj["currency"].upper()}')

parse_and_validate_webhook_with_logging(real_webhook_payload)




