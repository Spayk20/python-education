-- Сравнить цену каждого продукта n с средней ценой продуктов в категории
-- продукта n. Использовать window function. Таблица результата должна
-- содержать такие колонки: category_title, product_title, price, avg.

SELECT c.category_title, p.product_title, p.price, avg(p.price) OVER
	(PARTITION BY c.category_id)
	FROM products p LEFT JOIN categories c
		ON p.category_id = c.category_id;


-- Добавить 2 любых триггера и обработчика к ним, использовать транзакции.

BEGIN ;
DROP TABLE  trigger_table_of_prod;

CREATE TABLE IF NOT EXISTS trigger_table_of_prod(
    product_id smallint references products(product_id),
    old_product_title varchar,
    old_product_description varchar,
    old_price float,
    action varchar
);


DROP FUNCTION after_insert() CASCADE;

CREATE OR REPLACE FUNCTION after_insert()
RETURNS trigger
LANGUAGE plpgsql
AS
$$
    BEGIN
        IF NEW.product_title <> OLD.product_title OR
           NEW.product_description <> OLD.product_description OR
           NEW.price <> OLD.price
            THEN
            INSERT INTO trigger_table_of_prod(product_id, action, old_product_title, old_product_description, old_price)
            VALUES(product_id, 'update', OLD.product_title, OLD.product_description, OLD.price);
        end if;
        RETURN NEW;
end; $$;


CREATE TRIGGER aftar_insert
    BEFORE UPDATE
    ON products
    FOR EACH ROW
    EXECUTE PROCEDURE after_insert();

UPDATE products
SET price = 333
WHERE product_id = 34;

select * from products;
select * from trigger_table_of_prod;

ROLLBACK;
COMMIT;



BEGIN;
CREATE OR REPLACE FUNCTION on_delete()
returns trigger
language plpgsql
as
    $$
    BEGIN
        insert into trigger_table_of_prod(product_id, action)
        VALUES(OLD.product_id, 'delete');
        RAISE NOTICE 'This product already deleted',  OLD.product_id;
    end;
    $$;

CREATE TRIGGER loggigng_delete_products
  BEFORE DELETE
  ON products
  FOR EACH ROW
  EXECUTE PROCEDURE on_delete();

DELETE FROM products
WHERE product_id = 33;

SELECT * FROM trigger_table_of_prod;

ROLLBACK;
COMMIT;