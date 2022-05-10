-- first table 'potential_customers' --
begin; -- start 0--
select *
from potential_customers;

savepoint first_checkpoint_insert_new_data; -- first task --
insert into potential_customers(potential_customers_id, email, name, surname, second_name, city)
VALUES (21, 'email@pt_c_21.com', 'name ptc 21', 'surname ptc 21', 'second name ptc 21', 'city 7020'),
       (22, 'email@pt_c_22.com', 'name ptc 22', 'surname ptc 22', 'second name ptc 22', 'city 7021'),
       (23, 'email@pt_c_3.com', 'name ptc 23', 'surname ptc 23', 'second name ptc 23', 'city 7022'),
       (24, 'email@pt_c_4.com', 'name ptc 24', 'surname ptc 24', 'second name ptc 24', 'city 7023');
select *
from potential_customers;
rollback to savepoint first_checkpoint_insert_new_data; -- return default date --
commit; -- save new date --

savepoint second_checkpoint_update_date; -- second task --
update potential_customers
set name = 'Changer Name'
where potential_customers_id in (1, 2, 3, 4, 5, 6);
select *
from potential_customers;
rollback to savepoint second_checkpoint_update_date; -- return default date --
commit; -- save new date --

savepoint third_checkpoint_update_date; -- third task --
delete
from potential_customers
where potential_customers_id in (1, 2, 3, 4, 5, 6);
select *
from potential_customers;
rollback to savepoint third_checkpoint_update_date; -- return default date --
commit;
-- save new date --

-- all command --
savepoint default_check; -- first task --
insert into potential_customers(potential_customers_id, email, name, surname, second_name, city)
VALUES (21, 'email@pt_c_21.com', 'name ptc 21', 'surname ptc 21', 'second name ptc 21', 'city 7020'),
       (22, 'email@pt_c_22.com', 'name ptc 22', 'surname ptc 22', 'second name ptc 22', 'city 7021'),
       (23, 'email@pt_c_3.com', 'name ptc 23', 'surname ptc 23', 'second name ptc 23', 'city 7022'),
       (24, 'email@pt_c_4.com', 'name ptc 24', 'surname ptc 24', 'second name ptc 24', 'city 7023');

select *
from potential_customers;

savepoint first_step;

update potential_customers
set name = 'Student'
where potential_customers_id in (21, 22, 23, 24);

select *
from potential_customers;
rollback to savepoint first_step;

savepoint second_step;
delete
from potential_customers
where potential_customers_id in (1, 2, 3, 4, 5, 6);

rollback to savepoint first_step;

select *
from potential_customers;

rollback to savepoint default_check;

select *
from potential_customers;
end;
-- end--

-- end work first table --

-- second table 'orders' --
begin; -- start --
select *
from orders;

savepoint first_checkpoint_insert_new_data; -- first task --
insert into orders(order_id, carts_cart_id, order_status_id, shipping_total, total, created_at, updated_at)
VALUES (12311, 94, 4, 50, 56465.468, '2012-01-07 00:00:00.00', '2013-10-07 00:00:00.00'),
       (1501, 2000, 5, 70, 4654.654, '2013-10-07 00:00:00.00', '2014-10-07 00:00:00.00'),
       (2000, 101, 1, 80, 5465.54, '2044-03-07 00:00:00.00', '2045-10-07 00:00:00.00'),
       (1502, 1600, 3, 1, 1.66, '2022-11-07 00:00:00.00', '2023-10-07 00:00:00.00');
rollback to savepoint first_checkpoint_insert_new_data; -- return default date --
commit; -- save new date --

savepoint second_checkpoint_update_date; -- second task --
update orders
set order_status_id = 5
where order_status_id != 5;
-- or --
update orders
set order_status_id = 5
where created_at between '2020-02-28 00:00:00.00' and now();
rollback to savepoint second_checkpoint_update_date; -- return default date --
commit; -- save new date --

savepoint third_checkpoint_update_date; -- third task --
delete
from orders
where order_status_id = 5;
rollback to savepoint third_checkpoint_update_date; -- return default date --
commit;
-- save new date --

-- all command --
savepoint default_check; -- first task --
insert into orders(order_id, carts_cart_id, order_status_id, shipping_total, total, created_at, updated_at)
VALUES (12311, 94, 4, 50, 56465.468, '2012-01-07 00:00:00.00', '2013-10-07 00:00:00.00'),
       (1501, 2000, 5, 70, 4654.654, '2013-10-07 00:00:00.00', '2014-10-07 00:00:00.00'),
       (2000, 101, 1, 80, 5465.54, '2044-03-07 00:00:00.00', '2045-10-07 00:00:00.00'),
       (1502, 1600, 3, 1, 1.66, '2022-11-07 00:00:00.00', '2023-10-07 00:00:00.00');

select *
from orders;

savepoint first_step;

update orders
set order_status_id = 5
where order_status_id != 5;
-- or --
update orders
set order_status_id = 5
where created_at between '2020-02-28 00:00:00.00' and now();
rollback to savepoint second_checkpoint_update_date; -- return default date --

select *
from orders;
rollback to savepoint first_step;

savepoint second_step;

delete
from orders
where order_status_id = 5;

rollback to savepoint first_step;

select *
from potential_customers;

rollback to savepoint default_check;

select *
from potential_customers;


end; -- end--
-- end work second table --

-- third table 'products' --
begin; -- start --
select *
from products;

savepoint first_checkpoint_insert_new_data; -- first task --

insert into products(product_id, product_title, product_description, in_stock, price, slug, category_id)
VALUES (4001, 'Product 4001', 'Product description 4001', 50, 56465.468, 'Product-4001', 1),
       (4002, 'Product 4002', 'Product description 4002', 70, 4654.654, 'Product-4002', 5),
       (4003, 'Product 4003', 'Product description 4003', 80, 5465.54, 'Product-4003', 10),
       (4004, 'Product 4004', 'Product description 4004', 1, 1.66, 'Product-4004', 20);
select *
from products;
rollback to savepoint first_checkpoint_insert_new_data; -- return default date --
commit; -- save new date --

savepoint second_checkpoint_update_date; -- second task --
update products
set product_title = 'new product', slug = 'new product'
where product_id in (4000, 3999, 3998, 3997);
select *
from products;
rollback to savepoint second_checkpoint_update_date; -- return default date --
commit; -- save new date --

savepoint third_checkpoint_update_date; -- third task --
delete
from products
where product_id % 5 = 0;
select *
from products;
rollback to savepoint third_checkpoint_update_date; -- return default date --
commit;

-- all command --
savepoint default_check; -- first task --
insert into products(product_id, product_title, product_description, in_stock, price, slug, category_id)
VALUES (4001, 'Product 4001', 'Product description 4001', 50, 56465.468, 'Product-4001', 1),
       (4002, 'Product 4002', 'Product description 4002', 70, 4654.654, 'Product-4002', 5),
       (4003, 'Product 4003', 'Product description 4003', 80, 5465.54, 'Product-4003', 10),
       (4004, 'Product 4004', 'Product description 4004', 1, 1.66, 'Product-4004', 20);

select *
from products;
savepoint first_step;

update products
set product_title = 'new product', slug = 'new product'
where product_id in (4001, 4002, 4003, 4004);

select *
from products;
rollback to savepoint first_step;

savepoint second_step;
delete
from products
where product_id in (4001, 4002, 4003, 4004);

rollback to savepoint first_step;

select *
from products;

rollback to savepoint default_check;

end; -- end --
-- end work third table --