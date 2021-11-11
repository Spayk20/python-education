-- Задание 1.2.1
-- Создать бд, создать таблицы, добавить связи между таблицами, заполнить таблицу данными
--(их нужно сгенерировать в большом количестве - для этого можно использовать последовательности, собственные или
-- встроенные функции - никаких внешних генераторов).

DROP DATABASE IF EXISTS rent_cars;
CREATE DATABASE rent_cars;


BEGIN;
ROLLBACK;

-- Таблицы адресов
CREATE TABLE IF NOT EXISTS state (
    state_id SERIAL PRIMARY KEY NOT NULL,
    state_name varchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS street (
    street_id SERIAL PRIMARY KEY NOT NULL,
    street_name varchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS city (
    city_id SERIAL PRIMARY KEY NOT NULL,
    city_name varchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS address (
    address_id SERIAL PRIMARY KEY NOT NULL,
    streets_street_id INT REFERENCES street(street_id) NOT NULL,
    cities_city_id INT REFERENCES city(city_id) NOT NULL,
    states_state_id INT REFERENCES state(state_id) NOT NULL
);

-- Таблицы автомобилей
CREATE TABLE IF NOT EXISTS car_brand (
    brand_id SERIAL PRIMARY KEY NOT NULL,
    brand_name varchar(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS car_model (
  model_id SERIAL PRIMARY KEY NOT NULL,
  car_brand_brand_id INT REFERENCES car_brand(brand_id),
  model_name varchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS cars (
    car_id SERIAL PRIMARY KEY NOT NULL,
    car_brand_brand_id INT REFERENCES car_brand(brand_id),
    car_model_model_id INT REFERENCES car_model(model_id),
    car_plate varchar(10) NOT NULL
);

--Таблица номеров телефонов
CREATE TABLE IF NOT EXISTS phones (
    phone_id SERIAL PRIMARY KEY NOT NULL,
    phone_number int NOT NULL
);

--Табицы кастомеров
CREATE TABLE IF NOT EXISTS customer (
    user_id SERIAL PRIMARY KEY NOT NULL,
    first_name varchar(25) NOT NULL,
    second_name varchar(25) NOT NULL,
    phones_phone_id INT REFERENCES phones(phone_id),
    cars_car_id INT REFERENCES cars(car_id),
    address_address_id INT REFERENCES address(address_id)
);

--Таблица адреса офиса
CREATE TABLE IF NOT EXISTS branch (
    branch_id SERIAL PRIMARY KEY NOT NULL,
    phones_phone_id INT REFERENCES phones (phone_id),
    address_address_id INT REFERENCES address(address_id)
);

--Таблица связей автомобилей с офисами
CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY NOT NULL,
    cars_car_id INT REFERENCES cars(car_id),
    branch_branch_id INT REFERENCES branch(branch_id)
);

-- Таблица ордеров
CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY NOT NULL,
    customer_user_id INT REFERENCES customer(user_id) NOT NULL,
    products_product_id INT REFERENCES products(product_id) NOT NULL,
    price money NOT NULL,
    renting_period timestamp(2) NOT NULL,
    renting_day timestamp(2) NOT NULL
);

COMMIT;

begin;

CREATE OR REPLACE FUNCTION generator_of_address()
    returns VARCHAR
    LANGUAGE plpgsql
as $$
    DECLARE
        var_r record;
    BEGIN
        for var_r in
            select generate_series(1,500) as id
        loop
            insert into street (street_name)
            values (('street ' || var_r.id)::text);
            insert into city (city_name)
            values (('city ' || var_r.id)::text);
            insert into state (state_name)
            values (('state ' || var_r.id)::text);
        END loop;
        RETURN var_r;
    END;
$$;

select generator_of_address();
select * from street;
select * from city;
select * from state;
rollback;
commit;

-- Я сделал ошибку, исправил с помощью удаленияданных из таблиц и обнуления последовательности
-- TRUNCATE street cascade;
-- TRUNCATE city cascade;
-- TRUNCATE state cascade;
--
-- ALTER SEQUENCE street_street_id_seq RESTART WITH 1;
-- ALTER SEQUENCE city_city_id_seq RESTART WITH 1;
-- ALTER SEQUENCE address_address_id_seq RESTART WITH 1;
-- ALTER SEQUENCE state_state_id_seq RESTART WITH 1;

-- пока что должен остаться пустым
select * from address;

--заполнение таблицы связей
begin;
insert into address (streets_street_id, cities_city_id, states_state_id)
    select s.street_id, c.city_id, st.state_id
    from street as s
    join city c on c.city_id=s.street_id
    join state st on st.state_id =s.street_id;

select * from address;
commit;

begin;
CREATE OR REPLACE FUNCTION generator_of_cars()
    returns VARCHAR
    LANGUAGE plpgsql
as $$
    DECLARE
        var_r record;
    BEGIN
        for var_r in
            select generate_series(1, 1000) as id
        loop
            insert into car_brand (brand_name)
            values (('cb ' || var_r.id)::text);
            insert into car_model (model_name)
            values (('model ' || var_r.id)::text);
        END loop;
        RETURN var_r;
    END;
$$;
select generator_of_cars();
select * from car_model;
select * from car_brand;
savepoint save_generator_of_cars;

update car_model c
set car_brand_brand_id = (select brand_id
                        from car_brand
                        where brand_id=c.model_id)
where (car_brand_brand_id::text = '') IS NOT FALSE;

ROLLBACK to savepoint save_generator_of_cars;
savepoint save_cars_model;
ROLLBACK to savepoint save_cars_model;
ROLLBACK;
commit;

begin;

CREATE OR REPLACE FUNCTION cars()
    returns VARCHAR
    LANGUAGE plpgsql
as $$
    DECLARE
        var record;
    BEGIN
        for var in
            select generate_series(1, 500) as id
        loop
            insert into cars (car_plate, car_brand_brand_id, car_model_model_id)
            values (substr(md5(random()::text), 0, 10),
                    var.id, var.id
                    );
        END loop;
        RETURN var;
    END;
$$;

select cars();
select * from cars where car_id=500;
commit;



begin;
-- генерация номеров телефонов

CREATE OR REPLACE FUNCTION phone_num_generator()
    returns VARCHAR
    LANGUAGE plpgsql
as $$
    DECLARE
        var record;
    BEGIN
        for var in
            select generate_series(1, 1000) as id
        loop
            insert into phones (phone_number)
            values (floor(random()*1000000000));
        END loop;
        RETURN var;
    END;
$$;

select phone_num_generator();
select * from phones;
commit;

-- генераця кастомеров
begin;
CREATE OR REPLACE FUNCTION customer_gen()
    returns VARCHAR
    LANGUAGE plpgsql
as $$
    DECLARE
        var record;
    BEGIN
        for var in
            select generate_series(1, 500) as id
        loop
            insert into customer (first_name, second_name, phones_phone_id, cars_car_id, address_address_id)
            values ('name ' || var.id, 'second_name ' || var.id, var.id, var.id, var.id);
        END loop;
        RETURN var;
    END;
$$;

select customer_gen();
select * from customer;
commit;

-- генерация офисов
begin;
CREATE OR REPLACE FUNCTION branch_gen()
    returns VARCHAR
    LANGUAGE plpgsql
as $$
    DECLARE
        var record;
    BEGIN
        for var in
            select generate_series(1, 500) as id
        loop
            insert into branch (phones_phone_id, address_address_id)
            values (500+var.id, var.id);
        END loop;
        RETURN var;
    END;
$$;

select branch_gen();
select * from branch;
commit;

-- генерация товаров (услуг)
begin;
CREATE OR REPLACE FUNCTION products_gen()
    returns VARCHAR
    LANGUAGE plpgsql
as $$
    DECLARE
        var record;
    BEGIN
        for var in
            select generate_series(1, 500) as id
        loop
            insert into products (cars_car_id, branch_branch_id)
            values (var.id, var.id);
        END loop;
        RETURN var;
    END;
$$;

select products_gen();
select * from products;
commit;


-- генерация заказов
begin;
CREATE OR REPLACE FUNCTION orders_gen()
    returns VARCHAR
    LANGUAGE plpgsql
as $$
    DECLARE
        var record;
    BEGIN
        for var in
            select generate_series(1, 500) as id
        loop
            insert into orders (customer_user_id, products_product_id, price, renting_period, renting_day)
            values (var.id, var.id, floor(random()*10000)::int::money,
                    (format('2021-%s-%s', floor(random()*10+1), floor(random()*10+1)))::timestamp,
                    (format('2021-%s-%s', floor(random()*10+1), floor(random()*10+1)))::timestamp);
        END loop;
        RETURN var;
    END;
$$;

select orders_gen();
select * from orders;
commit;

