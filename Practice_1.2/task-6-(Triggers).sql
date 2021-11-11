-- Задание 6
-- Добавить 2 триггера (один из них ДО операции по изменению данных, второй после) и функции или процедуры-обработчики к ним.


-- Триггер на запрет удаления из таблицы, срабатывает до удаления

begin;
create or replace function without_delete()
    returns trigger
    language plpgsql
as
    $$
    BEGIN
        raise 'You have not permissions to delete users';
    end;
    $$;

ROLLBACK;

CREATE TRIGGER alert_deleting
  BEFORE DELETE
  ON customer
  FOR EACH ROW
  EXECUTE PROCEDURE without_delete();

DELETE from customer where user_id = 50;

ROLLBACK;
COMMIT;



-- триггер на запрет любых изменений в таблице срабатывает вместо изменения

drop view best_customers_view;
create or replace view best_customers_view as
	select * from best_customers;

drop function err_messages cascade;

create or replace function err_messages()
	returns trigger
	language plpgsql
as
$$
begin
	if TG_OP = 'INSERT' then
		raise notice 'Sorry, you can not insert raw';
		return old;
	elsif TG_OP = 'DELETE' then
		raise notice 'Sorry, you can not delete raw';
		return old;
	elsif TG_OP = 'UPDATE' then
		raise notice 'Sorry, you can not update raw';
		return old;
	end if;
end;
$$;

drop trigger replacement on best_customers_view;

create trigger replacement
	instead of insert or update or delete
	on best_customers_view
	for each row
	execute procedure err_messages();

insert into best_customers_view(user_id, best_buy)
	values(101, 2802::money);

update best_customers_view set best_buy = 2802::money
	where user_id = 101;

delete from best_customers_view where user_id = 101;

select * from best_customers
order by user_id;

rollback;


-- триггер на добавление удаленной строки в другую таблицу

create or replace function log_best_customers_delete()
returns trigger
language plpgsql as
$$
begin
	create table if not exists deleted_best_customers(
		user_id integer,
	    best_buy money
	    );
	raise notice '%, %', new.user_id, old.user_id;
	insert into deleted_best_customers(user_id, best_buy)
		values(old.user_id, old.best_buy);
	return old;
end;
$$;

drop trigger replacement on best_customers;

create trigger delete_best_customers_log
	after delete
	on best_customers
	for each row
	execute procedure log_best_customers_delete();


begin transaction;
    select * from best_customers;
    delete from best_customers where user_id = 14;
    select * from best_customers;
    select * from deleted_best_customers;
rollback;
