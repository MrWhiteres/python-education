"""module that implements a linked list"""


class Elem:
    """object to use in the linked list"""
    next_symbol = None
    value = None

    def __init__(self, value) -> object:
        self.value = value
        self.key = None

    def __str__(self):
        return f'Elem<{self.value}>'


class LinkedList:
    """class that implements the linked list"""
    count = 0

    def __init__(self):
        self.head = None

    def prepend(self, elem: Elem):
        """method to add a new element to the beginning of the list"""
        elem = Elem(elem)
        elem.next_symbol = self.head
        self.head = elem
        self.count += 1

    def append(self, new_element: Elem):
        """method to add a new element to the end of the list"""
        if self.head is None:
            self.head = Elem(new_element)
            self.count += 1
            return
        tail = self.head
        while tail.next_symbol:
            tail = tail.next_symbol
        tail.next_symbol = Elem(new_element)
        self.count += 1

    def insert(self, element: Elem, new_element):
        """method for adding a new element to a list after another element"""
        element = self.__find_element(element)
        if not element:
            print('add element operation failed')
            return False
        new_element = Elem(new_element)
        new_element.next_symbol = element.next_symbol
        element.next_symbol = new_element
        self.count += 1

    def find_tail(self):
        """method for finding the last element"""
        elem = self.head
        while elem.next_symbol is not None:
            elem = elem.next_symbol
        return elem

    def __find_element(self, subject_of_search):
        """method to find element"""
        elem = self.head
        while elem.next_symbol is not None:
            if elem.value == subject_of_search:
                return elem
            elem = elem.next_symbol
            if elem.value == subject_of_search:
                return elem
        return False if self.head.value != subject_of_search else elem

    def delete(self, element: Elem):
        """method to remove an element by its value"""
        element = self.__find_element(element)
        if not element:
            print('delete element operation failed')
            return False
        if self.head.value == element:
            self.head = None
            self.count -= 1
            return
        previous = self.__find_previous(element)
        if previous is None:
            self.head = element.next_symbol
            self.count -= 1
        else:
            previous.next_symbol = element.next_symbol
            self.count -= 1

    def __find_previous(self, elem_find):
        """method to find the previous element"""
        elem = self.head
        while elem.next_symbol is not None:
            if elem.next_symbol is elem_find:
                return elem
            elem = elem.next_symbol

    def lookup(self, subject_of_search):
        """method for finding and outputting the index of an element"""
        index = 0
        elem = self.head
        while elem.next_symbol is not None:
            if elem.value == subject_of_search:
                return f'Index "{subject_of_search}" - {index}'
            index += 1
            elem = elem.next_symbol
            if elem.value == subject_of_search:
                return f'Index "{subject_of_search}" - {index}'
        return False

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
