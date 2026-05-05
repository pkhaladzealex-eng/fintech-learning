# Day 33: API-to-DB Integration & Analytics

## Objective
The goal was to bridge real-time data from Stripe API directly into our local SQL database and perform basic financial analytics using SQL queries.

## Technical Tasks
- **Live Data Fetching:** Used Stripe SDK to retrieve specific charge objects (`ch_...`).
- **Data Transformation:** Formatted API responses (converting cents to dollars) before database insertion.
- **SQL Analytics:** - Automated data insertion using `executemany()`.
  - Used SQL aggregate functions (`SUM`, `AVG`) to calculate financial metrics directly from the DB.

## Results
- Total records: 5 charges.
- Total amount: 150 USD.
- Average amount: 30.0 USD.
