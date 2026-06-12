# Import libraries and our custom helpers
import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Look one folder up to find selenium_utils.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium_utils import login_to_site, fill_checkout_form, verify_checkout_result

print("Initializing Chrome WebDriver...")
driver = webdriver.Chrome()

try:
    # Open site
    print("Navigating to SauceDemo...")
    driver.get("https://www.saucedemo.com")

    # Use helper to login
    print("Logging in using helper...")
    login_to_site(driver, "standard_user", "secret_sauce")
    time.sleep(2)

    # Use helper to go to checkout and fill form
    print("Filling checkout form using helper...")
    driver.get("https://www.saucedemo.com/checkout-step-one.html")
    fill_checkout_form(driver, "Alex", "Tester", "0101")

    # Click continue button
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)

    # Use helper to verify result
    print("Verifying result using helper...")
    if verify_checkout_result(driver):
        print("✓ Payment step succeeded")
        driver.save_screenshot("day69_success.png")
        print("Screenshot saved!")
    else:
        print("✗ Payment step failed or timed out")

except Exception as e:
    print(f"System Error: {e}")

finally:
    # Close browser
    print("Closing browser...")
    driver.quit()