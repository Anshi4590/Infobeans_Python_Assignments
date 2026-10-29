create database if not exists Employee_Management_system;

use Employee_Management_system;

create table if not exists employee(

    employee_id int primary key auto_increment,
    employee_name varchar(50),
    department varchar(50),
    city varchar(50),
    salary decimal(10,2),
    joining_date date,
    experience int unsigned,
    age smallint unsigned,
    gender enum("female","male","others"),
    employment_type enum("full_time","part_time","contract","intern"),
    skills set("java","python","spring","react","sql"),
    email varchar(50),
    manager_id varchar(50)
);




INSERT INTO employees
(employee_id, employee_name, department, city, salary, joining_date,
 experience, age, gender, employment_type, skills, email, manager_id)
VALUES
(1, 'Aarav Sharma', 'IT', 'Indore', 75000, '2020-05-15', 6, 29,
 'MALE', 'FULL_TIME', 'JAVA,SQL', 'aarav@company.com', NULL),

(2, 'Sneha Patel', 'Finance', 'Pune', 65000, '2021-08-10', 5, 28,
 'FEMALE', 'CONTRACT', 'PYTHON,SQL', 'sneha@company.com', 1),

(3, 'Amit Verma', 'HR', 'Delhi', 38000, '2022-03-20', 3, 26,
 'MALE', 'INTERN', 'SQL', NULL, 1),

(4, 'Simran Gupta', 'Development', 'Indore', 90000, '2023-06-12', 4, 30,
 'FEMALE', 'FULL_TIME', 'JAVA,SPRING,SQL', 'simran@company.com', 1),

(5, 'Sahil Khan', 'IT', 'Mumbai', 55000, '2024-01-05', 3, 27,
 'MALE', 'PART_TIME', 'PYTHON,REACT', NULL, 2),

(6, 'Ananya Singh', 'Marketing', 'Bhopal', 42000, '2025-02-18', 2, 25,
 'FEMALE', 'INTERN', 'PYTHON', 'ananya@company.com', NULL),

(7, 'Mohit Jain', 'Finance', 'Pune', 82000, '2019-11-25', 8, 34,
 'MALE', 'FULL_TIME', 'JAVA,SQL,SPRING', 'mohit@company.com', 2),

(8, 'Sakshi Mishra', 'IT', 'Delhi', 48000, '2025-07-01', 1, 24,
 'FEMALE', 'PART_TIME', 'REACT,SQL', 'sakshi@company.com', 4),

(9, 'Arjun Mehta', 'Development', 'Indore', 35000, '2023-09-14', 2, 23,
 'MALE', 'CONTRACT', 'PYTHON,JAVA', NULL, 4),

(10, 'Aditi Rao', 'Development', 'Delhi', 60000, '2026-02-10', 1, 22,
 'FEMALE', 'FULL_TIME', 'PYTHON,REACT,SQL', NULL, NULL);


select * from employee;


-- 1. Find employees from IT, Finance, or HR who joined after '2023-01-01', have salary between ₹40,000 and ₹90,000, and have experience greater than 3 years.

select "Find employees from IT, Finance, or HR who joined after '2023-01-01', have salary between ₹40,000 and ₹90,000, and have experience greater than 3 years." as query_01;

select * from employee 
where department in ("it","finance","hr")and
joining_date>2023-01-01 and salary between 40000 and 90000
and experience>3;

-- q2. Find employees whose email is NULL, salary is greater than ₹50,000, and joining date is after '2022-01-01'.

select 'Find employees whose email is NULL, salary is greater than ₹50,000, and joining date is after '2022-01-01'.'as query_02;

select * from employee 
where email is null and
salary>50000 and joining_date>2022-01-01;


-- q3. Find employees whose manager_id is NOT NULL, department is not HR, and salary is either below ₹40,000 or above ₹80,000.

select "Find employees whose manager_id is NOT NULL, department is not HR, and salary is either below ₹40,000 or above ₹80,000.
" as query_03;

select * from employee
where manager_id is not null and 
department <>"hr" and (salary >80,000 or salary<40000);

-- q4. Find employees from Indore, Pune, or Delhi who joined between '2022-01-01' and '2025-12-31', have salary greater than ₹45,000, and experience of at least 3 years.


select "Find employees from Indore, Pune, or Delhi who joined between '2022-01-01' and '2025-12-31', have salary greater than ₹45,000, and experience of at least 3 years." as query_04;


select * from employee 
where city in ("indore","pune","delhi")
and joining_date>2022-01-01;

-- q5. Find employees who are FULL_TIME, have JAVA or PYTHON in their skills, salary greater than ₹50,000, and email is NOT NULL.

select "Find employees who are FULL_TIME, have JAVA or PYTHON in their skills, salary greater than ₹50,000, and email is NOT NULL." as query_05;


select * from employee
where employment_type = "full_time" and
skills in ('java','python') and
salary>50000 and email is not null;


-- q6. Find employees whose name starts with A or S, joining date is after '2023-01-01', salary is between ₹30,000 and ₹80,000, and age is between 25 and 35.

select 'Find employees whose name starts with A or S, joining date is after '2023-01-01', salary is between ₹30,000 and ₹80,000, and age is between 25 and 35.' as query_06;


select * from employee
where (employee_name like as 'A%'
or employee_name like as 'S%') and joining_date = '2023-01-01'
and salary between 30000 and 80000 and
age between 25 and 35;

-- q7. Find employees who belong to IT or Finance, have JAVA in skills, experience greater than 4 years, and salary is NOT between ₹50,000 and ₹80,000.

select 'Find employees who belong to IT or Finance, have JAVA in skills, experience greater than 4 years, and salary is NOT between ₹50,000 and ₹80,000.'as query_07;

select * from employee
where department in ('it','finance') and
skills = 'java' and experience>4 and salary not between 50000 and 80000;


-- q8. Find employees whose department is IT, HR, or Marketing, city is not Mumbai, salary is greater than ₹40,000, and either email is NULL or manager_id is NULL.

select 'Find employees whose department is IT, HR, or Marketing, city is not Mumbai, salary is greater than ₹40,000, and either email is NULL or manager_id is NULL.' as query_08;


select * from employee
where department in('it','hr','marketing')
and city <> 'mumbai' and
salary>40000 and (email is null or manager_id is null);


-- Q9. Find employees who joined after '2022-01-01', are not INTERN, have salary greater than ₹45,000, and have either SQL or PYTHON in their skills.

select 'Find employees who joined after '2022-01-01', are not INTERN, have salary greater than ₹45,000, and have either SQL or PYTHON in their skills.' as query_09;

select * from employee
where joining_date > 2022-01-01 and employee_type<>'intern'
and salary>45000 and skills in ('sql','python')


