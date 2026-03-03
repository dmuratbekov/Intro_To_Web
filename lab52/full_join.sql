-- 1. Retrieving All Customers and All Orders (Even If No Match Exists)
SELECT customers.name, orders.order_id, orders.total_amount
FROM customers
FULL JOIN orders ON customers.customer_id = orders.customer_id;


-- 2. Listing All Employees and All Departments (Including Unassigned Employees and Empty Departments)
SELECT employees.name, employees.dept_id, departments.dept_name
FROM employees
FULL JOIN departments ON employees.dept_id = departments.dept_id;


-- 3. Finding All Students and All Courses (Including Students Without Courses and Courses Without Students)
SELECT students.name, courses.course_name
FROM students
FULL JOIN enrollments ON students.student_id= enrollments.student_id
FULL JOIN courses ON enrollments.course_id = courses.course_id;