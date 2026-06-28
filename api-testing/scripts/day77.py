import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Initializing Chrome  WebDriver")
driver  = webdriver.Chrome()

# Set up smart wait for 10 seconds
wait = WebDriverWait(driver,10)

try:
    print("Navigating to Sauce Demo")
    driver.get("https://www.saucedemo.com")
    print(driver.current_url)


    # Login
    username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    username_field.send_keys("standard_user")
    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    print(driver.current_url)
    assert "inventory" in driver.current_url
    print("logged in")

    # Add product
    add_product = wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack")))
    add_product.click()
    print("Backpack added to the cart")

    add_product2 = wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-bike-light")))
    add_product2.click()
    print("Bike Light  added to the cart")

    # Open the cart page
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    print(driver.current_url)
    assert "cart.html" in driver.current_url
    print("Cart page opened")



    # Click on checkout button
    cart = wait.until(EC.presence_of_element_located((By.ID, "checkout")))
    cart.click()
    print(driver.current_url)
    assert "checkout-step-one" in driver.current_url
    print("Checkout page opened")

   # Enter checkout information
    first_name = wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
    first_name.send_keys("John")
    last_name = wait.until(EC.element_to_be_clickable((By.ID, "last-name")))
    last_name.send_keys("Doe")
    postal_code = wait.until(EC.element_to_be_clickable((By.ID, "postal-code")))
    postal_code.send_keys("12345")
    print("Checkout information entered")

    # Continue
    continue_button = wait.until(EC.presence_of_element_located((By.ID, "continue")))
    continue_button.click()
    print(driver.current_url)
    assert "checkout-step-two" in driver.current_url
    print("Checkout page opened")

    # Finish
    finish = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
    finish.click()
    print(driver.current_url)
    assert "checkout-complete" in driver.current_url
    print("Checkout completed")

    message = driver.find_element(By.CLASS_NAME, "complete-header").text
    print(message)
    assert message == "Thank you for your order!"
    print("Success message verified")

    # Screenshot
    driver.save_screenshot("day77-checkout-complete.png")
    print("Screenshot saved")



except Exception as e:
    print(f'Exception:{e}')
finally:
    driver.quit()



