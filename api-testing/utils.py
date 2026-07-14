import logging
import stripe
import json
import os
import sqlite3

import config

# WHY: Storing the API key securely in env variables prevents sensitive credentials leak on GitHub.
# WHAT COULD BREAK: If the environment key is missing, Stripe throws an AuthenticationError.
# Fix: Ensure `export STRIPE_API_KEY="..."` is run in the terminal before execution.
stripe.api_key = os.environ.get('STRIPE_API_KEY')

logging.basicConfig(
    filename=config.LOG_FILE_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def log_event(level, message):
    """Reusable function to pipeline clean logs both to file and console."""
    if level.upper() == "INFO":
        logging.info(message)
        print(f" INFO: {message}")
    elif level.upper() == "ERROR":
        logging.error(message)
        print(f" ERROR: {message}")


def validate_charge(charge_id, amount, status):
    """Reusable automated assertion function for verifying transactional integrity."""
    try:
        assert charge_id is not None, "Charge ID missing"
        assert amount > 0, "Amount must be a strict positive integer"
        assert status in ['succeeded', 'failed'], "Invalid transactional status"
        log_event("INFO", "✓ Multi-layer behavioral assertions passed successfully.")
        return True
    except AssertionError as e:
        log_event("ERROR", f"Assertion Gateway Broken: {e}")
        return False


# ==================== API SCRIPT SECTION ====================
def fetch_charge_safe(charge_id):
    # WHY: We query Stripe backend directly because UI checks are not enough.
    # A website can show "success" even if the API payment actually failed on the bank side.
    # WHAT COULD BREAK: If Stripe server is down or the charge_id does not exist,
    # it throws a StripeError. Fix: Catch StripeError safely so the whole test pipeline does not crash.
    log_event("INFO", f"Initiating secure network lookup for Charge Target: {charge_id}")
    try:
        charge = stripe.Charge.retrieve(charge_id)
        log_event("INFO", f"Successfully synced state details for transaction.")
        return charge
    except stripe.error.StripeError as e:
        log_event("ERROR", f"Stripe Provider Network Rejection: {e}")
        return None
    except Exception as e:
        log_event("ERROR", f"Unexpected structural runtime breakdown: {e}")
        return None


# ==================== DATABASE SCRIPT SECTION ====================
def log_transaction_to_db(user_id, amount, status):
    # WHY: We write results to SQLite to verify database state matches the API payment state.
    # WHAT COULD BREAK: If DB path is wrong or SQLite file is locked, it raises OperationalError.
    # Fix: Ensure database directory path exists in config.py.
    db_path = config.DATABASE_PATH
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        # WHY: We use parameterized queries (?) to protect the script against SQL Injection security risks.
        cursor.execute(
            "INSERT INTO transactions (user_id, amount, status) VALUES (?, ?, ?)",
            (user_id, amount, status)
        )
        # WHY: Explicitly committing saves changes to disk. Without this, changes are lost when connection closes.
        conn.commit()
        log_event("INFO", f"Successfully logged txn to database for User: {user_id}")
        return True
    except sqlite3.Error as e:
        # WHY: Rollback reverts any half-written changes if the transaction fails midway, avoiding database corruption.
        conn.rollback()
        log_event("ERROR", f"Database transaction failed: {e}")
        return False
    finally:
        # WHY: We must close the connection to prevent memory leaks and database file locks.
        conn.close()