-- 1. Joining Customers and Orders Tables
SELECT customers.name, orders.order_id, orders.total_amount
FROM customers
INNER JOIN orders ON customers.customer_id = orders.customer_id;


-- 2. Joining Employees and Departments
SELECT employees.name, departments.dept_name
FROM employees
INNER JOIN departments ON employees.dept_id = departments.dept_id;


-- 3. Joining Students and Courses with Enrollment
SELECT students.name, courses.course_name
FROM students
INNER JOIN enrollments ON students.student_id= enrollments.student_id
INNER JOIN courses ON enrollments.course_id = courses.course_id;


