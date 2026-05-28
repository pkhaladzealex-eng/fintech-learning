import logging
import stripe
import json
import os

# Get the exact absolute path of the api-testing folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE_PATH = os.path.join(BASE_DIR, 'logs', 'payment_logs.txt')

# Setup logging configuration dynamically using the absolute target path
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_event(level, message):
    """Reusable function to pipeline clean logs both to file and console."""
    if level.upper() == "INFO":
        logging.info(message)
        print(f"ℹ️ INFO: {message}")
    elif level.upper() == "ERROR":
        logging.error(message)
        print(f"❌ ERROR: {message}")

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

def fetch_charge_safe(charge_id):
    """Defensive handler executing safe provider network synchronization requests."""
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
