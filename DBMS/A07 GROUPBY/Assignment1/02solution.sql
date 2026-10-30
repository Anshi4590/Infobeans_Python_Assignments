create database if not exists student_performance_analysis;

use student_performance_analysis;


create table if not exists students(

    studentid int primary key auto_increment ,
    name  varchar(50),
    class int ,
    subject enum("math","science"),
    marks int,
    exam_date date
);


INSERT IGNORE INTO students
(name, class, subject, marks, exam_date)
VALUES
('John', 10, 'Math', 85, '2023-02-10'),
('Alice', 10, 'Science', 78, '2023-03-15'),
('Bob', 9, 'Math', 92, '2023-04-20'),
('David', 9, 'Science', 80, '2023-05-25'),
('Eve', 10, 'Math', 88, '2023-06-30'),
('Frank', 9, 'Science', 75, '2023-07-10'),
('Grace', 10, 'Math', 90, '2023-08-20'),
('Hank', 9, 'Math', 85, '2023-09-15'),
('Ivy', 10, 'Science', 82, '2023-10-10'),
('Jack', 9, 'Science', 79, '2023-11-05');



-- Query 01 - Find the total number of students in each class.
SELECT "Find the total number of students in each class." AS Query01;

select class ,count(*) from students 
group by class;


-- Query 02 - Find the highest marks scored in Math.
SELECT "Find the highest marks scored in Math." AS Query02;

select subject, max(marks) from students
group by subject 
having subject ="math"
;

-- Query 03 - Find the average marks in each subject.
SELECT "Find the average marks in each subject." AS Query03;


select subject ,avg(marks) as avg_marks from students
group by subject;


-- Query 04 - Find the total number of students who scored above 80.
SELECT "Find the total number of students who scored above 80." AS Query04;

select count(*) as total_students from students
where marks>80;


-- Query 05 - Find the number of students who took the exam in each month.
SELECT "Find the number of students who took the exam in each month." AS Query05;

select monthname(exam_date),count(*) as total_student from students

group by monthname(exam_date);




-- Query 06 - Find the subject where students scored the highest average marks.
SELECT "Find the subject where students scored the highest average marks." AS Query06;

select subject , avg(marks) as avg_marks from students
group by subject 
order by avg_marks desc
limit 1;


-- Query 07 - Find the student who scored the lowest marks in Science.
SELECT "Find the student who scored the lowest marks in Science." AS Query07;

select min(marks) from students
where subject ="science";



-- Query 08 - Find the number of students in each class who scored more than 85.
SELECT "Find the number of students in each class who scored more than 85." AS Query08;

select class , count(*) as total from students
where marks>85
group by class;



-- Query 09 - Find the average marks for each subject where the average is above 80.
SELECT "Find the average marks for each subject where the average is above 80." AS Query09;

select subject ,avg(marks) as avg_marks from students
group by subject
having avg_marks>80;



-- Query 10 - Find the student who scored the highest marks overall.
SELECT "Find the student who scored the highest marks overall." AS Query10;

select * from  students
order by marks desc limit 1;
 

drop table students;

