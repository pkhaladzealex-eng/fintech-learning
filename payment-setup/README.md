# 💳 Stripe Payment Integration & Testing Project

## 🌟 Project Overview
This project demonstrates a comprehensive QA testing process within the **Stripe Sandbox** environment. I have simulated real-world customer creation and transaction scenarios to verify system robustness and error handling.

---

## 📅 Day 1: Payment Testing Setup (Customers & Cards)
In the first phase, I focused on setting up the environment and creating test customers to cover various payment networks.

### Created Test Customers:
1. **John Doe** - Visa (`4242`)
2. **Jane Smith** - Visa (`5556`)
3. **Alex Ross** - American Express (`0005`)
4. **Sara Lane** - Mastercard (`3222`)
5. **Mark Brown** - Mastercard (`8210`)

### Why test with different card brands?
* **Validation Logic:** Ensuring the system handles 15-digit (Amex) vs 16-digit (Visa/MC) numbers.
* **Network Communication:** Verifying gateway responses across different financial networks.
* **UI/UX Feedback:** Checking if the frontend correctly identifies and displays card brand icons.

---

## 📅 Day 2: Transaction Outcome Testing
In this phase, I executed 5 manual transactions to test how the system handles different payment outcomes.

### 1. Successful Payment ✅
Verified the "Happy Path" where a standard transaction completes successfully.
![Successful Payment](./payment-setup/1-successful-payment.png)

### 2. Declined Card ❌
Simulated a generic bank decline to verify the system's rejection handling.
![Declined Card](./payment-setup/2-declined-card.png)

### 3. Insufficient Funds 💸
Verified the specific error message when a card has an inadequate balance.
![Insufficient Funds](./payment-setup/3-insufficient-funds.png)

### 4. Expired Card 📅
Tested the system's ability to validate and reject outdated card information.
![Expired Card](./payment-setup/4-expired-card.png)

### 5. Network / Processing Error ⚠️
Simulated a technical/processing failure to test system resilience.
![Network Error](./payment-setup/5-network-error.png)

---

## 💡 Key Learning Outcomes
* **Stripe Test Environment:** Mastering "Magic" card numbers to trigger specific API responses.
* **Error Handling:** Understanding the importance of granular error messages (e.g., distinguishing a decline from an expiration).
* **Transaction Lifecycle:** Tracking payments from `Pending` to `Succeeded` or `Failed` in the Dashboard.
* **QA Documentation:** Implementing a structured approach to screenshot naming and Git-based reporting.