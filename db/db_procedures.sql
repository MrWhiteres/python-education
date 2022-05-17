-- func set shipping_total = 0 if city_name = users.city --
create or replace function shipping_total_orders(city_name varchar)
    returns orders.shipping_total%type
    language plpgsql
as
$$
declare
    user_city_check record;
    sum_all_orders  orders.shipping_total%type=0;
begin
    for user_city_check in (select shipping_total, order_id, users.city
                            from orders
                                     join carts on carts.card_id = orders.carts_cart_id
                                     join users on users.user_id = carts.users_user_id)
        loop
            if user_city_check.city = city_name then -- run a loop to search for users with the same city, if a user with the same city name is found, we add the amount of his purchase to the total and update it to 0 --
                sum_all_orders = sum_all_orders + user_city_check.shipping_total;
                update orders set shipping_total = 0 where orders.order_id = user_city_check.order_id;
            end if;
        end loop;
    return sum_all_orders;
end;
$$;
-- check result working func --
select shipping_total_orders(city_name := 'city 20');
-- del func --
drop function shipping_total_orders(varchar);

-- first procedure 'change password' --
create or replace procedure change_user_password(id_user int, new_password varchar)
    language plpgsql
as
$$
declare
    old_password varchar;
begin
    -- get user password --
    select password
    into old_password
    from users
    where user_id = id_user;

    -- check new password --
    if old_password = new_password then
        raise exception 'Can not set passwords that exist now.';
    end if;

    update users
    set password = new_password
    where user_id = id_user;


end;
$$;
call change_user_password(id_user := '1', new_password := '123456');
select *
from users
where password = '123456';
-- drop procedure --
drop procedure change_user_password(id_user int, new_password varchar);

-- second procedure 'product price discount' -id_product or 'category product id' -id_category --
create or replace procedure product_price_discount(id_product int, discount float)
    language plpgsql
as
$$
declare
    old_price float = null;
begin
    select price
    into old_price
    from products
    where product_id = id_product;
    -- check raise --
    if discount = 0 then
        raise 'Discount != 0';
    elseif discount < 0 and discount > 1 then
        raise exception 'discount must be in (0 < discount < 0)';
    elseif old_price is null then
        raise 'category product not found';
    end if;
    -- discount worker --
    update products
    set price = round((price - (price * discount))::numeric, 2)
    where product_id = id_product;
    commit;
end;
$$;
call product_price_discount(id_product := 1, discount := 0.1);
-- check result --
select *
from products
where category_id = 1;
-- drop procedure --
drop procedure product_price_discount(id_product int, discount float);


-- third procedure 'sell product' --
create or replace procedure sell_products(id_product int, count_product int)
    language plpgsql
as
$$
declare
    product_stock int = null;
    new_stock     int = null;
begin
    select in_stock
    into product_stock
    from products
    where product_id = id_product;
    -- check if there is such a product --
    if product_stock is null then
        raise exception 'Product not found';
    end if;
    -- operation to change the quantity of products --
    update products
    set in_stock = in_stock - count_product
    where product_id = id_product;
    -- new value check --
    select in_stock
    into new_stock
    from products
    where product_id = id_product;
    -- If the new value is less than 0 returns the amount that was --
    if new_stock >= 0 then
        commit;
    else
        rollback;
    end if;
    if new_stock < 0 then
        raise 'the number of products to buy exceeds the amount in stock';
    end if;
end;
$$;
-- call procedure --
call sell_products(id_product := 1, count_product := 46);
-- check result --
select * from products where product_id = 1;
-- drop procedure --
drop procedure sell_products(id_product int, count_product int);