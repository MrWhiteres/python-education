"""module in which the binary tree data structure is implemented"""


class ElemTree:
    """element for working with data structure binary tree"""
    def __init__(self, value: int):
        self.left = None
        self.right = None
        self.value = value
        self.previous = None


class BinarySearchTree:
    """class in which the binary tree data structure is implemented"""
    count_elements = 0

    def __init__(self):
        self.head: ElemTree = None

    def insert(self, value: ElemTree):
        """add new element method"""
        if not isinstance(value, int):
            raise ValueError('Must by int')
        new_element = ElemTree(value)
        if self.head is None:
            self.head = new_element
            self.count_elements += 1
        else:
            tail_tree = self.head
            previous = None
            while tail_tree:
                if tail_tree.value == new_element.value:
                    print(f'Element her {value}')
                    return
                previous = tail_tree
                tail_tree, flag = (tail_tree.right, True) if \
                    new_element.value > tail_tree.value else (tail_tree.left, False)
            if flag:
                previous.right = new_element
            if not flag:
                previous.left = new_element
            self.count_elements += 1

    def lookup(self, value):
        """element lookup method"""
        tail_tree = self.head
        while tail_tree:
            if tail_tree.value == value:
                return tail_tree
            tail_tree = tail_tree.right if value > tail_tree.value else tail_tree.left
        return tail_tree if tail_tree and tail_tree.value == value else None

    def __delete_end(self, flag):
        """methods that complement the function of removing an element"""
        previous = None
        tail_tree = self.head.right if flag else self.head.left
        new_element = self.head.left if flag else self.head.right
        while tail_tree:
            tail_tree, flag_in = (tail_tree.right, True) if\
                self.head.left.value > tail_tree.value else (tail_tree.left, False)
        if not previous:
            previous = self.head.right if flag else self.head.left
        if flag_in:
            previous.right = new_element
        if not flag_in:
            previous.left = new_element
        self.head = previous
        self.count_elements -= 1

    def delete(self, value):
        """element removal method"""
        if self.lookup(value) == self.head:
            if not self.head.right and not self.head.left:
                self.head = None
                self.count_elements -= 1
            elif not self.head.right and self.head.left or self.head.right and not self.head.left:
                self.head = self.head.left if not self.head.right else self.head.right
                self.count_elements -= 1
            elif self.head.right and self.head.left:
                flag = True if self.head.right.value > self.head.left.value else False
                self.__delete_end(flag)
        else:
            self.__del_cont(value)

    def __del_cont(self, value):
        """methods that complement the function of removing an element"""
        if self.lookup(value):
            previous = None
            tail_tree = self.head
            while tail_tree.value != value:
                previous = tail_tree
                tail_tree, flag = (tail_tree.right, True)\
                    if value > tail_tree.value else (tail_tree.left, False)
            if not tail_tree.left and not tail_tree.right:
                element = None
            else:
                element = tail_tree.left if not tail_tree.left else tail_tree.right
            if flag:
                previous.right = element
            else:
                previous.left = element
            self.count_elements -= 1
            del tail_tree
        else:
            raise ValueError(f'Element Not found - {value}')

    def __str__(self):
        return f'{self.count_elements}\n{self.head}\n'
