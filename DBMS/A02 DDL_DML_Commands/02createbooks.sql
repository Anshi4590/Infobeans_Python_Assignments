-- QNO  2: Create and Populate books Table
-- Columns:

-- book_id INT

-- title VARCHAR(150)

-- author VARCHAR(100)

-- genre VARCHAR(50)

-- publication_year INT

-- price DECIMAL(6,2)

-- publisher VARCHAR(100)

-- Task:

USE Batch19;

CREATE TABLE IF NOT EXISTS books(

    book_id INT PRIMARY KEY,
    title VARCHAR(150),
    author VARCHAR(100),
    genre VARCHAR(50),
    publication_year INT,
    price DECIMAL(6,2),
    publisher VARCHAR(100)

);

-- Insert 4 book records.



INSERT IGNORE INTO books(book_id, title, author, genre, publication_year)
VALUES
    (1, 'Wings of Fire', 'A. P. J. Abdul Kalam', 'Autobiography', 1999),
    (2, 'The Alchemist', 'Paulo Coelho', 'Fiction', 1988),
    (3, 'Atomic Habits', 'James Clear', 'Self-Help', 2018),
    (4, 'Harry Potter', 'J. K. Rowling', 'Fantasy', 1997);


SELECT * FROM books;