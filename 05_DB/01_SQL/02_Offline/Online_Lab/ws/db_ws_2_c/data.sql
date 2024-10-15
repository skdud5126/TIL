-- 1. sql파일을 생성하고 각 요구 사항을 만족하는 코드를 작성하고 실행 결과를 확인하시오.

-- 2. BillingState에 저장되어 있는 데이터 값은 주 이름의 약자로 저장되어 있음을 주의한다.

-- a. "BillingCountry"를 기준으로 그룹화하고, 각 나라별 총판매액을 계산하여 조회하시오.

SELECT 
  BillingCountry, SUM(Total) AS 'TotalSales'
FROM
  invoices
GROUP BY
  BillingCountry;

-- b. "InvoiceDate"를 연도별로 그룹화하고, 각 연도별 총판매액을 계산하여 조회하시오.

SELECT
  strftime('%Y',"InvoiceDate") AS 'Year',
  SUM("Total") AS 'TotalSales'
FROM
  invoices
GROUP BY
  Year;


-- c. "BillingCountry"이 "USA"이고 "InvoicDate"가 2010년 01월 01이후인 레코드를 "BillingState"를 기준으로 그룹화하고, 각 주별로 총 주문 금액을 계산하여 조회하시오.

SELECT
 BillingCountry, SUM(Total) AS 'TotalSales'
FROM
  invoices
WHERE
    BillingCountry = 'USA'
  AND
  InvoiceDate > '2010-01-01'
GROUP BY
  BillingState;


-- d. "BillingCountry"이 "Germany"이거나 "BillingCountry"이 "France"인 레코드를 "BillingCountry"를 기준으로 그룹화하고, 각 나라별로 최대 주문 금액을 계산하여 조회하시오.

SELECT
  BillingCountry,
  MAX(Total) AS 'MaxOrderAmount'
FROM
  invoices
WHERE
  BillingCountry IN ('Germany', 'France')
GROUP BY
  BillingCountry;