-- task 2
-- select returns all data about users who live in cities numbered 1 10 20 40
select first_name, last_name, address, city.city_name, street_name, build_id
from customer
         left join customer_address on customer.address = customer_address.customer_address_id
         left join build on customer_address.customer_build_id = build.build_id
         left join street on build.street_build_id = street.street_id
         left join city on street.city_street_id = city.city_id
where city.city_id in (1, 10, 20, 40)
;

-- select returns the average number of days for which cars are happy and the average cost of cars
select round(avg(rent.period_renting)::numeric, 2) as average_days_penting,
       round(avg(car.price_usd)::numeric, 2)       as average_price_usd
from rent
         join car on rent.car_id = car.car_id;

-- select return only 10 users who spent the most money on car rental
select customer.customer_id, first_name, last_name, (rent.period_renting * car.price_usd) as total
from customer
         join rent on customer.customer_id = rent.customer_id
         left join car on car.car_id = rent.car_id
where rent.customer_id = customer.customer_id
order by (rent.period_renting * car.price_usd) desc
limit 10;


-- work in optimization
explain (analyse,buffers)
select car.car_number, car_model.car_model_id, car_model.car_model, car.price_usd
from car
         join car_model on car.car_model_id = car_model.car_model_id
         join automaker on car_model.automaker_id = automaker.automaker_id
where price_usd > 10000
  and car.branch_car_id < 1000
order by price_usd
limit 100;
-- Limit  (cost=2547.75..2548.00 rows=100 width=28) (actual time=16.290..16.307 rows=100 loops=1)
--   Buffers: shared hit=718
--   ->  Sort  (cost=2547.75..2549.03 rows=509 width=28) (actual time=16.288..16.300 rows=100 loops=1)
--         Sort Key: car.price_usd
--         Sort Method: top-N heapsort  Memory: 38kB
--         Buffers: shared hit=718
--         ->  Hash Join  (cost=259.86..2528.30 rows=509 width=28) (actual time=1.434..16.082 rows=507 loops=1)
--               Hash Cond: (car_model.automaker_id = automaker.automaker_id)
--               Buffers: shared hit=718
--               ->  Hash Join  (cost=230.36..2497.45 rows=509 width=32) (actual time=1.190..15.681 rows=507 loops=1)
--                     Hash Cond: (car_model.car_model_id = car.car_model_id)
--                     Buffers: shared hit=711
--                     ->  Seq Scan on car_model  (cost=0.00..1637.00 rows=100000 width=19) (actual time=0.007..5.559 rows=100000 loops=1)
--                           Buffers: shared hit=637
--                     ->  Hash  (cost=224.00..224.00 rows=509 width=17) (actual time=1.164..1.165 rows=507 loops=1)
--                           Buckets: 1024  Batches: 1  Memory Usage: 34kB
--                           Buffers: shared hit=74
--                           ->  Seq Scan on car  (cost=0.00..224.00 rows=509 width=17) (actual time=0.100..1.093 rows=507 loops=1)
--                                 Filter: ((price_usd > 10000) AND (branch_car_id < 1000))
--                                 Rows Removed by Filter: 9493
--                                 Buffers: shared hit=74
--               ->  Hash  (cost=17.00..17.00 rows=1000 width=4) (actual time=0.238..0.239 rows=1000 loops=1)
--                     Buckets: 1024  Batches: 1  Memory Usage: 44kB
--                     Buffers: shared hit=7
--                     ->  Seq Scan on automaker  (cost=0.00..17.00 rows=1000 width=4) (actual time=0.007..0.109 rows=1000 loops=1)
--                           Buffers: shared hit=7
-- Planning:
--   Buffers: shared hit=18
-- Planning Time: 0.393 ms
-- Execution Time: 16.338 ms


create index on car (car_id);
create index on car_model (car_model_id, automaker_id);
create index on automaker (automaker_id);
create index on car (price_usd);
create index on branch (branch_id);
drop index car_price_usd_idx;
drop index car_model_car_model_id_automaker_id_idx;
drop index car_car_id_idx;
drop index automaker_automaker_id_idx;
drop index branch_branch_id_idx;

-- Limit  (cost=0.85..644.10 rows=100 width=28) (actual time=0.026..1.119 rows=100 loops=1)
--   Buffers: shared hit=1387 read=90
--   ->  Nested Loop  (cost=0.85..3275.00 rows=509 width=28) (actual time=0.025..1.109 rows=100 loops=1)
--         Buffers: shared hit=1387 read=90
--         ->  Nested Loop  (cost=0.58..3125.89 rows=509 width=32) (actual time=0.019..0.948 rows=100 loops=1)
--               Buffers: shared hit=1088 read=89
--               ->  Index Scan using car_price_usd_idx on car  (cost=0.29..452.10 rows=509 width=17) (actual time=0.013..0.450 rows=100 loops=1)
--                     Index Cond: (price_usd > 10000)
--                     Filter: (branch_car_id < 1000)
--                     Rows Removed by Filter: 788
--                     Buffers: shared hit=872 read=5
--               ->  Index Scan using car_model_car_model_id_automaker_id_idx on car_model  (cost=0.29..5.25 rows=1 width=19) (actual time=0.005..0.005 rows=1 loops=100)
--                     Index Cond: (car_model_id = car.car_model_id)
--                     Buffers: shared hit=216 read=84
--         ->  Index Only Scan using automaker_automaker_id_idx on automaker  (cost=0.28..0.29 rows=1 width=4) (actual time=0.001..0.001 rows=1 loops=100)
--               Index Cond: (automaker_id = car_model.automaker_id)
--               Heap Fetches: 100
--               Buffers: shared hit=299 read=1
-- Planning:
--   Buffers: shared hit=80 read=10
-- Planning Time: 0.790 ms
-- Execution Time: 1.146 ms
