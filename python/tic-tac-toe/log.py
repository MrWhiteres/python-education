from logging import getLogger, INFO, Formatter, FileHandler, StreamHandler
from sys import stdout


def get_logger(name=__file__, file='wins.log', encoding='utf-8'):
    """Making adjustments to the function for the current need"""
    log = getLogger(name)
    log.setLevel(INFO)
    formatter = Formatter('[%(asctime)s] %(filename)s:%(lineno)d'
                          ' %(levelname)-8s %(message)s')

    f_h = FileHandler(file, encoding=encoding)
    f_h.setFormatter(formatter)
    log.addHandler(f_h)

    s_h = StreamHandler(stream=stdout)
    s_h.setFormatter(formatter)
    log.addHandler(s_h)

    return log


logger = get_logger()
