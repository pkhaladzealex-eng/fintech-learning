import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("Initializing Chrome WebDriver...")
driver = webdriver.Chrome()

try:

    print("Navigating to SauceDemo Login Page...")
    driver.get("https://www.saucedemo.com")
    time.sleep(2)


    print("Entering authentication credentials...")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)


    print("Navigating to Checkout Form...")
    driver.get("https://www.saucedemo.com/checkout-step-one.html")
    time.sleep(2)


    print("\n[Locating Form Fields Elements...]")

    first_name_field = driver.find_element(By.ID, "first-name")
    print(f"-> Found Element by ID: {first_name_field.get_attribute('id')}")

    last_name_field = driver.find_element(By.NAME, "lastName")
    print(f"-> Found Element by NAME: {last_name_field.get_attribute('name')}")

    postal_code_field = driver.find_element(By.ID, "postal-code")
    print(f"-> Found Element by ID: {postal_code_field.get_attribute('id')}")


    output_img = "checkout_form_automated.png"
    print(f"\nCapturing form state programmatically as {output_img}...")
    driver.save_screenshot(output_img)
    print("Automated screenshot saved successfully.")

except Exception as e:
    print(f"Execution Error: Could not locate fields. Details: {e}")

finally:

    print("\nClosing browser lifecycle...")
    driver.quit()