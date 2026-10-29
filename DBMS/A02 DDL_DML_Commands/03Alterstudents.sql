--
-- QNO  3: ALTER students Table


desc students;


-- Add a column dob DATE


ALTER TABLE students
ADD COLUMN dob DATE;


-- Rename column phone to mobile_number


ALTER TABLE students
RENAME COLUMN phone to mobile_number;


-- Modify column age to SMALLINT


ALTER TABLE students
MODIFY COLUMN age SMALLINT;


-- Drop column email

ALTER TABLE students 
DROP COLUMN email;



desc students;

