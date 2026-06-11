# Import required libraries
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Initializing Chrome WebDriver...")
driver = webdriver.Chrome()

# Set up smart wait for 10 seconds
wait = WebDriverWait(driver, 10)

try:
    # Initialize browser and navigate to site
    print("Navigating to SauceDemo...")
    driver.get("https://www.saucedemo.com")

    # Login to account
    print("Loging in...")
    username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    username_field.send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Fill checkout form and submit
    print("Filling checkout form...")
    driver.get("https://www.saucedemo.com/checkout-step-one.html")
    driver.find_element(By.ID, "first-name").send_keys("Alex")
    driver.find_element(By.NAME, "lastName").send_keys("Tester")
    driver.find_element(By.ID, "postal-code").send_keys("0101")
    driver.find_element(By.ID, "continue").click()

    # Verify if the next page loaded successfully
    print("Verifying payment step...")
    try:
        # We wait for the page title element to appear
        success_msg = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "title")))
        print("✓ Payment step succeeded")

        # Take screenshot of success result
        driver.save_screenshot("day68_success.png")
        print("Screenshot saved!")
    except:
        print("✗ Payment step failed or timed out")

except Exception as e:
    # Main error handling
    print(f"System Error: {e}")

finally:
    # Close browser session
    print("Closing browser...")
    driver.quit()