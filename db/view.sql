-- create view products --
create view products_view as
select product_id, product_title, category_id
from products;
-- test select in view --
select *
from products_view
where category_id % 2 = 0
  and product_id % 2 = 0
order by product_title desc;
-- drop view --
drop view if exists products_view;

-- create view order_status and order --
create view order_stat as
select order_id, carts_cart_id, total, order_statuses.status_name
from orders
         left join order_statuses on orders.order_status_id = order_statuses.order_status_id
where orders.order_status_id = order_statuses.order_status_id;
-- test select in view --
select *
from order_stat
where status_name in ('Finished', 'Canceled')
order by total desc;
-- drop view --
drop view if exists order_stat;

-- create view products and category --
create view category_products as
select product_id, product_title, in_stock, price, category_title
from products
         left join categories on categories.category_id = products.category_id
where products.category_id = categories.category_id;
-- test select in view --
select product_title, price, category_title
from category_products
where in_stock > 40
  and price > 100
order by product_title desc;
-- drop view --
drop view if exists category_products;


-- create custom materialized view --
create materialized view customers as
select user_id, first_name, last_name, orders.order_id, count(user_id) as count_orders
from users
         left join carts on users.user_id = carts.users_user_id
         left join cart_product on carts.card_id = cart_product.carts_cart_id
         left join orders on carts.card_id = orders.carts_cart_id
where users_user_id is not null
  and orders.order_id is not null
  and carts.card_id is not null
group by user_id, first_name, last_name, users_user_id, orders.order_id
order by count_orders desc;

select *
from customers;
-- drop view --
drop materialized view customers;