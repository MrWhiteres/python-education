"""module in which the recursive factorial is tested"""

from python.algoritms.factorial import RecursiveFactorial
import pytest
from math import factorial


@pytest.mark.parametrize('element', [i for i in range(2, 960)])
def test_recursive_factorial(element):
    """the results of the recursive factorial are compared with the
     work of computing the factorial using the math library"""
    assert RecursiveFactorial(element).result == factorial(element)


@pytest.mark.parametrize('value, exception', [(0, ValueError),
                                              ('Set', TypeError),
                                              (-100, ValueError),
                                              (0.99, TypeError),])
def test_recursive_factorial_bad_element(value, exception):
    with pytest.raises(exception):
        assert RecursiveFactorial(value)
