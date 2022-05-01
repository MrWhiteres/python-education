"""binary search testing module"""

import pytest
from python.algoritms.binary_search import BinarySearch


@pytest.fixture
def array():
    """function returns a list of 1000 elements"""
    return range(1000)


@pytest.mark.parametrize("value", [i for i in range(1000)])
def test_binary_search_good(array, value):
    """test to find 1000 items in a list"""
    my_search = BinarySearch(array, value)
    assert my_search.result == value


@pytest.mark.parametrize("value, exception", [('123', TypeError),
                                              ([123,123], TypeError)])
def test_binary_search_bad(array, value, exception):
    """test to find 1000 items in a list"""
    with pytest.raises(exception):
        assert BinarySearch(array, value)