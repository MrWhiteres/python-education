explain(analyse ,buffers)
select products.product_title, count(cart_product.products_product_id) as add_to_cart
from cart_product
         left join products on products.product_id = cart_product.products_product_id
         left join orders on orders.carts_cart_id = cart_product.carts_cart_id
where products.product_id = products_product_id
group by products_product_id, products.product_title
having count(products_product_id) > 0
order by count(products_product_id) desc;
-- index no, default --
-- Sort  (cost=990.15..999.31 rows=3665 width=24) (actual time=10.019..10.184 rows=3742 loops=1)
--   Sort Key: (count(cart_product.products_product_id)) DESC
--   Sort Method: quicksort  Memory: 389kB
--   Buffers: shared hit=167
--   ->  HashAggregate  (cost=635.75..773.19 rows=3665 width=24) (actual time=8.914..9.509 rows=3742 loops=1)
-- "        Group Key: cart_product.products_product_id, products.product_title"
--         Filter: (count(cart_product.products_product_id) > 0)
--         Batches: 1  Memory Usage: 913kB
--         Buffers: shared hit=167
--         ->  Hash Left Join  (cost=241.75..553.29 rows=10995 width=16) (actual time=1.209..6.373 rows=10995 loops=1)
--               Hash Cond: (cart_product.carts_cart_id = orders.carts_cart_id)
--               Buffers: shared hit=167
--               ->  Hash Join  (cost=195.00..382.85 rows=10995 width=20) (actual time=0.915..4.018 rows=10995 loops=1)
--                     Hash Cond: (cart_product.products_product_id = products.product_id)
--                     Buffers: shared hit=154
--                     ->  Seq Scan on cart_product  (cost=0.00..158.95 rows=10995 width=8) (actual time=0.004..0.674 rows=10995 loops=1)
--                           Buffers: shared hit=49
--                     ->  Hash  (cost=145.00..145.00 rows=4000 width=16) (actual time=0.904..0.904 rows=4000 loops=1)
--                           Buckets: 4096  Batches: 1  Memory Usage: 232kB
--                           Buffers: shared hit=105
--                           ->  Seq Scan on products  (cost=0.00..145.00 rows=4000 width=16) (actual time=0.022..0.424 rows=4000 loops=1)
--                                 Buffers: shared hit=105
--               ->  Hash  (cost=28.00..28.00 rows=1500 width=4) (actual time=0.289..0.290 rows=1500 loops=1)
--                     Buckets: 2048  Batches: 1  Memory Usage: 69kB
--                     Buffers: shared hit=13
--                     ->  Seq Scan on orders  (cost=0.00..28.00 rows=1500 width=4) (actual time=0.004..0.121 rows=1500 loops=1)
--                           Buffers: shared hit=13
-- Planning:
--   Buffers: shared hit=32
-- Planning Time: 0.236 ms
-- Execution Time: 10.479 ms

