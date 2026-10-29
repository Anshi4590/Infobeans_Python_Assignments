-- Assignment 2 — Product Management System
-- Table: products

-- Create a products table with:

-- Product ID
-- Product Name
-- Category
-- Brand
-- City
-- Price
-- Stock
-- Rating
-- Manufacturing Date
-- Data Requirements


create database product_management_system;

use product_management_system;

create table products(

    product_id int primary key auto_increment,
    product_name varchar(50),
    category varchar(50),
    brand varchar(50),
    city varchar(50),
    price decimal(10,2),
    stock int not null,
    rating tinyint check (rating between 1 and 5),
    mfg_date date
);

-- Insert at least 8 products.

-- Your data should include:

-- Categories: Electronics, Furniture, Clothing, Grocery
-- At least 5 different brands
-- Cities: Indore, Bhopal, Pune, Mumbai, Delhi
-- Price: ₹500 to ₹1,00,000
-- Stock: 0 to 100
-- Rating: 1 to 5
-- Manufacturing dates from 2021 to 2026
-- Some products with the same category
-- Some products with the same brand
-- Some similar prices
-- Some products with zero stock

INSERT INTO products
(product_name, category, brand, city, price, stock, rating, mfg_date)
VALUES
('Smartphone', 'Electronics', 'Samsung', 'Delhi', 45000.00, 25, 4.5, '2025-03-15'),

('Smart TV', 'Electronics', 'Sony', 'Pune', 55000.00, 30, 4.7, '2024-06-20'),

('Mega Sofa', 'Furniture', 'IKEA', 'Indore', 58000.00, 25, 4.4, '2024-04-14'),

('Study Table', 'Furniture', 'Nilkamal', 'Pune', 18000.00, 0, 3.8, '2025-01-12'),

('Cargo Pants', 'Clothing', 'Puma', 'Bhopal', 799.00, 50, 3.5, '2024-08-05'),

('Running Shoes', 'Clothing', 'Adidas', 'Delhi', 3500.00, 40, 4.2, '2023-07-18'),

('Rice 5kg', 'Grocery', 'Tata Sampann', 'Mumbai', 650.00, 100, 4.5, '2026-01-15'),

('Laptop', 'Electronics', 'HP', 'Pune', 80000.00, 15, 4.8, '2025-09-10'),

('Refrigerator', 'Electronics', 'LG', 'Indore', 50000.00, 12, 4.3, '2025-05-17'),

('Microwave Oven', 'Electronics', 'boAt', 'Bhopal', 2800.00, 7, 4.1, '2024-11-25');

SELECT * FROM products;



-- SQL Queries
-- 1. Find products whose price is greater than ₹30,000 AND rating is at least 4, but exclude products from Mumbai.

select " Find products whose price is greater than ₹30,000 AND rating is at least 4, but exclude products from Mumbai." as query_01;


select* from  products
where price >30000 and
rating >=4 and city!= "mumbai";

-- 2. Find products whose stock is less than 20 OR price is greater than ₹75,000, and whose category is not Grocery.

select "2. Find products whose stock is less than 20 OR price is greater than ₹75,000, and whose category is not Grocery." as query_02;


select * from products
where stock<20 or price>75000 and 
category!= "grocery";

-- 3. Find products whose price is between ₹15,000 and ₹60,000 AND rating is between 3 and 5, and which were manufactured after 2022.

select "Find products whose price is between ₹15,000 and ₹60,000 AND rating is between 3 and 5, and which were manufactured after 2022.
" as query_03;

select * from products
where price between 15000 and 60000 and
rating between 3 and 5 and 
year(mfg_date)>2022;

-- 4. Find products from Indore, Pune, or Delhi whose price is greater than ₹20,000 AND stock is not 0.

select "Find products from Indore, Pune, or Delhi whose price is greater than ₹20,000 AND stock is not 0." as query_04;

select * from products
where city in("indore","pune","delhi") or price>20000 and stock!=0;

-- 5. Find products belonging to Electronics or Furniture using IN.

select "5. Find products belonging to Electronics or Furniture using IN." as query_05;


select * from products
where category in ("electronics","furniture");

-- 6. Find products belonging to Electronics, Clothing, or Grocery using IN.

