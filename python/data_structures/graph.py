"""module in which the graph data structure is implemented"""

class GraphList:
    """modified linked list to work with graph data structure"""
    def __init__(self):
        self.head = None

    count = 0

    def __append(self, value, *connections):
        """method to add a new element to the beginning of the list"""
        elem = ElemGraph(value, connections)
        elem.next = self.head
        if self.head:
            self.head.previous = elem
        self.head = elem
        self.count += 1

    def lookup(self, subject_of_search):
        """method for finding and outputting the index of an element"""
        for i in self:
            if i.value == subject_of_search:
                return i
        return False

    def deletes(self, element):
        """method to remove an element by its value"""
        element = self.lookup(element)
        if not element:
            print('delete element operation failed')
            return False
        if element.previous and element.next:
            element.previous.next = element.next
            element.next.previous = element.previous
        elif element.previous and not element.next:
            element.previous.next = None
            self.head = element.previous
        elif not element.previous and element.next:
            element.next.previous = None
            self.head = element.next
        elif not element.previous and not element.next:
            self.head = None
        self.count -= 1

    def __check_duplicate(self, value):
        """duplicate checking method"""
        element = self.head
        for i in self:
            if i.value == value:
                return element
        return False

    def __iter__(self):
        return self.__generator()

    def __generator(self):
        """Returns generator of collection"""
        elem = self.head
        while elem is not None:
            yield elem
            elem = elem.next

    def __next__(self):
        return next(self.__generator)


class ElemGraph:
    """element that is necessary to work with the graph data structure"""
    next = None
    previous = None
    status = False

    def __init__(self, value, list_elem):
        self.value = value
        self.connected = GraphList()
        self.list_elem = list_elem


class Graph:
    """the class in which the graph data structure is implemented"""
    count_graphs = 0

    def __init__(self):
        self.head = None

    def insert(self, value, *connections):
        """add new element method"""
        if self.lookup(value):
            return None
        if not self.head:
            self.head = ElemGraph(value, connections)
            self.count_graphs += 1
            return
        head = self.head
        new_graph = ElemGraph(value, connections)
        for i in self:
            head = i
        new_graph.previous = head
        head.next = new_graph
        self.__connect()
        self.count_graphs += 1

    def __connect(self):
        """method to check and connect All elements with current existing graphs"""
        for element in self:
            for elem in element.list_elem:
                for element_2 in self:
                    if element == element_2:
                        continue
                    if elem == element_2.value and not element.connected.lookup(elem):
                        element.connected._GraphList__append(element_2.value, *element_2.list_elem)

    def lookup(self, search):
        """element lookup method"""
        for i in self:
            if i.value == search:
                return i
        return None

    def delete(self, search):
        """removal method"""
        if not self.lookup(search):
            return None
        else:
            elem = self.lookup(search)
            if self.head.value == search and self.head.next:
                self.head = self.head.next
                self.head.previous = None
            elif self.head.value == search and not self.head.next:
                self.head = None
            elif elem.previous and elem.next:
                elem.previous.next = elem.next
                elem.next.previous = elem.previous
            elif elem.previous and not elem.next:
                elem.previous.next = None
            elif not elem.previous and elem.next:
                elem.next.previous = None
            elif not elem.previous and not elem.next:
                self.head = None
            self.count_graphs -= 1
            self.__del_connect(search)

    def __del_connect(self, item):
        """unlinking a deleted element"""
        for i in self:
            if i.connected.lookup(item):
                i.connected.deletes(item)

    def __iter__(self):
        return self.__generator()

    def __generator(self):
        """Returns generator of collection"""
        elem = self.head
        while elem is not None:
            yield elem
            elem = elem.next

    def __next__(self):
        return next(self.__generator)
