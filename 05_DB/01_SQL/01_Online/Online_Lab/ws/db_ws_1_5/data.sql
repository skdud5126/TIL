-- 1. age가 30세 이상이면서 balance가 1000이상인 사용자들의 정보를 조회하시오.

SELECT
  *
FROM
  users
WHERE
  AGE >= 30
  AND
  balance >= 1000;

-- 2. balance가 1000이하인 사용자들 중에서 age가 20세 이하인 사용자들의 정보를 조회하시오.

SELECT
  *
FROM
  users
WHERE
  balance <= 1000
  AND
  age <= 20;

-- 3. first_name이 '현'으로 시작하고 country가 '제주특별자치도'인 사용자들 중에서 가장 age가 많은 사용자의 정보를 조회하시오.
SELECT
  *
FROM
  users
WHERE
  first_name LIKE '현%'
  AND
  country = '제주특별자치도'
ORDER BY
  age DESC
LIMIT 1;

-- 4. last_name이 '박'이고 age가 25세 이상인 사용자들 중에서 가장 age가 어린 사용자의 정보를 조회하시오.

SELECT
  *
FROM
  users
WHERE
  last_name = '박'
  AND
  age >= 25
ORDER BY
  age
LIMIT 1;


-- 5. first_name이 '재은'이거나 '영일'인 사용자들 중에서 balance가 가장 많은 사용자의 정보를 조회하시오.

SELECT
  *
FROM
  users
WHERE
  first_name = '재은'
  OR
  first_name = '영일'
ORDER BY
  balance DESC
LIMIT 1;

-- 6. 각 country별로 가장 많은 balance를 가진 사용자의 정보를 조회하고 balance를 내림차순으로 정렬하시오.

SELECT
  *
FROM
  users
GROUP BY
  country
HAVING
  MAX(balance)
ORDER BY
  balance DESC;

-- 7. age가 30세 이상이면서, balance가 age가 30세이상인 사용자들의 평균 balance보다 높은 사용자의 정보를 조회하시오.

SELECT
  *
FROM users
WHERE age >= 30
AND balance >= (SELECT AVG(balance) FROM users WHERE age>=30);