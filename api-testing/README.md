	# Stripe API Testing - Day 4

This folder contains API request tests performed using Postman.

## Requests Performed:
1. **Create Successful Charge**: Verified payment processing with a valid test card.
2. **Create Declined Charge**: Verified system behavior when a card is declined.
3. **Retrieve Charge Details**: Fetched details of an existing transaction using its ID.

## Screenshots:
![Successful Charge](./Day-04-Postman-API-Testing-Basics/1-successful-charge.png)
![Declined Charge](./Day-04-Postman-API-Testing-Basics/2-declined-charge.png)
![Retrieve Details](./Day-04-Postman-API-Testing-Basics/3-retrieve-details.png)

---

## Day 5: Refund Flow & Verification
In this session, I handled the post-payment lifecycle by processing a refund and verifying its status.

1. **Create Refund**: Sent a `POST` request to `/v1/refunds` using a specific Charge ID (`ch_...`).
2. **Retrieve Refund Status**: Verified the refund details and confirmed the status via a `GET` request.

### Screenshots (Day 5):
![Create Refund Success](./Day-05-Stripe-Refund-Flow-Testing/day-5-create-refund-success.png)
![Retrieve Refund Status](./Day-05-Stripe-Refund-Flow-Testing/day-5-retrieve-refund-status.png)

### Key Takeaway:
Successfully linked a refund to an existing charge and confirmed that Stripe correctly updates the transaction's lifecycle status to reflect the reversal of funds.

---

## Day 6: Stripe API Python Setup
Transitioned from Postman to automation using the **Stripe Python SDK**.

1. **Environment Configuration**: Set up secure API key management using environment variables.
2. **Charge Creation**: Successfully automated a $25.00 payment via a Python script.

### Files & Screenshots (Day 6):
* [Python Code](./Day-06-Stripe-Charge-Creation-Basics/stripe_test_day6.py)
* ![Success Charge](./Day-06-Stripe-Charge-Creation-Basics/day6_result.png)

---

## Day 7: Stripe API Error Handling
Focused on system resilience and handling payment failures.

1. **Simulated Failure**: Used `tok_chargeDeclined` to trigger an intentional card rejection.
2. **Exception Handling**: Implemented `try-except` blocks to catch and display user-friendly error messages from Stripe's API.

### Files & Screenshots (Day 7):
* [Python Code](./Day-07-Stripe-API-Error-Handling/stripe_test_day7.py)
* ![Declined Error](./Day-07-Stripe-API-Error-Handling/day7_result.png)

### Key Takeaway:
Learned that robust API integration isn't just about successful paths, but also about gracefully managing real-world scenarios like declined cards.
---

# Day 8: Stripe API Practice (Repetition)

Today I practiced handling successful and declined payments using the Stripe Charge API.

### Successful Payment
* [Success Case Code](./Day-08-Repetition/practice_success.py)
![Success Screenshot](./Day-08-Repetition/practice_success.png)

### Declined Payment (Error Handling)
* [Error Case Code](./Day-08-Repetition/practice_error.py)
![Error Screenshot](./Day-08-Repetition/practice_error.png)

# API Testing & Fintech Learning
---
## Day 9: Stripe Refund Automation
### Overview
Automated the process of creating a charge and immediately issuing a full refund using the Stripe API.

### Implementation & Results
* [Refund Script Code](Day-09-Stripe-Refund-Automation/stripe_refund.py)
![Refund Test Results](Day-09-Stripe-Refund-Automation/terminal_refund_test_results.png)

---

## Day 10: SQL Database Setup
### Overview
Created a local SQLite database to store and manage transaction data. Defined a schema and populated it with test data.

### Implementation & Results
* [SQL Database File](Day-10-SQL-Transactions/payments.db)
* [SQL Setup Script](Day-10-SQL-Transactions/test_transactions.sql)
![SQL Test Results](Day-10-SQL-Transactions/sql_test_results.png)


---

## Day 11: Advanced SQL Queries
### Overview
Practiced data retrieval techniques using SQL. Performed filtering and aggregation on the transactions database.

### Tasks Performed:
1. **Fetch All Data**: Verified all records in the table.
2. **Filtered Selection**: Selected transactions with a `succeeded` status.
3. **Data Aggregation**: Calculated the total revenue using the `SUM()` function.

### Implementation & Results
* [SQL Queries File](./Day-11-SQL-Queries/queries.sql)
![SQL Queries Results](./Day-11-SQL-Queries/sql_queries_results.png)


---

