from game_view import Board, View
from random import shuffle
from log import logger


class GameController:
    """The class is the controller for the tic-tac-toe game"""
    symbol_list = ['X', '0']
    tur = 1

    def __init__(self, board: Board, players_list: list, view: View):
        self.board = board
        self.players_list = players_list
        self.view = view

    @staticmethod
    def checker(player, result_funk, tur):
        """Statistical method that checks if the
         player has won and if he won, a record is made in his statistics"""
        if result_funk:
            logger.info(f'Player {player.name} won')
            player.add_to_dict(tur, True)
            return True
        return False

    def winner(self, winner, board, loser):
        """Method is responsible for adding a Victory to the winner and a record to the
         loser of the defeat"""
        if self.checker(winner, board.check_all(winner.symbol), self.tur):
            loser.add_to_dict(self.tur, False)
            return True
        return False

    def shuffle_list(self):
        """method is responsible for shuffling lists"""
        shuffle(self.players_list)
        shuffle(self.symbol_list)

    def new_game(self):
        """Method in which all the game logic happens"""
        self.shuffle_list()
        player_1, player_2 = self.players_list[0], self.players_list[1]
        player_1.take_symbol(self.symbol_list[0])
        player_2.take_symbol(self.symbol_list[1])
        count = 0
        self.view.show_board(self.board.board)
        self.game_engine(count, player_1, player_2)
        next_game = self.view.next_game()

        if self.view.checker_later(next_game):
            self.tur += 1
            logger.info(f"Current account between player {player_1.name} and player"
                        f" {player_2.name}: {player_1.show_win()}/{player_2.show_win()}")
            self.board.clear_bord()
            self.new_game()
        if not self.view.checker_later(next_game):
            logger.info(f"Game between the to-too player {player_1.name} "
                        f"and the player {player_2.name} has ended."
                        f" Games played - {self.tur}")
            self.view.winner_stat(player_1)
            self.view.winner_stat(player_2)
            self.board.clear_bord()
            return False

    def game_engine(self, count, player_1, player_2):
        """this is where the whole game happens"""
        while True:
            self.view.print_empty()

            if count >= 2:
                if self.winner(player_2, self.board, player_1):
                    break
            self.view.mover(player_1.name, player_1.symbol, self.board)
            self.view.show_board(self.board.board)
            if self.board.draw():
                logger.info('Game ended in a draw')
                player_1.add_to_dict(self.tur, None)
                player_2.add_to_dict(self.tur, None)
                break
            self.view.print_empty()

            if count >= 2:
                if self.winner(player_1, self.board, player_2):
                    break
            self.view.mover(player_2.name, player_2.symbol, self.board)
            self.view.show_board(self.board.board)

            if self.board.draw():
                logger.info('Game ended in a draw')
                player_1.add_to_dict(self.tur, None)
                player_2.add_to_dict(self.tur, None)
                break
            count += 1
