-- 1) Create database
CREATE DATABASE university;

-- 2) Create user (замени пароль на свой)
CREATE USER uni_user WITH PASSWORD '12345';

-- 3) Give permissions
GRANT ALL PRIVILEGES ON DATABASE university TO uni_user;

-- 4) Connect (в psql можно так)
-- \c university

-- 5) Create table
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  full_name VARCHAR(100) NOT NULL,
  age INT CHECK (age > 0),
  city VARCHAR(50)
);

-- 6) Insert data
INSERT INTO students (full_name, age, city) VALUES
('Alice Johnson', 20, 'Bishkek'),
('Bob Smith', 22, 'Osh'),
('Charlie Brown', 19, 'Karakol');

-- 7) Select
SELECT * FROM students;

-- 8) Example filter
SELECT * FROM students WHERE age >= 20;