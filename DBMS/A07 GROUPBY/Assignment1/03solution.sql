-- 01.Find the total number of employees in each department and display only those departments having more than 2 employees. (GROUP BY + HAVING)

select "Find the total number of employees in each department and display only those departments having more than 2 employees. (GROUP BY + HAVING)
" as query_01;

select dept ,count(*) as total_employees from employees
group by dept
having total_employees>2;

-- 02.Find the total salary paid in each department and display the results in descending order of total salary. (GROUP BY + ORDER BY)

select "Find the total salary paid in each department and display the results in descending order of total salary. (GROUP BY + ORDER BY)" as query_02;

select dept , sum(salary) as total_salary from employees
group by dept
order by total_salary desc;

-- 03.Find the job role that has the highest total salary payout, displaying only roles where total salary is above 10,000. (GROUP BY + HAVING + ORDER BY)

select "Find the job role that has the highest total salary payout, displaying only roles where total salary is above 10,000. (GROUP BY + HAVING + ORDER BY)" as query_03;

select job_role ,sum(salary) as total_salary from employees
group by job_role 
having total_salary >10000
order by total_salary desc;

-- 04.Find the average salary of employees who joined after 2022, displaying only job roles where the average salary is above 4500. (WHERE + GROUP BY + HAVING)

select "Find the average salary of employees who joined after 2022, displaying only job roles where the average salary is above 4500. (WHERE + GROUP BY + HAVING)
" as query_04;

select job_role, avg(salary) as avg from employees
where year(hire_date)>2022 
group by job_role
having avg>4500;

-- 05. Find departments where the total salary exceeds 10,000 and order the results in ascending order of department name. (GROUP BY + HAVING + ORDER BY)

select "Find departments where the total salary exceeds 10,000 and order the results in ascending order of department name. (GROUP BY + HAVING + ORDER BY)" as query_05;


select dept , sum(salary) as total_salary from employees
group by dept
having  total_salary >10000
order by dept asc;