import json

# Day 29: Automated Script to parse real Stripe Webhook JSON
def parse_webhook_data():
    # The raw JSON payload exactly as received from Stripe
    raw_json_data = """
    {
      "object": {
        "id": "ch_3TSMOwJP62O0ob1e0X1bJbEj",
        "object": "charge",
        "amount": 6000,
        "status": "succeeded",
        "created": 1777662422,
        "currency": "usd"
      },
      "previous_attributes": null
    }
    """

    # Step 6: Parse the JSON string into a Python dictionary
    # We use json.loads() to convert the string text into a searchable object
    webhook_payload = json.loads(raw_json_data)

    # Step 7: Extract specific fields
    # In your JSON, the data is inside the "object" key directly
    charge_details = webhook_payload["object"]

    charge_id = charge_details["id"]
    amount = charge_details["amount"] / 100  # Convert cents to dollars
    status = charge_details["status"]
    timestamp = charge_details["created"]

    # Step 8: Print each field clearly in the terminal
    print("\n" + "="*40)
    print("STRIPE WEBHOOK DATA EXTRACTION")
    print("="*40)
    print(f"Charge ID:  {charge_id}")
    print(f"Amount:     ${amount:.2f}")
    print(f"Status:     {status.upper()}")
    print(f"Timestamp:  {timestamp}")
    print("="*40 + "\n")

if __name__ == "__main__":
    parse_webhook_data()