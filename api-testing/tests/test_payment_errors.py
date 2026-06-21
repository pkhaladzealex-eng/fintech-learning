# Import testing framework and tools
import sys
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Find the main project directory automatically to import helpers and config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selenium_utils import login_to_site, fill_checkout_form, verify_checkout_result
from config import DATABASE_PATH as DB_PATH



# Test 1: Simulating a declined card scenario
def test_declined_card_payment(driver):
    print("\n--- Running: test_declined_card_payment ---")

    driver.get("https://www.saucedemo.com")
    login_to_site(driver, "standard_user", "secret_sauce")

    # Go to checkout and fill with a mock declined card token name
    driver.get("https://www.saucedemo.com/checkout-step-one.html")
    fill_checkout_form(driver, "tok_chargeDeclined", "Tester", "0000")
    driver.find_element(By.ID, "continue").click()

    # On Swag Labs, any completed form goes through, so we verify we reach step two
    result = verify_checkout_result(driver)
    assert result == True, "Failed to navigate during declined card simulation"
    print("UI handled the submission. API would decline this token.")


# Test 2: Simulating form validation with missing data (Postal Code)
def test_missing_cvv(driver):
    print("\n--- Running: test_missing_cvv ---")

    driver.get("https://www.saucedemo.com")
    login_to_site(driver, "standard_user", "secret_sauce")

    driver.get("https://www.saucedemo.com/checkout-step-one.html")
    # Leaving the postal code (last field) completely empty to trigger error
    fill_checkout_form(driver, "Alex", "Tester", "")
    driver.find_element(By.ID, "continue").click()

    # Assert that the error message container appears on the screen
    error_element = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert error_element.is_displayed(), "Validation error message did not appear!"
    assert "Error: Postal Code is required" in error_element.text
    print(f"✓ Form validation caught the error: {error_element.text}")


# Test 3: Simulating a payment timeout scenario
def test_payment_timeout(driver):
    print("\n--- Running: test_payment_timeout ---")

    driver.get("https://www.saucedemo.com")
    login_to_site(driver, "standard_user", "secret_sauce")

    # Simulate an artificial slow connection timeout threshold (e.g. 2 seconds)
    driver.set_page_load_timeout(2)

    try:
        driver.get("https://www.saucedemo.com/checkout-step-two.html")
        print("Page loaded within the timeout limit.")
    except Exception as e:
        print(f"Timeout handled successfully: Connection took too long.")
        assert "timeout" in str(e).lower()
        # Today is a learning day
        #update daily progress
