from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1.
def login_to_site(driver, username, password):
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    username_field.send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

# 2.
def add_products_to_cart(driver):
    wait = WebDriverWait(driver, 10)

    backpack = wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack")))
    backpack.click()

    bike_light = wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-bike-light")))
    bike_light.click()

# 3.
def navigate_to_checkout(driver):
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    checkout_btn = wait.until(EC.presence_of_element_located((By.ID, "checkout")))
    checkout_btn.click()

# 4.
def fill_checkout_form(driver, first_name, last_name, postal_code):
    wait = WebDriverWait(driver, 10)
    first_name_field = wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
    first_name_field.send_keys(first_name)

    driver.find_element(By.ID, "last-name").send_keys(last_name)
    driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    driver.find_element(By.ID, "continue").click()

# 5.
def complete_checkout(driver):
    wait = WebDriverWait(driver, 10)
    finish_btn = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
    finish_btn.click()