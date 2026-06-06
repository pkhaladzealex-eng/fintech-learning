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


    print("\n[Interacting with Form Fields...]")


    first_name_field = driver.find_element(By.ID, "first-name")
    first_name_field.send_keys("Alex")
    print("-> Entered First Name: Alex")


    last_name_field = driver.find_element(By.NAME, "lastName")
    last_name_field.send_keys("Pkhaladze")
    print("-> Entered Last Name: Pkhaladze")


    postal_code_field = driver.find_element(By.ID, "postal-code")
    postal_code_field.send_keys("0101")
    print("-> Entered Postal/Billing Code: 0101")


    time.sleep(3)


    output_img = "filled_checkout_form.png"
    print(f"\nCapturing filled form state programmatically as {output_img}...")
    driver.save_screenshot(output_img)
    print("Automated screenshot of filled form saved successfully.")

except Exception as e:
    print(f"Execution Error during form interaction: {e}")

finally:

    print("\nClosing browser lifecycle...")
    driver.quit()