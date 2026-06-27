from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
     #Initializing webdriver
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")
    print(driver.current_url)
    time.sleep(3)


     #Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(3)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(3)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    print(driver.current_url)
    assert "inventory" in driver.current_url
    print("Logged in")

     #Add product to the cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(3)
    print("Backpack added to the cart")

     #Open the cart page
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(3)
    print(driver.current_url)
    assert "cart.html" in driver.current_url
    print("Cart Page Opened")

     #Click on checkout button
    driver.find_element(By.ID, "checkout").click()
    time.sleep(3)
    print(driver.current_url)
    assert "checkout-step-one" in driver.current_url
    print("Checkout page opened")

     #Enter checkout information
    driver.find_element(By.ID, "first-name").send_keys("John")
    time.sleep(3)
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    time.sleep(3)
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    time.sleep(3)
    print("Checkout information entered")

     #Click on continue
    driver.find_element(By.ID, "continue").click()
    time.sleep(3)
    print(driver.current_url)
    assert "checkout-step-two" in driver.current_url
    print("Checkout overview page opened")

     #Click finish
    driver.find_element(By.ID,"finish").click()
    time.sleep(2)
    print(driver.current_url)
    assert "checkout-complete" in driver.current_url
    print("Checkout completed")

    message = driver.find_element(By.CLASS_NAME, "complete-header").text
    print(message)
    assert message == "Thank you for your order!"
    print("Success message verified")

     #Screenshot
    driver.save_screenshot("day76-checkout-complete.png")
    print("Screenshot saved")

except Exception as e:
    print(e)

finally:
    driver.quit()









