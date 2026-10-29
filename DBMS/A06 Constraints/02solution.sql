create database if not exists employee_management_system;

use employee_management_system;

create table employee(

    emp_id int primary key auto_increment,
    emp_name varchar(50) not null,
    email varchar(100) not null UNIQUE,
    phone varchar(15) not null UNIQUE,
    department varchar(30) not null,
    designation varchar(30) not null,
    age int not null CHECK(age between 21 and 60),
    salary decimal(10,2) not null CHECK(salary >15000),
    experience int not null CHECK(experience between 0 and 35),
    year(joining_year) int not null,
    status varchar(20) not null ENUM('ACTIVE','INACTIVE','ONLEAVE'),
    bonus decimal(10,2) not null unsigned

);

ALTER TABLE employee
add constraint check_age CHECK(experience<=age),

add constraint check_experience , check_salary CHECK(experience>=10 and salary>50000),

add constraint CHECK(
    department = 'it'and
    designation in ( 'Developer', 'Tester', 'Team Lead' )
    or 
    department = 'hr'and
    designation in ('HR Executive', 'HR Manager')
    or
    department = 'finance'and
    designation in ('Accountant', 'Finance Manager')
    or
    department = 'sales'and
    designation in ('Sales Executive', 'Sales Manager')
    
),

add constraint CHECK(
    status = 'active'
    or (status ='inactive' and bonus = 0)
    or (status = 'onleave' and bonus<= salary*0.20)
),

add constraint CHECK(experience<=joining_year and
joining_year<2026);


INSERT INTO employee
(emp_name, email, phone, department, designation, age, salary, experience, joining_year, status, bonus)
VALUES
('Aarav Sharma', 'aarav.sharma@gmail.com', '9876501001', 'IT', 'Software Engineer', 25, 35000.00, 2, 2023, 'ACTIVE', 5000.00),

('Priya Verma', 'priya.verma@gmail.com', '9876501002', 'HR', 'HR Executive', 28, 42000.00, 5, 2021, 'ACTIVE', 7000.00),

('Rahul Patel', 'rahul.patel@gmail.com', '9876501003', 'Finance', 'Accountant', 32, 55000.00, 8, 2018, 'INACTIVE', 10000.00),

('Sneha Gupta', 'sneha.gupta@gmail.com', '9876501004', 'Sales', 'Sales Executive', 24, 28000.00, 1, 2024, 'ACTIVE', 3000.00),

('Vikram Singh', 'vikram.singh@gmail.com', '9876501005', 'IT', 'Team Lead', 38, 85000.00, 12, 2014, 'ACTIVE', 15000.00),

('Neha Joshi', 'neha.joshi@gmail.com', '9876501006', 'HR', 'HR Manager', 42, 75000.00, 15, 2011, 'ONLEAVE', 12000.00),

('Rohan Mehta', 'rohan.mehta@gmail.com', '9876501007', 'Finance', 'Finance Manager', 45, 95000.00, 20, 2008, 'ACTIVE', 20000.00),

('Kavya Mishra', 'kavya.mishra@gmail.com', '9876501008', 'Sales', 'Sales Manager', 35, 68000.00, 10, 2016, 'INACTIVE', 8000.00),

('Aditya Jain', 'aditya.jain@gmail.com', '9876501009', 'IT', 'Senior Developer', 30, 62000.00, 7, 2019, 'ONLEAVE', 9000.00),

('Pooja Tiwari', 'pooja.tiwari@gmail.com', '9876501010', 'Marketing', 'Marketing Executive', 26, 32000.00, 3, 2022, 'ACTIVE', 4000.00);



-- ?  not null testing

-- (null, 'karan@example.com', '9000000008',
--  'Sales', 'Sales Executive', 26, 32000, 4, 2022, 'Inactive', 0),

-- ('Pooja', null, '9000000009',
--  'Sales', 'Sales Manager', 38, 70000, 12, 2014, 'OnLeave', 14000),

-- ('Mohit', 'mohit@example.com', '9000000010',
--  'IT', 'Developer', 32, null, 8, 2018, 'Active', 7000);

-- ? unique testing
-- ('Pooja', 'mohit@example.com', '9000000009',
--  'Sales', 'Sales Manager', 38, 70000, 12, 2014, 'OnLeave', 14000),

-- ('Mohit', 'mohit@example.com', '9000000009',
--  'IT', 'Developer', 32, null, 8, 2018, 'Active', 7000);

-- ? indivdual check testing 

-- Test 6: Age equal to 18

INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Test6', 'test6@example.com', '9110000006',
 'IT', 'Developer', 18, 30000, 0, 2026, 'Active', 1000);


-- Test 7: Salary equal to 10000

INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Test7', 'test7@example.com', '9110000007',
 'IT', 'Developer', 25, 10000, 4, 2022, 'Active', 1000);

-- Test 8 : Try inserting an employee with experience equal to -2.

INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Test8', 'test8@example.com', '9110000008',
 'IT', 'Developer', 25, 10000, -4, 2022, 'Active', 1000);


-- Test 9 : Try inserting an employee with bonus equal to -500.

INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Test9', 'test9@example.com', '9110000009',
 'IT', 'Developer', 25, 10000, -4, 2022, 'Active', -500);

-- Test 10 : Try inserting an employee with status equal to Retired.

INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Test10', 'test10@example.com', '9110000010',
 'IT', 'Developer', 25, 30000, 4, 2022, 'Retired', 1000);

-- ? combination CHECK testing COMMENT

-- Test 11: Age 25 and Experience 10
INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Test11', 'test11@example.com', '9110000011',
 'IT', 'Developer', 25, 60000, 10, 2016, 'Active', 5000);

-- Test 12: experience 12 and salary 35000

INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Test11', 'test11@example.com', '9110000011',
 'IT', 'Developer', 25, 35000, 12, 2016, 'Active', 5000);

-- Test 13: department IT  and designation HR Mamager

INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Test11', 'test11@example.com', '9110000011',
 'IT', 'HR Manager', 25, 35000, 12, 2016, 'Active', 5000);


-- Test 14 : status inactive and bonus 5000
INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Test12', 'test12@example.com', '9110000012',
 'IT', 'HR Manager ', 25, 35000, 12, 2016, 'InActive', 5000);

-- Test 15: OnLeave Status, Salary 50000, Bonus 15000

INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Test15', 'test15@example.com', '9110000015',
 'IT', 'Developer', 30, 50000, 8, 2020, 'OnLeave', 15000);

-- Test 16: Joining Year 2020 and Experience 10

INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Test16', 'test16@example.com', '9110000016',
 'IT', 'Developer', 35, 60000, 10, 2020, 'Active', 5000);

-- Test 17 : Joining Year 2027

INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Test17', 'test17@example.com', '9110000017',
 'IT', 'Developer', 30, 40000, 5, 2027, 'Active', 5000);







