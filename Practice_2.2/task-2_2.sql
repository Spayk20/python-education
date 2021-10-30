-- Task 1
SELECT * from users;

SELECT first_name, middle_name, last_name FROM users;

select user_id AS "ID",
       first_name AS "First name",
       last_name AS "Last name",
       middle_name AS "Midle name",
       phone_number AS "Phone number",
       email,
       password AS "Password",
       is_staff AS "Is staff",
       country as "Country",
       city AS "City",
       address AS "Adress"
from users;

-- Task 1.2
SELECT product_title FROM products;

--Task 1.3
SELECT status_name FROM order_status;



--Task 2
SELECT * FROM orders WHERE order_status_order_status_id=4;



--Task 3.1
SELECT * FROM products WHERE price>80 AND price<=150;

SELECT product_title, price
FROM  products
WHERE price > 80.00 and price <= 150.00;

--Task 3.2
SELECT * FROM orders WHERE create_at > '2020.10.01' ORDER BY create_at;

SELECT order_id, create_at
FROM orders
WHERE create_at > '10-01-2020'
ORDER BY create_at;

--Task 3.3
SELECT * FROM orders WHERE create_at BETWEEN '2020.01.01' AND '2020.06.01' and order_status_order_status_id = 1 ORDER BY create_at;

--Task 3.4
SELECT * FROM products WHERE category_id = 7 OR category_id = 11 or category_id = 18;


--Task 3.5
SELECT * FROM "orders" WHERE order_status_order_status_id = 1 OR order_status_order_status_id = 2 OR
                             order_status_order_status_id = 3 AND orders.create_at BETWEEN '2020.01.01' AND '2020.12.31';

--Task 3.6
SELECT * FROM carts INNER JOIN "orders" ON cart_id = carts.cart_id WHERE order_status_order_status_id = 1 OR
                                                                      order_status_order_status_id = 5;

SELECT o.cart_cart_id, os.status_name
FROM orders AS o
JOIN order_status os ON os.order_status_id = o.order_status_order_status_id
WHERE order_status_order_status_id = 1 OR order_status_order_status_id = 3;

--Task 4.1
SELECT AVG(total) from "orders" WHERE order_status_order_status_id=4;

SELECT AVG(total) AS Average_Price
FROM orders
WHERE order_status_order_status_id = 4;


--Task 4.2
SELECT MAX(total)
FROM orders
WHERE order_status_order_status_id=4 AND create_at BETWEEN '2020.09.01' AND '2020.12.31';