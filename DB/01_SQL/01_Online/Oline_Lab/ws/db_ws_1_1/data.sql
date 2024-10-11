-- 1. users테이블의 모든 데이터를 조회하시오.
SELECT
  *
FROM
  users;

-- 2. age가 18세 미만인 유저의 목록을 조회하시오.

SELECT 
  *
FROM
  users
WHERE
  age < 18;

-- 3. age가 18세 미만읜 유저의 age와 phone필드만 조회하시오.
SELECT
  age, phone
FROM
  users
WHERE
  age < 18;