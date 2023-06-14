# join

```sql
샘플 코드
-- 코드를 입력하세요
SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME FROM ANIMAL_OUTS 
    LEFT JOIN ANIMAL_INS
    ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID 
    WHERE ANIMAL_INS.ANIMAL_ID is NULL 
    ORDER BY ANIMAL_ID, NAME asc ;
```

INNER JOIN 의 경우 JOIN으로도 사용가능(pgadmin) 기준

식: SELECT 컬럼명 FROM 테이블 명

INNER JOIN 조인할 테이블 명

ON 조건 절(테이블명.조건컬럼) = 조인할 테이블 명.조건컬럼

```python
-- INNER JOIN
SELECT payment_id, payment.customer_id, first_name
FROM payment
INNER JOIN customer
ON payment.customer_id = customer.customer_id;

-- 풀 아우터 조인 , IS NULL EXAMPLE
SELECT * FROM customer
FULL OUTER JOIN payment
ON customer.customer_id = payment.customer_id
WHERE customer.customer_id IS null
OR payment.payment_id IS null;

-- LEFT JOIN
SELECT film.film_id, film.title, inventory_id
FROM film
LEFT OUTER JOIN inventory ON
inventory.film_id = film.film_id;

-- LEFT JOIN without Inner JOIN
SELECT film.film_id, film.title, inventory_id
FROM film
LEFT OUTER JOIN inventory ON
inventory.film_id = film.film_id
```

WHERE inventory.film_id IS NULL;