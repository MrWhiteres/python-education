"""Module is designed to calculate the Fibonacci number"""
from time import time
from log import logger


def gen_fibo(num):
    """Generator that returns the value of Fibonacci numbers"""
    assert num >= 0
    fib_num_first, fib_num_second = 0, 1
    for _ in range(num - 1):
        fib_num_first, fib_num_second = fib_num_second, fib_num_first + fib_num_second
        yield fib_num_second


def show_fibo(num):
    """Method in which viewing of all Fibonacci numbers from a given range is implemented"""
    worker = gen_fibo(num)
    start_work = time()
    while True:
        try:
            print(next(worker), end=' ')
        except StopIteration:
            print()
            logger.info('Running time of the generator'
                        f' in the while loop - second:{time() - start_work}')
            break
        finally:
            pass


if __name__ == "__main__":
    show_fibo(10)
    # or
    # start_work = time()
    # num = gen_fibo(10)
    # for i in num:
    #     print(i)
    # logger.info(f'Running time of the generator'
    #             f' in the while loop - second:{time() - start_work}')
