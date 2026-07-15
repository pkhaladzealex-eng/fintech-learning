Markdown
# Deployment and Execution Guide

This guide contains step-by-step instructions on how to set up and run the Fintech Payment Testing Automation Suite on your local machine.

---

## 1. Prerequisites

Before installing the project, make sure you have the following software installed:

* **Python:** Version 3.8 or higher.
* **Google Chrome:** The latest stable version of the Chrome browser.
* **Operating System:** macOS, Windows, or Linux.
* **Git:** Installed on your machine to clone the repository.

---

## 2. Installation Steps

Follow these exact terminal commands to clone and set up the project environment:

1. **Clone the repository:**

```bash
git clone [https://github.com/pkhaladzealex-eng/fintech-learning.git](https://github.com/pkhaladzealex-eng/fintech-learning.git)
```
Navigate to the project folder:

```Bash
cd fintech-learning
```
Install the required Python packages:

```Bash
pip install selenium pytest stripe
```
Set up your environment variable for Stripe API:

On macOS/Linux:

```Bash
export STRIPE_API_KEY="your_test_key_here"
```

On Windows (Command Prompt - CMD):

```DOS
set STRIPE_API_KEY="your_test_key_here"
```

On Windows (PowerShell):

```PowerShell
$env:STRIPE_API_KEY="your_test_key_here"
```

3. Running Tests
To run the entire automated testing suite, execute the following command in your terminal:

```Bash
python3 -m pytest api-testing/tests/ -v -s
```

4. Expected Output
When you run the tests successfully, Pytest will output a detailed log in the terminal. A successful run should look like this:

```Plaintext
api-testing/tests/test_checkout_flow.py::test_successful_checkout PASSED [ 50%]
api-testing/tests/test_payment_verification.py::test_stripe_and_db_sync PASSED [100%]

========================== 2 passed in 12.45s ==========================
```
Additionally, a local log file will be generated or updated inside the logs directory:
`api-testing/logs/payment_logs.txt`

5. Troubleshooting Common Errors
Here are the 4 most common issues you might run into and how to quickly solve them:

Error 1: ModuleNotFoundError (No module named 'pytest' or 'selenium')
Why it happens: The required Python packages are not installed in your current Python environment.

How to fix: Simply run `pip install selenium pytest stripe` again. If you are using a virtual environment, make sure it is activated.

Error 2: Stripe API Key Missing / AuthenticationError
Why it happens: The code cannot find the Stripe API key because the environment variable was not set correctly.

How to fix: Run the `export STRIPE_API_KEY="your_key"` command in the exact same terminal window where you are running the tests.

Error 3: Database Connection / sqlite3.OperationalError
Why it happens: The database path defined in `config.py` does not exist on your computer.

How to fix: Open `config.py` and update the `DATABASE_PATH` variable to match the correct location of your local `fintech_main.db` file.

Error 4: ChromeDriver / SessionNotCreatedException
Why it happens: Your Chrome browser version is too new or too old for the installed Selenium driver configuration.

How to fix: Update Google Chrome to the latest version. Modern Selenium versions automatically download the matching driver, so updating Chrome usually fixes this instantly.

6. Project Structure
Here is a quick overview of how this repository is organized:

`api-testing/tests/` - Contains all automated Pytest scripts (UI and API).

`api-testing/scripts/`- Contains helper files like `selenium_utils.py`.

`global_data/` - Holds the SQLite `fintech_main.db` database file.

`config.py` - Central configuration file for paths and parameters.

`utils.py` - Reusable utility functions for Stripe API and logging.