-- add index --
create index on cart_product(carts_cart_id, products_product_id);
create index on products(product_id);
create index on orders(carts_cart_id);
-- Sort  (cost=990.15..999.31 rows=3665 width=24) (actual time=11.981..12.179 rows=3742 loops=1)
--   Sort Key: (count(cart_product.products_product_id)) DESC
--   Sort Method: quicksort  Memory: 389kB
--   Buffers: shared hit=167
--   ->  HashAggregate  (cost=635.75..773.19 rows=3665 width=24) (actual time=10.626..11.400 rows=3742 loops=1)
-- "        Group Key: cart_product.products_product_id, products.product_title"
--         Filter: (count(cart_product.products_product_id) > 0)
--         Batches: 1  Memory Usage: 913kB
--         Buffers: shared hit=167
--         ->  Hash Left Join  (cost=241.75..553.29 rows=10995 width=16) (actual time=1.362..7.587 rows=10995 loops=1)
--               Hash Cond: (cart_product.carts_cart_id = orders.carts_cart_id)
--               Buffers: shared hit=167
--               ->  Hash Join  (cost=195.00..382.85 rows=10995 width=20) (actual time=1.082..4.893 rows=10995 loops=1)
--                     Hash Cond: (cart_product.products_product_id = products.product_id)
--                     Buffers: shared hit=154
--                     ->  Seq Scan on cart_product  (cost=0.00..158.95 rows=10995 width=8) (actual time=0.006..0.902 rows=10995 loops=1)
--                           Buffers: shared hit=49
--                     ->  Hash  (cost=145.00..145.00 rows=4000 width=16) (actual time=1.068..1.069 rows=4000 loops=1)
--                           Buckets: 4096  Batches: 1  Memory Usage: 232kB
--                           Buffers: shared hit=105
--                           ->  Seq Scan on products  (cost=0.00..145.00 rows=4000 width=16) (actual time=0.025..0.417 rows=4000 loops=1)
--                                 Buffers: shared hit=105
--               ->  Hash  (cost=28.00..28.00 rows=1500 width=4) (actual time=0.275..0.275 rows=1500 loops=1)
--                     Buckets: 2048  Batches: 1  Memory Usage: 69kB
--                     Buffers: shared hit=13
--                     ->  Seq Scan on orders  (cost=0.00..28.00 rows=1500 width=4) (actual time=0.005..0.114 rows=1500 loops=1)
--                           Buffers: shared hit=13
-- Planning:
--   Buffers: shared hit=66 read=11
-- Planning Time: 0.971 ms
-- Execution Time: 12.500 ms

-- drop index --
drop index cart_product_carts_cart_id_products_product_id_idx;
drop index products_product_id_idx;
drop index orders_carts_cart_id_idx;

set work_mem to '1MB';
-- no index and work in 1 mb --
-- Sort  (cost=1755.65..1764.81 rows=3665 width=24) (actual time=16.320..16.555 rows=3742 loops=1)
--   Sort Key: (count(cart_product.products_product_id)) DESC
--   Sort Method: quicksort  Memory: 389kB
-- "  Buffers: shared hit=167, temp read=40 written=40"
--   ->  GroupAggregate  (cost=1291.30..1538.69 rows=3665 width=24) (actual time=11.790..15.693 rows=3742 loops=1)
-- "        Group Key: cart_product.products_product_id, products.product_title"
--         Filter: (count(cart_product.products_product_id) > 0)
-- "        Buffers: shared hit=167, temp read=40 written=40"
--         ->  Sort  (cost=1291.30..1318.79 rows=10995 width=16) (actual time=11.779..13.070 rows=10995 loops=1)
-- "              Sort Key: cart_product.products_product_id, products.product_title"
--               Sort Method: external merge  Disk: 320kB
-- "              Buffers: shared hit=167, temp read=40 written=40"
--               ->  Hash Left Join  (cost=241.75..553.29 rows=10995 width=16) (actual time=1.497..7.281 rows=10995 loops=1)
--                     Hash Cond: (cart_product.carts_cart_id = orders.carts_cart_id)
--                     Buffers: shared hit=167
--                     ->  Hash Join  (cost=195.00..382.85 rows=10995 width=20) (actual time=1.209..4.804 rows=10995 loops=1)
--                           Hash Cond: (cart_product.products_product_id = products.product_id)
--                           Buffers: shared hit=154
--                           ->  Seq Scan on cart_product  (cost=0.00..158.95 rows=10995 width=8) (actual time=0.005..0.823 rows=10995 loops=1)
--                                 Buffers: shared hit=49
--                           ->  Hash  (cost=145.00..145.00 rows=4000 width=16) (actual time=1.196..1.197 rows=4000 loops=1)
--                                 Buckets: 4096  Batches: 1  Memory Usage: 232kB
--                                 Buffers: shared hit=105
--                                 ->  Seq Scan on products  (cost=0.00..145.00 rows=4000 width=16) (actual time=0.024..0.678 rows=4000 loops=1)
--                                       Buffers: shared hit=105
--                     ->  Hash  (cost=28.00..28.00 rows=1500 width=4) (actual time=0.279..0.280 rows=1500 loops=1)
--                           Buckets: 2048  Batches: 1  Memory Usage: 69kB
--                           Buffers: shared hit=13
--                           ->  Seq Scan on orders  (cost=0.00..28.00 rows=1500 width=4) (actual time=0.010..0.121 rows=1500 loops=1)
--                                 Buffers: shared hit=13
-- Planning:
--   Buffers: shared hit=32
-- Planning Time: 0.338 ms
-- Execution Time: 17.160 ms

