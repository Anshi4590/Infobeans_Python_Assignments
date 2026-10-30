
-- ---

-- # Section 2: HAVING Clause Practice (Q11–Q20)

-- **Q11.** Find cities having more than 2 completed sales. Sort cities by completed sales count descending.

select "Find cities having more than 2 completed sales. Sort cities by completed sales count descending." as query_11;


select city,count(*) as total from sales
where status = "completed"
group by city
having total >2
order by total desc;


-- **Q12.** Find categories having total quantity greater than 10. Sort by total quantity descending.


select "Find categories having total quantity greater than 10. Sort by total quantity descending." as query_12;


select category,sum(quantity) as total from sales
group by category
having total >10
order by total desc;

-- **Q13.** Find cities having total sales greater than 50,000. Sort by total sales descending.


select "Find cities having total sales greater than 50,000. Sort by total sales descending." as query_13;


select city,sum(price*quantity) as total from sales
group by city
having total>50000
order by total desc;

-- **Q14.** Find customer types having average product price greater than 10,000. Sort by average price descending.

select "Find customer types having average product price greater than 10,000. Sort by average price descending." as query_14;


select customer_type, avg(price) as avg from sales
group by customer_type
having  avg>10000
order by avg desc;

-- **Q15.** Find categories having average discount greater than 400. Sort by average discount descending.


select "Find categories having average discount greater than 400. Sort by average discount descending.." as query_15;


select category, avg(discount) as avg from sales
group by category
having  avg>400
order by avg desc;

-- **Q16.** Find payment methods having more than 2 completed transactions. Sort by transaction count descending.


select "Find categories having average discount greater than 400. Sort by average discount descending.." as query_16;


select category, avg(discount) as avg from sales
group by category
having  avg>400
order by avg desc;

-- **Q17.** Find cities where the maximum product price is greater than 20,000. Sort by maximum price descending.


select "Find cities where the maximum product price is greater than 20,000. Sort by maximum price descending." as query_17;


select city, max(price) as max_price from sales
group by city
having  max_price>20000
order by max_price desc;

-- **Q18.** Find categories where the minimum product price is less than 2,000. Sort by minimum price ascending.

select " Find categories where the minimum product price is less than 2,000. Sort by minimum price ascending." as query_18;


select category,min(price) as min_price from sales
group by category
having  min_price<20000
order by min_price asc;

-- **Q19.** Find customer types where total discount is greater than 2,000. Sort by total discount descending.

select " Find customer types where total discount is greater than 2,000. Sort by total discount descending." as query_19;


select customer_type,sum(discount) as total from sales
group by customer_type
having total > 2000
order by total desc;

-- **Q20.** Find cities where average quantity per transaction is greater than 4. Sort by average quantity descending.


select " Find cities where average quantity per transaction is greater than 4. Sort by average quantity descending." as query_20;


select city,avg(quantity) as avg from sales
group by city
having avg>4
order by avg desc;
