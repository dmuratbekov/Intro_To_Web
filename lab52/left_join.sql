-- 1. Retrieving All Customers and Their Orders (Even Those Without Orders)
SELECT customers.name, orders.order_id, orders.total_amount
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id;


-- 2. Listing All Employees with Their Departments (Including Unassigned Employees)
SELECT employees.name, departments.dept_name
FROM employees
LEFT JOIN departments ON employees.dept_id = departments.dept_id;


-- 3. Finding Students and Their Enrolled Courses (Including Students Without Courses)
SELECT students.name, courses.course_name
FROM students
LEFT JOIN enrollments ON students.student_id = enrollments.student_id
LEFT JOIN courses ON enrollments.course_id = courses.course_id;


