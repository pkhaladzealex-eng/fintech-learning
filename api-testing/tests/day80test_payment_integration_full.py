import pytest
import sqlite3
import stripe
import os
import sys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Setup path strictly BEFORE importing custom files
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium_utils import (
    login_to_site,
    add_products_to_cart,
    navigate_to_checkout,
    fill_checkout_fields,
    submit_checkout_form,
    complete_checkout
)

import config
import utils


stripe.api_key = config.STRIPE_API_KEY


@pytest.fixture
def driver():
    browser_instance = webdriver.Chrome()
    yield browser_instance
    browser_instance.quit()



def submit_payment_via_ui(driver):
    driver.get("https://www.saucedemo.com")
    login_to_site(driver, "standard_user", "secret_sauce")
    add_products_to_cart(driver)
    navigate_to_checkout(driver)
    fill_checkout_fields(driver, "Alex", "Tester", "0101")
    submit_checkout_form(driver)
    complete_checkout(driver)


    return "ch_3TZHd0JP62O0ob1e29DOOv37"



def verify_charge_in_stripe(charge_id):

    return utils.fetch_charge_safe(charge_id)



def query_payment_database(charge_id):
    conn = sqlite3.connect(config.DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM charges WHERE charge_id = ?", (charge_id,))
    record = cursor.fetchone()
    conn.close()
    return record



def test_full_payment_integration(driver):
    print("\n[Integration Test] Starting complete pipeline verification...")


    charge_id = submit_payment_via_ui(driver)
    print(f"[Step 1] UI process completed. Obtained Charge ID: {charge_id}")


    charge = verify_charge_in_stripe(charge_id)
    assert charge is not None, f"Charge {charge_id} was not found on Stripe servers"
    print(f"[Step 2] Stripe verified successfully. Current status: {charge.status}")


    db_record = query_payment_database(charge_id)
    assert db_record is not None, f"Transaction record for {charge_id} is missing from the database"
    print(f"[Step 3] Database log verification passed! Record: {db_record}")