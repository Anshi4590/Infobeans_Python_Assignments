
-- ---

-- # Section 4: Multiple Conditions with HAVING (Q31–Q40)

-- **Q31.** Find cities having more than 2 completed transactions and total sales greater than 50,000. Sort by total sales descending.

select "Find cities having more than 2 completed transactions and total sales greater than 50,000. Sort by total sales descending." as query_31;


select city , count(*) as completed_transaction , sum(price*quantity) as total_sales from sales
where  status = "completed"
group by city
having completed_transaction>2 and total_sales >50000 
order by total_sales desc;


-- **Q32.** Find categories having total quantity greater than 8 and average price greater than 2,000. Sort by total quantity descending.

select "Find categories having total quantity greater than 8 and average price greater than 2,000. Sort by total quantity descending." as query_32;


select category, avg(price) as avg_price,sum(quantity) as total_quantity from sales
group by category
having avg_price>2000 and total_quantity>8
order by total_quantity desc;

-- **Q33.** Find customer types having more than 2 transactions and total discount greater than 2,000. Sort by total discount descending.

select "Find customer types having more than 2 transactions and total discount greater than 2,000. Sort by total discount descending." as query_33;


select customer_type, count(*) as transaction ,sum(discount) as total_discount from sales
group by customer_type
having transaction>2 and total_discount >2000
order by total_discount  desc;

-- **Q34.** Find cities having average quantity greater than 3 and maximum product price greater than 20,000. Sort by average quantity descending.

select " Find cities having average quantity greater than 3 and maximum product price greater than 20,000. Sort by average quantity descending.." as query_34;


select city, avg(quantity) as avg, max(price) as max from sales
group by city
having avg>3 and max>20000
order by avg  desc;

-- **Q35.** Find categories having more than 2 completed transactions and total sales greater than 20,000. Sort by total sales descending.

select " Find categories having more than 2 completed transactions and total sales greater than 20,000. Sort by total sales descending." as query_35;


select category, count(*) as completed_transaction, sum(price*quantity) as total_sales from sales
where status = "completed"
group by category
having completed_transaction>2 and total_sales>20000
order by total_sales desc;


-- **Q36.** Find payment methods having more than 2 completed transactions and average price greater than 10,000. Sort by average price descending.

select " Find payment methods having more than 2 completed transactions and average price greater than 10,000. Sort by average price descending" as query_36;


select payment_method, count(*) as completed_transaction, avg(price) as avg from sales
where status = "completed"
group by payment_method
having completed_transaction>2 and avg>10000
order by avg desc;

-- **Q37.** Find cities having total quantity greater than 8 and average discount greater than 300. Sort by total quantity descending.


select " Find cities having total quantity greater than 8 and average discount greater than 300. Sort by total quantity descending." as query_37;


select city, avg(discount) as avg_discount, sum(quantity) as total_quantity from sales
group by city
having avg_discount>300 and total_quantity>8
order by total_quantity desc;

-- **Q38.** Find customer types having average price greater than 5,000 and total quantity greater than 8. Sort by total quantity descending.


select " Find customer types having average price greater than 5,000 and total quantity greater than 8. Sort by total quantity descending." as query_38;


select customer_type, avg(price) as avg_price, sum(quantity) as total_quantity from sales
group by customer_type
having avg_price>5000 and total_quantity>8
order by total_quantity desc;


-- **Q39.** Find categories having minimum price below 2,000 and maximum price above 20,000. Sort by maximum price descending.

select "Find categories having minimum price below 2,000 and maximum price above 20,000. Sort by maximum price descending.
" as query_39;


select category, min(price) as min_price, max(price) as max_price from sales
group by category
having min_price<2000 and max_price>20000
order by max_price desc;

-- **Q40.** Find cities having total discount greater than 1,000 and total sales greater than 30,000. Sort by total sales descending.


select "Find cities having total discount greater than 1,000 and total sales greater than 30,000. Sort by total sales descending.
" as query_40;


select city, sum(discount) as total_discount, sum(price*quantity) as total_sales from sales
group by city
having total_discount>1000 and total_sales>30000
order by total_sales desc;
-- ---
