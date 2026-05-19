
import json

def stream_webhook_matrix():
    print("--- Day 47: Stripe Webhook Event Specification Matrix ---\n")

    events = {
        "charge.succeeded": {
            "description": "Fires immediately when a customer's payment is successfully authorized and captured.",
            "when_it_fires": "Triggered upon successful balance movement into the platform account registry.",
            "contains_data": ["charge_id", "amount_cents", "currency", "payment_method_details", "customer_metadata"]
        },
        "charge.failed": {
            "description": "Fires when a transaction attempt is declined by the gateway or issuing institution.",
            "when_it_fires": "Triggered by insufficient parameters, fraud detection, or expired processing cards.",
            "contains_data": ["charge_id", "amount_cents", "failure_code", "failure_message", "outcome_type"]
        },
        "charge.refunded": {
            "description": "Fires when an active completed charge is either partially or fully reversed.",
            "when_it_fires": "Triggered via manual dashboard interventions or automated refund API requests.",
            "contains_data": ["charge_id", "amount_refunded", "refund_id", "receipt_number", "status_logs"]
        }
    }

    # Dynamic parsing iterator loop
    for event_name, event_meta in events.items():
        print(f"Event Type : {event_name}")
        print(f"Description: {event_meta['description']}")
        print(f"Triggers   : {event_meta['when_it_fires']}")
        print(f" Payload Keys: {', '.join(event_meta['contains_data'])}")
        print("-" * 80)

if __name__ == "__main__":
    stream_webhook_matrix()
