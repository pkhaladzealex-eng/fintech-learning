Stripe Payment Integration Testing
Project Overview
This project demonstrates the testing of various payment outcomes using the Stripe Dashboard in Test Mode. The goal was to simulate real-world transaction scenarios and verify how the system handles different card responses.

Completed Tasks
Set up Stripe account in Test Mode.

Created 5 manual transactions with specific outcomes.

Documented results with screenshots in the /payment-setup folder.

Test Scenarios & Results
Successful Payment: Verified the basic payment flow using a standard test card.

Declined Card: Simulated a generic decline to test the system's rejection handling.

Insufficient Funds: Verified the error message when a card has a low balance.

Expired Card: Tested the validation of the card's expiration date.

Network/Processing Error: Simulated a technical failure using a specific processing error test card.

What I Learned
Stripe Test Environment: How to use "Magic" card numbers to trigger specific API responses without using real money.

Error Handling: Importance of clear error messages (e.g., distinguishing between a declined card and an expired one).

Transaction Lifecycle: How to track a payment from "Pending" to "Succeeded" or "Failed" in the dashboard.

QA Documentation: The value of naming screenshots clearly for easier bug tracking and reporting.