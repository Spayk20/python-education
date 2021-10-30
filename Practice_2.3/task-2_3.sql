-- Task 1
CREATE TABLE potential_customers (
    id INTEGER NOT NULL PRIMARY KEY,
    email VARCHAR(25),
    name VARCHAR NOT NULL,
    surname VARCHAR NOT NULL,
    second_name VARCHAR NOT NULL,
    city VARCHAR(50));

INSERT INTO potential_customers (id, email, name, surname, second_name, city) VALUES
	(1, 'user1@mail.com', 'name1', 'surname1', 'second_name1', 'city1'),
	(2, 'user1@mail.com', 'name2', 'surname2', 'second_name2', 'city2'),
	(3, 'user3@mail.com', 'name3', 'surname3', 'second_name3', 'city1'),
	(4, 'user4@mail.com', 'name4', 'surname4', 'second_name4', 'city3'),
	(5, 'user5@mail.com', 'name5', 'surname5', 'second_name5', 'city3'),
	(6, 'user6@mail.com', 'name6', 'surname6', 'second_name6', 'city2'),
	(7, 'user7@mail.com', 'name7', 'surname7', 'second_name7', 'city17'),
    	(8, 'user8@mail.com', 'name8', 'surname8', 'second_name8', 'city17'),
    	(9, 'user9@mail.com', 'name9', 'surname9', 'second_name9', 'city4'),
    	(10, 'user10@mail.com', 'name10', 'surname10', 'second_name10', 'city17');

SELECT name, email
FROM potential_customers
WHERE city='city 17';

SELECT first_name, email
FROM users
WHERE city='city 17';


SELECT U.first_name, U.email FROM users U
WHERE U.city = 'city 17'
UNION
SELECT p.name, p.email FROM potential_customers p
WHERE p.city = 'city 17';


-- Task 2
SELECT first_name, email FROM users
ORDER BY city, first_name ASC;


-- Task 3
SELECT category_title, COUNT(p.category_id) FROM categories c
LEFT JOIN products p on p.category_id = c.category_id
GROUP BY c.category_title
ORDER BY COUNT(p.category_id) DESC;


SELECT category_title, COUNT(category_title) FROM products
JOIN categories ON products.category_id=categories.category_id
GROUP BY category_title, products.category_id
ORDER BY COUNT(products.category_id) DESC;


-- Task 4.1
SELECT * FROM products WHERE product_id NOT IN
(
	SELECT DISTINCT products_product_id FROM cart_products cp
);

SELECT * FROM products
    LEFT JOIN cart_products ON products_product_id=product_id
    WHERE cart_products.cart_cart_id IS NULL;


-- Task 4.2
SELECT product_title, cart_products.cart_cart_id, order_id FROM products
    LEFT JOIN cart_products ON products_product_id = product_id
    LEFT JOIN carts ON carts.cart_id = cart_cart_id
    LEFT JOIN orders ON carts.cart_id = orders.cart_cart_id
    WHERE orders.order_id IS NULL;


-- Task 4.3
SELECT product_title, COUNT(product_title) FROM products
    JOIN cart_products ON cart_products.products_product_id = products.product_id
    JOIN carts ON cart_cart_id = carts.cart_id
    GROUP BY product_title
    ORDER BY COUNT(product_title)
    DESC LIMIT 10;

-- Task 4.4
SELECT product_title, COUNT(product_title) FROM products
    LEFT JOIN cart_products ON cart_products.products_product_id = products.product_id
    LEFT JOIN carts ON cart_cart_id = carts.cart_id
    LEFT JOIN orders ON carts.cart_id = orders.cart_cart_id
    WHERE orders.order_id IS NOT NULL
    GROUP BY product_title
    ORDER BY COUNT(product_title) DESC
    LIMIT 10;


-- Task 4.5
SELECT first_name, last_name, total FROM users
    JOIN carts ON user_id=cart_id
    ORDER BY total DESC
    LIMIT 5;


-- Task 4.6
SELECT order_id, first_name, middle_name, last_name, COUNT(email) FROM orders
	LEFT JOIN carts ON cart_cart_id = cart_id
	LEFT JOIN users ON 	users_uses_id = user_id
	GROUP BY order_id, cart_id, user_id, users_uses_id
	ORDER by COUNT(email)
	DESC LIMIT 5;


-- Task 4.7 (Я не уверен что это работает правильно)
select u.*, count(o.order_id) AS ordered, count(c.cart_id) as in_cart from users u left join carts c
on u.user_id = c.users_uses_id left join orders o
on c.cart_id = o.cart_cart_id
group by u.user_id
order by count(o.order_id), count(c.cart_id) desc
limit 5;
