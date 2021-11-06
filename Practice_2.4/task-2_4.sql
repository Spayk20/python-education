select * from potential_customers

-- INSERT в таблицу potential_customers

begin;

select * from potential_customers pc
order by id desc limit 13;

insert into potential_customers(id, email, "name", surname, second_name, city)
values (12, 'user12@mail.com', 'John', '3Volta', 'Vasiljevich', 'city 11');

insert into potential_customers(id, email, "name", surname, second_name, city)
values (13, 'user13@mail.com', 'Vinn', 'Drisel', 'Ostapovich', 'city 15');

savepoint first_insert;

insert into potential_customers(id, email, "name", surname, second_name, city)
values (14, 'user14@mail.com', 'Bro', 'Bor', 'Rob', 'city 17');

rollback to savepoint first_insert;

commit;




-- Расширенный вариант
set transaction isolation level serializable;

begin;

select * from potential_customers
order by id ASC limit 13;


update potential_customers
	set name = 'New_name1', surname = 'New_surname1', second_name = 'New_second_name1'
where id = 1;

savepoint update_name;

alter table potential_customers
	rename name to Name;

savepoint alter_rename;

delete from potential_customers where id = 3;

savepoint delete_id3;

insert into potential_customers (id, email, Name, surname, second_name, city)
values
	(3, 'user33@mail.com', 'new_name33', 'new_surname33', 'new_second_name33', 'city 33');

release savepoint delete_id3;
release savepoint alter_rename;
release savepoint update_name;
rollback to savepoint update_name;
rollback;
commit;




-- Транзакция для таблицы Products

begin;

select * from products
order by product_id desc limit 15;

insert into products(product_id, product_title, product_description, in_stock, price, slug, category_id)
values (5555, 'LoveIs', 'Gum', 100, 5, 'LoveIs', 5);

savepoint new_prod;

delete from products where product_title = 'LoveIs';

rollback to savepoint new_prod;

update products
set in_stock = 500
where product_title = 'LoveIs';

savepoint updating;

delete from products where product_description = 'Gum';

rollback to savepoint updating;
release savepoint new_prod;

update products
set in_stock = in_stock - 20
where product_title = 'LoveIs';

commit;


-- Транзакция для таблицы Orders

begin;
savepoint start;

update orders set total=0;

select * from orders;

rollback to savepoint start;

select * from orders;

update orders set shipping_total=0;

select * from orders;

rollback;