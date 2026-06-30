import os
import sys
import pytest
from selenium import webdriver

# Setup path strictly BEFORE importing custom files
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# შემოვიტანოთ ყველა გამზადებული ფუნქცია სუფთა ტესტისთვის
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

    # 1. საიტზე შესვლა და ავტორიზაცია
    print("[Test] Navigating to Sauce Demo and logging in...")
    driver.get("https://www.saucedemo.com")
    login_to_site(driver, "standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

    # 2. პროდუქტების დამატება (ვიყენებთ ლოკალურ უტილიტას)
    print("[Test] Adding selected items to the cart...")
    add_products_to_cart(driver)

    # 3. კალათაში გადასვლა
    print("[Test] Redirecting to checkout step one...")
    navigate_to_checkout(driver)
    assert "checkout-step-one" in driver.current_url

    # 4. ფორმის შევსება
    print("[Test] Entering shipping details into the form...")
    fill_checkout_form(driver, "John", "Doe", "12345")
    assert "checkout-step-two" in driver.current_url

    # 5. შეკვეთის დასრულება
    print("[Test] Submitting and completing the purchase order...")
    complete_checkout(driver)
    assert "checkout-complete" in driver.current_url

    # 6. სქრინშოტის შენახვა
    driver.save_screenshot("day78-checkout-complete.png")
    print("[Test] Screenshot saved successfully.")