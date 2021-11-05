CREATE table Users
(
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    password VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    middle_name VARCHAR(255),
    is_staff SMALLINT,
    country VARCHAR(255),
    city VARCHAR(255),
    address text
);

CREATE table Carts
(
    cart_id SERIAL PRIMARY KEY,
    Users_uses_id INT REFERENCES Users(user_id),
    subtotal DECIMAL,
    total DECIMAL,
    timestamp timestamp(2)
);

CREATE TABLE Order_status
(
    order_status_id SERIAL PRIMARY KEY,
    status_name VARCHAR(255)
);

CREATE table Orders
(
    order_id SERIAL PRIMARY KEY,
    Cart_cart_id INT REFERENCES Carts(cart_id),
    Order_status_order_status_id INT REFERENCES Order_status(order_status_id),
    shipping_total DECIMAL,
    total DECIMAL,
    create_at timestamp(2),
    update_at timestamp(2)
);

CREATE TABLE Categories
(
    category_id SERIAL PRIMARY KEY,
    category_title VARCHAR(255),
    category_description TEXT
);

CREATE TABLE Products
(
    product_id SERIAL PRIMARY KEY,
    product_title VARCHAR(255),
    product_description TEXT,
    in_stock INT,
    price FLOAT,
    slug VARCHAR(45),
    category_id INT REFERENCES Categories(category_id)
);

CREATE TABLE Cart_products
(
    cart_cart_id INT REFERENCES Carts(cart_id),
    products_product_id INT REFERENCES Products(product_id)
);

COPY  users(
     user_id,
     email,
     password,
     first_name,
     last_name,
     middle_name,
     is_staff,
     country,
     city,
     address)
FROM '/usr/src/users.csv'
DELIMITER ',' CSV;

COPY  Carts(
     cart_id,
     Users_uses_id,
     subtotal,
     total,
     timestamp
   )
FROM '/usr/src/carts.csv'
DELIMITER ',';

COPY  categories(
     category_id,
     category_title,
     category_description
   )
FROM '/usr/src/categories.csv'
DELIMITER ',';

COPY  products(
     product_id,
     product_title,
     product_description,
     in_stock,
     price,
     slug,
     category_id)
FROM '/usr/src/products.csv'
DELIMITER ',';


COPY  cart_products(
     cart_cart_id,
     products_product_id
   )
FROM '/usr/src/cart_products.csv'
DELIMITER ',';

COPY  order_status(
     order_status_id,
     status_name
   )
FROM '/usr/src/order_statuses.csv'
DELIMITER ',';

COPY  orders(
     order_id,
     cart_cart_id,
     Order_status_order_status_id,
     shipping_total,
     total,
     create_at,
    update_at
   )
FROM '/usr/src/orders.csv'
DELIMITER ',';

SELECT * FROM Users
ORDER BY user_id ASC LIMIT 10;

-- Phone number column to the Users table
ALTER TABLE Users ADD COLUMN phone_number INT;

-- Changing of column type (int -> varchar)
ALTER TABLE Users ALTER COLUMN phone_number TYPE VARCHAR(13);

-- Checking products prices
SELECT product_title, price
FROM Products
ORDER BY product_id;

-- Get x2 price from DB
SELECT product_title, price * 2
FROM Products
ORDER BY product_id;

-- update Products price (x2)
UPDATE Products
SET price = price * 2;



SELECT t.*
FROM public.users t
LIMIT 501