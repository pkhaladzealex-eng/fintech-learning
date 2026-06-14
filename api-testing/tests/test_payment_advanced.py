# Import test framework and tools
import sys
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Find the main project directory automatically to import selenium_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selenium_utils import login_to_site, fill_checkout_form, verify_checkout_result


# Setup and Cleanup browser session using pytest fixture
@pytest.fixture
def driver():
    print("\n[Setup] Opening Chrome Browser...")
    d = webdriver.Chrome()

    yield d  # This provides the driver instance to our tests

    print("\n[Cleanup] Closing Chrome Browser...")
    d.quit()


# Test 1: Successful checkout using driver fixture
def test_payment_success(driver):
    print("Running: test_payment_success...")

    # 1. Open site and login
    driver.get("https://www.saucedemo.com")
    login_to_site(driver, "standard_user", "secret_sauce")

    # 2. Go to checkout and fill form
    driver.get("https://www.saucedemo.com/checkout-step-one.html")
    fill_checkout_form(driver, "Alex", "Tester", "0101")
    driver.find_element(By.ID, "continue").click()

    # 3. Assert result
    result = verify_checkout_result(driver)
    assert result == True


# Test 2: Declined checkout using driver fixture
def test_payment_failed(driver):
    print("Running: test_payment_failed...")

    # 1. Open site and login with wrong password
    driver.get("https://www.saucedemo.com")
    login_to_site(driver, "standard_user", "wrong_password")

    # 2. Try to go to checkout
    driver.get("https://www.saucedemo.com/checkout-step-one.html")

    # 3. Assert result (should be False)
    result = verify_checkout_result(driver)
    assert result == False