-- Написать 2 любые хранимые процедуры с использованием условий, циклов и транзакций.

ALTER TABLE potential_customers ADD COLUMN passport_id smallint;

BEGIN;
    CREATE OR REPLACE PROCEDURE create_passport_id()
    LANGUAGE plpgsql
    AS $$
        DECLARE
            create_passport smallint;
            var record;
        BEGIN
            FOR var in
                SELECT passport_id
                FROM potential_customers
            loop
                if var.passport_id is not NULL THEN
                    create_passport = (SELECT (random()*(32767-0)+0)::smallint);
                    UPDATE potential_customers
                    SET passport_id = create_passport
                    WHERE var.passport_id is not NULL;
                    RAISE NOTICE 'Users passport id does not exist. Automatically generated: %', create_passport;
                end if;
            end loop;
        end;
    $$;

CALL create_passport_id();

SELECT * FROM potential_customers;

ROLLBACK;

DROP PROCEDURE create_passport_id();



-- 2nd variant

BEGIN;
    CREATE OR REPLACE PROCEDURE test2()
    LANGUAGE plpgsql
    AS $$
        DECLARE
            var record;
        BEGIN
            FOR var in
                SELECT city
                FROM potential_customers
            loop
                if var.city = 'city 17' THEN
                    UPDATE potential_customers
                    SET passport_id = 0170
                    WHERE var.city = 'city 17';
                elseif var.city = 'city 1' THEN
                    UPDATE potential_customers
                    SET passport_id = 1111
                    WHERE var.city = 'city 1';
                    ROLLBACK;
                end if;
            end loop;
        end
    $$;

-- Test
CALL test2();

SELECT * FROM potential_customers;

DROP PROCEDURE test2();

ROLLBACK;