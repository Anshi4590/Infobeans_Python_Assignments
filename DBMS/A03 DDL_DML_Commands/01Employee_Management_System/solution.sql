
-- Part 1: Create and select database

CREATE DATABASE IF NOT EXISTS employee_management;
USE employee_management;


-- Part 2: Create employees table

CREATE TABLE IF NOT EXISTS employees (
    employee_id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    employee_code CHAR(6) NOT NULL UNIQUE,
    employee_name VARCHAR(100) NOT NULL,
    age TINYINT UNSIGNED,
    number_of_children TINYINT UNSIGNED DEFAULT 0,
    experience_months SMALLINT UNSIGNED,
    salary DECIMAL(10,2),
    performance_score FLOAT,
    productivity_score DOUBLE,
    department_id MEDIUMINT UNSIGNED,
    employee_status ENUM('active','inactive','on_leave','resigned')
        DEFAULT 'active',
    skills SET('java','python','react','c++','aws','mysql'),
    gender ENUM('female','male','others'),
    date_of_birth DATE,
    joining_date DATE,
    login_time TIME,
    interview_datetime DATETIME,
    birth_year YEAR,
    is_active BOOLEAN DEFAULT TRUE,
    short_note TINYTEXT,
    employee_description TEXT,
    training_history MEDIUMTEXT,
    employee_profile LONGTEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);

-- Verify table structure
DESC employees;


-- Part 3: Insert 15 employees

INSERT IGNORE INTO employees (
    employee_code, employee_name, age, number_of_children,
    experience_months, salary, performance_score, productivity_score,
    department_id, employee_status, skills, gender,
    date_of_birth, joining_date, login_time, interview_datetime,
    birth_year, is_active, short_note, employee_description,
    training_history, employee_profile
)
VALUES
('EMP001','Rahul Sharma',25,0,24,52500.50,8.5,92.4567,1,'active','java,python,mysql','male','2001-03-15','2024-01-10','09:00:00','2023-12-20 10:30:00',2001,TRUE,'Good performer','Software developer.','Python and SQL training.','Backend developer.'),
('EMP002','Priya Verma',28,1,48,78500.75,9.2,95.6789,2,'active','python,react,aws','female','1998-07-21','2022-05-16','09:15:00','2022-04-25 11:00:00',1998,TRUE,'Team leader','Frontend developer.','React training.','Frontend team lead.'),
('EMP003','Aman Patel',32,2,84,95000.25,7.8,86.2345,3,'on_leave','java,mysql','male','1994-11-08','2019-06-03','09:30:00','2019-05-20 14:00:00',1994,FALSE,'On leave','Database developer.','SQL training.','Enterprise developer.'),
('EMP004','Neha Singh',24,0,12,45000.00,8.1,89.1234,1,'active','python,react','female','2002-02-11','2025-02-01','08:55:00','2025-01-15 09:30:00',2002,TRUE,'Quick learner','Junior developer.','Web development training.','Web developer.'),
('EMP005','Rohit Gupta',35,2,120,125000.25,9.5,98.7654,4,'active','java,aws,mysql','male','1991-05-19','2016-03-14','08:45:00','2016-02-20 15:00:00',1991,TRUE,'Senior engineer','Senior engineer.','Cloud training.','Cloud specialist.'),
('EMP006','Anjali Mishra',27,0,36,68000.50,8.7,91.5678,2,'inactive','python,mysql','female','1999-09-04','2023-07-17','09:10:00','2023-06-25 10:00:00',1999,FALSE,'Former employee','HR analyst.','Analytics training.','Data analyst.'),
('EMP007','Vikas Yadav',41,3,180,145000.75,9.1,96.4321,5,'active','java,aws,react','male','1985-01-27','2010-08-09','08:30:00','2010-07-20 12:30:00',1985,TRUE,'Department head','Technical manager.','Management training.','Engineering leader.'),
('EMP008','Sneha Jain',23,0,6,38000.25,7.5,82.3456,1,'active','python,react','female','2003-06-13','2026-04-06','09:20:00','2026-03-15 11:30:00',2003,TRUE,'New joiner','Web developer.','Python training.','Junior developer.'),
('EMP009','Karan Mehta',30,1,60,87500.00,8.9,94.2345,3,'resigned','java,mysql,aws','male','1996-10-22','2021-02-15','09:05:00','2021-01-28 13:00:00',1996,FALSE,'Resigned','Backend engineer.','Java training.','Database developer.'),
('EMP010','Pooja Tiwari',29,1,54,82000.50,8.6,90.9876,2,'active','python,aws','female','1997-04-09','2022-11-21','09:25:00','2022-10-30 10:15:00',1997,TRUE,'Reliable worker','HR technology specialist.','Cloud training.','HR systems specialist.'),
('EMP011','Arjun Rao',38,2,144,118000.75,9.3,97.1234,4,'active','java,react,mysql','male','1988-08-17','2014-04-07','08:40:00','2014-03-10 14:30:00',1988,TRUE,'Experienced','Full-stack engineer.','Architecture training.','Business applications developer.'),
('EMP012','Kavya Desai',26,0,30,61000.25,8.0,87.6543,5,'on_leave','python,mysql,aws','female','2000-12-02','2023-10-02','09:35:00','2023-09-15 09:45:00',2000,FALSE,'On leave','Data analyst.','SQL training.','Reporting specialist.'),
('EMP013','Suresh Kumar',50,3,240,175000.50,9.7,99.8765,3,'active','java,python,mysql,aws','male','1976-03-28','2005-01-03','08:20:00','2004-12-10 16:00:00',1976,TRUE,'Expert mentor','Principal engineer.','Advanced architecture training.','Technical mentor.'),
('EMP014','Meera Joshi',33,2,96,102500.75,8.8,93.4567,1,'active','python,react,aws','female','1993-07-06','2018-09-24','09:12:00','2018-09-01 11:15:00',1993,TRUE,'Project owner','Software engineer.','Agile training.','Software delivery coordinator.'),
('EMP015','Dev Malhotra',22,0,3,32000.00,7.2,78.9876,5,'inactive','java,python','others','2004-05-14','2026-07-01','09:40:00','2026-06-15 10:45:00',2004,FALSE,'Probation','Trainee developer.','Programming training.','Learning software development.');



