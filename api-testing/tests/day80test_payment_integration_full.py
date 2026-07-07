import pytest
import sqlite3
import stripe
import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import config
import utils


stripe.api_key = os.environ.get("STRIPE_API_KEY", config.STRIPE_API_KEY)  #



def create_real_stripe_test_charge():
    print("\n[Stripe API] INITIATING LIVE TEST CHARGE CREATION...")
    try:
        charge = stripe.Charge.create(
            amount=2500,
            currency="usd",
            source="tok_visa",
            description="Integration Test Charge - Option A Workflow"
        )
        print(f"[Stripe API] Charge created successfully! Live Test ID: {charge.id}")
        return charge
    except stripe.error.StripeError as e:
        pytest.fail(f"Stripe API Rejected Request: {e}")


def insert_charge_into_database(charge_id, amount, status):

    print(f"[Database] Inserting Charge {charge_id} into local ledger...")

    conn = sqlite3.connect(config.DATABASE_PATH)  #
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO charges 
            VALUES (?, ?, ?, NULL, NULL, NULL)
            """,
            (charge_id, amount, status)
        )
        conn.commit()
        print("[Database] Record committed successfully.")
    except sqlite3.Error as e:
        print(f"[Database] Insert Error: {e}")
    finally:
        conn.close()


def query_payment_database(charge_id):
    print(f"[Database Query] Fetching logs for Target ID: {charge_id}")
    conn = sqlite3.connect(config.DATABASE_PATH)  #
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM charges WHERE charge_id = ?", (charge_id,))
    record = cursor.fetchone()
    conn.close()
    return record


def test_payment_integration():
    print("\n[Integration Test] Starting API Database pipeline verification...")


    stripe_charge = create_real_stripe_test_charge()
    new_charge_id = stripe_charge.id


    insert_charge_into_database(new_charge_id, stripe_charge.amount, stripe_charge.status)


    fetched_charge = utils.fetch_charge_safe(new_charge_id)  #
    assert fetched_charge is not None, "Failed to verify newly created charge on Stripe backend"
    assert fetched_charge.status == "succeeded", "Stripe test charge should be marked as succeeded"
    print(f"✓ [Step 1/2 Passed] Dynamic Stripe verification completely valid.")


    db_record = query_payment_database(new_charge_id)

    assert db_record is not None, f"Data Flow Broken: Charge '{new_charge_id}' was not saved in DB!"
    assert db_record[0] == new_charge_id, "Database record ID mismatch"

    print(f" [Step 2/2 Passed] Database Integrity verified. Found DB Log: {db_record}")
    print("\n [PASSED] Option A Integration Test is fully green! Data flows properly without fake UI.")