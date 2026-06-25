import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("Initializing webdriver")
driver = webdriver.Chrome()

try:
    print("Navigating to Saucedemo Login page...")
    driver.get("https://www.saucedemo.com")
    time.sleep(5)


    print("Entering authentication credentials...")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(5)

    print("Navigating to Checkout Form...")
    driver.get("https://www.saucedemo.com?checkout-step-one/html")
    time.sleep(5)

    print("\n[Locating Form Fields Elements...]")

    first_name_field = driver.find_element(By.ID, "first-name")
    last_name_field = driver.find_element(By.ID, "last-name")
    postal_code_field = driver.find_element(By.ID, " postal-code")
except Exception as e:
    print(e)

finally:
    driver.quit()