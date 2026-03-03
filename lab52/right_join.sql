-- 1. Retrieving All Orders and Their Customers (Even Those Without Registered Customers)
SELECT orders.order_id, orders.total_amount, customers.name
FROM customers
RIGHT JOIN orders ON customers.customer_id = orders.customer_id;


-- 2. Listing All Departments and Their Employees (Including Departments Without Employees)
SELECT departments.dept_name, employees.name
FROM employees
RIGHT JOIN departments ON employees.dept_id = departments.dept_id;


-- 3. Finding All Courses and Their Enrolled Students (Including Courses Without Students)
SELECT courses.course_name, students.name
FROM students
RIGHT JOIN enrollments ON students.student_id = enrollments.student_id
RIGHT JOIN courses ON enrollments.course_id = courses.course_id;
