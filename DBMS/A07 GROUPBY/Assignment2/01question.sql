create database if not exists a07;

use a07;

create table if not exists staff_delete (

    staff_id int primary key auto_increment,
    staff_name varchar(50),
    department varchar(50),
    city varchar(50),
    salary decimal(10,2),
    experince int,
    age int,
    joining_date date,
    status varchar(20)
);

insert ignore into staff_delete values
('Aarav', 'IT', 'Indore', 48000, 3, 26, '2022-04-15', 'Active'),
('Bhavna', 'HR', 'Bhopal', 56000, 5, 31, '2020-08-20', 'Active'),
('Chetan', 'Finance', 'Delhi', 62000, 7, 35, '2018-03-10', 'Active'),
('Divya', 'IT', 'Pune', 78000, 9, 38, '2016-11-05', 'Active'),
('Eshan', 'Sales', 'Indore', 51000, 4, 29, '2021-06-18', 'Inactive'),
('Farah', 'HR', NULL, 68000, 6, 34, '2019-01-25', 'Active'),
('Gaurav', 'Finance', 'Mumbai', 74000, 8, 40, '2017-09-12', 'Active'),
('Heena', 'IT', 'Delhi', 59000, 5, 30, '2020-02-17', 'Inactive'),
('Ishaan', 'Sales', 'Pune', 45000, 2, 25, '2023-01-10', 'Active'),
('Jaya', 'HR', 'Indore', 72000, 7, 36, '2018-07-22', 'Active');



-- Q1. Delete the employee whose name is Aarav using his staff_id.

delete from staff_delete
where staff_id = 1;

select * from staff_delete;


-- Q2. Delete all employees who belong to the Sales department.

delete from staff_delete
where department = "sales";

select * from staff_delete;



-- Q3. Delete all employees whose salary is below ₹50,000.


delete from staff_delete
where salary <50000;
select* from staff_delete;


-- Q4. Delete all employees who belong to HR and have at least 5 years of experience.

delete from staff_delete
where department = "hr" and experience>=5;

select* from staff_delete;


-- Q5. Delete all employees who are from Indore or Bhopal.

delete from staff_delete
where city in ("indore","bhopal");

select* from staff_delete;


-- Q6. Delete all employees who belong to neither IT nor Finance.

delete from staff_delete
where department not in("it","finance");

select* from staff_delete;


-- Q7. Delete all employees whose salary is between ₹50,000 and ₹65,000, inclusive.

delete from staff_delete
where salary between 50000 and 65000;

select* from staff_delete;


-- Q8. Delete all employees who have less than 5 years of experience and whose status is Inactive.

delete from staff_delete
where status = "inactive" and experience<5;

select* from staff_delete;


-- Q9. Delete all employees whose names start with the letter D.

delete from staff_delete
where staff_name like "D%";

select* from staff_delete;


-- Q10. Delete all employees whose city is NULL.

delete from staff_delete
where city is null;

select* from staff_delete;


-- Q11. Delete all employees who joined before January 1, 2020 and have a salary of at least ₹60,000.

delete from staff_delete
where joining_date<"2020-01-01" and salary>=60000;

select* from staff_delete;


-- Q12. Delete all employees who belong to IT or HR, have at least 3 years of experience, and earn less than ₹70,000.

delete from staff_delete
where department in ("hr" , "it")  and experience>=3 and salary<70000;

select* from staff_delete;


-- Q13. Delete all employees who are not from Sales, have salary above ₹55,000, and are currently Active.

delete from staff_delete
where department <>"sales" and salary>55000 and status = "active";

select* from staff_delete;


-- Q14. Delete all employees who belong to Finance or HR and have a salary below ₹65,000.

delete from staff_delete
where department in("hr","finance") and salary<65000;

select* from staff_delete;


-- Q15. Delete the employee with the lowest salary from the table. If multiple employees have the same lowest salary, delete only one employee.

delete from staff_delete order by salary asc limit 1;
select* from staff_delete;



-- Q16. Delete the employee with the highest salary from the table. If multiple employees have the same highest salary, delete only one employee.

delete from staff_delete order by salary desc limit 1;

select* from staff_delete;


-- Q17. Delete only the lowest-paid employee who belongs to IT or HR, has at least 3 years of experience, and earns less than ₹70,000.

delete from staff_delete
where department in("hr","finance") and experience>=3 and salary<70000
order by salary asc limit 1;

select* from staff_delete;


-- Q18. Delete only the highest-paid Active employee having at least 5 years of experience.

delete from staff_delete
where status = "active" and experience>=5
order by salary desc limit 1;

select* from staff_delete;

-- Q19. Delete only the lowest-paid employee who is neither from HR nor Sales, has at least 3 years of experience, and earns below ₹70,000.

delete from staff_delete
where department  not in("hr","sales") and experience>=3 and salary<70000
order by salary asc limit 1;

select* from staff_delete;

-- Q20. Delete all employees who satisfy either of the following conditions:

-- IT employees having at least 5 years of experience and salary below ₹80,000
-- Finance employees having salary below ₹65,000


delete from staff_delete
where department in("it") and experience>=5 and salary<80000 or
department = "finance" and salary <65000;

select* from staff_delete;