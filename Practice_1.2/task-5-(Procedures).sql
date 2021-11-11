-- Задание 5
-- Написать 2 любые хранимые процедуры. В них использовать транзакции для insert, update, delete.

-- 1я хранимая процедура

create table best_customers(
  user_id serial primary key not null,
  best_buy money  not null
);

begin;
    create or replace procedure best_of_the_best()
    language plpgsql
    AS $$
        declare
            var record;
        begin
            for var in
                select distinct o.customer_user_id,
                                max(o.price) over (partition by o.customer_user_id) as max
                from orders o
                limit 10
            loop
                if var.max = 100::money  then
                    raise notice 'Error';
                    rollback ;
                end if;
                -- INSERT
                insert into best_customers(best_buy) values(var.max);
                -- UPDATE
                update orders set price = 0::money where customer_user_id = var.customer_user_id;
            end loop;
        end;
    $$;
call best_of_the_best();
select * from best_customers;
select * from orders;
rollback;
commit;

drop procedure best_of_the_best();



-- 2я хранимая процедура

begin;


create or replace procedure add_new_car(car_name varchar(10), car_model int)
language plpgsql
as $$
declare
	name_of_car cars.car_plate%type;
	new_plate varchar(15) := 'abc3434ba';
begin
	update cars set car_plate = new_plate
		where car_plate = car_name
		returning car_plate
		into name_of_car;
	if name_of_car is not null then
        commit;
		raise notice 'New car plate set to %', name_of_car;
		update cars set car_model_model_id = car_model
		where car_plate = new_plate;
		commit;
	else
		raise notice 'Car plate of the new car set %', new_plate;
		insert into cars (car_id, car_brand_brand_id, car_model_model_id, car_plate)
			values(501, 501, 501, new_plate);
	end if;
end;
$$;

rollback;

call add_new_car('ax495d0xx', 3);

select * from cars
order by car_id;

drop procedure add_new_car(car_name varchar(10), car_model int);