select * from employees;

-- Part 4 — TIMESTAMP Requirement

-- For created_at:

-- The employee creation date and time should automatically be captured by MySQL.

-- For updated_at:

-- The employee modification date and time should automatically change whenever the employee record is updated.

-- Then:

-- Insert an employee.
-- Check created_at and updated_at.
-- Update the employee's name.
-- Check both timestamps again.
-- Verify that created_at remains unchanged.
-- Verify that updated_at changes.

-- This follows the timestamp behavior covered in your notes.

UPDATE employees set employee_name = "Rahul Verma"
where employee_id = 1;

-- Part 5 — DDL Operations

-- After creating and inserting data into employees, perform the following operations.

-- ALTER TABLE
-- Add a column:
-- phone_number
-- Add a column:
-- email
-- Modify the size of employee_name.
-- Modify the size of employee_code.
-- Rename short_note to:
-- employee_note

ALTER TABLE employee 
ADD column phone_number,
ADD column email,
MODIFY employee_name varchar(50),
MODIFY employee_code char(8),
RENAME short_note to employee_note;

-- Drop the email column.
-- Drop the phone_number column.

alter table employee
drop column email,
drop column  phone_number;

select "email and phone number column are deleted" as message;

-- AUTO_INCREMENT using ALTER

-- Create another table:

-- employee_documents

-- Initially create document_id as a normal integer column.


desc employee;

create table employee_documents (
    document_id int,
    document_name varchar(40),
    employee_name varchar(40)

);


-- Then use ALTER TABLE to make document_id an AUTO_INCREMENT column.

alter table employee_documents 
modify document_id int not null AUTO_INCREMENT
add primary key(document_id);

-- CREATE TABLE AS SELECT

-- Create:

-- employee_backup

-- using the existing employees table.

-- Copy the employee data into it.

create table employee_backup as 
select * from employee;

TRUNCATE table employee_backup;

-- TRUNCATE

-- Create:

-- employee_test

create table emplyee_test (
    employee_id int primary key ,
    employee_name varchar(50),
    Department varchar(20)
);

-- Insert some records.

INSERT INTO emplyee_test (employee_id, employee_name, Department)
VALUES
(1, 'Rahul', 'IT'),
(2, 'Priya', 'HR'),
(3, 'Amit', 'Finance'),
(4, 'Sneha', 'IT'),
(5, 'Rohit', 'Marketing');

desc employee_test;

-- Display the records.

select*from employee_test;


-- TRUNCATE the table.

TRUNCATE table employee_test;

-- Display the records again.

select * from employee_test;


-- Verify that the table still exists.
-- DROP

show table employee_test;

drop table employees;

-- Finally:

-- Drop employee_test.
-- Drop employee_documents.
-- Verify the tables using SHOW TABLES.


drop table employee_test;
drop table employee_documents;
show table employee_test;
show table employee_documents;