-- index on and work in 1 mb --
-- Sort  (cost=1755.65..1764.81 rows=3665 width=24) (actual time=15.018..15.169 rows=3742 loops=1)
--   Sort Key: (count(cart_product.products_product_id)) DESC
--   Sort Method: quicksort  Memory: 389kB
-- "  Buffers: shared hit=167, temp read=40 written=40"
--   ->  GroupAggregate  (cost=1291.30..1538.69 rows=3665 width=24) (actual time=10.834..14.430 rows=3742 loops=1)
-- "        Group Key: cart_product.products_product_id, products.product_title"
--         Filter: (count(cart_product.products_product_id) > 0)
-- "        Buffers: shared hit=167, temp read=40 written=40"
--         ->  Sort  (cost=1291.30..1318.79 rows=10995 width=16) (actual time=10.825..11.925 rows=10995 loops=1)
-- "              Sort Key: cart_product.products_product_id, products.product_title"
--               Sort Method: external merge  Disk: 320kB
-- "              Buffers: shared hit=167, temp read=40 written=40"
--               ->  Hash Left Join  (cost=241.75..553.29 rows=10995 width=16) (actual time=1.397..6.467 rows=10995 loops=1)
--                     Hash Cond: (cart_product.carts_cart_id = orders.carts_cart_id)
--                     Buffers: shared hit=167
--                     ->  Hash Join  (cost=195.00..382.85 rows=10995 width=20) (actual time=1.062..4.114 rows=10995 loops=1)
--                           Hash Cond: (cart_product.products_product_id = products.product_id)
--                           Buffers: shared hit=154
--                           ->  Seq Scan on cart_product  (cost=0.00..158.95 rows=10995 width=8) (actual time=0.006..0.693 rows=10995 loops=1)
--                                 Buffers: shared hit=49
--                           ->  Hash  (cost=145.00..145.00 rows=4000 width=16) (actual time=1.049..1.050 rows=4000 loops=1)
--                                 Buckets: 4096  Batches: 1  Memory Usage: 232kB
--                                 Buffers: shared hit=105
--                                 ->  Seq Scan on products  (cost=0.00..145.00 rows=4000 width=16) (actual time=0.027..0.482 rows=4000 loops=1)
--                                       Buffers: shared hit=105
--                     ->  Hash  (cost=28.00..28.00 rows=1500 width=4) (actual time=0.329..0.329 rows=1500 loops=1)
--                           Buckets: 2048  Batches: 1  Memory Usage: 69kB
--                           Buffers: shared hit=13
--                           ->  Seq Scan on orders  (cost=0.00..28.00 rows=1500 width=4) (actual time=0.005..0.116 rows=1500 loops=1)
--                                 Buffers: shared hit=13
-- Planning:
--   Buffers: shared hit=66 read=11
-- Planning Time: 1.069 ms
-- Execution Time: 15.566 ms