select "6. Find products belonging to Electronics, Clothing, or Grocery using IN." as query_06;

select * from products
where category in("Electronics", "Clothing","Grocery");

-- 7. Find products that are not from Indore or Bhopal using NOT IN.
select "7. Find products that are not from Indore or Bhopal using NOT IN." as query_07;


select * from products 
where city not in("indore","bhopal");


-- 8. Find products whose brand is not Samsung, LG, or Sony.

select "8. Find products whose brand is not Samsung, LG, or Sony." as query_08;

select * from products
where brand not in ("samsung","lg","sony");


-- 9. Find products whose price is between ₹10,000 and ₹50,000.

select "9. Find products whose price is between ₹10,000 and ₹50,000." as query_09;

select * from products
where  price between 10000 and 50000;

-- 10. Find products whose stock is between 20 and 60.

select "10. Find products whose stock is between 20 and 60." as query_10;


select * from products
where stock between 20 and 60;

-- 11. Find products whose rating is between 3 and 5, and whose price is greater than ₹20,000.

select " Find products whose rating is between 3 and 5, and whose price is greater than ₹20,000." as query_11;

select * from products
where rating between 3 and 5 and
price>20000;


-- 12. Find products manufactured between 2023 and 2025, whose category is Electronics or Furniture.


select " Find products manufactured between 2023 and 2025, whose category is Electronics or Furniture.
" as query_12;

select * from products
where year(mfg_date) between 2023 and 2025
and category in ("electronics","furniture");

-- 13. Find products whose name starts with S.

select "Find products whose name starts with S." as query_13;


select * from products 
where product_name = "S%";


-- 14. Find products whose name contains phone anywhere.

select "14. Find products whose name contains phone anywhere." as query_14;


select * from products
where product_name = "%phone%";


-- 15. Find products whose brand ends with a.

select "15. Find products whose brand ends with a." as query_15;

select * from products
where product_name = "%a";

-- 16. Find products from Indore or Pune, whose price is between ₹20,000 and ₹70,000, and whose rating is at least 4.

select "16. Find products from Indore or Pune, whose price is between ₹20,000 and ₹70,000, and whose rating is at least 4." as query_16;

select * from products
where city in("indore","pune")
and price between 20000 and 70000
and rating>=4;

-- 17. Find products belonging to Electronics or Furniture, whose stock is greater than 10, whose price is less than ₹60,000, and whose manufacturing date is after 2022.
select "17. Find products belonging to Electronics or Furniture, whose stock is greater than 10, whose price is less than ₹60,000, and whose manufacturing date is after 2022.
" as query_17;


select * from products
where  category in ("Electronics" , "Furniture")
and stock>10 and price<60000
and year(mfg_date)>2022;

-- 18. Find products whose name contains the letter a, whose price is NOT between ₹10,000 and ₹50,000, and whose stock is greater than 5.

select "18. Find products whose name contains the letter a, whose price is NOT between ₹10,000 and ₹50,000, and whose stock is greater than 5." as query_18;


select * from products
where product_name = "%a%"
and price not between 10000 and 50000
and stock>5;

-- 19. Find products manufactured between 2022 and 2025, belonging to Electronics, Clothing, or Furniture, having a rating greater than 3, and whose city is not Mumbai.

select "19. Find products manufactured between 2022 and 2025, belonging to Electronics, Clothing, or Furniture, having a rating greater than 3, and whose city is not Mumbai.
" as query_19;

select * from products
where year(mfg_date) between 2022 and 2025
and category in("Electronics", "Clothing","Furniture,")
and rating>3 and city <> "mumbai";

-- 20.  Find products whose name starts with S or M, whose city is not Indore or Mumbai, whose price is between ₹15,000 and ₹80,000, whose rating is at least 4, and whose manufacturing date is after 2023.

select " Find products whose name starts with S or M, whose city is not Indore or Mumbai, whose price is between ₹15,000 and ₹80,000, whose rating is at least 4, and whose manufacturing date is after 2023." as query_20;


select * from products
where product_name in("s%","m%")
and city not in("indore","mumbai")
and price between 15000 and 80000
and rating>=4 and year(mfg_date)>2023;

drop database product_management_system