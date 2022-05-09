-- task 1 --
-- create new table --
create table potential_customers
(
    potential_customers_id int unique,
    email                  varchar(255),
    name                   varchar(255),
    surname                varchar(255),
    second_name            varchar(255),
    city                   varchar(255)
);

-- insert new date --
INSERT INTO potential_customers(potential_customers_id, email, name, surname, second_name, city)
VALUES (1, 'email@pt_c_1.com', 'name ptc 1', 'surname ptc 1', 'second name ptc 1', 'city 7000'),
       (2, 'email@pt_c_2.com', 'name ptc 2', 'surname ptc 2', 'second name ptc 2', 'city 7001'),
       (3, 'email@pt_c_3.com', 'name ptc 3', 'surname ptc 3', 'second name ptc 3', 'city 7002'),
       (4, 'email@pt_c_4.com', 'name ptc 4', 'surname ptc 4', 'second name ptc 4', 'city 7003'),
       (5, 'email@pt_c_5.com', 'name ptc 5', 'surname ptc 5', 'second name ptc 5', 'city 7004'),
       (6, 'email@pt_c_6.com', 'name ptc 6', 'surname ptc 6', 'second name ptc 6', 'city 7005'),
       (7, 'email@pt_c_7.com', 'name ptc 7', 'surname ptc 7', 'second name ptc 7', 'city 7006'),
       (8, 'email@pt_c_8.com', 'name ptc 8', 'surname ptc 8', 'second name ptc 8', 'city 7007'),
       (9, 'email@pt_c_9.com', 'name ptc 9', 'surname ptc 9', 'second name ptc 9', 'city 7008'),
       (10, 'email@pt_c_10.com', 'name ptc 10', 'surname ptc 10', 'second name ptc 10', 'city 7009'),
       (11, 'email@pt_c_11.com', 'name ptc 11', 'surname ptc 11', 'second name ptc 11', 'city 7010'),
       (12, 'email@pt_c_12.com', 'name ptc 12', 'surname ptc 12', 'second name ptc 12', 'city 7011'),
       (13, 'email@pt_c_13.com', 'name ptc 13', 'surname ptc 13', 'second name ptc 13', 'city 7012'),
       (14, 'email@pt_c_14.com', 'name ptc 14', 'surname ptc 14', 'second name ptc 14', 'city 7013'),
       (15, 'email@pt_c_15.com', 'name ptc 15', 'surname ptc 15', 'second name ptc 15', 'city 7014'),
       (16, 'email@pt_c_16.com', 'name ptc 16', 'surname ptc 16', 'second name ptc 16', 'city 7015'),
       (17, 'email@pt_c_17.com', 'name ptc 17', 'surname ptc 17', 'second name ptc 17', 'city 7016'),
       (18, 'email@pt_c_18.com', 'name ptc 18', 'surname ptc 18', 'second name ptc 18', 'city 7017'),
       (19, 'email@pt_c_19.com', 'name ptc 19', 'surname ptc 19', 'second name ptc 19', 'city 7018'),
       (20, 'email@pt_c_20.com', 'name ptc 20', 'surname ptc 20', 'second name ptc 20', 'city 7019');
-- output all name and email in potential_customers and users in city 17 --
select potential_customers.name,
       potential_customers.email,
       users.first_name,
       users.last_name,
       users.middle_name,
       users.phone_number
from users,
     potential_customers
where users.city = 'city 17';
-- task 2 --
-- output all users sorted alphabetically and by city --
select first_name, last_name, middle_name, city
from users
order by city asc, first_name asc;
-- task 3 --
-- output all category names sorted by number of products --
select categories.category_title
from categories,
     products
where categories.category_id = products.category_id
group by categories.category_title, products.category_id
order by count(products.in_stock) desc;
-- task 4 --
-- task 4.1 --
-- output products that have never been added to the cart --
select *
from products
where not exists(select *
                 from cart_product
                 where cart_product.products_product_id = products.product_id
    );
-- task 4.2 --
-- output all products that did not fall into any 1 order. (but could get into the basket) --
select products.product_title, products.price
from products
         left join cart_product on product_id = products_product_id
where products_product_id is NULL;
-- task 4.3 --
-- top 10 product add to cart --
select products.product_title, count(cart_product.products_product_id) as add_to_cart
from cart_product,
     products
where products.product_id = products_product_id
group by products_product_id, products.product_title
having count(products_product_id) > 0
order by count(products_product_id) desc
limit 10;
-- task 4.4 --
-- top 10 product add to cart and order--
select products.product_title, count(cart_product.products_product_id) as add_to_cart
from cart_product,
     products
         left join orders on orders.carts_cart_id = carts_cart_id
where products.product_id = products_product_id
group by products_product_id, products.product_title
having count(products_product_id) > 0
order by count(products_product_id) desc
limit 10;
-- task 4.5 --
-- top 5 users who spent the most money --
select users.first_name, users.last_name, carts.total as total_spent
from carts,
     users
where users.user_id = carts.users_user_id
group by users.first_name, users.last_name, carts.total
order by carts.total desc
limit 5;
-- task 4.6 --
-- top 5 users who made the most orders (number of orders) --
select users.first_name, users.last_name, count(carts.users_user_id) as total_orders
from carts,
     users
where users.user_id = carts.users_user_id
group by users.first_name, users.last_name, carts.users_user_id
limit 5;
-- task 4.7 --
-- top 5 users who created carts but never placed orders --
select users.first_name
from carts
         left join orders on card_id = orders.carts_cart_id
         inner join users on carts.users_user_id = users.user_id
where orders.carts_cart_id is null
  and users.user_id = carts.users_user_id
group by users.first_name
order by count(carts.card_id) desc
limit 5;









