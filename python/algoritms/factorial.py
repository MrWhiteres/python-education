"""module implements the recursive factorial class"""


class RecursiveFactorial:
    """class implements the functionality of calculating the recursive factorial"""

    def __init__(self, number):
        self.number = self.__checker(number)
        self.result = self.__recur_factorial(self.number)

    @staticmethod
    def __checker(number):
        """this method, the incoming data is checked by their type
         and also if the type is a number that it is greater than one"""
        if not isinstance(number, int):
            raise TypeError(f'{number} must by int.')
        if 0 <= number <= 1 or number < 0:
            raise ValueError(f'{number} value must be greater than 1.')
        return number

    def __recur_factorial(self, number):
        """here is the main work of calculating the factorial"""
        if number == 1:
            return number
        else:
            return number * self.__recur_factorial(number - 1)

    def __str__(self):
        return f'Factorial {self.number} = {self.result}.'
