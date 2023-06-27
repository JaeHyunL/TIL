# Check

CHECK로 맞춤 조건을 설정

```sql
CREATE TABLE example(
ex_id SERIAL PRIMARY KEY,
age SMALLINT CHECK (age >21),
parent_age SMALLINT CHECK(
parent_age > age)
);
```

age 보다 큰 값만 들어갈수잇도록 제약 조건 설정.