## Day 12: Database Verification Script
### Overview
Developed a Python script to bridge the gap between backend logic and the database. The script automates data retrieval and performs calculations on transaction records.

### Tasks Performed:
1. **Database Connection**: Established a secure connection to the SQLite database using Python.
2. **Data Extraction**: Executed SQL queries within the script to fetch all transaction details.
3. **Automated Calculation**: Implemented logic to calculate the total amount paid across all records.

### Implementation & Results
* [Python Verification Script](./Day-12/verify_payment.py)
![Payment Verification Results](./Day-12/payment_verification_output.png)

### Key Takeaway:
Practiced the "Code-to-Database" workflow, ensuring that data stored in SQL can be accurately processed and validated using Python logic.


---

## Day 13: Reflections & Integration Summary
### Overview
Synthesized the knowledge gained from working with SQL and Python automation. Documented the key lessons on how these tools work together in a payment testing environment.

### Key Learnings:
1. **SQL for Payment Testing**: Learned to use SQL as a "truth checker" to verify transaction data (amount, currency, status) directly in the database.
2. **Python-SQL Connection**: Mastered the "bridge" concept—using Python libraries and cursors to automate database tasks.
3. **The "Connection Chain"**: Explored how real-time actions (like Stripe clicks) sync with backend databases.

### Implementation & Results
* [Detailed Learning Log](../payment-setup/learnings.md)

### Key Takeaway:
Understanding the flow from a user's action to a Python script and finally to a SQL database entry is crucial for full-stack payment testing.
---

## Day 14: Payment Flow Documentation
### Overview
Documented the end-to-end payment lifecycle, visualizing how a user action triggers an API process, updates the system's database, and is finally verified by a QA tester using SQL.

### Tasks Performed:
1. **Flow Visualization**: Created a **Mermaid Sequence Diagram** to map the interaction between the User, Stripe API, and the Database.
2. **Architecture Mapping**: Detailed the step-by-step logic from the "Pay" button click to the SQL verification.
3. **Verification Logic**: Documented the specific SQL query used to check the final state of a transaction in the database.

### Implementation & Results:
* [Detailed Payment Flow Documentation](../payment-setup/payment-flow.md)

### Key Takeaway:
Visualizing the flow helped bridge the gap between frontend actions and backend database updates. It clarified how Stripe Webhooks serve as the messenger that tells our database to update a record, which we then verify using SQL queries.


## Day 15: Stripe Webhook Verification via Postman
### Overview
Returned to Postman to trigger a real-time event and verify the system's external communication via Webhooks. This session focused on how an API request triggers an asynchronous notification (Webhook) in the Stripe ecosystem.

### Tasks Performed:
1. **API Request (Postman)**: Created a `POST` request to `/v1/charges` to simulate a $25.00 payment using Stripe's test environment.
2. **Webhook Monitoring**: Accessed the Stripe Dashboard's Workbench to monitor incoming events triggered by the API call.
3. **Event Validation**: Verified that the `charge.succeeded` event was correctly generated with the matching transaction details (amount, currency, and ID).

### Implementation & Results:
* [Day 15 Task Folder](./Day_15_stripe_webhook_event/)
![Stripe Webhook Event Result](./Day_15_stripe_webhook_event/day15-stripe-webhook-event.png)

### Key Takeaway:
Confirmed the link between a manual API call (Postman) and the automatic notification system (Webhooks). This is a critical step in payment testing, as it ensures that the backend and third-party services stay in sync after a transaction is processed.

---

## Day 16: Webhook Concepts & Simulation
### Overview
Explored the theoretical and practical foundation of Webhooks. Created a Python-based simulation to understand how a system "listens" for asynchronous events from third-party services like Stripe.

### Tasks Performed:
1. **Conceptual Documentation**: Explained the "Push" mechanism of webhooks vs. the "Pull" mechanism of standard APIs via code comments.
2. **Simulation Script**: Developed `webhook_listener.py` to simulate a server waiting for incoming event data.
3. **Data Structure Mapping**: Defined a sample JSON payload representing a `charge.succeeded` event to visualize the data structure received by a webhook.

### Implementation & Results:
* [Day 16 Task Folder](./Day_16_Webhook_Concept/)
![Webhook Simulation Result](./Day_16_Webhook_Concept/day16-webhook-concept.png)

### Key Takeaway:
Learned that Webhooks act as "Messengers"  that notify our system automatically when an event occurs. Understanding the JSON payload structure is vital for QA testing to verify that the backend correctly processes these automated notifications.
