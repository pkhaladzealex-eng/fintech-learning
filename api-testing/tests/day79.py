import os
import sys
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Setup path strictly BEFORE importing custom files
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



def test_complete_shopping_flow(driver):
    print("\n[Test] Running: test_complete_shopping_flow...")

    driver.get("https://www.saucedemo.com")
    login_to_site(driver, "standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

    add_products_to_cart(driver)

    navigate_to_checkout(driver)
    assert "checkout-step-one" in driver.current_url

    fill_checkout_form(driver, "John", "Doe", "12345")
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

    print("[Test] Submitting checkout form with invalid data (Empty First Name)...")
    fill_checkout_form(driver, "", "Doe", "abc")

    try:
        error_element = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        assert error_element.is_displayed(), "Error message should be visible"
        print(f"✓ Validation error caught: {error_element.text}")
    except:
        pytest.fail("Expected error message not found - form may have submitted incorrectly")

    assert "checkout-step-one" in driver.current_url, "Page should NOT advance with invalid data"


    driver.save_screenshot("day79-checkout-error.png")
