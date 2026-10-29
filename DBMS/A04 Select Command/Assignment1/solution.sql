-- Create an employees table with the following information:

-- Employee ID
-- Employee Name
-- Department
-- City
-- Salary
-- Experience in years
-- Age
-- Joining Date


create database if not exists employee_management_system;

use employee_management_system;


create table if not exists employee(

    employee_id int primary key auto_increment,
    employee_name varchar(50),
    department varchar(50),
    city varchar(20),
    salary decimal(10,2),
    experience decimal(4,1) default 0.0,
    age int unsigned,
    joining_date date
    
);


-- Insert at least 15 employees with different values.

INSERT IGNORE INTO employee (
    employee_name,
    department,
    city,
    salary,
    experience,
    age,
    joining_date
)
VALUES
('Aarav Sharma', 'IT', 'Indore', 75000.00, 5.0, 28, '2021-03-15'),
('Priya Verma', 'HR', 'Bhopal', 45000.00, 3.0, 25, '2023-06-10'),
('Rohan Patel', 'Finance', 'Pune', 65000.00, 6.0, 32, '2020-01-20'),
('Sneha Gupta', 'Sales', 'Mumbai', 50000.00, 4.0, 27, '2022-08-12'),
('Vikram Singh', 'IT', 'Bangalore', 90000.00, 8.0, 35, '2020-11-05'),
('Ananya Joshi', 'HR', 'Indore', 40000.00, 2.0, 24, '2024-02-18'),
('Karan Mehta', 'Finance', 'Mumbai', 70000.00, 7.0, 33, '2021-07-25'),
('Pooja Mishra', 'Sales', 'Bhopal', 35000.00, 1.0, 22, '2025-04-01'),
('Rahul Yadav', 'IT', 'Pune', 80000.00, 6.0, 30, '2022-05-14'),
('Neha Agrawal', 'Finance', 'Bangalore', 60000.00, 4.0, 29, '2023-09-11'),
('Amit Tiwari', 'Sales', 'Indore', 50000.00, 3.0, 26, '2024-07-08'),
('Kavya Nair', 'IT', 'Mumbai', 100000.00, 10.0, 40, '2020-06-22'),
('Sahil Jain', 'HR', 'Pune', 45000.00, 2.0, 23, '2026-01-15'),
('Ishita Rao', 'Finance', 'Bhopal', 65000.00, 5.0, 31, '2022-12-03'),
('Dev Malhotra', 'IT', 'Bangalore', 75000.00, 9.0, 38, '2021-10-19');


select * from employee;

-- Q1- Employees whose salary is greater than ₹60,000.

select "Employees whose salary is greater than ₹60,000" as query_01;

select * from employee 
where salary>60000;

-- Q2 Employees whose salary is less than ₹50,000.

select "Employees whose salary is less than ₹50,000." as query_02;


select * from employee
where salary<50000;

-- Q3 Employees whose age is greater than 30.

select "Employees whose age is greater than 30." as query_03;

select * from employee
where age>30;


-- Q4 Employees whose experience is greater than or equal to 5 years.

select "Employees whose experience is greater than or equal to 5 years." as query_04;


select * from employee
where experience>=5;


-- Q5 Employees working in IT or Finance.

select "Employees working in IT or Finance." as query_05;

select * from employee
where department in("IT","finance");

-- Q6 Employees working in IT, HR, or Sales.

select "Employees working in IT, HR, or Sales." as query_06;

select * from employee
where department in("IT","HR","sales");

-- & Question-07 Employees not working in IT or HR.
select "Employees not working in IT or HR." as query_07;


select * from employee
where department not in("IT","HR");


-- & Question-08 Employees from Indore or Pune.
select "Employees from Indore or Pune." as query_08;

select * from employee
where city in("indore","pune");


-- & Question-09 Employees who are not from Indore, Mumbai, or Bhopal.
select "Employees who are not from Indore, Mumbai, or Bhopal." as query_9;

select * from  employee
where city not in ("indore","mumbai","bhopal");

-- & Question-10 Employees whose salary is between ₹40,000 and ₹70,000.
select "Employees whose salary is between ₹40,000 and ₹70,000." as query_10;


select * from employee
where salary between 40000 and 70000;


-- & Question-11 Employees whose age is between 25 and 35.

select "Employees whose age is between 25 and 35." as Query_11;


select * from employee
where age between 25 and 35;


-- Question-12 Employees whose experience is between 3 and 7 years.

select "Employees whose experience is between 3 and 7 years." as query_12;

select * from employee
where experience between 3 and 7;

-- Question-13 Employees who joined between 2022 and 2025.

select "Employees who joined between 2022 and 2025." as query_13;

select * from employee
where year(joining_date) between 2022 and 2025;

-- q14 Employees who joined before 2023.

