-- Basic SELECT Queries:
-- step 1
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    department TEXT,
    salary INTEGER,
    hire_date DATE
);

INSERT INTO employees (first_name, last_name, department, salary, hire_date) VALUES
('Alice', 'Smith', 'HR', 50000, '2020-06-15'),
('Bob', 'Johnson', 'IT', 70000, 2019-08-23'),
('Charlie', 'Williams', 'Finance', 65000, 2021-03-11'),
('David', 'Brown', 'IT', 72000, '2018-09-30'),
('Emma', 'Davis', 'HR', '48000, 2022-01-05');

-- step 2
SELECT * FROM employees;

-- step 3
SELECT first_name, salary FROM employees WHERE salary > 60000;

-- step 4
SELECT * FROM employees WHERE department = 'IT';


-- Filtering Data with WHERE
SELECT * FROM employees WHERE salary > 60000;

SELECT * FROM employees WHERE hire_date > '2020-01-01';

SELECT * FROM employees WHERE department IN ('HR', 'Finance');


-- Filtering with LIKE (Pattern Matching)
SELECT * FROM employees WHERE first_name LIKE 'A%';

SELECT * FROM employees WHERE last_name LIKE '%son';

SELECT * FROM employees WHERE first_name LIKE '%e';


-- Filtering with BETWEEN
SELECT * FROM employees WHERE salary BETWEEN 60000 AND 70000;

SELECT * FROM employees WHERE hire_date BETWEEN '2019-01-01' AND '2020-12-31';


-- Filtering with IN
SELECT * FROM employees WHERE department IN ('IT', 'HR');

SELECT * FROM employees WHERE salary IN (40000, 65000, 72000);


-- Sorting Data with ORDER BY
SELECT * FROM employees ORDER BY first_name ASC;

SELECT * FROM employees ORDER BY salary DESC;

SELECT * FROM employees ORDER BY department ASC, salary DESC;
