-- Design and create a Library Management System database in MySQL

create database if not EXISTS Library_Management_System;

use Library_Management_System;

create table  if not EXISTS books
(

    book_id int primary key AUTO_INCREMENT,
    book_title varchar(50) not null,
    author_name varchar(20) not null,
    ISBN_number bigint ,
    price decimal(10,2),
    number_of_copies smallint unsigned not null default 0,
    book_category enum(        
        'FICTION',
        'SCIENCE',
        'TECHNOLOGY',
        'HISTORY',
        'EDUCATION',
        'FANTASY',
        'BIOGRAPHY',
        'OTHER'
    )not null default 'OTHER',
    Publication_date date,
    is_available BOOLEAN,
    books_description mediumtext

    );


create table students(
    student_id int primary key AUTO_INCREMENT,
    student_name varchar(50) not null,
    registration_number varchar(20),
    age smallint unsigned,
    gender enum("male","female","others"),
    birth_date date,
    contact_number bigint unsigned,
    email varchar(50),
    is_active boolean not null default true,
    student_register_date date not null default(current_date)
);


create table book_issue(
    student_name varchar(50) not null,
    book_name varchar(20) not null,
    issue_date date,
    expected_return_date date,
    actual_return_date date,
    fine_amount decimal(10,2),
    is_returned  boolean,
    remarks varchar(100),
    created_at timestamp default current_timestamp

);


INSERT INTO books
(book_title, author_name, ISBN_number, price, number_of_copies,
 book_category, Publication_date, is_available, books_description)
VALUES
('The Alchemist', 'Paulo Coelho', '9780061122415', 299.00, 5, 'FICTION', '1988-01-01', TRUE, 'A story about dreams and destiny'),
('Wings of Fire', 'A P J Abdul Kalam', '9788173711466', 350.00, 4, 'BIOGRAPHY', '1999-01-01', TRUE, 'Autobiography of APJ Abdul Kalam'),
('Clean Code', 'Robert Martin', '9780132350884', 650.00, 3, 'TECHNOLOGY', '2008-08-01', TRUE, 'A guide to writing clean code'),
('Brief History', 'Stephen Hawking', '9780553380163', 450.00, 2, 'SCIENCE', '1988-04-01', TRUE, 'An introduction to the universe'),
('The Hobbit', 'J R R Tolkien', '9780547928227', 399.00, 0, 'FANTASY', '1937-09-21', FALSE, 'A fantasy adventure story'),
('India After Gandhi', 'Ram Guha', '9780060198817', 599.00, 3, 'HISTORY', '2007-08-15', TRUE, 'History of modern India'),
('Think Again', 'Adam Grant', '9781984878106', 499.00, 6, 'EDUCATION', '2021-02-02', TRUE, 'Learn to rethink your opinions'),
('The Silent Patient', 'Alex Michaelides', '9781250301697', 320.00, 2, 'FICTION', '2019-02-05', TRUE, 'A psychological thriller'),
('Cosmos', 'Carl Sagan', '9780345539434', 550.00, 0, 'SCIENCE', '1980-01-01', FALSE, 'An exploration of the universe'),
('Harry Potter', 'J K Rowling', '9780747532699', 450.00, 7, 'FANTASY', '1997-06-26', TRUE, 'A young wizard begins his journey');



INSERT INTO students
(student_name, registration_number, age, gender, birth_date,
 contact_number, email, is_active)
VALUES
('Rahul Sharma', 'REG001', 21, 'male', '2005-01-15', 9876500001, 'rahul@example.com', TRUE),
('Priya Verma', 'REG002', 20, 'female', '2006-03-22', 9876500002, 'priya@example.com', TRUE),
('Amit Patel', 'REG003', 22, 'male', '2004-06-10', 9876500003, 'amit@example.com', TRUE),
('Sneha Singh', 'REG004', 19, 'female', '2007-02-18', 9876500004, 'sneha@example.com', TRUE),
('Rohit Jain', 'REG005', 23, 'male', '2003-11-05', 9876500005, 'rohit@example.com', TRUE),
('Neha Gupta', 'REG006', 21, 'female', '2005-07-12', 9876500006, 'neha@example.com', TRUE),
('Karan Mehta', 'REG007', 20, 'male', '2006-09-08', 9876500007, 'karan@example.com', TRUE),
('Pooja Yadav', 'REG008', 22, 'female', '2004-12-20', 9876500008, 'pooja@example.com', FALSE),
('Arjun Rao', 'REG009', 21, 'male', '2005-04-25', 9876500009, 'arjun@example.com', TRUE),
('Ananya Das', 'REG010', 20, 'female', '2006-08-14', 9876500010, 'ananya@example.com', TRUE);



INSERT INTO book_issue
(student_name, book_name, issue_date, expected_return_date,
 actual_return_date, fine_amount, is_returned, remarks)
VALUES
('Rahul Sharma', 'The Alchemist', '2026-09-01', '2026-09-15', '2026-09-14', 0.00, TRUE, 'Returned on time'),
('Priya Verma', 'Clean Code', '2026-09-03', '2026-09-17', NULL, 0.00, FALSE, 'Not returned yet'),
('Amit Patel', 'Wings of Fire', '2026-09-05', '2026-09-19', '2026-09-22', 30.00, TRUE, 'Returned late'),
('Sneha Singh', 'The Hobbit', '2026-09-07', '2026-09-21', NULL, 0.00, FALSE, 'Pending return'),
('Rohit Jain', 'Cosmos', '2026-09-08', '2026-09-22', '2026-09-20', 0.00, TRUE, 'Returned early'),
('Neha Gupta', 'Think Again', '2026-09-10', '2026-09-24', '2026-09-27', 30.00, TRUE, 'Three days late'),
('Karan Mehta', 'Harry Potter', '2026-09-12', '2026-09-26', NULL, 0.00, FALSE, 'Book still with student'),
('Pooja Yadav', 'Brief History', '2026-09-14', '2026-09-28', '2026-09-28', 0.00, TRUE, 'Returned on due date'),
('Arjun Rao', 'India After Gandhi', '2026-09-16', '2026-09-30', NULL, 0.00, FALSE, 'Awaiting return'),
('Ananya Das', 'The Silent Patient', '2026-09-18', '2026-10-02', '2026-10-05', 30.00, TRUE, 'Returned three days late');


desc table books;
desc table students;
desc table book_issue;

SELECT * FROM books;

SELECT * FROM students;

SELECT * FROM book_issue;


show databases;

show tables;

drop database if exists Library_Management_System;