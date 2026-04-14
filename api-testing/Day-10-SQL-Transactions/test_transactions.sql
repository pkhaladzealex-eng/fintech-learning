-- Create table
CREATE TABLE IF NOT EXISTS payments (
    id INTEGER PRIMARY KEY,
    customer_name VARCHAR(50),
    amount DECIMAL(10, 2),
    status VARCHAR(20)
);

-- Insert test data
INSERT INTO payments (customer_name, amount, status) VALUES
('Tech Enthusiast', 50.00, 'succeeded'),
('Global User', 120.50, 'pending'),
('Creative Mind', 75.25, 'refunded');

-- Select data to verify
SELECT * FROM payments;