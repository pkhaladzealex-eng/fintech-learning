from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Helper to login to SauceDemo
def login_to_site(driver, username, password):
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    username_field.send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

# Helper to fill checkout form
def fill_checkout_form(driver, first_name, last_name, postal_code):
    driver.find_element(By.ID, "first-name").send_keys(first_name)
    driver.find_element(By.NAME, "lastName").send_keys(last_name)
    driver.find_element(By.ID, "postal-code").send_keys(postal_code)

# Helper to verify checkout success
def verify_checkout_result(driver):
    wait = WebDriverWait(driver, 10)
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "title")))
        return True
    except:
        return False