CREATE TABLE orderS (
  order_id INTEGER PRIMARY KEY AUTOINCREMENT,
  order_date DATE NOT NULL,
  total_amount REAL NOT NULL
);

INSERT INTO orders (order_date, total_amount)
VALUES ('2023-07-15', 50.99),
      ('2023-07-16', 75.5),
      ('2023-07-17', 30.25);

CREATE TABLE customers (
  customer_Id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  phone TEXT NOT NULL
);


INSERT INTO customers (name, email,phone)
VALUES ('허균', 'hong.gildong@example.com', '010-1234-5678'),
      ('김영희', 'kim.younghee@example.com', '010-9876-5432'),
      ('이철수', 'lee.cheolsu@example.com','010-5555-4444');

PRAGMA table_info('orders');

DELETE FROM "orderS" WHERE order_id = 3;

UPDATE customers SET name = '홍길동' WHERE "customer_Id" = 1;

SELECT
  *
FROM "orderS";

SELECT
  *
FROM customers;