set work_mem to '100MB';
-- no index and work in 100 mb --
-- Sort  (cost=990.15..999.31 rows=3665 width=24) (actual time=11.122..11.322 rows=3742 loops=1)
--   Sort Key: (count(cart_product.products_product_id)) DESC
--   Sort Method: quicksort  Memory: 389kB
--   Buffers: shared hit=167
--   ->  HashAggregate  (cost=635.75..773.19 rows=3665 width=24) (actual time=9.969..10.629 rows=3742 loops=1)
-- "        Group Key: cart_product.products_product_id, products.product_title"
--         Filter: (count(cart_product.products_product_id) > 0)
--         Batches: 1  Memory Usage: 913kB
--         Buffers: shared hit=167
--         ->  Hash Left Join  (cost=241.75..553.29 rows=10995 width=16) (actual time=1.236..6.998 rows=10995 loops=1)
--               Hash Cond: (cart_product.carts_cart_id = orders.carts_cart_id)
--               Buffers: shared hit=167
--               ->  Hash Join  (cost=195.00..382.85 rows=10995 width=20) (actual time=0.962..4.531 rows=10995 loops=1)
--                     Hash Cond: (cart_product.products_product_id = products.product_id)
--                     Buffers: shared hit=154
--                     ->  Seq Scan on cart_product  (cost=0.00..158.95 rows=10995 width=8) (actual time=0.005..0.736 rows=10995 loops=1)
--                           Buffers: shared hit=49
--                     ->  Hash  (cost=145.00..145.00 rows=4000 width=16) (actual time=0.951..0.952 rows=4000 loops=1)
--                           Buckets: 4096  Batches: 1  Memory Usage: 232kB
--                           Buffers: shared hit=105
--                           ->  Seq Scan on products  (cost=0.00..145.00 rows=4000 width=16) (actual time=0.021..0.421 rows=4000 loops=1)
--                                 Buffers: shared hit=105
--               ->  Hash  (cost=28.00..28.00 rows=1500 width=4) (actual time=0.270..0.271 rows=1500 loops=1)
--                     Buckets: 2048  Batches: 1  Memory Usage: 69kB
--                     Buffers: shared hit=13
--                     ->  Seq Scan on orders  (cost=0.00..28.00 rows=1500 width=4) (actual time=0.003..0.112 rows=1500 loops=1)
--                           Buffers: shared hit=13
-- Planning:
--   Buffers: shared hit=38
-- Planning Time: 0.267 ms
-- Execution Time: 11.636 ms

-- index on and work in 100 mb --
-- Sort  (cost=990.15..999.31 rows=3665 width=24) (actual time=10.019..10.197 rows=3742 loops=1)
--   Sort Key: (count(cart_product.products_product_id)) DESC
--   Sort Method: quicksort  Memory: 389kB
--   Buffers: shared hit=167
--   ->  HashAggregate  (cost=635.75..773.19 rows=3665 width=24) (actual time=8.907..9.508 rows=3742 loops=1)
-- "        Group Key: cart_product.products_product_id, products.product_title"
--         Filter: (count(cart_product.products_product_id) > 0)
--         Batches: 1  Memory Usage: 913kB
--         Buffers: shared hit=167
--         ->  Hash Left Join  (cost=241.75..553.29 rows=10995 width=16) (actual time=1.227..6.344 rows=10995 loops=1)
--               Hash Cond: (cart_product.carts_cart_id = orders.carts_cart_id)
--               Buffers: shared hit=167
--               ->  Hash Join  (cost=195.00..382.85 rows=10995 width=20) (actual time=0.945..4.069 rows=10995 loops=1)
--                     Hash Cond: (cart_product.products_product_id = products.product_id)
--                     Buffers: shared hit=154
--                     ->  Seq Scan on cart_product  (cost=0.00..158.95 rows=10995 width=8) (actual time=0.006..0.730 rows=10995 loops=1)
--                           Buffers: shared hit=49
--                     ->  Hash  (cost=145.00..145.00 rows=4000 width=16) (actual time=0.928..0.929 rows=4000 loops=1)
--                           Buckets: 4096  Batches: 1  Memory Usage: 232kB
--                           Buffers: shared hit=105
--                           ->  Seq Scan on products  (cost=0.00..145.00 rows=4000 width=16) (actual time=0.036..0.451 rows=4000 loops=1)
--                                 Buffers: shared hit=105
--               ->  Hash  (cost=28.00..28.00 rows=1500 width=4) (actual time=0.276..0.277 rows=1500 loops=1)
--                     Buckets: 2048  Batches: 1  Memory Usage: 69kB
--                     Buffers: shared hit=13
--                     ->  Seq Scan on orders  (cost=0.00..28.00 rows=1500 width=4) (actual time=0.005..0.116 rows=1500 loops=1)
--                           Buffers: shared hit=13
-- Planning:
--   Buffers: shared hit=67 read=11
-- Planning Time: 1.536 ms
-- Execution Time: 10.504 ms