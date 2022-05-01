"""module for testing linked list data structure class"""

from python.data_structures.linked_list import LinkedList
import pytest


@pytest.fixture
def linked_list():
    """function returns an object of class linked list"""
    linked = LinkedList()
    linked.prepend(2)
    linked.prepend(3)
    linked.prepend(14)
    linked.prepend(-190)
    linked.prepend(50)
    linked.prepend("Vasia?")
    return linked


@pytest.mark.parametrize("value", [15, 'Petia', 'Serega'])
def test_prepend(linked_list, value):
    """test adding a new element to the beginning of the list"""
    count = linked_list.count
    linked_list.prepend(value)
    assert linked_list.head.value == value and count + 1


@pytest.mark.parametrize("value", [15, 'Petia', 'Serega'])
def test_append(linked_list, value):
    """adding an element to the end of a list"""
    count = linked_list.count
    linked_list.append(value)
    tail = linked_list.find_tail()
    assert tail.value == value and count + 1


@pytest.mark.parametrize("value, number", [(2, "Python"), ('Vasia?', 'working'), (14, 15)])
def test_insert_good(value, number, linked_list):
    """test adding element by index with friend of current element right"""
    count = linked_list.count
    linked_list.insert(value, number)
    assert linked_list.lookup(number) and count + 1


@pytest.mark.parametrize("value, number", [(0, "Python"), ('Vas', 'working'), (13, 15)])
def test_insert_bad(value, number, linked_list):
    """test with erroneous indexes when adding an element"""
    count = linked_list.count
    linked_list.insert(value, number)
    assert not linked_list.lookup(number) and count + 1


@pytest.mark.parametrize('del_element', [2, 3, 14, -190, 50])
def test_delete_one_element(linked_list, del_element):
    """test removing one element"""
    count = linked_list.count
    linked_list.delete(del_element)
    assert not linked_list.lookup(del_element) and linked_list.count == count - 1


def test_delete_all_element(linked_list):
    """test to remove all elements"""
    linked_list.delete(2)
    linked_list.delete(3)
    linked_list.delete(14)
    linked_list.delete(50)
    linked_list.delete(-190)
    linked_list.delete('Vasia?')
    assert linked_list.count == 0 and not linked_list.head


@pytest.mark.parametrize('search', [2, 3, 14, -190, 50, 'Vasia?'])
def test_lookup_good(linked_list, search):
    """element search test by value that exists"""
    assert linked_list.lookup(search)


@pytest.mark.parametrize('search', [10, 0, 15, list, 33, 'Petia?'])
def test_lookup_dad(linked_list, search):
    """search test for elements that are not in the linked list"""
    assert not linked_list.lookup(search)
