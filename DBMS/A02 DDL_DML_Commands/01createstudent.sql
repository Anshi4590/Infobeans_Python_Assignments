-- QNO  1: Create and Populate students Table
-- Columns:

-- id INT

-- name VARCHAR(100)

-- age INT

-- gender VARCHAR(10)

-- address VARCHAR(150)

-- phone VARCHAR(15)

-- email VARCHAR(100)

-- Task:


CREATE DATABASE Batch19;

USE Batch19;


CREATE TABLE IF NOT EXISTS students(

    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    student_address VARCHAR(150),
    phone VARCHAR(15),
    email VARCHAR(100)
    
);


-- Insert 5 different student records with dummy data.

INSERT IGNORE INTO students(student_id,student_name,age,gender,student_address,phone,email)
VALUES
    (1,'Anshika Sahu',23,'Female','Indore',8974378821,'anshikasahu9926@gmail.com'),
    (2,'Devanshi Raghuwanshi',24,'Female','GanjBasoda',9923341872,'devanshi8921@gmail.com'),
    (3,'Dipanshu Gupta',20,'Male','Jhabua',9978527823,'dipanshu2276@gmail.com'),
    (4,'Ishan Sharma',22,'Male','Nagada',8892236781,'ishansharma6742@gmail.com'),
    (5,'Eshan Jain',21,'Male','Bhopal',8974378821,'jainex9090@gmail.com');



SELECT * FROM students;

