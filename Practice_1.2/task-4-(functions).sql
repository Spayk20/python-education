--Задание 4
--Создать 2 функции (одна из них должна возвращать таблицу, одна из них должна использовать циклы,
--одна из них должна использовать курсор

begin;
create or replace function user_phone_number (user_id_phone int)
returns table (
  phone varchar)
language plpgsql
as $$
declare
    var_r record;
begin
  for var_r in (
            select ('+180'||p.phone_number::text) as user_phone from customer c
        join phones p on c.phones_phone_id = p.phone_id
        where c.cars_car_id = user_id_phone)
      loop
                phone := var_r.user_phone;
           return next;
  end loop;
end; $$;

select * from user_phone_number(53);

rollback;

commit;

drop function if exists user_phone_number;



-- 2я функция с использованием курсора, замена номера у указаного айди

begin;

create or replace function search_phone_number(search_number int, new_number int)
returns void
language plpgsql
as $$
declare
	cur cursor for select * from phones;
begin
	for rec in cur
	    loop
		if rec.phone_id = search_number then
			raise notice 'Phone number % was found', rec;
			update phones set phone_number = new_number
				where phone_id = search_number;
		end if;
-- 		if not found then
-- 			raise notice 'The phone not found';
-- 			rollback;
-- 		end if;
	end loop;
end;
$$;

select * from search_phone_number(1, 15018399);

select * from phones
	order by phone_id;

rollback;

drop function if exists search_phones;