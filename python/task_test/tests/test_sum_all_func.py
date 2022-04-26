from python.task_test.func import sum_all
import pytest


@pytest.mark.parametrize('args', [(1, 2, 3, 4, 5),
                                  (1.2, 2.3, 3.4, 4.5, 5.6),
                                  (1, 2, 3, 4, 5, 1.2, 2.3, 3.4, 4.5, 5.6)])
def test_sum_all_good(args):
    """function tests the sum of the input arguments"""
    assert sum_all(*args)


@pytest.mark.parametrize('exception , args', [(TypeError, ([1], 2, 3, 4, 5)),
                                              (TypeError, ([1, 2, 3], [1, 2, 3])),
                                              (TypeError, ('asd', 123, 4 + 5j))])
def test_sum_all_bad(exception, args):
    """function returns errors and for using incorrect data types"""
    with pytest.raises(exception):
        assert sum_all(*args)
