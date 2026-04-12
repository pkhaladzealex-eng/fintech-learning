-- 1. SELECT all transactions
SELECT * FROM test_transactions;

-- 2. SELECT transactions with status = 'succeeded'
SELECT * FROM test_transactions WHERE status = 'succeeded';

-- 3. SELECT total amount of all transactions
SELECT SUM(amount) AS total_amount FROM test_transactions;
