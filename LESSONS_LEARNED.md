# Lessons Learned: Technical Deep-Dive

This document details five major technical concepts that I initially struggled with during my automation journey, explaining my early mistakes, the core logic behind each concept, and how I understand them today.

---

## 1. Pytest Fixtures and Scope

### What I got wrong initially
At first, I did not understand how Pytest fixtures managed their lifecycle. I used to create a new browser instance inside every single test function. I thought that to keep tests independent, I had to open and close the browser manually every time.

### Why I was wrong
This approach made my test suite incredibly slow and heavy. Opening a fresh browser for ten different test cases takes a lot of time and system memory. I did not realize that Pytest fixtures have a built-in feature called "scope" (like function, class, or module) that can automatically handle this lifecycle for me.

### What I learned & How to explain it
I learned that a fixture is like a setup assistant. By setting the scope to `module` or `class`, I can open the browser just once, run multiple tests inside that screen, and then close it automatically when they finish. To explain it simply: imagine renting a car for a whole weekend trip instead of returning the car and renting a new one every time you want to drive to a different shop.

---

## ## 2. Database Transactions (COMMIT and ROLLBACK)

### What I got wrong initially
When testing databases, I thought that simply running an `INSERT` or `UPDATE` SQL query inside my Python script would immediately change the data forever. I would run a test, check the database app, and get confused why my test data was not actually visible inside the tables.

### Why I was wrong
I was missing the concept of transactions. Databases do not save changes permanently the moment you type a query; they wait in a temporary state. If you do not officially seal the action, the database throws away the changes when the code finishes running.

### What I learned & How to explain it
I learned that you must use `connection.commit()` to save your data permanently, or `connection.rollback()` to cancel the changes if a test steps into an error. Think of it like writing an essay on Google Docs: typing the words is just a draft, but pressing a manual "Save Changes" button is what actually locks it in. If you make a massive mistake, hitting "Undo" is your rollback.

---

## 3. API Rate Limiting

### What I got wrong initially
When I first started writing automated integration tests for the Stripe API, I ran my loops as fast as possible. I thought that a good automation script should spam the endpoint constantly without any pauses to finish the job faster. Suddenly, my tests started failing with unexpected 429 status errors.

### Why I was wrong
I did not know that external servers protect themselves from crashing by using rate limits. If one single user sends too many requests in one second, the server blocks them temporarily to save its bandwidth. My automation script was acting like a malicious attack.

### What I learned & How to explain it
I learned to respect API boundaries by checking server status codes and introducing small, intentional delays when running massive automated data loops. To explain it to a beginner: think of a popular fast-food counter. If one customer yells ten orders at the exact same second, the cashier will tell them to stop and wait. You have to give the server a moment to breathe.

---

## 4. Test Data Cleanup

### What I got wrong initially
In my early automation scripts, my tests would create fake users, dummy emails, and test credit card charges, and then I just left them inside the system. The next time I ran the exact same test suite, everything crashed because the system shouted that the username or email already existed.

### Why I was wrong
I was leaving "garbage" data behind, which ruined the testing environment. Automated tests must always start with a clean environment. If a previous test leaves leftover records, the next test will fail because of duplicate data conflicts, not because the code is broken.

### What I learned & How to explain it
I learned to always write a teardown step inside my fixtures to delete any created rows from the SQLite database right after the test completes. It is like baking a cake in a kitchen: before you start mixing ingredients for a new cake, you must wash the bowls and clean the table from the previous mess, otherwise your new cake will be ruined.

---

## 5. Explicit Waits (WebDriverWait) vs Hardcoded Sleep

### What I got wrong initially
Whenever my Selenium script could not find a button on a web page because the network was slow, I used to put `time.sleep(5)` right before that line. I thought adding these long pauses everywhere was a safe way to make sure the automation would never crash.

### Why I was wrong
This habit made my automation suite extremely slow and highly unstable. If a page loaded in 0.1 seconds, my script still wasted 5 full seconds doing nothing. If the page took 6 seconds to load on a bad day, the script crashed anyway. It was a lazy fix that did not adapt to reality.

### What I learned & How to explain it
I learned to use `WebDriverWait`, which actively watches the browser and moves forward the exact millisecond an element becomes visible. If the element appears early, the test continues immediately; if it takes longer, it waits safely up to a specific limit. It is like waiting for a friend at a bus stop: you do not blindly close your eyes for exactly one hour (`time.sleep`). Instead, you keep looking down the street and greet them the moment they arrive (`WebDriverWait`).