
-- Assignment 1 student management system

-- Q1. Create a database named school_db and use the database.

CREATE DATABASE IF NOT EXISTS school_db;

use school_db;

-- Q2. Create a table named student with:

CREATE TABLE IF NOT EXISTS student(
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    student_name VARCHAR(50),
    age INT,
    course VARCHAR(50),
    city VARCHAR(50),
    marks INT
    );


-- Q3. Insert the following 10 student records:

INSERT IGNORE INTO  student (student_name,age,course,city,marks)
VALUES 
    ('Rahul Sharma',21,'Python','Indore', 85),
    ('Priya Verma',22,'Java','Bhopal', 78),
    ('Amit Singh',20,'Python','Indore', 92),
    ('Neha Patel',23,'Java','Pune',81),
    ('Rohit Mehta',21,'Python','Mumbai',88),
    ('Sneha Jain',22,'Java','Indore',76),
    ('Karan Gupta',20,'Python','Delhi',95),
    ('Pooja Mishra',23,'Java','Bhopal',84),
    ('Ankit Tiwari',21,'Python','Pune',79),
    ('Riya Kapoor',22,'Java','Mumbai',91);


-- Q4. Display the structure of the student table using DESC.

DESC student;

-- Q5. Display all records from the student table.

SELECT * FROM student;

DROP TABLE student;
