"""module for testing stack data structure"""

from python.data_structures.stack import Stack
import pytest


@pytest.fixture
def my_stack():
    """function returns an object of class stack"""
    stack = Stack()
    return stack


@pytest.mark.parametrize('element_1,element_2,element_3,element_4', [(1, 2, 3, 4),
                                                                     ('asd', [123], ValueError, set)])
def test_peek(my_stack, element_1, element_2, element_3, element_4):
    """test function to get the last element from the stack"""
    my_stack.push(element_1)
    my_stack.push(element_2)
    my_stack.push(element_3)
    my_stack.push(element_4)
    assert my_stack.peek().value == element_1


@pytest.mark.parametrize('element_1,element_2,element_3,element_4', [(1, 2, 3, 4),
                                                                     ('asd', [123], ValueError, set)])
def test_push(my_stack, element_1, element_2, element_3, element_4):
    """test adding new elements to the stack"""
    my_stack.push(element_1)
    my_stack.push(element_2)
    my_stack.push(element_3)
    my_stack.push(element_4)
    assert my_stack.count == 4


@pytest.mark.parametrize('element_1,element_2,element_3,element_4', [(1, 2, 3, 4),
                                                                     ('asd', [123], ValueError, set)])
def test_pop(my_stack, element_1, element_2, element_3, element_4):
    """test Returning the last element from the stack"""
    my_stack.push(element_1)
    my_stack.push(element_2)
    my_stack.push(element_3)
    my_stack.push(element_4)
    assert my_stack.pop().value == element_4
