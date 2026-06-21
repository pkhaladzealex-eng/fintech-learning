# Import test framework and tools
import sys
import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Find the main project directory automatically to import selenium_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selenium_utils import login_to_site, fill_checkout_form, verify_checkout_result


# Test 1: Verify successful payment process
def test_payment_success():
    print("\nStarting Test: Payment Success...")
    driver = webdriver.Chrome()

    try:
        # 1. Open site
        driver.get("https://www.saucedemo.com")

        # 2. Login with correct credentials
        login_to_site(driver, "standard_user", "secret_sauce")

        # 3. Go to checkout and fill form
        driver.get("https://www.saucedemo.com/checkout-step-one.html")
        fill_checkout_form(driver, "Alex", "Tester", "0101")
        driver.find_element(By.ID, "continue").click()

        # 4. Check if we reached the next page successfully
        result = verify_checkout_result(driver)

        # Assert that the result is True
        assert result == True

    finally:
        # Always close browser after test
        driver.quit()


# Test 2: Verify failed payment process with wrong login
def test_payment_declined():
    print("\nStarting Test: Payment Declined...")
    driver = webdriver.Chrome()

    try:
        # 1. Open site
        driver.get("https://www.saucedemo.com")

        # 2. Login with WRONG password to trigger failure
        login_to_site(driver, "standard_user", "wrong_password")

        # 3. Try to go to checkout (it will fail because we are not logged in)
        driver.get("https://www.saucedemo.com/checkout-step-one.html")

        # 4. Check result (it should be False because we can't reach the page)
        result = verify_checkout_result(driver)

        # Assert that the result is False
        assert result == False

    finally:
        # Always close browser after test
        driver.quit()