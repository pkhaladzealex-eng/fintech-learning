import pytest
import sqlite3
import stripe
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import config
import utils

stripe.api_key = os.environ.get("STRIPE_API_KEY", config.STRIPE_API_KEY)


def create_real_stripe_test_charge():
    print("\n[Stripe API] Creating test charge...")
    try:
        charge = stripe.Charge.create(
            amount=2500,
            currency="usd",
            source="tok_visa",
            description="Integration Test Charge - Option A"
        )
        print(f"[Stripe API] Charge created: {charge.id}")
        return charge
    except stripe.error.StripeError as e:
        pytest.fail(f"Stripe API failed: {e}")


def insert_charge_into_database(charge_id, amount, status):
    print(f"[Database] Inserting {charge_id}...")
    conn = sqlite3.connect(config.DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO charges VALUES (?, ?, ?, NULL, NULL, NULL)",
        (charge_id, amount, status)
    )
    conn.commit()
    conn.close()
    print("[Database] Inserted successfully.")


def query_payment_database(charge_id):
    print(f"[Database] Querying {charge_id}...")
    conn = sqlite3.connect(config.DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM charges WHERE charge_id = ?", (charge_id,))
    record = cursor.fetchone()
    conn.close()
    return record


def cleanup_database(charge_id):
    conn = sqlite3.connect(config.DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM charges WHERE charge_id = ?", (charge_id,))
    conn.commit()
    conn.close()
    print(f"[Cleanup] Deleted {charge_id} from database.")


def test_payment_integration():
    print("\n[Integration Test] Starting...")

    # Step 1: Stripe
    stripe_charge = create_real_stripe_test_charge()
    new_charge_id = stripe_charge.id

    # Step 2: Insert + verify insert worked
    try:
        insert_charge_into_database(new_charge_id, stripe_charge.amount, stripe_charge.status)
    except Exception as e:
        pytest.fail(f"Database insert failed: {e}")

    # Step 3: Stripe verify
    fetched_charge = utils.fetch_charge_safe(new_charge_id)
    assert fetched_charge is not None, "Charge not found on Stripe"
    assert fetched_charge.status == "succeeded", "Charge status should be succeeded"
    print("✓ [Step 1/2] Stripe verification passed.")

    # Step 4: DB verify
    db_record = query_payment_database(new_charge_id)
    assert db_record is not None, f"Charge '{new_charge_id}' not found in DB"
    assert db_record[0] == new_charge_id, "Database record ID mismatch"
    print(f"✓ [Step 2/2] Database verification passed: {db_record}")

    # Step 5: Cleanup
    cleanup_database(new_charge_id)
    print("\n [PASSED] Integration test complete!")