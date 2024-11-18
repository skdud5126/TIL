
-- 현재 hotels 테이블의 전체 데이터를 조회한다.
SELECT
 * 
FROM 
  hotels;

-- grade 필드의 값을 모두 대문자로 수정한다.

UPDATE hotels
SET grade = UPPER(grade);

-- 수정된 전체 데이터의 grade 필드의 값만 조회한다.

SELECT
  grade
FROM
  hotels;

-- customers 테이블을 생성한다.
CREATE TABLE customers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT NOT NULL
);

-- reservations 테이블을 생성한다.
CREATE TABLE reservations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  customer_id INTEGER NOT NULL,
  room_num INTEGER NOT NULL,
  check_in TEXT NOT NULL,
  check_out TEXT NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES customers(id), 
  FOREIGN KEY (room_num) REFERENCES hotels(room_num)
);

PRAGMA table_info('reservations');


-- 고객 정보와 예약정보를 각각 최소 4개 이상씩 삽입한다.
INSERT INTO customers
VALUES  (1, '홍길동', 'john@example.com'),
        (2, '박지영', 'jane@example.com'),
        (3, '김미영', 'alice@example.com'),
        (4, '이철수', 'bob@example.com');


INSERT INTO reservations
VALUES  (1, 1, 101, '2024-03-20', '2024-03-25'),
        (2, 2, 202, '2024-03-21', '2024-03-24'),
        (3, 3, 303, '2024-03-22', '2024-03-26'),
        (4, 4, 404, '2024-03-23', '2024-03-27');
SELECT * FROM customers;

SELECT * FROM reservations;