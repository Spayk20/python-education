-- Задание 3
-- Создать 3 представления (1 из них должно быть материализированным и хранить данные от "тяжелого" запроса).

--список всех телефонов кастомеров
begin;
     CREATE VIEW customer_phones AS
        select c.first_name, c.second_name, phone_number::text from customer c
        join phones p on c.phones_phone_id = p.phone_id;

select * from customer_phones;
commit;
drop view customer_phones;

--список аренд которые длились до 100 дней

begin;
create view days_rents as
	select * from rent_cars.public.orders
	where extract(day from renting_period - renting_day) between 0 and 100
	order by price;

select * from days_rents;
commit;
drop view days_rents;


-- материализированное представление всех офисов

create materialized view branches_addresses as
	select b as branch, c as city, s as street, b2 as state from branch b
		join address a  on a.address_id = b.address_address_id
		join city c on c.city_id = a.cities_city_id
		join street s on s.street_id = a.streets_street_id
		join state b2 on b2.state_id = a.states_state_id
		order by c;

refresh materialized view branches_addresses;
select from branches_addresses;