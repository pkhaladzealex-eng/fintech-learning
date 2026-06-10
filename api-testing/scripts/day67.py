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
    print("Navigating to SauceDemo...")
    driver.get("https://www.saucedemo.com")

    print("Waiting for username field...")
    # NOTE: WebDriverWait is better than time.sleep().
    # It stops waiting immediately when element appears.
    # It saves testing time and prevents errors.
    username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    username_field.send_keys("standard_user")

    # Login to account
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Wait 2 seconds to see the page
    time.sleep(2)

    # Take screenshot
    output_filename = "day67_smart_wait.png"
    driver.save_screenshot(output_filename)
    print("Screenshot saved!")

except Exception as e:
    print(f"Error: {e}")

finally:
    print("Closing browser...")
    driver.quit()