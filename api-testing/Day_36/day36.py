import json
from datetime import datetime


webhook_payload = """ {
  "object": {
    "id": "ch_3TUX2FJP62O0ob1e1Tu1E0ot",
    "object": "charge",
    "amount": 7500,
    "amount_captured": 7500,
    "amount_refunded": 0,
    "application": null,
    "application_fee": null,
    "application_fee_amount": null,
    "balance_transaction": "txn_3TUX2FJP62O0ob1e1hS1dxZ7",
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
    "calculated_statement_descriptor": "STRIPE SUCCESS",
    "captured": true,
    "created": 1778179955,
    "currency": "usd",
    "customer": null,
    "description": "Tesat Day 35",
    "destination": null,
    "dispute": null,
    "disputed": false,
    "failure_balance_transaction": null,
    "failure_code": null,
    "failure_message": null,
    "fraud_details": {},
    "livemode": false,
    "metadata": {},
    "on_behalf_of": null,
    "order": null,
    "outcome": {
      "advice_code": null,
      "network_advice_code": null,
      "network_decline_code": null,
      "network_status": "approved_by_network",
      "reason": null,
      "risk_level": "normal",
      "risk_score": 62,
      "seller_message": "Payment complete.",
      "type": "authorized"
    },
    "paid": true,
    "payment_intent": "pi_3TUX2FJP62O0ob1e1vyKvdOz",
    "payment_method": "pm_1TUX2FJP62O0ob1es0RO2j8m",
    "payment_method_details": {
      "card": {
        "amount_authorized": 7500,
        "authorization_code": "109099",
        "brand": "visa",
        "checks": {
          "address_line1_check": null,
          "address_postal_code_check": "pass",
          "cvc_check": "pass"
        },
        "country": "US",
        "ds_transaction_id": null,
        "exp_month": 4,
        "exp_year": 2027,
        "extended_authorization": {
          "status": "disabled"
        },
        "fingerprint": "eXyUbefTuHxHtTK2",
        "funding": "credit",
        "incremental_authorization": {
          "status": "unavailable"
        },
        "installments": null,
        "last4": "4242",
        "mandate": null,
        "multicapture": {
          "status": "unavailable"
        },
        "network": "visa",
        "network_token": {
          "used": false
        },
        "network_transaction_id": "101881218598101",
        "overcapture": {
          "maximum_amount_capturable": 7500,
          "status": "unavailable"
        },
        "regulated_status": "unregulated",
        "three_d_secure": null,
        "wallet": null
      },
      "type": "card"
    },
    "radar_options": {},
    "receipt_email": null,
    "receipt_number": null,
    "receipt_url": "https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xVEhsckZKUDYyTzBvYjFlKPS-888GMgYJFqGgl206LBa_7npNLHfZKPU9BROWwvW51AIR6rWHU300iQuEUZRwVTKUtWNEqkJvmCJA",
    "refunded": false,
    "review": null,
    "shipping": null,
    "source": null,
    "source_transfer": null,
    "statement_descriptor": "STRIPE SUCCESS",
    "statement_descriptor_suffix": null,
    "status": "succeeded",
    "transfer_data": null,
    "transfer_group": null
  },
  "previous_attributes": null
}"""


data = json.loads(webhook_payload)
#print(type(data))

charge_id = data["object"]["id"]
amount = data["object"]["amount"]
status = data["object"]["status"]
timestamp = data["object"]["created"]


readable_date = datetime.fromtimestamp(timestamp)

print(f"Charge ID: {charge_id}")
print(f"Amount: {amount / 100} USD")
print(f"Status: {status}")
print(f"Date: {readable_date}")

