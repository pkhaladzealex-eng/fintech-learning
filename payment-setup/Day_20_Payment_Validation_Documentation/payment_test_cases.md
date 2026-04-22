# 💳 Stripe Payment System - Manual Test Cases

## Test Case 1: Successful payment with Visa
- **Priority:** High
- **Steps:**
  1. Access Stripe Checkout.
  2. Select 'Visa' card option.
  3. Enter valid Visa details (4242...).
  4. Click 'Pay'.
- **Expected Result:** Payment status is 'Succeeded', transaction appears in Stripe Dashboard.
- **Evidence:** Screenshot of successful payment confirmation.
---

## Test Case 2: Successful payment with Mastercard
- **Priority:** High
- **Steps:**
  1. Access Stripe Checkout.
  2. Select 'Mastercard' card option.
  3. Enter valid Mastercard details (5555...).
  4. Click 'Pay'.
- **Expected Result:** Payment status is 'Succeeded', card brand correctly identified as 'Mastercard'.
- **Evidence:** Screenshot of Stripe dashboard showing Mastercard transaction.
---

## Test Case 3: Declined Payment - Insufficient Funds
- **Priority:** Critical
- **Steps:**
  1. Access Stripe Checkout.
  2. Enter a test card designed to fail for 'Insufficient Funds' (e.g., tok_chargeDeclinedInsufficientFunds).
  3. Click 'Pay'.
- **Expected Result:** System displays an error message: 'Your card has insufficient funds.' No transaction is created in the database.
- **Evidence:** Screenshot of the error message on the UI.
---

## Test Case 4: Successful payment with American Express (Amex)
- **Priority:** Medium
- **Steps:**
  1. Access Stripe Checkout.
  2. Enter valid Amex card details (34... or 37...).
  3. Click 'Pay'.
- **Expected Result:** Payment succeeds, brand identified as 'Amex'.
- **Evidence:** Screenshot of the Stripe receipt for an Amex transaction.
---

## Test Case 5: Declined Payment - Expired Card
- **Priority:** High
- **Steps:**
  1. Access Stripe Checkout.
  2. Enter a card with an expiration date in the past (e.g., 01/22).
  3. Click 'Pay'.
- **Expected Result:** Error message: 'Your card's expiration date is invalid.'
- **Evidence:** Screenshot of UI validation error.
---

## Test Case 6: Declined Payment - Incorrect CVC
- **Priority:** High
- **Steps:**
  1. Access Stripe Checkout.
  2. Enter valid card number and expiration date.
  3. Enter an incorrect 3-digit CVC (e.g., 000).
  4. Click 'Pay'.
- **Expected Result:** Payment is declined. Error message: 'Your card's security code is incorrect.'
- **Evidence:** Screenshot of the CVC validation error.
---


## Test Case 7: Validation - Empty Required Fields
- **Priority:** Medium
- **Steps:**
  1. Access Stripe Checkout.
  2. Leave all fields (Card number, Expiry, CVC) empty.
  3. Click 'Pay'.
- **Expected Result:** UI prevents submission. Multiple error messages appear under each empty field.
- **Evidence:** Screenshot of the highlighted empty fields.
---

## Test Case 8: Successful Refund Processing
- **Priority:** High
- **Steps:**
  1. Go to Stripe Dashboard -> Payments.
  2. Select a successful 'Succeeded' transaction.
  3. Click 'Refund' and confirm.
- **Expected Result:** Payment status changes to 'Refunded', and money is sent back to the customer's account.
- **Evidence:** Screenshot of the Stripe dashboard showing 'Refunded' status.
---

## Test Case 9: Backend - Webhook Confirmation
- **Priority:** Critical
- **Steps:**
  1. Complete a successful test payment.
  2. Check Stripe Dashboard -> Developers -> Webhooks.
  3. Inspect the 'payment_intent.succeeded' event.
- **Expected Result:** Webhook returns a '200 OK' response, confirming our server received the data.
- **Evidence:** Log entry showing the 200 OK status in Stripe Webhooks.
---

## Test Case 10: Database - Record Verification
- **Priority:** High
- **Steps:**
  1. Perform a successful payment.
  2. Open terminal and run the 'customer_query.py' script.
  3. Verify the new customer and payment method are present.
- **Expected Result:** The SQL database is updated with the correct payment information.
- **Evidence:** Terminal output showing the new customer entry from the DB.
---
