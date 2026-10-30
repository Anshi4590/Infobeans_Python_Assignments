


-- # Section 5: LIMIT & TOP N Practice (Q41–Q46)

-- **Q41.** Find the top 3 cities based on total sales, considering only completed transactions with quantity greater than 1 and displaying only cities having more than 1 transaction.

select "Find the top 3 cities based on total sales, considering only completed transactions with quantity greater than 1 and displaying only cities having more than 1 transaction.
" as query_41;


select city , sum(price*quantity) as total_sales , count(*) as transactions from sales
where status = "completed" and quantity>1
group by city
having transactions>1
order by total_sales desc
limit 3;

-- **Q42.** Find the top 3 categories based on total quantity where discount is greater than 300 and total quantity is greater than 5.

select "Find the top 3 categories based on total quantity where discount is greater than 300 and total quantity is greater than 5." as query_42;


select category, sum(quantity) as total_quantity  from sales
where discount>300 
group by category
having total_quantity>5
order by total_quantity desc
limit 3;

-- **Q43.** Find the top 3 customer types based on average sales amount where status is Completed and transaction count is greater than 1.

select "Find the top 3 customer types based on average sales amount where status is Completed and transaction count is greater than 1." as query_43;


select customer_type, avg(price*quantity) as avg_sales ,count(*) as transactions from sales
where status = "completed" 
group by customer_type
having transactions>1
order by avg_sales desc
limit 3;

-- **Q44.** Find the top 3 cities based on total discount for UPI transactions where status is Completed and total discount is greater than 500.


select "Find the top 3 cities based on total discount for UPI transactions where status is Completed and total discount is greater than 500." as query_44;


select city , sum(discount) as total_discount from sales
where status = "completed" and  payment_method = "upi"
group by city
having total_discount>500
order by total_discount desc
limit 3;

-- **Q45.** Find the top 3 categories based on total sales where quantity is greater than 2, average price is greater than 1,000, and total sales exceeds 10,000.


select "Find the top 3 categories based on total sales where quantity is greater than 2, average price is greater than 1,000, and total sales exceeds 10,000.

" as query_45;


select category , sum(price*quantity) as total_sales ,avg(price) as avg_price from sales
where quantity>2
group by category
having total_sales >10000 and avg_price>1000
order by total_sales desc
limit 3;

-- **Q46.** Find the top 3 cities based on average order value where status is Completed, total quantity is greater than 5, and transaction count is greater than 1.

select "Find the top 3 cities based on average order value where status is Completed, total quantity is greater than 5, and transaction count is greater than 1.

" as query_46;


select city , avg(price*quantity) as avg_price , sum(quantity) as total_quantity , count(*) as transactions from sales  
where status = "completed"
group by city
having total_quantity>5 and transactions>1
order by avg_price desc
limit 3;
-- ---

-- # Section 6: Ranking & Advanced GROUP BY Practice (Q47–Q49)



-- **Q47.** Find the second-highest city based on total sales after considering only completed transactions and cities having at least 2 transactions.



select "Find the second-highest city based on total sales after considering only completed transactions and cities having at least 2 transactions.

" as query_47;


select city ,sum(price*quantity) as total_sales, count(*) as transactions from sales  
where status = "completed"
group by city
having  transactions>=2
order by total_sales desc
limit 1  offset 1;

-- **Q48.** Find the third-highest category based on total quantity where quantity is greater than 2 and total discount exceeds 500.

select "Find the third-highest category based on total quantity where quantity is greater than 2 and total discount exceeds 500.

" as query_48;


select category , sum(discount) as total_discount, sum(quantity) as total_quantity from sales  
where quantity>2
group by category
having  total_discount>500
order by total_quantity desc
limit 1  offset 2;


-- **Q49.** Find the 2nd and 3rd highest customer types based on total sales where status is Completed and average price is greater than 5,000.

-- ---

select "Find the 2nd and 3rd highest customer types based on total sales where status is Completed and average price is greater than 5,000.

" as query_49;


select customer_type ,sum(price*quantity) as total_sales, avg(price) as avg_price from sales  
where status = "completed"
group by customer_type
having  avg_price>5000
order by total_Sales desc
limit 2  offset 1;


-- # Section 7: Master-Level Combined Conditions (Q50)

-- **Q50.** Find the top 3 cities where all the following conditions are satisfied:

-- 1. Status is Completed.
-- 2. Payment method is UPI or Card.
-- 3. Quantity is greater than 1.
-- 4. Number of transactions is greater than 1.
-- 5. Total quantity is greater than 5.
-- 6. Total sales is greater than 20,000.

-- ---


select " Find the top 3 cities where all the following conditions are satisfied:

-- 1. Status is Completed.
-- 2. Payment method is UPI or Card.
-- 3. Quantity is greater than 1.
-- 4. Number of transactions is greater than 1.
-- 5. Total quantity is greater than 5.
-- 6. Total sales is greater than 20,000.

" as query_50;


select city ,  sum(price*quantity) as total_sales  ,  count(*) as transactions, sum(quantity) as total_quantity  from sales  
where status = "completed" and payment_method in("upi","card") and quantity>1
group by city
having  transactions >1 and total_sales >20000 and total_quantity>5
order by total_sales desc
limit 3  ;


