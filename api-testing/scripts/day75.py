import time
from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("https://web.whatsapp.com/")
    time.sleep(15)

    output_filename = "day75.png"
    driver.save_screenshot(output_filename)

except Exception as e:
    print(e)
finally:
    driver.quit()

