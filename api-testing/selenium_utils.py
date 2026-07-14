from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 1. User login action
def login_to_site(driver, username, password):
    # WHY: We use an explicit wait of 10s instead of time.sleep().
    # It dynamically checks the page and moves forward the millisecond the input is ready.
    # WHAT COULD BREAK: If the login page is extremely slow to load (> 10s),
    # it throws a TimeoutException. Fix: Increase wait time limit in config.
    wait = WebDriverWait(driver, 10)

    # WHY: We use By.ID because ID attributes are highly stable in CSS layouts
    # and do not break when HTML design changes.
    username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    username_field.send_keys(username)

    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


# 2. Add specific test products to the shopping basket
def add_products_to_cart(driver):
    wait = WebDriverWait(driver, 10)

    # WHY: We wait for the exact product buttons to be present before clicking.
    # On dynamic sites, buttons can be disabled or unclickable for the first fraction of a second.
    # WHAT COULD BREAK: If a product ID is changed in the store catalogue,
    # the wait will timeout. Fix: Update locator IDs.
    backpack = wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack")))
    backpack.click()

    bike_light = wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-bike-light")))
    bike_light.click()


# 3. Navigate directly to the checkout section
def navigate_to_checkout(driver):
    wait = WebDriverWait(driver, 10)

    # WHY: We click the cart icon first to trigger the session checkout state in the browser.
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    checkout_btn = wait.until(EC.presence_of_element_located((By.ID, "checkout")))
    checkout_btn.click()


# 4. Fill in customer checkout data
def fill_checkout_fields(driver, first_name, last_name, postal_code):
    wait = WebDriverWait(driver, 10)

    # WHY: We wait for the first-name field to ensure the form transition animation has finished.
    # Typing into animating or half-rendered fields can lead to lost keystrokes.
    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys(first_name)
    wait.until(EC.presence_of_element_located((By.ID, "last-name"))).send_keys(last_name)
    wait.until(EC.presence_of_element_located((By.ID, "postal-code"))).send_keys(postal_code)


# 5. Submit customer form to proceed
def submit_checkout_form(driver):
    wait = WebDriverWait(driver, 10)
    # WHY: We wait for the button to be 'clickable' instead of just 'present'.
    # This avoids clicking errors if an animation is still blocking the button.
    wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()


# 6. Complete purchase transaction
def complete_checkout(driver):
    wait = WebDriverWait(driver, 10)
    finish_btn = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
    finish_btn.click()