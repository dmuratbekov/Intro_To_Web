DROP TABLE IF EXISTS students;

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50),
  city VARCHAR(50),
  grade INT
);

INSERT INTO students (name, city, grade) VALUES
('Aziret', 'Bishkek', 85),
('Bektur', 'Bishkek', 70),
('Daniel', 'Osh', 90),
('Ali', 'Osh', 60);

-- COUNT
SELECT COUNT(*) FROM students;

-- SUM
SELECT SUM(grade) FROM students;

-- AVG
SELECT AVG(grade) FROM students;

-- MIN & MAX
SELECT MIN(grade), MAX(grade) FROM students;

-- GROUP BY
SELECT city, COUNT(*) 
FROM students
GROUP BY city;

-- HAVING
SELECT city, COUNT(*) 
FROM students
GROUP BY city
HAVING COUNT(*) > 1;