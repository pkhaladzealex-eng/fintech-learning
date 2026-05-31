import hashlib
import sqlite3
import sys
import os

# Append parent directory to path so python can locate utils and config modules flawlessly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils
import config


def process_webhook_failure_secured(charge_id, customer_email, customer_id, raw_error_message):
    print("--- Day 59: Secure Data Masking & Telemetry Pipeline ---")

    # 1. SECURITY: Hash the charge_id using SHA-256 (One-way cryptographic transformation)
    # This ensures the real Stripe Charge ID is never exposed in flat files.
    hashed_charge_id = hashlib.sha256(charge_id.encode()).hexdigest()

    # 2. SECURITY: Extract strict Error Code only, discard sensitive/raw trace details
    # Example: "Card Declined: Insufficient Funds on Visa 4242" -> becomes -> "CARD_DECLINED"
    if "Declined" in raw_error_message or "decline" in raw_error_message.lower():
        secure_error_code = "ERR_PAYMENT_DECLINED"
    elif "API Key" in raw_error_message or "key" in raw_error_message.lower():
        secure_error_code = "ERR_AUTH_INVALID_KEY"
    else:
        secure_error_code = "ERR_GENERIC_INTERNAL_FAIL"

    # 3. PREPARE DATA VERSIONS:
    # Safe version for persistent log file storage (Hashed ID, No Email, Code only)
    safe_log_message = (
        f"Webhook Failure intercepted | "
        f"Hashed_ID: {hashed_charge_id[:15]}... | "
        f"Cust_ID: {customer_id} | "
        f"Code: {secure_error_code}"
    )

    # Full version for Local Console Debugging ONLY (Exposes raw data for QA root-cause discovery)
    full_console_debug = (
        f"   [LOCAL DEBUG] Live Failure Context Details:\n"
        f"   • Real Charge ID : {charge_id}\n"
        f"   • Customer Email : {customer_email}\n"
        f"   • Database Target: {customer_id}\n"
        f"   • Raw Trace Log  : {raw_error_message}\n"
    )

    # 4.  DIVERGENT PIPELINE ROUTING:
    # Output FULL sensitive context exclusively to the screen (Console)
    print(full_console_debug)

    # Write MASKED/SAFE metadata dynamically to the payment_logs.txt file via utils
    utils.log_event("ERROR", f"SECURE-MASK: {safe_log_message}")


if __name__ == "__main__":
    # Mock data context representing a sensitive failed webhook arrival event
    sensitive_charge_id = "ch_3TZHd0JP62O0ob1e29DOOv37"
    sensitive_email = "qaengineeralexander+john@gmail.com"
    sensitive_cust_id = "cus_UGdGpL2aG13kxG"
    sensitive_raw_error = "Stripe Provider Network Rejection: Invalid API Key provided: st_test_**********2345"

    process_webhook_failure_secured(
        charge_id=sensitive_charge_id,
        customer_email=sensitive_email,
        customer_id=sensitive_cust_id,
        raw_error_message=sensitive_raw_error
    )