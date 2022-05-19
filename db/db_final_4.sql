-- task 4
-- 1 func - table: return user table by rent ID
create or replace function get_customers(id_rent int)
    returns table
            (
                customer_id  int,
                first_name   varchar,
                last_name    varchar,
                rent_id      int,
                car_id       int,
                date_renting timestamp
            )
    language plpgsql
as
$$
begin
    return query
        select customer.customer_id,
               customer.first_name,
               customer.last_name,
               rent.rent_id,
               rent.car_id,
               rent.date_renting
        from customer
                 join rent on customer.customer_id = rent.customer_id and rent.rent_id = id_rent;
end;
$$;
-- check result
select *
from get_customers(id_rent := 15);

-- 2 func - loop working: return sum rent
create or replace function shipping_total_rent(id_customers int)
    returns integer
    language plpgsql
as
$$
declare
    customer_id_check record;
    sum_all_rent      int=0;
begin
    for customer_id_check in (select *
                              from rent
                                       join customer on rent.customer_id = customer.customer_id
                                       join car on car.car_id = rent.car_id)
        loop
            if customer_id_check.customer_id = id_customers then
                sum_all_rent = sum_all_rent + customer_id_check.price_usd;
            end if;
        end loop;
    return sum_all_rent;
end;
$$;
-- check result
select *
from shipping_total_rent(id_customers := 4);

-- 3 func - use cursor: return count rent customers
create or replace function get_all_rent_customer(customers_id int)
    returns text
    language plpgsql as
$$
declare
    customer_rent_id int = 0; -- default number
    record_rent      record;
    cursor_rent cursor (find_rent_id int) for select customer.customer_id
                                              from customer
                                                       left join rent on customer.customer_id = rent.customer_id
                                              where customers_id = customer.customer_id; -- cursor
begin
    open cursor_rent(customers_id);
    loop
        fetch cursor_rent into record_rent;
        exit when not found;
        customer_rent_id = customer_rent_id + 1;
    end loop;
    close cursor_rent;
    return customer_rent_id;
end;
$$;
-- check result
select *
from get_all_rent_customer(customers_id := 4)