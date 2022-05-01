"""class in which the stack data structure is implemented"""
from python.data_structures.linked_list import Elem


class Queue:
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

    def enqueue(self, new_element: Elem):
        """method to add a new element to the end of the queue"""
        elem = Elem(new_element)
        elem.next_symbol = self.head
        self.head = elem
        self.count += 1

    def dequeue(self):
        """removing an element from the front of the queue"""
        if self.head is None:
            return "Empty queue"
        tail = self.peek()
        previous = self.find_previous(tail)
        if not previous:
            self.count -= 1
            return tail
        previous.next_symbol = None
        self.count -= 1
        return tail

    def find_previous(self, elem_find):
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
