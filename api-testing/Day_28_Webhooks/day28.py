"""
Day 28: Understanding Webhook Events
Explanation:
Webhooks are automated messages sent from Stripe when an event happens.
- charge.succeeded: Triggered when a payment is successfully captured.
- charge.failed: Triggered when a payment attempt fails (e.g., declined card).
"""

import json


def get_sample_succeeded_event():
    # Sample JSON structure for a successful charge
    return {
        "id": "evt_123_success",
        "type": "charge.succeeded",
        "data": {
            "object": {
                "id": "ch_123",
                "amount": 5000,
                "currency": "usd",
                "status": "succeeded"
            }
        }
    }


def get_sample_failed_event():
    # Sample JSON structure for a failed charge
    return {
        "id": "evt_123_failed",
        "type": "charge.failed",
        "data": {
            "object": {
                "id": "ch_124",
                "amount": 5000,
                "currency": "usd",
                "status": "failed",
                "failure_message": "Your card has insufficient funds."
            }
        }
    }


def main():
    print("--- Sample Webhook: charge.succeeded ---")
    print(json.dumps(get_sample_succeeded_event(), indent=4))

    print("\n--- Sample Webhook: charge.failed ---")
    print(json.dumps(get_sample_failed_event(), indent=4))


if __name__ == "__main__":
    main()