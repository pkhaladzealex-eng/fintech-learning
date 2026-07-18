# Day 89: Mock Interview Scenario

This document contains a full practice interview conversation. It covers real-world automation, manual testing logic, and technical challenge questions using simple and clear answers.

---

### Q1: Tell me about yourself and your background.
* **Interviewer:** "Tell me about yourself and your background."
* **Me:** "I am a QA Automation Engineer. I am 39 years old, and I recently made a career transition from factory operations into the tech industry. For the past 89 days, I have been coding every single day, learning Python, Selenium, Pytest, and databases. I also do crowdsourced testing on uTest, where I have already reached a Bronze Rated status by testing real apps."

### Q2: Walk me through your biggest project.
* **Interviewer:** "Walk me through your biggest project."
* **Me:** "My main project is an automated payment testing suite for a fintech shop. The script opens the web store, logs in, adds products to the cart, and fills out the checkout form. After submission, it securely checks the Stripe API backend to verify the payment status and then checks our local database to ensure the transaction record is logged perfectly."

### Q3: Explain the architecture of your automation suite.
* **Interviewer:** "Explain the architecture of your automation suite."
* **Me:** "I split my code into three clean layers to keep it simple. First, `config.py` holds all paths and keys. Second, `utils.py` handles general functions like SQLite database connections and Stripe API network requests. Finally, `selenium_utils.py` contains reusable UI browser flows, and the actual test execution runs inside Pytest scripts."

### Q4: What was your biggest technical challenge in this project?
* **Interviewer:** "What was your biggest technical challenge in this project?"
* **Me:** "My biggest challenge was test instability caused by slow network loading. Sometimes the automation script looked for a web button before the web page completely finished loading, causing the tests to crash. I solved this by removing all blind pauses and replacing them with flexible explicit waits using `WebDriverWait`."

### Q5: How do you protect sensitive data like Stripe API keys in your code?
* **Interviewer:** "How do you protect sensitive data like Stripe API keys in your code?"
* **Me:** "I never hardcode private passwords or secret API keys directly inside my source code. Instead, I store them safely inside a hidden local `.env` environment file. Then, I use Python's built-in `os.environ` module to read these secret tokens directly into memory when the automation runs."

### Q6: Tell me about a critical bug you found and how you reported it.
* **Interviewer:** "Tell me about a critical bug you found and how you reported it."
* **Me:** "While doing exploratory testing on the Citymapper app, I found a UI freeze. When searching for a city on an iPhone 16e, typing exactly three characters—like 'Rok'—caused the app to lock on a solid green screen. I reported this bug with clear environment details, exact reproduction steps, and screenshots showing that a hard restart was required."

### Q7: What would you do if an automated test fails randomly on CI/CD?
* **Interviewer:** "What would you do if an automated test fails randomly on CI/CD?"
* **Me:** "First, I check the automated log file and screenshots taken at the moment of the crash to see if a random pop-up or modal blocked the page. Second, I check if it is a timing issue. If the server was running slow, I increase the explicit wait time limit to give the UI elements more time to render safely."

### Q8: Why is database validation important in payment testing?
* **Interviewer:** "Why is database validation important in payment testing?"
* **Me:** "Testing only the user interface is dangerous because a web browser can show a successful checkout screen even if the backend database fails to save the data. Database validation checks the actual table records to confirm that the customer's user ID, payment amount, and currency match the real charge perfectly."

### Q9: How has your experience on uTest helped you as an automation engineer?
* **Interviewer:** "How has your experience on uTest helped you as an automation engineer?"
* **Me:** "uTest gives me real-world practice with different mobile devices, production environments, and actual release cycles. It taught me how to find logical edge cases, write professional bug reports, and think like a real user. This manual testing experience helps me know exactly what parts of an app are most important to automate."

### Q10: How would you improve your current testing project in the future?
* **Interviewer:** "How would you improve your current testing project in the future?"
* **Me:** "I want to set up an automated CI/CD pipeline using GitHub Actions so my tests run automatically every time code changes. I also plan to add mobile automation using Appium to test mobile payment interfaces, and add load testing to see how the checkout handles many users at the same time."