select "Employees who joined before 2023." as query_14;


select * from employee
where year(joining_date)<2023;

-- Q15 Employees who joined after 2024.

select "Employees who joined after 2024." as query_15;

select * from employee
where year(joining_date)>2024;


-- Q16 Employees from Indore AND working in IT.

select "Employees from Indore AND working in IT." as query_16;

select * from employee
where city = "indore" and department ="it";


-- Q17 Employees working in IT AND having salary greater than ₹70,000.

select "Employees working in IT AND having salary greater than ₹70,000." as Query_17;


select * from employee
where department = "it" and salary>70000;

-- Q18 Employees whose salary is between ₹50,000 and ₹90,000 AND experience is greater than 4 years.

select "Employees whose salary is between ₹50,000 and ₹90,000 AND experience is greater than 4 years." as query_18;


select * from employee
where salary between 50000 and 90000 and experience>4; 

-- Q19 Employees working in IT or Finance AND salary greater than ₹60,000.

select "Employees working in IT or Finance AND salary greater than ₹60,000." as query_19;


select * from employee
where department in ("it","finance") and salary>60000;

-- Q20 Employees whose joining date is between 2021 and 2024 AND salary is greater than ₹50,000.

select "Employees whose joining date is between 2021 and 2024 AND salary is greater than ₹50,000" as query_20;


select * from employee 
where year(joining_date) between 2021 and 2024 
and salary>50000;


-- Q21 Employees whose salary is not between ₹40,000 and ₹70,000.

select "Employees whose salary is not between ₹40,000 and ₹70,000." as query_21;


select * from employee
where salary not between 40000 and 70000;


-- Q22 Employees whose department is not IT, HR, or Sales.

select "Employees whose department is not IT, HR, or Sales." as query_22;

select * from employee
where department not in ("it","hr","sales");


-- Q23 Employees whose joining date is not between 2022 and 2025.

select "Employees whose joining date is not between 2022 and 2025." as query_23;

select * from employee
where year(joining_date) not between 2022  and 2025;


-- Q24 Employees from Indore or Pune, whose salary is between ₹45,000 and ₹80,000, and whose experience is more than 3 years.

select "Employees from Indore or Pune, whose salary is between ₹45,000 and ₹80,000, and whose experience is more than 3 years." as query_24;


select * from employee
where city in ("indore","pune") and 
salary between 45000 and 80000 and 
experience>3;

-- Q25 Employees who did not join between 2020 and 2023 and whose salary is greater than ₹60,000.


select "Employees who did not join between 2020 and 2023 and whose salary is greater than ₹60,000." as query_25;


select * from employee
where year(joining_date) not between 2020 and 2023
and salary>60000;

-- Q26 Find employees who are from Indore, Pune, or Bangalore, whose salary is between ₹50,000 and ₹90,000, and whose experience is at least 4 years.


select "Find employees who are from Indore, Pune, or Bangalore, whose salary is between ₹50,000 and ₹90,000, and whose experience is at least 4 years." as query_26;


select * from employee
where city in("indore","pune","bangalore") and
salary between 50000 and 90000 and 
experience>=4;

-- Q27 Find employees who are not from Bhopal or Mumbai, are not working in HR, and joined between 2021 and 2025.

select "Find employees who are not from Bhopal or Mumbai, are not working in HR, and joined between 2021 and 2025." as query_27;


select * from employee
where city not in ("bhopal","mumbai") and
department!="hr" and year(joining_date) between 2021 and 2025;

-- Q28 Find employees working in IT or Finance, whose salary is greater than ₹60,000, whose age is between 25 and 35, and who joined after 2022.

select "Find employees working in IT or Finance, whose salary is greater than ₹60,000, whose age is between 25 and 35, and who joined after 2022." as query_28;


select * from employee
where department in("it","finance") and
salary >60000 and 
age between 25 and 35 
and year(joining_date)>2022;

-- Q29 Find employees whose salary is NOT between ₹40,000 and ₹75,000, whose experience is between 2 and 8 years, and who are not working in Sales.


select "Find employees whose salary is NOT between ₹40,000 and ₹75,000, whose experience is between 2 and 8 years, and who are not working in Sales." as query_29;


select * from employee
where salary not between 40000 and 75000
and experience between 2 and 8 and 
department!="sales";


-- Q30 Find employees who are from Indore or Pune, working in IT, Finance, or HR, with salary between ₹45,000 and ₹85,000, and who joined between 2020 and 2024.


select "Find employees who are from Indore or Pune, working in IT, Finance, or HR, with salary between ₹45,000 and ₹85,000, and who joined between 2020 and 2024." as query_30;


select * from employee 
where city in("indore","pune")
and department in ("it","hr","finance")
and salary between 45000 and 85000
and year(joining_date) between 2020 and 2024;


drop database employee_management_system;