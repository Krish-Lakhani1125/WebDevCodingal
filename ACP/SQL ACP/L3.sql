CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    emp_name TEXT(50),
    department TEXT(50),
    salary DECIMAL(10,2)
);

INSERT INTO employee VALUES
(1, 'John', 'HR', 45000),
(2, 'Alice', 'Finance', 60000),
(3, 'David', 'IT', 75000),
(4, 'Sophia', 'Marketing', 50000),
(5, 'Michael', 'IT', 85000);

SELECT * FROM employee;

SELECT SUM(salary) AS total_salary
FROM employee;

SELECT AVG(salary) AS average_salary
FROM employee;

SELECT COUNT(department) AS total_departments
FROM employee;

SELECT MIN(salary) AS minimum_salary
FROM employee;

SELECT MAX(salary) AS maximum_salary
FROM employee;