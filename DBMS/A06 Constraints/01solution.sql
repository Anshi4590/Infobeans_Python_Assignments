-- Create a table named `Students` with the following columns and constraints
create database if not exists a06;
use a06;


drop table if exists student;

CREATE TABLE IF NOT EXISTS student(

    studentid int primary key ,
    name varchar(50) not null,
    age int check(age between 18 and 25),
    marks decimal(5,2) check(marks between 0 and 100)

);

insert into student (studentid ,name ,age ,marks )
values
 (101, 'Alice', 20, 85.5),
 (102, 'Bob', 19, 90.0),
 (103, 'Charlie', 22, 100.0),
 (104, 'David', 24, 75.0);


select * from student;



drop table if exists patient;

create table if not exists patient(

    patientid int primary key,
    patientname  varchar(50) not null,
    age int check(age between 1 and 100),

    admissionstatus ENUM('admitted', 'discharged')
    DEFAULT 'admitted',

    treatmentcost decimal(10,2) check(treatmentcost>=1000)

);


insert into patient(patientid, patientname , age , admissionstatus, treatmentcost) 
values
(201, 'Michael', 25, 'Admitted', 5000),
(202, 'Linda', 100, 'Admitted', 8000),
(203, 'David', 40, DEFAULT, 1200),
(204, 'Sarah', 30, 'Discharged', 1000);


select * from patient;

drop table if exists gymmembers;

create table if not exists gymmembers(

    memberid int primary key,
    membername varchar(50) not null,
    membershiptype ENUM('basic', 'premium', 'vip')
    DEFAULT 'basic',
    monthlyfee  decimal(6,2) check(monthlyfee>=500)

);

insert into gymmembers(memberid,membername,membershiptype,monthlyfee) values

(501, 'John', 'Premium', 1200),
(502, 'Emma', 'basic', 800),
(503, 'Daniel', DEFAULT, 700),
(504, 'Sophia', 'VIP', 500);


select * from gymmembers;