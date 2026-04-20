# Fintech QA Progress Report (Days 1-16)

## 1. What I've Built
* **Stripe Environment**: Set up a functional Sandbox environment for risk-free testing.
* **Manual Testing**: Used Postman to verify charge creation, declines, and refund flows.
* **Python Automation**: Developed scripts to automate payments and handle API errors gracefully.
* **Database Integration**: Created an SQLite database to store transactions and verified them using Python logic.
* **Webhook Architecture**: Visualized payment flows and built a simulation for real-time notifications.

## 2. What I Understand Now
* I understand how an API request (POST/GET) travels from a client to a server and back.
* I can read and parse JSON data to extract specific transaction details like status and amount.
* I understand the role of SQL as a "source of truth" for verifying if an API action actually updated the system.
* I am comfortable using Git/GitHub to document and version-control my work.

## 3. What's Still Confusing
* Connecting all parts (Stripe -> Webhook -> Python -> SQL) into one seamless automation flow still feels complex.
* Handling very large, nested JSON objects in Python requires more practice.

## 4. Next Skills to Learn
* Learning **pytest** to write professional-grade automated tests.
* Understanding **Mocking** to test APIs without needing a real connection every time.