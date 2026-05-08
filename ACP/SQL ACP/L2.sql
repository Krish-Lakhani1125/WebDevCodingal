-- Create Customer Table
CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50),
    grade INT
);

-- Insert Sample Records
INSERT INTO customer VALUES
(1, 'John', 'New York', 200),
(2, 'Alice', 'Chicago', 150),
(3, 'David', 'New York', 90),
(4, 'Sophia', 'Boston', 120),
(5, 'Michael', 'New York', 300);

-- Customers who belong to New York OR have grade above 100
SELECT *
FROM customer
WHERE city = 'New York'
   OR grade > 100;

-- Customers who belong to New York AND have grade above 100
SELECT *
FROM customer
WHERE city = 'New York'
  AND grade > 100;