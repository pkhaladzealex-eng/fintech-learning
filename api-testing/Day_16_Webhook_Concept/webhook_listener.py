print("🚀 Waiting for webhook events...")
print("Listening on http://localhost:5000/webhook (Simulation)")

# How Webhooks Work:
# 1. An event occurs in a service (e.g., Stripe processes a payment).
# 2. The service sends an HTTP POST request to a pre-configured URL (our webhook).
# 3. This is a "Push" mechanism, meaning the server tells us about the update
#    automatically, so we don't have to keep asking "is it done yet?".

sample_webhook_data = {
    "id": "evt_3TNF...",
    "type": "charge.succeeded",
    "created": 1713368738,
    "data": {
        "object": {
            "id": "ch_3TNF...",
            "amount": 2500,
            "currency": "usd",
            "status": "succeeded"
        }
    }
}

# In a real scenario, we would parse this data and update our database.
print(f"\nExample of received data: {sample_webhook_data['type']}")