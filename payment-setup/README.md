# Day 1:Payment Testing Setup - Stripe Dashboard

## Overview
This folder contains the initial setup for payment testing using the Stripe Sandbox environment. I have created 5 test customers to simulate real-world checkout scenarios with different card issuers.

## Created Test Customers
I created the following customers to cover major payment networks:
1. **John Doe** - Visa (4242)
2. **Jane Smith** - Visa (5556)
3. **Alex Ross** - American Express (0005)
4. **Sara Lane** - Mastercard (3222)
5. **Mark Brown** - Mastercard (8210)

## Why different payment methods?
Testing with various card brands (Visa, Mastercard, Amex) is crucial for:
* **Validation Logic:** Ensuring the system correctly identifies 15-digit card numbers (Amex) vs 16-digit (Visa/MC).
* **Payment Processing:** Verifying that the payment gateway communicates correctly with different financial networks.
* **UI Feedback:** Checking if the frontend displays the correct card brand icons based on the input.

## Importance for Payment Testing
Setting up test customers allows us to verify the "Happy Path" (successful registration and card binding) without using real money. It ensures that the integration between our application and Stripe is robust and ready for transaction testing.








## Day 2: Account & Card Setup

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