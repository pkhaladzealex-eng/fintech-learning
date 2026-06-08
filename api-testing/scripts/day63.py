import time
from selenium import webdriver

print("Initializing Chrome WebDriver...")
driver = webdriver.Chrome()

try:
    print("Navigating to Stripe Login Page...")
    driver.get("https://dashboard.stripe.com/login")
    
    print("Waiting for page elements to render...")
    time.sleep(5)
    
    output_filename = "stripe_dashboard.png"
    print(f"Capturing screenshot programmatically as {output_filename}...")
    driver.save_screenshot(output_filename)
    
    print("Screenshot saved successfully!")

except Exception as e:
    print(f"An error occurred during automation: {e}")

finally:
    print("Closing the automated browser session...")
    driver.quit()
