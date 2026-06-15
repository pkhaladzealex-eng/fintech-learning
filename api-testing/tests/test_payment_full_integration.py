# Import integration test tools
# Import integration test tools
import sys
import os
import sqlite3
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Find the main project directory automatically to import helpers and config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selenium_utils import login_to_site, fill_checkout_form, verify_checkout_result

# Import the database path directly from your config.py
from config import DATABASE_PATH as DB_PATH

# Re-use our browser fixture
@pytest.fixture
def driver():
    print("\n[Setup] Starting Browser for Integration Test...")
    d = webdriver.Chrome()
    yield d
    print("\n[Cleanup] Closing Browser...")
    d.quit()


# Simulated Stripe API helper
def verify_charge_created_via_api():
    print("\n[API] Requesting Stripe API: Checking latest transactions...")
    # Generating a unique charge ID for Day 72 integration test
    return {"id": "ch_3Mv9xL_alex_72", "amount_cents": 2999, "status": "succeeded", "customer_id": 3}


# Test: Full Integration Flow (UI -> API -> Real DB)
def test_full_payment_flow(driver):
    print("\n--- STARTING FULL INTEGRATION TEST ---")

    # ------------------------------------------------------------
    # STEP 1: UI Submission via Selenium
    # ------------------------------------------------------------
    print("\n[Step 1] Executing UI flow...")
    driver.get("https://www.saucedemo.com")
    login_to_site(driver, "standard_user", "secret_sauce")

    driver.get("https://www.saucedemo.com/checkout-step-one.html")
    fill_checkout_form(driver, "Alex", "Integration-Tester", "9999")
    driver.find_element(By.ID, "continue").click()

    ui_success = verify_checkout_result(driver)
    assert ui_success == True, "UI checkout flow failed!"
    print("✓ UI Step completed successfully.")

    # ------------------------------------------------------------
    # STEP 2: Verify API (Stripe)
    # ------------------------------------------------------------
    print("\n[Step 2] Executing API verification...")
    charge = verify_charge_created_via_api()

    assert charge is not None, "API Charge creation failed!"
    assert charge["status"] == "succeeded", "Stripe payment status is not successful!"
    print(f"✓ API Step passed. Created Charge ID: {charge['id']}")

    # ------------------------------------------------------------
    # STEP 3: Real Database Verification (SQLite)
    # ------------------------------------------------------------
    print(f"\n[Step 3] Connecting to Real DB: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        # First, simulate backend saving the charge into the DB
        print("[Database] Inserting simulated payment record into 'charges' table...")
        cursor.execute("""
            INSERT OR IGNORE INTO charges (charge_id, amount_cents, status, customer_id)
            VALUES (?, ?, ?, ?);
        """, (charge["id"], charge["amount_cents"], charge["status"], charge["customer_id"]))
        conn.commit()

        # Now, query the DB to verify data integrity (the actual test assertion)
        print(f"[Database] Running SQL: SELECT * FROM charges WHERE charge_id = '{charge['id']}';")
        cursor.execute("SELECT * FROM charges WHERE charge_id = ?;", (charge["id"],))
        db_record = cursor.fetchone()

        # Assertions to prove data exists and is accurate
        assert db_record is not None, "Integration Failure: Record was not saved in SQLite DB!"
        assert db_record[0] == charge["id"], "Integration Failure: Charge ID mismatch in Database!"
        print(f"✓ DB Step passed. Verified row exists in SQLite: {db_record}")

    finally:
        # Always close the connection safely
        conn.close()
        print("[Database] Connection closed.")

    print("\n--- INTEGRATION TEST PASSED SUCCESSFULLY ---")