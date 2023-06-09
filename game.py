import tic_tac_toe as ttt
from typing import Tuple
import abc

class Game(abc.ABC):
    
    def __init__(self, ttt_game:ttt.TicTacToeGame=None) -> None:
        if ttt_game :
            self.load_game(ttt_game)
        else:    
            self.new_game()

    @abc.abstractmethod
    def get_input(self) -> Tuple[int, int]:
        pass

    @abc.abstractmethod
    def display_error(self, error_msg:str) -> None:
        pass

    @abc.abstractmethod
    def display_game_state(self) -> None:
        pass

    @abc.abstractmethod
    def display_game_end(self, winner) -> None:
        pass

    def new_game(self) -> None:
        self.ttt_game = ttt.TicTacToeGame()
    
    def load_game(self, ttt_game:ttt.TicTacToeGame) -> None:
        self.ttt_game = ttt_game
    
    def play_game(self) -> None:
        self.display_game_state()
        play_next_round = True
        while play_next_round:
            correct_input = False
            while not correct_input:
                row, col = self.get_input()
                if row > 2 or col > 2:
                    self.display_error(f'Row and column values must be in between 0 and 2')
                    continue
                try:
                    self.ttt_game.player_move(row=row, col=col)
                    correct_input = True
                except AttributeError as e:
                    error_msg = e.args[0]
                    self.display_error(error_msg)
            play_next_round, winner = self.ttt_game.next_round()
            self.display_game_state()
        self.display_game_end(winner)

class ConsoleGame(Game):
    def get_input(self) -> Tuple[int, int]:
        row, col = None, None
        while not (isinstance(row,int) and isinstance(col,int)):
            coordinates = input(f"Player {self.ttt_game.get_current_player()} \
                            provide coordinates for your next move, \
                            sparated by ',' ")
            try:
                row, col = [int(coord) for coord in coordinates.split(',')]
            except ValueError as e:
                error_msg = e.args[0]
                self.display_error(error_msg + '\nTry again.')
        return row, col

    def display_error(self, error_msg: str) -> None:
        print(error_msg)

    def display_game_state(self) -> None:
        empty_line =     '   |   |   '
        separator_line = '-----------'
        fill_dict = {0:[2,5], 1:[6,9], 2:[10,11]}
        game_lines = [' ', ' ', ' ']
        board = self.ttt_game.tic_tac_toe_board.get_board()
        for row in range(3):
            for col in range(3):
                game_lines[row] += board[row][col] if board[row][col] else ' '
                game_lines[row] += empty_line[fill_dict[col][0]: 
                                              fill_dict[col][1]]
            game_lines[row] = empty_line + '\n' + game_lines[row] +'\n' \
                              + empty_line
        print(game_lines[0])
        print(separator_line)
        print(game_lines[1])
        print(separator_line)
        print(game_lines[2])
        
    def display_game_end(self, winner) -> None:
        if winner:
            print(f"The winner is '{winner}'!")
        else:
            print("It's a tie!")

    




