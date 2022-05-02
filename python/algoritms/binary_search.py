"""this module implements binary search"""


class BinarySearch:
    """class in which binary search is implemented"""

    def __init__(self, list_number: list, search: int):
        self.list = self.__checker(list_element=list_number)
        self.search = self.__checker(element=search)
        self.result = self.__binary_search(self.list, self.search)

    @staticmethod
    def __checker(list_element=None, element=None):
        """data type checkingх"""
        if not isinstance(element, int) and element:
            raise TypeError(f'Type "{element}" must be int.')
        if list_element:
            for i in list_element:
                if not isinstance(i, int):
                    raise TypeError(f'Type "{i}" must be int.')
            if list_element != sorted(list_element):
                return sorted(list_element)
            return list_element
        return element

    @staticmethod
    def __binary_search(list_element: list, search_elem: int):
        """function in which binary search occurs"""
        left, right = 0, len(list_element) - 1
        while left <= right:
            mid = (left + right) // 2
            if list_element[mid] == search_elem:
                return mid
            if list_element[mid] > search_elem:
                right = mid - 1
            else:
                left = mid + 1
        return None

    def __str__(self):
        if self.result:
            return f'Element search "{self.search}" found in array.' \
                   f' In the sorted list its index - {self.result}"'
        return f'This element - "{self.search}" is not in the array'
