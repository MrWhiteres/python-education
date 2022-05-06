CREATE DATABASE shop;

CREATE TABLE users
(
    user_id     int unique,
    email       varchar(255),
    password    varchar(255),
    first_name  varchar(255),
    last_name   varchar(255),
    middle_name varchar(255),
    is_staff    int,
    country     varchar(255),
    city        varchar(255),
    address     text
);


COPY users FROM '/usr/src/users.csv' WITH (FORMAT csv);


CREATE TABLE carts
(
    card_id       int unique,
    Users_user_id int references users (user_id),
    subtotal      decimal,
    total         decimal,
    timestamp     timestamp(2)
);

COPY carts FROM '/usr/src/carts.csv' WITH (FORMAT csv);


CREATE TABLE categories
(
    category_id          int unique,
    category_title       varchar(255),
    category_description text
);

COPY categories FROM '/usr/src/categories.csv' WITH (FORMAT csv);

create table products
(
    product_id          int unique,
    product_title       varchar(255),
    product_description text,
    in_stock            int,
    price               float,
    slug                varchar(45),
    category_id         int references categories (category_id)
);

COPY products FROM '/usr/src/products.csv' WITH (FORMAT csv);

create table cart_product
(
    carts_cart_id       int references carts (card_id),
    products_product_id int references products (product_id)
);

copy cart_product from '/usr/src/cart_products.csv' WITH (FORMAT csv);

create table order_statuses
(
    order_status_id int unique,
    status_name     varchar(255)
);

copy order_statuses from '/usr/src/order_statuses.csv' WITH (FORMAT csv);

create table orders
(
    order_id        int unique,
    carts_cart_id   int references carts (card_id),
    order_status_id int references order_statuses (order_status_id),
    shipping_total  decimal,
    total           decimal,
    created_at      timestamp(2),
    updated_at      timestamp(2)
);

copy orders from '/usr/src/orders.csv' WITH (FORMAT csv);


alter table users
    add column phone_number int;

alter table users
    alter column phone_number type varchar;

update products
set price = price * 2;