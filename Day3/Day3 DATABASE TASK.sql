-- CREATE DATABASE day3taskdatabase
USE day3taskdatabase; 

-- CREATE TABLE employees(
--     employee_id INT AUTO_INCREMENT PRIMARY KEY,
--     employee_name VARCHAR(100),
--     position VARCHAR(100),
--     salary DECIMAL(10,2)
-- );

-- INSERT INTO employees (employee_name, position, salary) VALUES
-- 	('혜린', 'PM', 9000),
--     ('은우', 'Frontend', 92000),
--     ('가을', 'Backend', 92000),
--     ('지수', 'Frontend', 7800),
--     ('민혁', 'Frontend', 96000), 
--     ('하온', 'Backend', 130000);

-- UPDATE employees
-- SET salary = 8000
-- WHERE employee_id = 2;

-- SELECT employee_name, salary FROM employees 
-- WHERE salary <= 9000 

-- UPDATE employees 
-- set salary = salary * 1.10 
-- WHERE position = 'PM'

-- UPDATE employees 
-- set salary = salary *1.05 
-- where position = 'Backend'

-- DELETE from employees where employee_name = '민혁'

-- SELECT position, round(avg(salary), 0) as avg_salary
-- from employees 
-- group by position; 

delete from employees;



