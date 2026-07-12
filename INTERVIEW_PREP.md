# Day 83: Interview Preparation Q&A

### 1. "Walk me through your biggest project."
My biggest project is an end-to-end payment testing automation suite for a fintech platform. It automatically opens a shop website, logs in, adds items to the cart, and fills out checkout forms using Selenium. After submitting the checkout, the script connects to the Stripe API to verify the charge and then checks our local SQLite database to make sure the transaction was saved correctly. This project connects the user interface, backend API, and database logs into one unified pipeline.

### 2. "What's the difference between WebDriverWait and time.sleep()?"
`time.sleep()` is a blind freeze that stops the entire code for a fixed number of seconds, even if the element loads instantly. This makes tests very slow and unstable. On the other hand, `WebDriverWait` is smart because it checks the browser every 500 milliseconds and moves forward as soon as the element appears. It only throws an error if the element fails to load before the maximum timeout limit.

### 3. "How do you structure automated tests?"
I organize my automation suite into clear, separate layers to keep the project clean. Inside `api-testing/tests/`, I keep the actual test scripts where assertions are evaluated. Reusable browser actions and helper tools are stored separately under `api-testing/scripts/` and `selenium_utils.py`. Finally, I use `config.py` to store global settings like paths, parameters, and base target URLs.

### 4. "Tell me about a bug you found and how you reported it."
I frequently perform exploratory testing on mobile apps to find edge-case bugs, and I recently reported two critical issues on the "Citymapper" app using an iPhone 16e. The first was a UI crash where typing exactly three characters (like "Rok" for "Rokycany") in the city search bar caused the app to freeze completely on a solid green screen. The second was an authentication logic bug: after manually updating my user profile names, logging out, and logging back in via Google SSO, the system incorrectly overwrote my custom data with legacy Google account metadata instead of keeping my updated information. I documented both bugs with clear environment details, reproduction steps, and expected versus actual results.

### 5. "What would you do if a test failed randomly?"
If a test fails randomly, the first thing I check is the synchronization because it is usually a timing issue caused by slow network loading. I replace any hardcoded delays with robust explicit waits to give the website elements proper time to render. Next, I look at the local log entries and automated screenshot captures from the failure milestone to see if a unexpected modal or pop-up blocked the script.

### 6. "How do you handle sensitive data (API keys, passwords)?"
I never write secret passwords or private API credentials directly inside the source code files. Instead, I store them safely inside a local hidden `.env` text file that is excluded from GitHub tracking. My codebase uses a configuration script to read these variables directly into memory during execution, keeping our data safe from public leaks.

### 7. "Why is database verification important in payment testing?"
Checking the user interface is not enough because a website can show a success message even if the backend system fails to process the order. Database validation ensures that transaction records are securely logged with correct amounts, currencies, and timestamps. It guarantees that the system data matches the actual customer charges perfectly.