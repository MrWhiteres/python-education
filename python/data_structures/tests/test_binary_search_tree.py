"""module for testing binary tree data structure"""

from python.data_structures.binary_search_tree import BinarySearchTree
import pytest


@pytest.mark.parametrize('head, left, right', [(20, 15, 25),
                                               (10, 0, 15),
                                               (1, -1, 2)])
def test_insert_two_section(head, left, right):
    """tests of adding 3 elements of average greater and lesser"""
    tree = BinarySearchTree()
    tree.insert(head)
    tree.insert(left)
    tree.insert(right)
    assert tree.head.value == head and tree.head.right.value == right and tree.head.left.value == left


@pytest.mark.parametrize('head, left, left_left', [(20, 15, 10),
                                                   (10, 0, -10),
                                                   (30, 29, 28)])
def test_insert_one_section(head, left, left_left):
    """test adding an element in one line"""
    tree = BinarySearchTree()
    tree.insert(head)
    tree.insert(left)
    tree.insert(left_left)
    assert tree.head.value == head and tree.head.left.value == left and tree.head.left.left.value == left_left


@pytest.mark.parametrize('head, right, right_right', [(20, 25, 30),
                                                      (0, 10, 20),
                                                      (30, 39, 48)])
def test_insert_one_section(head, right, right_right):
    """test adding an element in one line"""
    tree = BinarySearchTree()
    tree.insert(head)
    tree.insert(right)
    tree.insert(right_right)
    assert tree.head.value == head and tree.head.right.value == right and tree.head.right.right.value == right_right


@pytest.mark.parametrize('value,exception', [([123, 123], ValueError),
                                             ('asd', ValueError),
                                             (BinarySearchTree(), ValueError)])
def test_insert_bad_add(value, exception):
    """tests for adding elements with the wrong data type"""
    with pytest.raises(exception):
        tree = BinarySearchTree()
        assert tree.insert(value)


@pytest.mark.parametrize('head, left, right', [(20, 15, 25),
                                               (10, 0, 15),
                                               (1, -1, 2)])
def test_lookup(head, left, right):
    """element search test"""
    tree = BinarySearchTree()
    tree.insert(head)
    tree.insert(left)
    tree.insert(right)
    assert head == tree.lookup(head).value and left == tree.lookup(left).value and right == tree.lookup(right).value


@pytest.mark.parametrize('head, left, right', [(20, 15, 25),
                                               (10, 0, 15),
                                               (1, -1, 2)])
def test_lookup_bad(head, left, right):
    "element search test"
    tree = BinarySearchTree()
    tree.insert(head)
    tree.insert(left)
    tree.insert(right)
    assert not tree.lookup(head + 10) and not tree.lookup(head + right) and not tree.lookup(left + head - right)


@pytest.mark.parametrize('head, left, right', [(20, 15, 25),
                                               (10, 0, 15),
                                               (1, -1, 2)])
def test_delete_all(head, left, right):
    """test removing elements"""
    tree = BinarySearchTree()
    tree.insert(head)
    tree.insert(left)
    tree.insert(right)
    tree.delete(head)
    tree.delete(left)
    tree.delete(right)
    assert tree.count_elements == 0


@pytest.mark.parametrize('head, left, right', [(20, 15, 25),
                                               (10, 0, 15),
                                               (1, -1, 2)])
def test_delete_head(head, left, right):
    """test removing elements"""
    tree = BinarySearchTree()
    tree.insert(head)
    tree.insert(left)
    tree.insert(right)
    tree.delete(head)
    assert tree.count_elements == 2
