import os
import sys
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium_utils import (
    login_to_site,
    add_products_to_cart,
    navigate_to_checkout,
    fill_checkout_form,
    complete_checkout
)


@pytest.fixture
def driver():
    print("\n[Fixture] Initializing Chrome WebDriver...")
    browser_instance = webdriver.Chrome()
    yield browser_instance
    print("\n[Fixture] Closing Chrome WebDriver...")
    browser_instance.quit()


# Test 1
def test_complete_shopping_flow(driver):
    print("\n[Test] Running: test_complete_shopping_flow...")

    driver.get("https://www.saucedemo.com")
    login_to_site(driver, "standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

    add_products_to_cart(driver)
    navigate_to_checkout(driver)
    assert "checkout-step-one" in driver.current_url

    fill_checkout_form(driver, "John", "Doe", "12345")

    print("[Test] Clicking submit button from test...")
    driver.find_element(By.ID, "continue").click()
    assert "checkout-step-two" in driver.current_url

    complete_checkout(driver)
    assert "checkout-complete" in driver.current_url

    success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert success_message == "Thank you for your order!"


def test_checkout_with_invalid_input(driver):
    print("\n[Test] Running: test_checkout_with_invalid_input...")

    driver.get("https://www.saucedemo.com")
    login_to_site(driver, "standard_user", "secret_sauce")

    add_products_to_cart(driver)
    navigate_to_checkout(driver)

    # 1. Fill form fields - Leave first name empty manually
    print("[Test] Filling fields, leaving First Name empty...")
    fill_checkout_form(driver, "", "Doe", "12345")

    # 2. Click submit button
    print("[Test] Clicking submit button ...")
    driver.find_element(By.ID, "continue").click()

    # 3. Then check for error
    try:
        error_element = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        assert error_element.is_displayed(), "Error message should be visible"
        print(f" Validation error caught: {error_element.text}")
    except:
        pytest.fail("Expected error message not found - form may have submitted incorrectly")

    assert "checkout-step-one" in driver.current_url, "Page should NOT advance with invalid data"

    driver.save_screenshot("day79-checkout-error.png")
    print("[Test] Screenshot saved successfully.")