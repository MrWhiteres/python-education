-- task 5
-- change price car by id
create or replace procedure change_price_car(id_car int, new_price int)
    language plpgsql
as
$$
declare
    old_price int default null;
begin
    select price_usd into old_price from car where car_id = id_car;

    update car
    set price_usd = new_price
    where car_id = id_car;

    if new_price > 0 and new_price != old_price then
        commit;
    else
        rollback;
    end if;
end;
$$;
-- check result
call change_price_car(id_car := 1, new_price := 10);
select *
from car
where car_id = 1;

-- add new car
create or replace procedure add_new_car(id_car int, model_car_id int, number_car varchar, price int, car_id_branch int)
    language plpgsql
as
$$
begin
    insert into car(car_id, car_model_id, car_number, price_usd, branch_car_id)
    values (id_car, model_car_id, number_car, price, car_id_branch);

    if (car_id_branch > 0 and model_car_id <= 10000) and
       number_car != '' and price != 0 then
        commit;
    else
        rollback;
    end if;
end;
$$;
-- check result
call add_new_car(10001, 1 , '465219655', 1, 1);
select * from car where car_id = 10001;