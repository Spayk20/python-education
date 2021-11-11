-- Задание 2
-- Придумать 3 различных запроса SELECT с осмысленным использованием разных видов JOIN.
-- Используя explain добавить только необходимые индексы для уменьшения стоимости (cost) запросов.

EXPLAIN ANALYSE select c.first_name, o.order_id, p.cars_car_id, o.price
from orders o
join customer c on c.user_id=o.customer_user_id
join products p on o.products_product_id=p.product_id
where extract(day from o.renting_period - o.renting_day) between 0 and 100
ORDER BY price ASC;

-- select extract(day from o.renting_period - o.renting_day)
-- from orders o

create index on "customer"(second_name);
create index on "orders"(extract(day from renting_period - renting_day));



-- Поиск топ 10 кастомеров которые сделали за первый месяц 2021 года
begin transaction;
    -- (cost=24.35..24.38)
	explain analyze select * from orders o
			right join customer c on o.customer_user_id = c.user_id
	        where (c.user_id between 1 and 100) and (o.renting_day BETWEEN '2021.01.01' AND '2021.02.01')
	        order by o.price desc;

create index renting_day_idx on "orders"(renting_day);
--(cost=22.13..22.16)
drop index renting_day_idx;


-- поиск кастомеров которые потратили от 3000 до 5000
--(cost=33.02..33.29)
EXPLAIN (ANALYSE) select c.first_name, o.price from orders as o
join customer c on c.user_id = o.customer_user_id
where o.price between 3000::money and 5000::money
order by o.price desc;

create index orders_price_idx on "orders"(price);
--(cost=30.59..30.86)

drop index orders_price_idx;