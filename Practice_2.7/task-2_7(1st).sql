--1. Создать функцию, которая сетит shipping_total = 0 в таблице order, если город юзера
-- равен x. Использовать IF clause.

CREATE OR REPLACE FUNCTION shipping_total_zero(x varchar(255))
    RETURNS void
    LANGUAGE plpgsql
    AS
        $$
            DECLARE
                shipping_to_zero orders.shipping_total%type = 0;
                save_zero_order orders%rowtype;
            BEGIN
                SELECT  o.* FROM orders o
                right join carts c on o.cart_cart_id = c.cart_id
		        right join users u on c.users_uses_id = u.user_id
                WHERE u.city = x
                INTO save_zero_order;

                IF NOT FOUND THEN
                    RAISE NOTICE 'City does not exist';
                ELSE
                    RAISE NOTICE 'I will set shipping_total to 0 in order %', save_zero_order.order_id;
                    UPDATE orders SET shipping_total = shipping_to_zero
                    WHERE order_id = save_zero_order.order_id;
                end if;
            end
        $$;


SELECT shipping_total_zero('city 2');

select shipping_total, city from orders o
	    join carts c on o.order_id=c.cart_id
		join users u on c.users_uses_id=u.user_id;

rollback;

DROP FUNCTION shipping_total_zero(x varchar);


select shipping_total, city from orders o
	    join carts c on o.order_id=c.cart_id
		join users u on c.users_uses_id=u.user_id;