-- ---

-- # Section 3: WHERE + GROUP BY + HAVING Practice (Q21–Q30)

-- **Q21.** Find each city's total sales for completed UPI transactions where quantity is greater than 2. Display only cities having total sales greater than 10,000.

select "Find each city's total sales for completed UPI transactions where quantity is greater than 2. Display only cities having total sales greater than 10,000." as query_21;


select city , sum(price*quantity) as total_sales  from sales
where status = "completed" and payment_method = "upi" and quantity>2
group by city
having total_sales >10000;



-- **Q22.** Find each category's total quantity for completed transactions where discount is greater than 300. Display only categories having total quantity greater than 5.


select "Find each category's total quantity for completed transactions where discount is greater than 300. Display only categories having total quantity greater than 5." as query_022;


select category , sum(quantity) as total_quantity  from sales
where status = "completed" and discount>300
group by category
having total_quantity>5;


-- **Q23.** Find each customer type's average price for completed transactions where quantity >= 2. Display only customer types whose average price exceeds 10,000.

select "Find each customer type's average price for completed transactions where quantity >= 2. Display only customer types whose average price exceeds 10,000.." as query_23;


select customer_type, avg(price) as avg  from sales
where status = "completed" and quantity>=2
group by customer_type
having avg>10000;

-- **Q24.** Find each city's total discount for UPI transactions where quantity > 3. Display cities having total discount greater than 500.

select "Find each city's total discount for UPI transactions where quantity > 3. Display cities having total discount greater than 500." as query_024;


select city , sum(discount) as total_discount  from sales
where payment_method = "upi" and quantity>3
group by city
having total_discount>500;

-- **Q25.** Find each category's total sales where payment method is UPI or Card and status is Completed. Display categories having total sales greater than 10,000.

select "Find each category's total sales where payment method is UPI or Card and status is Completed. Display categories having total sales greater than 10,000." as query_025;


select category , sum(price*quantity) as total_sales  from sales
where  payment_method  in ("upi","card") and status = "completed"
group by category
having total_sales>10000;


-- **Q26.** Find each city's transaction count for January 2026 completed transactions. Display cities having at least 2 transactions.

select "Find each city's transaction count for January 2026 completed transactions. Display cities having at least 2 transactions." as query_026;


select city , count(*) as transaction_count from sales
where status = "completed" and sale_date >= '2026-01-01'
AND sale_date < '2026-02-01'
group by city
having transaction_count>=2;

-- **Q27.** Find each category's average sales amount where quantity >= 3 and status = Completed. Display categories whose average sales amount is greater than 5,000.



select " Find each category's average sales amount where quantity >= 3 and status = Completed. Display categories whose average sales amount is greater than 5,000." as query_27;


select category , avg(price*quantity) as avg_sales from sales
where quantity>=3 and status = "completed"
group by category
having avg_sales >5000;

-- **Q28.** Find each customer type's maximum price where payment method is Card and status is Completed. Display only customer types whose maximum price exceeds 20,000.



select " Find each customer type's maximum price where payment method is Card and status is Completed. Display only customer types whose maximum price exceeds 20,000." as query_28;


select customer_type , max(price) as max from sales
where payment_method = "card" and status = "completed"
group by customer_type
having max>20000;


-- **Q29.** Find each city's total quantity for Electronics and Clothing products where status is Completed. Display cities having total quantity greater than 5.


select " Find each city's total quantity for Electronics and Clothing products where status is Completed. Display cities having total quantity greater than 5." as query_29;


select city , sum(quantity) as total_quantity from sales
where category in('Electronics' ,'Clothing') and status = "completed"
group by city
having total_quantity>5;


-- **Q30.** Find each payment method's total sales where status is Completed and discount is greater than 400. Display payment methods having total sales greater than 20,000.


select "Find each payment method's total sales where status is Completed and discount is greater than 400. Display payment methods having total sales greater than 20,000." as query_30;


select payment_method , sum(price*quantity) as total_sales from sales
where discount>400 and status = "completed"
group by payment_method
having total_sales>20000;