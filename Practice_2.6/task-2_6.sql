--Представления для таблицы products

CREATE VIEW product_view
AS
SELECT product_id AS id,
product_title AS name,
product_description AS decsription,
in_stock,
price
FROM products
WHERE in_stock > 20
ORDER BY in_stock, price;

SELECT * FROM product_view;
DROP VIEW product_view;


--Представления для таблиц order_status и order

CREATE VIEW orders_order_status
AS
SELECT order_id AS id,
cart_cart_id AS cart,
status_name AS status,
o.total AS tot
FROM orders o
INNER JOIN carts c on c.cart_id = o.cart_cart_id join order_status os on os.order_status_id = o.order_status_order_status_id;

SELECT * FROM orders_order_status;

CREATE VIEW accepted_orders AS
SELECT * FROM orders_order_status
WHERE status = 'Accepted';

SELECT * FROM accepted_orders;

DROP VIEW orders_order_status CASCADE;


--Представления для таблиц products и category

CREATE VIEW products_categories_view as
SELECT DISTINCT categories.category_id, product_id, product_title, in_stock, price
FROM products, categories
GROUP BY categories.category_id, product_id
ORDER BY product_id;

SELECT * FROM products_categories_view;
DROP VIEW products_categories_view;


--Создать материализированное представление для "тяжелого" запроса на свое усмотрение.

CREATE MATERIALIZED VIEW not_finished_order AS
SELECT o.cart_cart_id, os.status_name
FROM orders AS o
JOIN order_status os ON os.order_status_id = o.order_status_order_status_id
WHERE order_status_order_status_id = 1 OR order_status_order_status_id = 3
GROUP BY O.cart_cart_id, os.status_name
ORDER BY sum(o.total) ASC
WITH NO DATA;

REFRESH MATERIALIZED VIEW not_finished_order;
SELECT * FROM not_finished_order;
DROP MATERIALIZED VIEW not_finished_order;