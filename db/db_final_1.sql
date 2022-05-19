-- task 1: create[db, table, add date] --
create database auto_rent;

-- address tables --
create table street
(
    street_id      int primary key unique,
    street_name    varchar(255),
    city_street_id int references city (city_id)
);

create table build
(
    build_id        int primary key unique,
    street_build_id int references street (street_id)
);

-- create phone number for customer and branch --
create table customer_phone_number
(
    number_id    int primary key unique,
    phone_number varchar(255)
);

create table branch_phone_number
(
    number_id    int primary key unique,
    phone_number varchar(255)
);

-- create address for customer and branch --

create table customer_address
(
    customer_address_id   int primary key unique,
    customer_build_id     int references build (build_id),
    phone_number_customer int references customer_phone_number (number_id)
);
create table branch_address
(
    branch_address_id   int primary key unique,
    branch_build_id     int references build (build_id),
    phone_number_branch int references branch_phone_number (number_id)
);

-- create customer and branch table --
create table customer
(
    customer_id int primary key unique,
    first_name  varchar(255),
    last_name   varchar(255),
    address     int references customer_address (customer_address_id)
);
create table branch
(
    branch_id     int primary key unique,
    branch_name   varchar(255),
    branch_number int,
    address       int references branch_address (branch_address_id)
);

-- create all table for car --
create table automaker
(
    automaker_id int unique primary key,
    car_name     varchar(255),
    count_cars   int
);
create table car_model
(
    car_model_id int primary key unique,
    car_model    varchar(255),
    automaker_id int references automaker (automaker_id)
);

create table car
(
    car_id        int unique primary key,
    car_model_id  int references car_model (car_model_id),
    car_number    varchar(255),
    price_usd     int,
    branch_car_id int references branch (branch_id)
);

create table rent
(
    rent_id        int primary key unique,
    customer_id    int references customer (customer_id),
    car_id         int references car (car_id),
    date_renting   timestamp,
    period_renting int
);


-- add date for all table --
-- return random number --
CREATE OR REPLACE FUNCTION random_between(low INT, high INT)
    RETURNS INT AS
$$
BEGIN
    RETURN floor(random() * (high - low + 1) + low);
END;
$$ language plpgsql;

-- add data in table city - №1
do
$$
    BEGIN
        for i in 1..1500
            loop
                insert into city(city_id, city_name) values (i, 'City name ' || i);
            end loop;
    end;
$$;
-- check table city
select *
from city;

-- add data in table street - №2
do
$$
    BEGIN
        for i in 1..20000
            loop
                insert into street(street_id, street_name, city_street_id)
                values (i, 'Street name ' || i, random_between(1, 1500));
            end loop;
    end;
$$;
-- check table street
select *
from street;

-- add data in table build - №3
do
$$
    BEGIN
        for i in 1..130000
            loop
                insert into build(build_id, street_build_id)
                values (i, random_between(1, 20000));
            end loop;
    end;
$$;
-- check table build
select *
from build;

-- add data in table customer phone number - №4
insert into customer_phone_number
select i, round((random() * 1000000000)::int)
from generate_series(1, 10000) as i;
-- check table customer_phone_number
select *
from customer_phone_number;

-- add data in table branch phone number - №5
insert into branch_phone_number
select i, round((random() * 1000000000)::int)
from generate_series(1, 10000) as i;
-- check table branch_phone_number
select *
from branch_phone_number;

-- add data in table customer_address - №6
do
$$
    BEGIN
        for i in 1..100000
            loop
                insert into customer_address(customer_address_id, customer_build_id, phone_number_customer)
                values (i, random_between(1, 130000), random_between(1, 10000));
            end loop;
    end;
$$;
-- check table customer_address
select *
from customer_address;

-- add data in table branch_address - №7
do
$$
    BEGIN
        for i in 1..100000
            loop
                insert into branch_address(branch_address_id, branch_build_id, phone_number_branch)
                values (i, random_between(1, 10000), random_between(1, 10000));
            end loop;
    end;
$$;
-- check table customer_address
select *
from branch_address;

-- add data in table customer - №8
insert into customer
select i, 'Customer First Name ' || i, 'Customer Last Name ' || i, random_between(1, 100000)
from generate_series(1, 20000) as i;
-- check table customer
select *
from customer;

-- add data in table branch - №9
insert into branch
select i, 'Branch name ' || i, i, random_between(1, 100000)
from generate_series(1, 10000) as i;
-- check table branch
select *
from branch;

-- add data in table automaker - №10
insert into automaker
select i, 'Car name ' || i, random_between(20, 500)
from generate_series(1, 1000) as i;
-- check table automaker
select *
from automaker;

-- add data in table car_model - №11
insert into car_model
select i, 'Model ' || i, random_between(1, 1000)
from generate_series(1, 100000) as i;
-- check table car_model
select *
from car_model;

-- add data in table car - №12
insert into car
select i,
       random_between(1, 100000),
       random_between(10000000, 100000000),
       random_between(100, 20000),
       random_between(1, 10000)
from generate_series(1, 10000) as i;
-- check table car_model
select *
from car;


-- add data in table rent - №13
insert into rent
select i,
       random_between(1, 20000),
       random_between(1, 10000),
       now(),
       random_between(1, 365)
from generate_series(1, 10000) as i;
-- check table rent
select *
from rent;

drop function random_between;