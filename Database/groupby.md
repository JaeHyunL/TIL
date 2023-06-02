# GROUP BY

각 카테고리별 그룹을 지어서 집계를 구함.

EXAMPLE

```sql
SELECT * FROM payment;
 
 SELECT customer_id, SUM(amount) FROM payment
 GROUP BY customer_id
 ORDER BY sum(amount) desc; 
 
 SELECT staff_id, customer_id,  SUM(amount) FROM payment
 GROUP BY staff_id, customer_id

SELECT DATE(payment_date) FROM payment

SELECT staff_id, COUNT(amount) FROM payment
GROUP BY staff_id
ORDER BY count asc;

SELECT * FROM film;7

SELECT rating, AVG(replacement_cost) FROM film
GROUP BY rating

SELECT customer_id, SUM(amount) 
  FROM payment
GROUP BY customer_id
ORDER BY SUM(amount) desc
LIMIT 5;
```