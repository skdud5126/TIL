--- 01. Querying data
SELECT 
  LastName
FROM
  employees;


SELECT
  LastName, FirstName
FROM
  employees;

SELECT
  *
FROM
  employees;

SELECT
  FirstName as '이름'
FROM
  employees;

SELECT
  Name, Milliseconds/60000 AS '재생 시간(분)'
FROM
  tracks;
--- 02. Sorting data

SELECT
  FirstName
FROM
  employees
ORDER BY
  FirstName;

SELECT
  FirstName
FROM
  employees
ORDER BY
  FirstName DESC;

SELECT 
  Country, City
FROM 
  customers
ORDER BY
  Country DESC,
  City ASC;

SELECT
  Name, Milliseconds/60000 as '재생시간(분)'
FROM
  tracks
ORDER BY
  Milliseconds DESC;


--- 03. Filtering data

-- 테이블 customers에서 Country필드의 모든 데이터를 오름차순 조회
SELECT
  Country
FROM
  customers
ORDER BY
  Country;

-- 테이블 customers에서 Country 필드의 모든 데이터를 중복없이 오름차순 조회
SELECT
  DISTINCT Country
FROM
  customers
ORDER BY
  Country;