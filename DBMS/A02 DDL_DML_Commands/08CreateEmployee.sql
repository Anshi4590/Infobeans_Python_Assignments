-- QNO  8: Create and Insert into employees Table
-- Columns:

-- emp_id INT

-- emp_name VARCHAR(100)

-- gender VARCHAR(10)

-- dob DATE

-- department VARCHAR(100)

-- position VARCHAR(100)

-- salary DECIMAL(8,2)

-- joining_date DATE

-- phone VARCHAR(15)

-- Task:


USE Batch19;


CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    gender VARCHAR(10),
    dob DATE,
    department VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(8,2),
    joining_date DATE,
    phone VARCHAR(15)
);

-- Insert 6 employee records

INSERT INTO employees
(emp_id, emp_name, gender, dob, department, position, salary, joining_date, phone)
VALUES
(1, 'Amit Sharma', 'Male', '1998-05-12', 'IT', 'Software Engineer', 55000.00, '2023-07-10', '9876543210'),
(2, 'Priya Verma', 'Female', '2000-08-20', 'HR', 'HR Executive', 35000.00, '2024-01-15', '9876543211'),
(3, 'Rahul Singh', 'Male', '1997-03-25', 'Finance', 'Accountant', 42000.00, '2022-06-01', '9876543212'),
(4, 'Neha Patel', 'Female', '1999-11-10', 'Marketing', 'Marketing Manager', 65000.00, '2021-09-20', '9876543213'),
(5, 'Rohan Gupta', 'Male', '2001-01-05', 'IT', 'Web Developer', 48000.00, '2024-03-11', '9876543214'),
(6, 'Sneha Jain', 'Female', '1996-07-18', 'Sales', 'Sales Executive', 38000.00, '2023-02-06', '9876543215');

-- Display all employee records

SELECT * FROM employees;


