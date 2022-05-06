-- task 1 --
-- output all user --
select user_id, first_name, last_name, middle_name
from users;
-- output all products --
select product_id, product_title, price
from products;
-- output all status product --
select order_id, orders.order_status_id, status_name
from orders,
     order_statuses;

-- task 2 --
-- output all finished order --
select *
from orders
where order_status_id = 4;

-- task 3 --
-- output all product if price product in 80 < price <= 150.00 --
select *
from products
where 80.00 < price
  and price <= 150.00;
-- output all orders that were made after  '01.10.2020' --
select *
from orders
where created_at > '2020-10-01'::timestamp;
-- or --
select *
from orders
where created_at between '2020-10-02' ::timestamp and now()::timestamp;
-- output all orders made in the first half of '2020' --
select *
from orders
where created_at >= '2020-01-01'::timestamp
  and created_at < '2020-07-01'::timestamp;
-- output all products if products category in (Category 7, Category 11, Category 18) --
select *
from products
where category_id in (7, 11, 18);
-- output all orders that are not completed before '12/31/2020' --
select *
from orders
where order_status_id NOT IN (4, 5)
  and updated_at <= '2020-12-31'::timestamp;
-- or --
select *
from orders
where order_status_id IN (1, 2, 3)
  and updated_at <= '2020-12-31'::timestamp;
-- output all not completed orders ? --
select *
from orders
where order_status_id = 2;

-- task 4 --
-- average sum of all completed orders --
select avg(total)
from orders
where order_status_id in (4, 5);
-- the maximum transaction amount for the 3rd quarter of 2020 --
select max(total)
from orders
where updated_at >= '2020-7-01'::timestamp
  and updated_at < '2020-10-1'::timestamp;