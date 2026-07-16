# Day 87: Future Project Roadmap

This document outlines how I plan to expand and improve my fintech testing suite after Day 90. It shows the steps I will take to make my automated tests more professional, automated, and ready for real-world scaling.

---

##  Phase 1: Months 4-5 (Cloud & CI/CD)

* **What to build:**
  1. Add a simple Flask API wrapper around my automated tests to trigger them with web requests.
  2. Deploy and host the entire testing suite on a cloud platform like AWS or Heroku.
  3. Create an automated CI/CD pipeline using GitHub Actions so that my tests run automatically on every code push.

* **What I will learn & Why it matters:**
  I will learn how to move my tests from running only on my personal computer to running on the cloud. Setting up GitHub Actions will teach me how software teams automatically test code before merging it, which is a key skill for any modern QA engineer. This makes my project accessible from anywhere and fully automated.

---

##  Phase 2: Months 6-7 (More Providers & Performance)

* **What to build:**
  1. Expand the suite to test multiple payment providers instead of just Stripe (such as PayPal and Square).
  2. Add basic performance and load testing to see how the checkout handles 100+ virtual users at the same time.
  3. Create a clean visual dashboard to display the test success/failure results in real-time.

* **What I will learn & Why it matters:**
  I will learn how to integrate different third-party APIs and handle different payment flows. Load testing will teach me how to find performance bottlenecks when a site gets crowded. Building a dashboard will make it easy to share clean, visual test reports with other developers or managers.

---

##  Phase 3: Months 8-9 (Advanced Automation & Mobile)

* **What to build:**
  1. Use simple machine learning algorithms to detect and flag flaky tests (tests that fail randomly due to network delay).
  2. Start mobile payment app testing by integrating Appium into my Python scripts.
  3. Add basic security and vulnerability tests to make sure user payment details are fully protected.

* **What I will learn & Why it matters:**
  I will learn how to use advanced tech like machine learning to make my tests more stable and reliable. Mobile testing with Appium will teach me how to write tests for iOS and Android apps, which is a highly demanded skill. Security testing will help me understand how to protect payment gateways from potential web attacks.