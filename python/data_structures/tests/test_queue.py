"""module for testing data structure queue"""

from python.data_structures.queues import Queue
import pytest


@pytest.fixture
def my_queue():
    """function that returns an object of the queue class"""
    que = Queue()
    que.enqueue(1)
    que.enqueue(2)
    return que


@pytest.mark.parametrize('value', [6, 7, 8, 9, 10])
def test_peek(my_queue, value):
    """test getting the element that is at the head of the queue"""
    count = my_queue.count
    my_queue.enqueue(value)
    assert my_queue.peek().value == value


@pytest.mark.parametrize('value', [6, 7, 8, 9, 10])
def test_enqueue(my_queue, value):
    """test adding a new element to the end of the queue"""
    count = my_queue.count
    my_queue.enqueue(value)
    assert my_queue.count == count + 1


@pytest.mark.parametrize('value', [6, 7, 8, 9, 10])
def test_dequeue(my_queue, value):
    """test to remove the first element from the queue"""
    count = my_queue.count
    first = my_queue.peek()
    end = my_queue.dequeue()
    assert my_queue.count == count - 1 and first == end
