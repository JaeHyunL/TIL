# 어드밴스 씨퀄 고급 쿼리

- Section Overview
  - Timestamps and EXTRACT
  - Math Function
  - String Function
  - Sub-query
  - Self-Join

## TIMESTAMPE EXTRACT

Postgresql에 타임정보

- TIME: 시간이 포함
- DATE: 날짜가 포함
- TIMESTAMP: 날짜와 시간이 포함
- TIMESTAMPZ: 날짜와 시간과 타임존이 포함

```sql
SHOW ALL 
데이터베이스에 속성 값 을 보여주는 명령어 

SHOW TIMEZONE
데이터베이스에 설정되어 있는 타임존 확인

SHOW NOW() 현재 시간 확인 
```

**데이트타임을 추출하는방법**

- EXTRACT()
  - extract를 통한 서브컴퍼넌트에 데이트 값을 추출
    - YEAR
    - MONTH
    - DAY
    - WEEK
    - QUARTER
  - EXTRACT(YEAR FROM date_col) 추출 대상이 되는 날짜 열을 입력
- AGE()
  - Age(Date_col) 데이터 베이스 시간으로ㅓ부터 얼마나 떨어지진지 알려줌
- TO_CHAR()
  - TO_CHAR(DATE_COL, “YYYY-MM-DD”)

## MATH

스킬에 간단한 쿼리를 아라보자

String, Math 등등

수정하고 결합하고 문자열을 결합하는 대표적인 예를 보여주심 .

String Function Description