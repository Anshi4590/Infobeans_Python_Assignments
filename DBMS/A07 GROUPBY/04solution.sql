-- Assignment 4: Student Analysis Using GROUP BY, HAVING and ORDER BY
-- Use the students table from Assignment 2.

-- Questions
-- Find the average marks in each subject and display only subjects where the average is above 80. (GROUP BY + HAVING)

select "Find the average marks in each subject and display only subjects where the average is above 80. (GROUP BY + HAVING)" as query_01;

select subject,avg(marks) as avg  from students
group by subject 
having avg >80;

-- Find the total number of students in each class and order them by class in descending order. (GROUP BY + ORDER BY)


select "Find the total number of students in each class and order them by class in descending order. (GROUP BY + ORDER BY)
" as query_02;

select class , count(*) as total_students from students
group by class 
order by class desc;


-- Find the subject where students scored the highest average marks, displaying only subjects where the average is above 85. (GROUP BY + HAVING + ORDER BY)

select "Find the subject where students scored the highest average marks, displaying only subjects where the average is above 85. (GROUP BY + HAVING + ORDER BY)
" as query_03;

select subject , avg(marks) as avg from students
group by subject
having avg>85
order by avg desc;


-- Find the student who scored the highest marks overall. (ORDER BY + LIMIT 1)


select "Find the student who scored the highest marks overall. (ORDER BY + LIMIT 1)
" as querry_04;

select max(marks) as highest_marks from students;


-- Find the number of students in each class who scored more than 85, displaying only classes with more than 2 such students. (GROUP BY + HAVING)


select "Find the number of students in each class who scored more than 85, displaying only classes with more than 2 such students. (GROUP BY + HAVING)" as query_05;


select class , count(*) as total_students from students
where marks>85 
group by class
having total_students>2;