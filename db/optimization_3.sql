explain(analyse ,buffers)
select products.product_title, products.price
from products
         left join cart_product on product_id = products_product_id
where products_product_id is NULL
order by products.price desc;
-- index no, default --
-- Sort  (cost=487.72..488.37 rows=258 width=20) (actual time=3.060..3.071 rows=258 loops=1)
--   Sort Key: products.price DESC
--   Sort Method: quicksort  Memory: 45kB
--   Buffers: shared hit=154
--   ->  Hash Anti Join  (cost=296.39..477.39 rows=258 width=20) (actual time=2.182..3.003 rows=258 loops=1)
--         Hash Cond: (products.product_id = cart_product.products_product_id)
--         Buffers: shared hit=154
--         ->  Seq Scan on products  (cost=0.00..145.00 rows=4000 width=24) (actual time=0.023..0.297 rows=4000 loops=1)
--               Buffers: shared hit=105
--         ->  Hash  (cost=158.95..158.95 rows=10995 width=4) (actual time=2.142..2.143 rows=10995 loops=1)
--               Buckets: 16384  Batches: 1  Memory Usage: 515kB
--               Buffers: shared hit=49
--               ->  Seq Scan on cart_product  (cost=0.00..158.95 rows=10995 width=4) (actual time=0.003..0.850 rows=10995 loops=1)
--                     Buffers: shared hit=49
-- Planning:
--   Buffers: shared hit=34 dirtied=1
-- Planning Time: 0.178 ms
-- Execution Time: 3.098 ms

-- add index --
create index on products(product_id);
create index on cart_product(products_product_id);
-- Sort  (cost=487.72..488.37 rows=258 width=20) (actual time=2.913..2.924 rows=258 loops=1)
--   Sort Key: products.price DESC
--   Sort Method: quicksort  Memory: 45kB
--   Buffers: shared hit=154
--   ->  Hash Anti Join  (cost=296.39..477.39 rows=258 width=20) (actual time=2.037..2.855 rows=258 loops=1)
--         Hash Cond: (products.product_id = cart_product.products_product_id)
--         Buffers: shared hit=154
--         ->  Seq Scan on products  (cost=0.00..145.00 rows=4000 width=24) (actual time=0.022..0.299 rows=4000 loops=1)
--               Buffers: shared hit=105
--         ->  Hash  (cost=158.95..158.95 rows=10995 width=4) (actual time=1.999..1.999 rows=10995 loops=1)
--               Buckets: 16384  Batches: 1  Memory Usage: 515kB
--               Buffers: shared hit=49
--               ->  Seq Scan on cart_product  (cost=0.00..158.95 rows=10995 width=4) (actual time=0.003..0.811 rows=10995 loops=1)
--                     Buffers: shared hit=49
-- Planning:
--   Buffers: shared hit=44 read=8
-- Planning Time: 0.340 ms
-- Execution Time: 2.950 ms

-- drop index --
drop index cart_product_products_product_id_idx;
drop index products_product_id_idx;

set work_mem to '1MB';
-- no index, work in 1 mb --
-- Sort  (cost=487.72..488.37 rows=258 width=20) (actual time=3.756..3.769 rows=258 loops=1)
--   Sort Key: products.price DESC
--   Sort Method: quicksort  Memory: 45kB
--   Buffers: shared hit=154
--   ->  Hash Anti Join  (cost=296.39..477.39 rows=258 width=20) (actual time=2.540..3.566 rows=258 loops=1)
--         Hash Cond: (products.product_id = cart_product.products_product_id)
--         Buffers: shared hit=154
--         ->  Seq Scan on products  (cost=0.00..145.00 rows=4000 width=24) (actual time=0.025..0.309 rows=4000 loops=1)
--               Buffers: shared hit=105
--         ->  Hash  (cost=158.95..158.95 rows=10995 width=4) (actual time=2.495..2.495 rows=10995 loops=1)
--               Buckets: 16384  Batches: 1  Memory Usage: 515kB
--               Buffers: shared hit=49
--               ->  Seq Scan on cart_product  (cost=0.00..158.95 rows=10995 width=4) (actual time=0.004..1.037 rows=10995 loops=1)
--                     Buffers: shared hit=49
-- Planning:
--   Buffers: shared hit=24
-- Planning Time: 0.217 ms
-- Execution Time: 3.800 ms

