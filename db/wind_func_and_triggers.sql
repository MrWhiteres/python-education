select category_title,
       product_title,
       price,
       round((avg(price) over (partition by products.category_id))::numeric, 2) as avg_category_price
from products
         join categories on products.category_id = categories.category_id
where products.category_id = categories.category_id;


-- first trigger, keeping track of price changes --
-- crate new table, data about price changes for products will be stored here --
create table changer_price_product
(
    changer_id int generated always as identity,
    product_id int     not null,
    old_price  numeric not null,
    new_price  numeric not null
);
-- trigger works when the price of the product changes --
create or replace function update_product_price()
    returns trigger
    language plpgsql
as
$$
begin
    if new.price != old.price and new.price > 0 then
        insert into changer_price_product(product_id, old_price, new_price)
        values (old.product_id, old.price, new.price);
    end if;
    return new;
end;
$$;
-- get trigger --
begin;
drop trigger if exists update_product_price_change on shop.public.products;
create trigger update_product_price_change
    before update
    on products
    for each row
execute procedure update_product_price();
commit;

-- here we see the old price --
select *
from products
where product_id = 1;

-- data is updated here or use procedure --
-- create or replace procedure sell_products(id_product int, count_product int)
--     language plpgsql
-- as
-- $$
-- declare
--     product_stock int = null;
--     new_stock     int = null;
-- begin
--     select in_stock
--     into product_stock
--     from products
--     where product_id = id_product;
--     -- check if there is such a product --
--     if product_stock is null then
--         raise exception 'Product not found';
--     end if;
--     -- operation to change the quantity of products --
--     update products
--     set in_stock = in_stock - count_product
--     where product_id = id_product;
--     -- new value check --
--     select in_stock
--     into new_stock
--     from products
--     where product_id = id_product;
--     -- If the new value is less than 0 returns the amount that was --
--     if new_stock >= 0 then
--         commit;
--     else
--         rollback;
--     end if;
--     if new_stock < 0 then
--         raise 'the number of products to buy exceeds the amount in stock';
--     end if;
-- end;
-- $$;
update products
set price = 10
where product_id = 1;
-- looking at the changes that have been written to the new table --
select *
from changer_price_product;
-- delete trigger function and table --
drop function update_product_price;
drop table changer_price_product;
drop trigger if exists update_product_price_change on shop.public.products;


-- second trigger, works when new products are added --
-- procedure for adding new products --
create or replace procedure add_product(id int, title varchar, description varchar, stock int, prod_price float,
                                        prod_slug varchar, cat_id int
)
    language plpgsql
as
$$
begin
    -- first category check --
    if cat_id < 1 then
        raise 'BAD category id';
    end if;
    -- adding new data --
    insert into products (product_id, product_title, product_description, in_stock, price, slug, category_id)
    VALUES (id, title, description, stock, prod_price,
            prod_slug, cat_id);
    -- checking new data pinning --
    if title != '' and description != '' and prod_slug != '' then
        commit;
    else
        rollback;
    end if;
end;
$$;
-- Trigger checking numbers --
create or replace function check_add_product()
    returns trigger
    language plpgsql
as
$$
begin
    if new.in_stock >= 0 and
       new.price > 0 and
       (new.category_id >= 1 or new.category_id <= 20)
    then
        return new;
    else
        return null;
    end if;
end;
$$;
-- get trigger --
create trigger trigger_add_product
    before insert
    on products
    for each row
execute procedure check_add_product();
-- test work --
select *
from products;
-- bad work -- 
call add_product(id := 4001, title := '', description := '', stock := 1, prod_price := 1, prod_slug := '',
                 cat_id := 1);
-- good work --
call add_product(id := 4001, title := 'Product 4001', description := 'Product description 4001', stock := 1, prod_price := 1, prod_slug := 'Product-4001',
                 cat_id := 1);
-- drop procedure/trigger/ func --
drop procedure add_product;
drop trigger trigger_add_product on shop.public.products;
drop function check_add_product;

