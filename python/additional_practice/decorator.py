"""This module works with decorators"""
from log import logger
from generator import show_fibo, time


def counter(func: object):
    """
    Decorator keeps count of how many times the function has been called
    """
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        logger.info(f"Function '{func.__name__}' has been executed {wrapper.count}.")
        return res

    wrapper.count = 0
    return wrapper


start_time = time()


def logger_time(func: object):
    """
    Method records and shows the execution time of the function
    """

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        logger.info(f"Function '{func.__name__}' has been running for {time() - start_time}.")
        return res

    wrapper.count = 0
    return wrapper


@counter
@logger_time
def gen(func):
    """Function for decorator example"""
    return next(func) if func is not None else ''


print(gen(show_fibo(5)))
print(gen(show_fibo(50)))
# print(gen(show_fibo(500)))
