"""Module that allows using the player class to
 create an object for the game tic-tac-toe"""


class Player:
    """Class to create player object"""
    symbol = None

    def __init__(self, name: str):
        """Method toolkit with required fields"""
        self.name = name
        self.game_list = {}

    def take_symbol(self, symbol: str):
        """Method to add symbol to player"""
        self.symbol = symbol

    def add_to_dict(self, number_game: int, param: bool):
        """Method allows you to add a dictionary
         game number and its result where True-Win/False-Lose"""
        self.game_list[number_game] = param

    def show_win(self):
        """Method that returns the number of wins"""
        win = 0
        for value in self.game_list.values():
            if value:
                win += 1
        return win



"""Module in which there is a class that allows
 you to create a playing field for the game tic-tac-toe"""


class Board:
    """Class that allows you to create a field object"""
    board = [None for _ in range(9)]

    def clear_bord(self):
        """Method creates a new field"""
        self.board = [None for _ in range(9)]

    def draw(self):
        if None not in self.board:
            return True
        return False

    def check_all(self, symbol: str):
        """Method uses checks to determine the winning combination"""
        return self.check_row(symbol) or self.check_diagonal(symbol) or self.check_colm(symbol)

    def check_row(self, symbol: str):
        """Method checks winning combinations line by line"""
        for i in range(3):
            row = self.board[i * 3:i * 3 + 3]
            if len(set(row)) == 1 and row[0] == symbol:
                return True
        return False

    def check_colm(self, symbol: str):
        """Method checks winning combinations by columns"""
        for i in range(3):
            colm = [self.board[i], self.board[i + 3], self.board[i + 6]]
            if len(set(colm)) == 1 and colm[0] == symbol:
                return True
        return False

    def check_diagonal(self, symbol: str):
        """Method checks winning combinations diagonally"""
        if [self.board[0], self.board[4], self.board[8]].count(symbol) == 3 or \
                [self.board[2], self.board[4], self.board[6]].count(symbol) == 3:
            return True
        return False
