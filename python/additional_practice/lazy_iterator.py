"""Module in which the following classes are implemented: zip,chain,product"""


class Zip:
    """Zip class performs element-by-element concatenation"""

    def __init__(self, *args: (list, tuple, str, range)):
        for i in args:
            if type(i) not in (list, tuple, str, range):
                raise TypeError("Valid data types: list, tuple, str.")
            if len(i) < 1:
                raise ValueError('Objects cannot be empty.')
        self.args = args
        self.iteration = self.min_iteration()
        self.iter = -1

    def min_iteration(self):
        """Method that returns the number of iterations"""
        return min([len(i) for i in self.args])

    def union_method(self):
        """Method in which elements are combined"""
        for i in range(self.iteration):
            union = []
            for j in self.args:
                union.append(j[i])
            yield tuple(union)

    def __iter__(self):
        """Method that allows the iterator to work"""
        return self.union_method()

    def __next__(self):
        """"Method for the function to return the next element"""
        object_iter = list(self.union_method())
        self.iter += 1
        if self.iter >= self.iteration:
            raise StopIteration
        return object_iter[self.iter]


class Chain:
    """Class in which the individual iterable objects are combined into one"""

    def __init__(self, *args: (list, tuple, str, range)):
        for i in args:
            if type(i) not in (list, tuple, str, range):
                raise TypeError("Valid data types: list, tuple, set, str.")
        self.args = args

    def union_method(self):
        """Method that does the job of concatenating all the element in one iteration"""
        result_union = []
        for i in self.args:
            for j in i:
                result_union.append(j)
        return result_union

    def __repr__(self):
        """Method allows you to immediately see the result of the object"""
        return str(self.union_method())


class Product:
    """union class"""

    def __init__(self, *args: (list, tuple, str, range)):
        for i in args:
            if type(i) not in (list, tuple, str, range):
                raise TypeError("Valid data types: list, tuple, set, str.")
        self.args = args

    def product(self):
        """The method adds honorary elements of the following sequences to the first element"""
        prod = []
        for first_element in self.args[0]:
            for i in self.args[1:]:
                for second_element in i:
                    prod.append((first_element, second_element))
        return prod

    def __repr__(self):
        """Method allows you to immediately see the result of the object"""
        return str(self.product())


# a = Zip('123', [1, 2, 3], range(1, 4), (1, 2, 3))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# a = Chain('123', [1, 2, 3], range(1, 4), (1, 2, 3))
# print(a)
# a = Product('abc', [1, 2, 3], '1bc')
# print(a)
