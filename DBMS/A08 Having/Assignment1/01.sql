create database if not exists sales_management_system;


use sales_management_system;

drop table if exists sales;


create table if not exists sales
( 
  sale_id int primary key auto_increment,
  customer_name varchar(50),
  city varchar(30),
  category varchar(30),
  product varchar(50),
  quantity int,
  price decimal(10,2),
  discount decimal(10,2),
  sale_date date,
  payment_method enum("upi","card","cash","net banking"),
  status enum("completed","pending","cancelled"),
  customer_type enum("new","regular","premium")

);


INSERT IGNORE INTO sales
(customer_name, city, category, product, quantity, price, discount, sale_date, payment_method, status, customer_type)
VALUES
('Rahul','Indore','Electronics','Laptop',2,60000,5000,'2026-01-05','Card','Completed','Premium'),
('Priya','Bhopal','Electronics','Mobile',3,25000,3000,'2026-01-07','UPI','Completed','Regular'),
('Amit','Indore','Clothing','Jeans',5,2000,500,'2026-01-10','Cash','Completed','New'),
('Sneha','Mumbai','Beauty','Cream',8,800,400,'2026-01-12','UPI','Completed','Premium'),
('Rohit','Pune','Electronics','Laptop',1,55000,4000,'2026-01-15','Card','Completed','Regular'),
('Neha','Delhi','Clothing','Kurti',6,1800,600,'2026-01-17','UPI','Completed','Premium'),
('Karan','Indore','Sports','Bat',4,3500,700,'2026-01-20','Cash','Completed','Regular'),
('Pooja','Bhopal','Beauty','Lipstick',10,600,300,'2026-01-22','UPI','Completed','New'),
('Vikas','Delhi','Books','SQL Book',7,900,200,'2026-01-25','Net Banking','Completed','Regular'),
('Anjali','Mumbai','Electronics','Watch',3,7000,800,'2026-01-27','Card','Completed','Premium'),
('Saurabh','Pune','Grocery','Rice',12,900,500,'2026-02-01','UPI','Completed','Regular'),
('Riya','Delhi','Electronics','AC',2,45000,5000,'2026-02-03','Card','Completed','Premium'),
('Manish','Indore','Clothing','Shirt',6,1500,300,'2026-02-05','UPI','Completed','New'),
('Komal','Bhopal','Furniture','Chair',3,8000,1000,'2026-02-07','Cash','Completed','Premium'),
('Deepak','Mumbai','Electronics','Speaker',5,3000,500,'2026-02-12','Card','Cancelled','Regular');


select * from sales;


-- **Q1.** Find the total number of completed sales for each city where quantity is greater than 2. Display cities in descending order of sales count.

select "Find the total number of completed sales for each city where quantity is greater than 2. Display cities in descending order of sales count." as query_01;


select city ,count(*)  as total_count  from sales
where status = "completed" and  quantity>2
group by city 
order by total_count desc;



-- **Q2.** Find the total quantity sold for each category where discount is greater than 300. Display highest quantity first.


select "Find the total quantity sold for each category where discount is greater than 300. Display highest quantity first.
" as query_02;


select category ,sum(quantity) as total_quantity from sales
where discount>300
group by category
order by  total_quantity desc;



-- **Q3.** Find the total sales amount for each city for completed sales only. Display highest-selling city first.


select "Find the total sales amount for each city for completed sales only. Display highest-selling city first.
" as query_03;


select city ,sum(price) as total_price from sales
where status = "completed"
group by city
order by  total_price desc;


-- **Q4.** Find the average product price for each category where quantity is at least 3. Display categories by average price descending.


select "Find the average product price for each category where quantity is at least 3. Display categories by average price descending.

" as query_04;


select category,avg(price) as avg_price from sales
where quantity>=3
group by category
order by avg_price desc;

-- **Q5.** Find the number of sales for each customer type where the order amount (quantity * price) is greater than 5000. Sort by number of sales descending.

select "Find the number of sales for each customer type where the order amount (quantity * price) is greater than 5000. Sort by number of sales descending.
" as query_05;


select customer_type,count(*) as total from sales
where price*quantity>5000
group by customer_type
order by total desc;



-- **Q6.** Find the total discount given for each city for UPI transactions. Display highest discount first.


select "Find the total discount given for each city for UPI transactions. Display highest discount first." as query_06;


select city,sum(discount) as total from sales
where payment_method = "upi"
group by city
order by total desc;



-- **Q7.** Find the total quantity sold through each payment method for completed transactions. Sort by total quantity descending.

select "Find the total quantity sold through each payment method for completed transactions. Sort by total quantity descending." as query_07;


select payment_method,sum(quantity) as total from sales
where status = "completed"
group by  payment_method
order by total desc;


-- **Q8.** Find the average discount for each category where quantity is greater than 4. Display highest average discount first.

select "Find the average discount for each category where quantity is greater than 4. Display highest average discount first." as query_08;


select category,avg(discount) as avg_discount from sales
where quantity>4
group by  category
order by avg_discount desc;


-- **Q9.** Find the maximum product price for each city where the status is Completed. Sort by maximum price descending.


select "Find the maximum product price for each city where the status is Completed. Sort by maximum price descending." as query_09;


select city,max(price) as max_price from sales
where status = "completed"
group by  city
order by max_price desc;


-- **Q10.** Find the minimum product price for each category where discount is greater than 300. Sort by minimum price ascending.


select "Find the minimum product price for each category where discount is greater than 300. Sort by minimum price ascending." as query_10;


select category,min(price) as min_price from sales
where discount>300
group by category
order by min_price asc;



