-- task 6
-- 1 trigger before
create or replace function update_car_price()
    returns trigger
    language plpgsql
as
$$
begin
    if new.price_usd = old.price_usd or new.price_usd <= 0 then
        raise 'Check your date';
    end if;
    return new;
end;
$$;

create trigger trigger_update_car_price
    before update
    on car
    for each row
execute function update_car_price();

update car
set price_usd = 0
where car_id = 1;
-- check result
select *
from car
where car_id = 1;
drop trigger trigger_update_car_price on auto_rent.public.car;

-- table and use 2 func/ 2 trigger before and after
-- func return customer last and first name
create or replace function get_customer_name(id_car int)
    returns varchar
    language plpgsql
as
$$
declare
    customer_name varchar;
begin
    select customer.last_name || ' ' || customer.first_name
    into customer_name
    from car
             join rent on car.car_id = rent.car_id
             join customer on customer.customer_id = rent.customer_id
    where car.car_id = id_car;
    return customer_name;
end;
$$;
-- function informs the buyer about the approaching end or end of the car rental period
create or replace function end_period_renting()
    returns trigger
    language plpgsql
as
$$
declare
    name_customer varchar;
begin
    name_customer = get_customer_name(id_car := new.car_id);
    if new.period_renting > old.period_renting then
        raise notice 'Dear ,%, under the % contract, the car rental time was increased by - %',name_customer, new.rent_id, new.period_renting - old.period_renting;
    end if;
    if new.period_renting = 1 then
        raise notice 'Dear ,%, according to the contract % the rental period ends tomorrow.',name_customer, new.rent_id;
    end if;
    if new.period_renting = 0 then
        raise notice 'Dear ,%, according to the contract % the rental period ends..',name_customer, new.rent_id;
    else
        return null;
    end if;
    return new;
end;
$$;
-- mini function to check if auto rental period value is a positive number
create or replace function before_period_renting()
    returns trigger
    language plpgsql
as
$$
begin
    if new.period_renting < 0 then
        raise 'period_renting must by >= 0';
    end if;
    return new;
end;
$$;
-- 2 triggers that work before and after data update
create trigger after_update_period_rent
    after update
    on rent
    for each row
execute function end_period_renting();

create trigger before_update_period_rent
    before update
    on rent
    for each row
execute function before_period_renting();
-- test work
update rent
set period_renting = 1
where rent_id = 1;
-- check result
select * from rent where rent_id = 1;

-- drop func and trigger
drop function if exists get_customer_name;
drop function if exists end_period_renting;
drop function if exists before_period_renting;
drop trigger if exists after_update_period_rent on auto_rent.public.rent;
drop trigger if exists before_update_period_rent on auto_rent.public.rent;