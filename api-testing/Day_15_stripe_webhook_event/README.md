### Day 15: Stripe API Charge via Postman & Webhook Verification

**Objective:** Create a charge using Stripe API in Postman and verify the triggered webhook event in the Stripe Dashboard.

**Actions Performed:**
1. Set up a POST request to https://api.stripe.com/v1/charges in Postman.
2. Added Bearer Token authorization.
3. Defined body parameters: amount=2500, currency=usd, source=tok_visa.
4. Successfully triggered the charge.

**Result:**
The API request returned a 200 OK status, and the Stripe Dashboard registered a charge.succeeded event.

**Screenshot of the Webhook Event:**
![Stripe Webhook Event](day15-stripe-webhook-event.png)
