# Day 85: Code Refactoring Notes

This document highlights three major code smells that were refactored to make the payment automation suite cleaner, more secure, and portable.

---

### Refactor 1: Removing Hardcoded Database Paths
* **What I fixed:** Replaced hardcoded absolute paths to the SQLite database with a central configuration variable.
* **Why it matters:** Absolute paths like `/Users/alexpkhaladze/...` only work on my local computer. If an interviewer runs this project on their PC, the tests will crash immediately because that path does not exist. Using a config file makes the system portable.

#### Before (Fragile):
```python
# Hardcoded local path directly inside the script
conn = sqlite3.connect('/Users/alexpkhaladze/desktop/fintech-learning/global_data/fintech_main.db')
```
After (Refactored):

```Python
# Path is loaded dynamically from central configuration

import config
conn = sqlite3.connect(config.DATABASE_PATH)
```
Refactor 2: Removing Hardcoded API Credentials
What I fixed: Replaced hardcoded Stripe API secret keys with system environment variables.

Why it matters: Writing API keys directly in code is a critical security issue. If pushed to GitHub, bots will steal the keys within seconds. Moving them to environmental variables (os.environ) keeps credentials private.

Before (Fragile):

```Python

# Dangerous: API keys visible to everyone on GitHub
stripe.api_key = "sk_test_51Nx..."
```
After (Refactored):

```Python
# Safe: Read from secure local environment configuration
import os
stripe.api_key = os.environ.get('STRIPE_API_KEY')
```
Refactor 3: Eliminating Duplicate Logging Logic
What I fixed: Consolidated duplicated console print and file logging codes into one single helper function (log_event) inside utils.py.

Why it matters: Previously, multiple test scripts wrote logs manually using inconsistent formats. Creating a centralized log function keeps our codebase clean (DRY - Don't Repeat Yourself) and ensures that all logs have the exact same format.

Before (Fragile):
```Python
# Repeated print and file writing statements scattered everywhere
print(f"INFO: Checking transaction {charge_id}")
with open("logs.txt", "a") as f:
    f.write(f"INFO: Checking transaction {charge_id}\n")
```    
After (Refactored):
```Python
# One unified clean handler
from utils import log_event
log_event("INFO", f"Initiating secure network lookup for Charge Target: {charge_id}")
```