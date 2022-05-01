"""test module for data structure in graph"""

from python.data_structures.graph import Graph
import pytest


@pytest.fixture
def graphs():
    """function that returns the created element of the graph class"""
    graph_1 = Graph()
    graph_1.insert('Vasil', "Misha", 'Fedia')
    graph_1.insert('Misha', "Vasil", 'Fedia')
    graph_1.insert('Fedia', "Misha", 'Vasil')
    return graph_1


def test_insert(graphs):
    """test adding new elements"""
    graph_1 = graphs
    assert graph_1.head.connected.count == 2 and graph_1.count_graphs == 3


def test_lookup(graphs):
    """element search test"""
    graph_1 = graphs
    assert graph_1.lookup("Vasil") and graph_1.lookup('Fedia') and\
           not graph_1.lookup(123) and graph_1.count_graphs == 3


@pytest.mark.parametrize('del_element', ['Vasil', "Misha", 'Fedia'])
def test_delete_one_element(del_element, graphs):
    """test removing one element"""
    graph_1 = graphs
    graph_1.delete(del_element)
    assert graph_1.count_graphs == 2 and graph_1.head.connected.count == 1


def test_delete_all_element(graphs):
    """test deleting All elements and their links"""
    graph_1 = graphs
    graph_1.delete('Vasil')
    graph_1.delete('Misha')
    graph_1.delete('Fedia')
    assert graph_1.count_graphs == 0 and not graph_1.head
