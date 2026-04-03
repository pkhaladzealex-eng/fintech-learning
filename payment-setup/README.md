# Payment Testing Setup - Stripe Dashboard

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
