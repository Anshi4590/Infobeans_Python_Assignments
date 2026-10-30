create database if not exists a07;

use a07;

create table if not exists employees
(
    id int primary key auto_increment,
    name varchar(50) not null,
    dept enum("hr","it","finance"),
    job_role enum("manager","recruiter","developer","tester","analyst"),
    salary decimal(10,2),
    hire_date date

);

insert ignore into employees(name,dept,job_role,salary,hire_date)

values ('Alice', 'HR','Manager',6000.00 , '2022-01-15'),
('Bob', 'HR', 'Recruiter', 4000.00 ,'2023-03-20'),
('Charlie', 'IT', 'Developer',5000.00 ,'2022-07-25'),
('David' ,'IT' ,'Developer' ,5500.00,'2021-12-05'),
('Eve', 'IT', 'Tester', 4500.00, '2023-06-10'),
('Frank', 'IT', 'Tester',4800.00, '2023-09-12'),
('Grace', 'Finance', 'Analyst', 5200.00, '2021-11-18'),
('Hank', 'Finance', 'Analyst', 5300.00, '2022-04-30'),
('Ivy', 'Finance', 'Manager', 7000.00, '2023-08-14'),
('Jack', 'HR', 'Recruiter', 4200.00, '2022-10-05');


-- 01. Find the total number of employees in each department.


select dept ,count(*) from employees
group by dept;

-- 02. Find the average salary of employees in each job role.


select job_role,avg(salary) from employees
group by job_role;

-- 03. Find the highest salary in the IT department.

select dept,max(salary) from employees
group by dept
having dept = "it";

-- 04. Find the lowest salary among all employees.

select min(salary)
from  employees;

-- 05. Count the number of employees who joined after January 1, 2023.

select hire_date ,count(*) as employees_count from employees
group by hire_date
having hire_date > "2023-01-01";

-- 06. Find the total salary paid in each department.

select dept ,sum(salary) from employees
group by dept;


-- 07. Find the job role that has the highest total salary payout.

select "Find the job role that has the highest total salary payout." as query_07;

select job_role , sum(salary) as total_salary from employees
group by job_role
order by  total_salary desc
limit 1;
 
-- 08. Find the average salary of employees who joined after 2022.

select "Find the average salary of employees who joined after 2022." as query_08;

select avg(salary) as avg_salary from employees
where year(hire_date)>2022;


-- 09. Find departments where the total salary exceeds 10,000.

select "Find departments where the total salary exceeds 10,000." as query_09;

select dept ,sum(salary) as total_salary from employees
group by dept
having total_salary>10000;

-- 10. Find the department with the highest number of employees.

select "Find the department with the highest number of employees." as query_10;

select dept,count(*) as total_employees from employees

group by dept
order by total_employees desc
limit 1;



drop table employees;

 


