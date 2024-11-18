-- 각 부서의 최고 연령 직원과 해당 부서의 평균 연령을 함께 조회한다.
  -- 부서별 최고나이, 평균나이, 가장 나이가 많은 직원의 이름이 출력되어야 한다.
SELECT d.name AS "department", e.name AS 'oldest_employee', MAX(e.age) AS 'max_age', AVG(e.age) AS 'avg_avg'
FROM employees e
JOIN departments d
ON d.id = e.departmentId
GROUP BY d.name;

-- 부서별로 가장 많은 급여를 받는 직원의 정보와 그 급여를 함께 조회한다.
  -- 부서별 가장 높은 연봉을 받는 직원의 연봉, 이름을 출력한다.
SELECT d.name AS department, e.name AS highest_paid_employee ,MAX(e.salary) AS max_salary
FROM employees e
JOIN departments d
ON d.id = e.departmentId
GROUP BY d.id;


-- 부서별로 연령대 별 직원 수를 조회한다.
  -- 30세 이하, 30세~40세 사이, 40세 이상으로 구분한다.
  -- 각 부서별, 연령대별 직원 수를 출력한다.

SELECT d.name AS department,
  CASE 
    WHEN e.age < 30 THEN  'Under 30'
    WHEN e.age BETWEEN 30 AND 40 THEN 'BETWEEN 30 - 40'
    ELSE 'Over 40'
  END AS 'age_group',
  COUNT(*) AS 'num_employees'
FROM employees e
JOIN departments d
ON d.id = e.departmentId
GROUP BY d.name, age_group;

-- 부서별로 최고 급여를 받는 직원을 제외한 평균 급여 조회한다.

SELECT 
  d.name AS 'department', 
  avg(salary) AS 'avg_salary_excluding_highest'
FROM 
  employees e
JOIN 
  departments d
ON d.id = e.departmentId
WHERE (e.salary, e.departmentId) NOT IN 
  (SELECT 
    MAX(salary), departmentId 
  FROM 
    employees
    GROUP BY departmentId
    )
GROUP BY d.name;


-- 만약, 각 부서별 직원 데이터가 부족하다면, 데이터를 추가로 삽입하여 올바른 데이터가 조회되는지 확인한다.
INSERT INTO employees (name, salary, age, departmentId) VALUES
('이규보', 1700, 77, 1),
('김구', 126000, 21, 2),
('유관순', 82000, 41, 4),
('안중근', 23000, 37, 3);