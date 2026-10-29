-- QNO 9:


-- You are designing a system to store movie reviews. Start with basic details and then evolve the table structure using ALTER, RENAME, TRUNCATE, and DROP, and perform INSERT operations at each stage.

--  Initial Table Creation:
-- Create a table movie_reviews with the following columns:

-- review_id INT

-- movie_title VARCHAR(150)

-- reviewer_name VARCHAR(100)

-- rating DECIMAL(2,1)

-- review_text TEXT


USE Batch19;


CREATE TABLE movie_reviews(

    review_id INT PRIMARY KEY , 
    movie_title VARCHAR(50), 
    reviewer_name VARCHAR(100), 
    rating DECIMAL(2,1), 
    review_text TEXT
    );


--  Insert 3 sample movie reviews

INSERT INTO movie_reviews
(review_id, movie_title, reviewer_name, rating, review_text)
VALUES
(1, 'The Odyssey', 'Anshika', 9.0, 'An epic journey about courage, survival, and the desire to return home.'),
(2, 'The Pursuit of Happyness', 'Anshika', 9.5, 'An inspiring movie about perseverance, struggle, and never giving up on your dreams.'),
(3, 'Me Before You', 'Anshika', 9.0, 'An emotional love story about life, love, and how people can change our perspectives.');




-- Step 1: Add More Columns (ALTER)
-- Add the following columns using ALTER:
-- review_date DATE

-- platform VARCHAR(50) — (e.g., IMDb, Rotten Tomatoes)

-- likes INT


ALTER TABLE movie_reviews 
ADD column review_date DATE,
ADD column platform VARCHAR(50),
ADD column likes INT; 


--  Insert 2 more rows with new columns

INSERT INTO movie_reviews (review_id, movie_title, reviewer_name, rating, review_text, review_date , platfrom , likes)
VALUES
(4,'3 idiots','Raj',8.5,'It was an movie depicting true values of life',19-04-2025,'Netflix',7),
(5,'5 Feet Apart',10,'This movie explains the significance of human touch',18-08-2026,'Cinehd',10);

--  Step 2: Rename a Column
-- Rename the column reviewer_name to critic_name

ALTER TABLE movie_reviews 
RENAME  column reviewer_name to critic_name;




--  Step 3: Modify Column Types
-- Modify:

-- rating to DECIMAL(3,1)

-- movie_title to VARCHAR(200)

ALTER TABLE movie_reviews
MODIFY column rating DECIMAL(3,1),
MODIFY column movie_title VARCHAR(200);




--  Step 4: Drop an Unnecessary Column
-- Drop the likes column

ALTER TABLE movie_reviews
DROP column likes;


--  Step 5: Truncate the Table
-- Truncate the table so all data is removed


TRUNCATE TABLE movie_reviews;


--  Step 6: Rename the Table
-- Rename movie_reviews to archived_reviews



RENAME table movie_reviews to archived_reviews;



--  Step 7: Drop the Table
-- Finally, drop the archived_reviews table

DROP TABLE archived_reviews;