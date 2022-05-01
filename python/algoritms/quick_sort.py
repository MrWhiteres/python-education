"""Quick sort is implemented in this module"""


class QuickSort:
    """class that takes a List checks it and sorts it using the quick sort method"""

    def __init__(self, list_number: list):
        self.list = self.__checker(list_element=list_number)
        self.result = self.__quick_sorted()

    @staticmethod
    def __checker(list_element=None):
        """data type checkingх"""
        for i in list_element:
            if not isinstance(i, int):
                raise TypeError(f'Type "{i}" must be int.')
        return list_element

    def __quick_sorted(self):
        """variant of quick sorting is implemented by an interactive method"""
        result = self.list
        stack = [0] * len(self.list)
        index = 0
        stack[index] = 0
        index += 1
        stack[index] = len(self.list) - 1
        while index >= 0:
            end_index = stack[index]
            index -= 1
            start_index = stack[index]
            index -= 1
            previo = self.__index(result, start_index, end_index)
            if previo - 1 > start_index:
                index += 1
                stack[index] = start_index
                index += 1
                stack[index] = previo - 1
            if previo + 1 < end_index:
                index += 1
                stack[index] = previo + 1
                index += 1
                stack[index] = end_index
        return result

    @staticmethod
    def __index(list_elem, low, high):
        """index get method"""
        start_index = low - 1
        end_index = list_elem[high]
        for i in range(low, high):
            if list_elem[i] <= end_index:
                start_index += 1
                list_elem[start_index], list_elem[i] = list_elem[i], list_elem[start_index]
        list_elem[start_index + 1], list_elem[high] = list_elem[high], list_elem[start_index + 1]
        return start_index + 1

    # def __quick_sorted(self, list_for_sorted):
    #     """method in which quick sorting occurs in a recursive format"""
    #     if len(list_for_sorted) < 2:
    #         return list_for_sorted
    #     else:
    #         pivot = list_for_sorted[0]
    #         left_side = [i for i in list_for_sorted[1:] if i <= pivot]
    #         right_side = [i for i in list_for_sorted[1:] if i > pivot]
    #         return self.__quick_sorted(left_side) + [pivot] + self.__quick_sorted(right_side)

    def __str__(self):
        return str(self.result)
