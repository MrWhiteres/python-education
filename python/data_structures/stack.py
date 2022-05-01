"""module in which a data structure 'Stack' is implemented as a class"""
from python.data_structures.linked_list import Elem


class Stack:
    """class in which the stack data structure is implemented"""
    count = 0

    def __init__(self):
        self.head = None

    def peek(self):
        """method for finding the last element"""
        elem = self.head
        while elem.next_symbol is not None:
            elem = elem.next_symbol
        return elem

    def push(self, new_element):
        """add new element method"""
        elem = Elem(new_element)
        elem.next_symbol = self.head
        self.head = elem
        self.count += 1

    def pop(self):
        """removing the last element"""
        if self.head is None:
            return "Empty stack"
        element = self.head
        if element.next_symbol is not None:
            self.head = element.next_symbol
        self.count -= 1
        return element

    def __find_previous(self, elem_find):
        """method to find the previous element"""
        elem = self.head
        while elem.next_symbol is not None:
            if elem.next_symbol is elem_find:
                return elem
            elem = elem.next_symbol

    def __iter__(self):
        self.generator = self.__generator()
        return self

    def __generator(self):
        """Returns generator of collection"""
        elem = self.head
        while elem is not None:
            yield elem.value
            elem = elem.next_symbol

    def __next__(self):
        return next(self.generator)
