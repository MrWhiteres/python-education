"""terminal modules"""
from game_logic import Player, Board
from game_controller import GameController
from log import logger
from string import ascii_letters
from abc import ABC, abstractmethod


class View(ABC):
    """class for gui"""

    def __init__(self, board: Board):
        self.board = board

    @abstractmethod
    def check_num_menu(self):
        """Statistical method for checking the input number"""

    @abstractmethod
    def menu(self):
        """gui menu"""

    @abstractmethod
    def reader_logs(self):
        """reader logs"""

    @abstractmethod
    def del_logs(self):
        """del logs"""

    @abstractmethod
    def show_board(board):
        """render board"""

    @abstractmethod
    def checker_later(later):
        """ check later"""

    @abstractmethod
    def next_game(self):
        """continue game"""

    @abstractmethod
    def num_check_board(number: int):
        """check num in range board"""

    @abstractmethod
    def check_free_and_move(board, number: int, symbol: str):
        """check and move"""

    @abstractmethod
    def mover(self, name, symbol, board):
        """mover"""

    @abstractmethod
    def print_empty(self):
        """return empty print"""

    @abstractmethod
    def winner_stat(player):
        """return winner stats"""


class TerminalView(View):
    """class responsible for displaying and user input"""

    def __init__(self, board: Board):
        self.board = board

    @staticmethod
    def check_num_menu(num):
        """Statistical method for checking the input number"""
        while True:
            if len(num) == 1 and num not in ascii_letters and int(num) in [1, 2, 3, 4]:
                return int(num)
            num = input('Wrong input. Must be digit or 1/2/3/4: ')

    def menu(self):
        """Method in which the functionality of the main menu of the game is implemented"""
        while True:
            choice = self.check_num_menu(input('Game menu:\n1 - Start game on 2 players\n2'
                                               ' - Show win logs\n3 - Clear log file\n4 - Exit\n'))
            if choice == 1:
                player_list = []
                for i in range(2):
                    player_list.append(Player(input(f"Player - {i + 1} name: ")))
                game = GameController(self.board, player_list, self)
                game.new_game()
                print('thanks for playing')
            if choice == 2:
                self.reader_logs()
            if choice == 3:
                self.del_logs()
            if choice == 4:
                print('Thank you for playing See you')
                break

    @staticmethod
    def reader_logs():
        """Method for reading log files"""
        with open('wins.log', "r", encoding='utf-8') as file:
            for line in file.readlines():
                print(line)
        print('Return in main menu.')
        logger.info('Log file shows')

    @staticmethod
    def del_logs():
        """Method for deleting log file"""
        with open('wins.log', "w", encoding='utf-8'):
            pass
        logger.warning('Logs have been deleted')
        print('Return in main menu.')

    @staticmethod
    def show_board(board):
        """Field output method"""
        iterator = 0
        sim = '|'
        while iterator < 9:
            if iterator in [3, 6]:
                print()
                sim = '|'
            print(sim, board[iterator].center(2) if board[iterator] is not None else ' ',
                  '|', end=' ')
            iterator += 1
            sim = ''

    @staticmethod
    def checker_later(later):
        """Statistical method that checks the letter And if not, it will be necessary
         to enter it correctly"""
        while True:
            if later.lower() in ['y', 'n']:
                if later.lower() == 'y':
                    return True
                if later.lower() == 'n':
                    return False
            else:
                later = input('letter should only be (y/n): ')

    @staticmethod
    def next_game():
        """function that takes over the user's response to continue the game"""
        question = input('Want to continue playing?: (yes[y]/mo(n): ')
        return question

    @staticmethod
    def num_check_board(number: int):
        """Methods check the incoming element that it is a number and
         is included in the field's range of numbers"""
        while True:
            if len(number) == 1 and number not in ascii_letters and \
                    int(number) in [i + 1 for i in range(3 ** 2)]:
                return int(number)
            number = input('Number must be in range 1-9: ')

    @staticmethod
    def check_free_and_move(board, number: int, symbol: str):
        """Method checks if the field element is empty
         and if it is empty then the move will be made"""
        while True:
            number -= 1
            if board[number] is None:
                board[number] = symbol
                break
            number = int(input('Error: '))

    def mover(self, name, symbol, board):
        """Method is responsible for the move"""
        move = input(f'Player {name} move {symbol}: ')
        self.check_free_and_move(board.board, self.num_check_board(move), symbol)

    @staticmethod
    def print_empty():
        print()

    @staticmethod
    def winner_stat(player):
        """Method allows you to get the ratio of games to win 'win rate'"""
        win = 0
        for value in player.game_list.values():
            if value:
                win += 1
        print(f'{player.name} Win-rate - {win / len(player.game_list) * 100}%.')
