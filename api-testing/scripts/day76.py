import time
from selenium import webdriver
from selenium.webdriver.common.by import By


print("Initializing Chrome WebDriver")
driver = webdriver.Chrome()

try:

    print("Navigating to SauceDemo Login Page")
    driver.get("https://www.saucedemo.com")
    time.sleep(3)

    print("Entering authentification credentials")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.CLASS_NAME, "login_logo").text

    login_button = driver.find_element(By.CLASS_NAME, "submit-button")
    print(f"Find element by CLASS: {login_button.get_attribute('type')}")


    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    print("Navigating to Checkout Form")
    driver.get("https://www.saucedemo.com/checkout-step-one.html")
    time.sleep(3)

except Exception as e:
    print(f"Execution Error: {e}")

finally:
    print("Closing browser")
    driver.quit()




