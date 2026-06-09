import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("Initializing Chrome webdriver...")
driver = webdriver.Chrome()
try:
    print("Navigating to Login page...")
    driver.get("https://www.saucedemo.com")
    time.sleep(2)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)



    driver.get("https://www.saucedemo.com/checkout-step-one.html")
    time.sleep(2)
    driver.find_element(By.ID, "first-name").send_keys("Alex")
    driver.find_element(By.NAME, "lastName").send_keys("Tester")
    driver.find_element(By.ID, "postal-code").send_keys("0101")
    time.sleep(2)

    driver.find_element(By.ID, "continue").click()
    time.sleep(2)

    driver.save_screenshot("checkout_commplete.png")

    result_text = driver.find_element(By.CLASS_NAME, "title").text
    print("Payment Step result:", result_text)
except Exception as e:
    print(f'An Error occurred during automation: {e}')
finally:
    print("Closing browser lifecycle...")
    driver.quit()
