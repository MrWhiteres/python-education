"""quick sort test module"""

from python.algoritms.quick_sort import QuickSort
import pytest
from random import shuffle
from string import ascii_letters


@pytest.fixture
def array():
    """function returns a list with a million values"""
    return list(range(1000000))

@pytest.fixture
def array_2():
    """function returns a list with a million values"""
    return [i for i in ascii_letters]


def test_quick_sort(array):
    """in the test, using the Shuffle method, the
     resulting list is shuffled for further sorting"""
    shuffle(array)
    assert QuickSort(array).result == sorted(array)

@pytest.mark.parametrize('exception', [TypeError])
def test_quick_sort_bad(array_2, exception):
    with pytest.raises(exception):
        assert QuickSort(array_2)