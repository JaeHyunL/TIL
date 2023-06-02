# HAVNING



group by 로 묶은 절 중에 조건을 환산.

EXAMPLE

```sql
SELECT customer_id, SUM(amount) FROM payment
WHERE customer_id NOT IN (184, 87, 477)
GROUP BY customer_id
HAVING SUM(amount) > 100

SELECT customer_id, COUNT(amount)
	FROM payment
GROUP BY customer_id
HAVING COUNT(amount) >= 40

SELECT customer_id, SUM(amount)
	FROM payment
WHERE staff_id = 2
GROUP BY customer_id
HAVING SUM(amount) > 100
```