"""module in which the Hash table data structure is implemented"""

from python.data_structures.linked_list import LinkedList


class HashLinked(LinkedList):
    """modified linked list data structure adapted for Hash tables"""

    def __init__(self):
        self.head = None

    def lookup(self, subject_of_search, list_finder=None):
        """method to find element"""
        if self.head is None:
            return False
        elem = self.head if list_finder is None else list_finder.head
        if elem.next_symbol is None and elem.value.value == subject_of_search:
            return elem.key, elem.value
        while elem.next_symbol is not None:
            if elem.value == subject_of_search:
                return elem.key, elem.value
            elem = elem.next_symbol
            if elem.value == subject_of_search:
                return elem.key, elem.value
        return False


class ElemHasher:
    """element to be used in the hash table"""

    def __init__(self, key, value):
        self.key: (int, str) = key
        self.value: any = value
        self.hash: int = None
        self.next_element = None
        self.previous = None
        self.list_collision = HashLinked()


class HashTable:
    """class in which the hash table is implemented"""
    count = 0

    def __init__(self):
        self.head: ElemHasher = None

    @staticmethod
    def __hash_func(value):
        """method to calculate hash value"""
        if isinstance(value, int):
            return value % 30
        hash_total = 0
        for i in value:
            hash_total += ord(i)
        return hash_total % 30

    def lookups(self, search):
        """method to search"""
        if self.head.next_element is None and self.head.key == search:
            return self.head.key, self.head.value
        if self.head.next_element is None and self.head.key != search:
            return 'Error search'
        hash_search = self.__hash_func(search)
        tail = self.head
        while tail.next_element:
            if hash_search == tail.hash and tail.key == search:
                return tail.key, tail.value
            if hash_search == tail.hash and tail.key != search:
                return tail.list_collision.lookup(search, tail.list_collision)
            tail = tail.next_element
        if hash_search == tail.hash and tail.key == search:
            return tail.key, tail.value
        if hash_search == tail.hash and tail.key != search:
            return tail.list_collision.lookup(search, tail.list_collision) or tail.key == search

    @staticmethod
    def __check_duplicate(tail, new):
        """duplicate checking method"""
        result = tail.list_collision.lookup(new.key, tail.list_collision) or tail.key == new.key
        return result

    def delete(self, key):
        """method to remove an element"""
        if self.head.next_element is None and self.head.key == key:
            self.head = None
            self.count -= 1
        if self.head.next_element is not None or self.head.key == key:
            hash_search = self.__hash_func(key)
            tail = self.head
            previous = None
            while tail.next_element:
                previous = tail
                if hash_search == tail.hash and tail.key == key:
                    if tail.previous:
                        tail.previous.next_element = tail.next_element if tail else None
                        self.count -= 1
                        return
                    tail.next_element = tail.next_element.previous.next_element.next_element
                    self.count -= 1
                    return
                if hash_search == tail.hash and tail.key != key:
                    return tail.list_collision.lookup(key, tail.list_collision) or tail.key == key
                tail = tail.next_element
            if hash_search == tail.hash and tail.key == key:
                previous.next_element = None
                self.count -= 1

            if hash_search == tail.hash and tail.key != key:
                self.count -= 1
                return tail.list_collision.lookup(key, tail.list_collision) or tail.key == key
        return None

    def insert(self, key, value):
        """element insertion method"""
        new = ElemHasher(key, value)
        new.hash = self.__hash_func(new.key)
        if self.head is None:
            self.head = new
            self.count += 1
        else:
            tail = self.head
            if tail.hash == new.hash:
                if self.__check_duplicate(self.head, new):
                    print('Element her')
                    return
                self.head.list_collision.add_to_head(new)
                self.count += 1
            else:
                previous = tail
                while tail.next_element:
                    if tail.hash == new.hash:
                        if self.__check_duplicate(self.head, new):
                            print('Element her')
                            return
                        self.head.list_collision.add_to_head(new)
                        self.count += 1
                        return
                    tail = tail.next_element
                    tail.previous = previous if previous != tail else None
                    previous = tail
                new.next_element = self.head
                self.head.previous = new
                self.head = new
                self.count += 1
