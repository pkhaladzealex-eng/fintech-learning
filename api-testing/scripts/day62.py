from selenium import webdriver
from selenium.webdriver.chrome.service import Service


print("Initializing Chrome WebDriver...")
driver = webdriver.Chrome()

try:

    print("Navigating to Google...")
    driver.get("https://www.google.com")


    print("Page title parsed successfully:")
    print("-" * 30)
    print("Page title:", driver.title)
    print("-" * 30)

finally:
    
    print("Closing the browser session...")
    driver.quit()