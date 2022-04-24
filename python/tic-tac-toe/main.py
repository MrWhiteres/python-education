"""Module in which checks are carried out"""
from game_view import TerminalView
from game_logic import Board


def test():
    """Function for tests"""
    case = TerminalView(Board())
    case.menu()


if __name__ == "__main__":
    test()