-- yes index, work in 1 mb --
-- Sort  (cost=487.72..488.37 rows=258 width=20) (actual time=3.159..3.172 rows=258 loops=1)
--   Sort Key: products.price DESC
--   Sort Method: quicksort  Memory: 45kB
--   Buffers: shared hit=154
--   ->  Hash Anti Join  (cost=296.39..477.39 rows=258 width=20) (actual time=2.161..3.094 rows=258 loops=1)
--         Hash Cond: (products.product_id = cart_product.products_product_id)
--         Buffers: shared hit=154
--         ->  Seq Scan on products  (cost=0.00..145.00 rows=4000 width=24) (actual time=0.024..0.317 rows=4000 loops=1)
--               Buffers: shared hit=105
--         ->  Hash  (cost=158.95..158.95 rows=10995 width=4) (actual time=2.116..2.117 rows=10995 loops=1)
--               Buckets: 16384  Batches: 1  Memory Usage: 515kB
--               Buffers: shared hit=49
--               ->  Seq Scan on cart_product  (cost=0.00..158.95 rows=10995 width=4) (actual time=0.004..0.850 rows=10995 loops=1)
--                     Buffers: shared hit=49
-- Planning:
--   Buffers: shared hit=44 read=8
-- Planning Time: 0.332 ms
-- Execution Time: 3.200 ms

set work_mem to '100MB';
-- no index, work in 100 mb --
-- Sort  (cost=487.72..488.37 rows=258 width=20) (actual time=3.514..3.529 rows=258 loops=1)
--   Sort Key: products.price DESC
--   Sort Method: quicksort  Memory: 45kB
--   Buffers: shared hit=154
--   ->  Hash Anti Join  (cost=296.39..477.39 rows=258 width=20) (actual time=2.454..3.455 rows=258 loops=1)
--         Hash Cond: (products.product_id = cart_product.products_product_id)
--         Buffers: shared hit=154
--         ->  Seq Scan on products  (cost=0.00..145.00 rows=4000 width=24) (actual time=0.114..0.406 rows=4000 loops=1)
--               Buffers: shared hit=105
--         ->  Hash  (cost=158.95..158.95 rows=10995 width=4) (actual time=2.317..2.317 rows=10995 loops=1)
--               Buckets: 16384  Batches: 1  Memory Usage: 515kB
--               Buffers: shared hit=49
--               ->  Seq Scan on cart_product  (cost=0.00..158.95 rows=10995 width=4) (actual time=0.007..0.925 rows=10995 loops=1)
--                     Buffers: shared hit=49
-- Planning:
--   Buffers: shared hit=24
-- Planning Time: 0.164 ms
-- Execution Time: 3.558 ms

-- yes index, work in 100 mb --
-- Sort  (cost=487.72..488.37 rows=258 width=20) (actual time=3.073..3.086 rows=258 loops=1)
--   Sort Key: products.price DESC
--   Sort Method: quicksort  Memory: 45kB
--   Buffers: shared hit=154
--   ->  Hash Anti Join  (cost=296.39..477.39 rows=258 width=20) (actual time=2.139..3.015 rows=258 loops=1)
--         Hash Cond: (products.product_id = cart_product.products_product_id)
--         Buffers: shared hit=154
--         ->  Seq Scan on products  (cost=0.00..145.00 rows=4000 width=24) (actual time=0.023..0.293 rows=4000 loops=1)
--               Buffers: shared hit=105
--         ->  Hash  (cost=158.95..158.95 rows=10995 width=4) (actual time=2.098..2.099 rows=10995 loops=1)
--               Buckets: 16384  Batches: 1  Memory Usage: 515kB
--               Buffers: shared hit=49
--               ->  Seq Scan on cart_product  (cost=0.00..158.95 rows=10995 width=4) (actual time=0.004..0.836 rows=10995 loops=1)
--                     Buffers: shared hit=49
-- Planning:
--   Buffers: shared hit=44 read=8
-- Planning Time: 0.403 ms
-- Execution Time: 3.116 ms