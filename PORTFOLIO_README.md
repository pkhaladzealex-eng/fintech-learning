# Fintech Payment Testing Automation Suite

### 1. Project Title
Fintech Payment Testing Automation Suite

### 2. What It Does
This repository contains automated tests for a fintech payment platform. It tests user interface flows, covers API validation for credit card processing, and verifies that payment logs are correctly stored inside the database. The suite ensures that the entire system works correctly from end to end.

### 3. Tech Stack
* **Language:** Python 3
* **UI Testing:** Selenium WebDriver
* **Framework:** Pytest
* **Payment API:** Stripe API
* **Database:** SQLite3

### 4. Folder Structure
* `api-testing/tests/` - Contains all automated test files (UI, API, and Integration tests).
* `api-testing/scripts/` - Contains reusable helper functions and automation utility configurations.
* `config.py` - Stores global configuration variables, database paths, and API credentials.
* `utils.py` - Stores secure back-end functions and transactional assertion scripts.

### 5. How To Run
1. Clone this repository to your local computer.
2. Set up your environment variable for Stripe:
   ```bash
   export STRIPE_API_KEY="your_test_key_here"
   ```
Install dependencies:

```bash
pip install selenium pytest stripe
```
Run all tests:

```bash
python3 -m pytest api-testing/tests/ -v -s
```
### 6. Key Features
End-to-End Pipeline: Combines browser interaction, external API integration, and database queries in one single test script.

Page Object Design: Uses dedicated helper utilities to log into websites and navigate forms dynamically.

Negative Assertions: Includes test cases that purposefully enter invalid inputs to check that system forms show validation errors.

Strict Logs: Records every info and error milestone cleanly to terminal windows and internal log archives.

### 7. What I Learned
Explicit Waits: I learned that using WebDriverWait is much better than freezing tests with time.sleep(), because it makes automation dynamic and stable.

Integration Logic: I discovered how to fetch transactional metadata from Stripe backend logs to cross-reference payment states with local storage.

Structural Paths: I realized the importance of handling system imports correctly using python path insertions before script execution.

Error Prevention: I learned how to handle exceptions defensively using try/except architectures to stop automation frameworks from crashing instantly.
