-- 1й запрос

BEGIN;

EXPLAIN ANALYSE SELECT name, city from potential_customers
WHERE id > 3
ORDER BY city desc;
--Sort  (cost=16.05..16.27 rows=87 width=150) (actual time=0.037..0.038 rows=7 loops=1)

CREATE INDEX IF NOT EXISTS idx_name_id_city ON potential_customers
    USING btree(id, city) WHERE id = 3;

EXPLAIN ANALYSE SELECT name, city from potential_customers
WHERE id > 3
ORDER BY city desc;
--Sort  (cost=1.15..1.16 rows=3 width=150) (actual time=0.081..0.085 rows=7 loops=1)

DROP INDEX IF EXISTS idx_name_id_city;

ROLLBACK;


-- 2й запрос

explain analyze select * from orders
where total > 300 and create_at between '2018-01-01' and '2019-01-01';
--Seq Scan on orders  (cost=0.00..39.25 rows=281 width=39) (actual time=0.014..0.464 rows=278 loops=1)

create index idx_orders_total_create_at on orders (total, create_at);
explain analyze select * from orders
where total > 300 and create_at between '2018-01-01' and '2019-01-01';
--Seq Scan on orders  (cost=0.00..39.25 rows=281 width=39) (actual time=0.015..0.721 rows=278 loops=1)


-- 3й запрос

explain analyze select price, category_id from products
where category_id in (4, 17)
order by price asc
limit 10;
--Limit  (cost=164.98..165.01 rows=10 width=12) (actual time=1.353..1.358 rows=10 loops=1)

create index if not exists idx_product_category_id_price on products
	using btree(category_id, price) where category_id in(4, 17);
--Limit  (cost=33.19..33.21 rows=10 width=12) (actual time=0.559..0.566 rows=10 loops=1)

drop index if exists idx_product_category_id_price;