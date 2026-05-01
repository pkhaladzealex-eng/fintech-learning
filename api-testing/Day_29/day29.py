import json

# Day 29: Full automated script for parsing Stripe Webhook JSON
def parse_webhook_data():
    # Full, unmodified JSON structure directly from Stripe
    raw_json_data = """
    {
      "object": {
        "id": "ch_3TSMOwJP62O0ob1e0X1bJbEj",
        "object": "charge",
        "amount": 6000,
        "amount_captured": 6000,
        "amount_refunded": 0,
        "application": null,
        "application_fee": null,
        "application_fee_amount": null,
        "balance_transaction": "txn_3TSMOwJP62O0ob1e0SiH7dvm",
        "billing_details": {
          "address": {
            "city": null,
            "country": null,
            "line1": null,
            "line2": null,
            "postal_code": null,
            "state": null
          },
          "email": null,
          "name": null,
          "phone": null,
          "tax_id": null
        },
        "calculated_statement_descriptor": "ALEXANDER_QA_TEST SAND",
        "captured": true,
        "created": 1777662422,
        "currency": "usd",
        "customer": null,
        "description": "Python Stripe test, DAY 29",
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
          "risk_score": 15,
          "seller_message": "Payment complete.",
          "type": "authorized"
        },
        "paid": true,
        "payment_intent": null,
        "payment_method": "card_1TSMOwJP62O0ob1e9c3sNS32",
        "payment_method_details": {
          "card": {
            "amount_authorized": 6000,
            "authorization_code": "066507",
            "brand": "visa",
            "checks": {
              "address_line1_check": null,
              "address_postal_code_check": null,
              "cvc_check": "pass"
            },
            "country": "US",
            "ds_transaction_id": null,
            "exp_month": 5,
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
              "maximum_amount_capturable": 6000,
              "status": "unavailable"
            },
            "regulated_status": "unregulated",
            "three_d_secure": null,
            "wallet": null
          },
          "type": "card"
        },
        "receipt_email": null,
        "receipt_number": null,
        "receipt_url": "https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xVEhsckZKUDYyTzBvYjFlKNjz088GMgYFsUxqDtA6LBboGk8pzggTC5tZfowpyEFTugx0iheR3TejtxcqxTf9J6sAZvGYcHwAihui",
        "refunded": false,
        "review": null,
        "shipping": null,
        "source": {
          "id": "card_1TSMOwJP62O0ob1e9c3sNS32",
          "object": "card",
          "address_city": null,
          "address_country": null,
          "address_line1": null,
          "address_line1_check": null,
          "address_line2": null,
          "address_state": null,
          "address_zip": null,
          "address_zip_check": null,
          "allow_redisplay": "unspecified",
          "brand": "Visa",
          "country": "US",
          "customer": null,
          "cvc_check": "pass",
          "dynamic_last4": null,
          "email": null,
          "exp_month": 5,
          "exp_year": 2027,
          "fingerprint": "eXyUbefTuHxHtTK2",
          "funding": "credit",
          "last4": "4242",
          "metadata": {},
          "name": null,
          "phone": null,
          "regulated_status": "unregulated",
          "tokenization_method": null,
          "wallet": null
        },
        "source_transfer": null,
        "statement_descriptor": null,
        "statement_descriptor_suffix": null,
        "status": "succeeded",
        "transfer_data": null,
        "transfer_group": null
      },
      "previous_attributes": null
    }
    """

    # Step 6: Parse JSON string into Python dictionary
    data_dict = json.loads(raw_json_data)

    # Step 7: Extract fields from the top-level "object" key
    # In this specific JSON, charge details are nested inside "object"
    charge_details = data_dict["object"]

    charge_id = charge_details["id"]
    amount = charge_details["amount"] / 100  # Convert cents to dollars
    status = charge_details["status"]
    timestamp = charge_details["created"]

    # Step 8: Print the results clearly
    print("\n" + "="*45)
    print("      STRIPE REAL-TIME WEBHOOK PARSER")
    print("="*45)
    print(f"Charge ID:   {charge_id}")
    print(f"Total Paid:  ${amount:.2f}")
    print(f"Payment Status: {status.upper()}")
    print(f"Unix Created: {timestamp}")
    print("="*45 + "\n")

if __name__ == "__main__":
    parse_webhook_data()