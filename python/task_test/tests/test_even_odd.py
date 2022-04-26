from python.task_test.func import even_odd
import pytest


@pytest.mark.parametrize('x, result', [(3, "odd"),
                                       (-3, "odd"),
                                       (4, 'even'),
                                       (10.3, 'odd'),
                                       (-11.5, 'odd'),
                                       (101, "odd"),
                                       (-300, "even"),
                                       (43, 'odd'),
                                       (1013.3, 'odd'),
                                       (-23.5, 'odd')])
def test_even_good(x, result):
    """test checks the correctness of the answers in a good case"""
    assert even_odd(x) == result


@pytest.mark.parametrize('exception, number', [(TypeError, 'abc'),
                                               (TypeError, [1, 2, 3]),
                                               (TypeError, {1, 2, 3}),
                                               (TypeError, {1: 2}),
                                               (TypeError, None),
                                               (TypeError, Exception),
                                               (TypeError, even_odd(2)),
                                               (TypeError, 4 + 4j)])
def test_even_bad(exception, number):
    """test checks the correctness of the answers in the case of checking for errors"""
    with pytest.raises(exception):
        assert even_odd(number)
