import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    print("\n[Global Setup] Starting a single Chrome Browser session for all tests...")
    d = webdriver.Chrome()
    yield d
    print("\n[Global Cleanup] Closing the global Chrome Browser session...")
    d.quit()
@pytest.fixture(autouse=True)
def clean_browser_state(driver):

    yield

    try:
        driver.delete_all_cookies()
        driver.get("about:blank")
    except Exception:
        pass