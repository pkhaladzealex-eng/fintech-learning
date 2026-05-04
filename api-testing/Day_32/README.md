# Day 32: Database Integration & Data Aggregation

## Objective
The goal of this task was to automate the interaction between Python and SQLite by inserting real transaction data and performing financial calculations (aggregation) directly from the database.

## Technical Tasks
- **Database Schema:** Defined a structured table `charges` to store transaction metadata.
- **Data Persistence:** Automated the process of clearing old records and inserting fresh data using `executemany()`.
- **Financial Calculation:** Implemented a Python loop to aggregate the `amount` field from all database rows to calculate the total transaction volume.

## Key Learning
I learned how to bridge the gap between API results (from Day 31) and permanent storage (SQL), ensuring that data is not just fetched, but also correctly stored and analyzed.
