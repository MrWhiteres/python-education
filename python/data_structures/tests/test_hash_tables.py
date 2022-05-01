"""module for testing class hash table"""

from python.data_structures.hash_table import HashTable
import pytest


@pytest.fixture
def table_hash():
    """function that returns a Hash table object"""
    table = HashTable()
    table.insert(123, 'Vasia')
    table.insert(4, "Misha")
    return table


def test_lookups_good(table_hash):
    """element test"""
    table = table_hash
    assert table.lookups(123) and table.lookups(4)


def test_lookups_bad(table_hash):
    """element test"""
    table = table_hash
    assert not table.lookups(15) and not table.lookups('Avokado')


def test_delete(table_hash):
    """element removal test"""
    table = table_hash
    table.delete(123)
    assert table.count == 1


def test_insert():
    """test adding a new element"""
    table = HashTable()
    table.insert(123, 'Vasia')
    table.insert(4, "Misha")
    assert table.count == 2
