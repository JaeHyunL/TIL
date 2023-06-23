# 서브쿼리

서브쿼리를 이용하요 조금 더 복잡한 쿼리를 만들 수 있고 이것은 경우에때라 강력한 기능을 발휘함

```sql
SELECT title, rental_rate 
FROM film
WHERE rental_rate > (SELECT AVG(rental_rate) FROM film);

SELECT film_id, title
FROM film
WHERE film_id IN
(SELECT inventory.film_id from rental
INNER JOIN inventory ON inventory.inventory_id = rental.inventory_id
WHERE return_date BETwEEN '2005-05-29' AND '2005-05-30')
ORDER BY film_id

SELECT first_name, last_name
FROM customer AS c
WHERE EXISTS
(SELECT * FROM payment as p WHERE p.customer_id = c.customer_id
AND amount > 11)
```

### EXISTS

- 한 테이블이 다른테이블과 왜리키 와 같은 관계가 있을 때 유용
- 조건에 해당하는 ROW의 존재 유무와 이후 더 수행하지 않음
- 메인쿼리 → EXSITS 쿼리
- 일반적으로 IN에 비해 속도나 성능면에서 더 좋음

### IN

- 조건에 해당하는 ROW의 컬럼과 비교하여 체크
- SELECT절에서 조회한 컬럼 값으로 비교하여 EXISTS에 비해 성능 떨어짐
- IN 쿼리 → 메인 ㅋ쿼리

# 셀프조인

셀프 조인은 같은 표의 두 복사본 합처럼 보일 수 있슴

셀프 조인을 사용하면 표에 에일리어스를 사용

```sql
SELECT f1.title, f2.title, f1.length 
FROM film AS f1
INNER JOIN film AS f2 ON
f1.film_id != f2.film_id
AND f1.length = f2.length
```