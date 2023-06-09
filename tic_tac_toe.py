from typing import Literal, Tuple
import random

class TicTacToeBoard():

    def __init__(self, board=None) -> None:
        if board:
            self.board = board
        else:
            self.create_board()

    def create_board(self) -> None:
        self.board = [[None, None, None], [None, None, None], [None, None, None]]

    def get_board(self) -> None:
        return self.board
    
    def set_symbol(self, row: Literal[0,1,2], col: Literal[0,1,2], 
                   symbol: Literal['O', 'X']) -> None:
        if symbol not in ['O', 'X']:
            raise AttributeError(f"Symbol {symbol} not in ['O', 'X']")
        if self.get_symbol(row, col):
            raise AttributeError(f"Field [{row}, {col}] already set to \
                                {self.get_symbol(row, col)}")
        self.board[row][col] = symbol
    
    def get_symbol(self, row: Literal[0,1,2], col: Literal[0,1,2]) -> Literal['O', 'X', None]:
        return self.board[row][col]
        
class TicTacToeGame():
    players = ['O', 'X']
    
    def __init__(self, first_player:Literal['O', 'X']=None) -> None:
        self.new_game(first_player=first_player)
    
    def new_game(self, first_player:Literal['O', 'X']=None) -> None:
        self.tic_tac_toe_board = TicTacToeBoard()
        self.round = 1
        if first_player:
            if first_player in ['O', 'X']:
                self.first_player = first_player
            else:
                raise AttributeError((f"Player {first_player} not in ['O', 'X']"))
        else: 
            self.first_player = random.sample(['O', 'X'], 1)[0]
        self.current_player = self.first_player
    
    def load_game(self, board:TicTacToeBoard, current_player:Literal['X', 'O']) -> None:
        self.tic_tac_toe_board = board
        self.current_player = current_player

    def get_current_player(self) -> Literal['O', 'X']:
        return self.current_player
    
    def change_player(self) -> None:
        current_player_index = self.players.index(self.current_player)
        self.current_player = self.players[1 - current_player_index]

    def player_move(self, row: Literal[0,1,2], col: Literal[0,1,2]) -> None:
        self.tic_tac_toe_board.set_symbol(row=row, col=col, symbol=self.current_player)

    def check_move(self) -> bool:
        move_exists = False
        board = self.tic_tac_toe_board.get_board()
        for i in range(3):
            move_exists = move_exists or None in board[i]
        return move_exists
            
    def check_winner(self) -> Literal['O', 'X', None]:
        for i in range(3):
            if self.tic_tac_toe_board.get_symbol(i, 0) == \
                    self.tic_tac_toe_board.get_symbol(i, 1) == \
                    self.tic_tac_toe_board.get_symbol(i, 2):
                if self.tic_tac_toe_board.get_symbol(i, 0):
                    return self.tic_tac_toe_board.get_symbol(i, 0)
            if self.tic_tac_toe_board.get_symbol(0, i) == \
                    self.tic_tac_toe_board.get_symbol(1, i) == \
                    self.tic_tac_toe_board.get_symbol(2, i):
                if self.tic_tac_toe_board.get_symbol(0, i):
                    return self.tic_tac_toe_board.get_symbol(0, i)
        if self.tic_tac_toe_board.get_symbol(0, 0) == \
                self.tic_tac_toe_board.get_symbol(1, 1) == \
                self.tic_tac_toe_board.get_symbol(2, 2):
            if self.tic_tac_toe_board.get_symbol(0, 0):
                return self.tic_tac_toe_board.get_symbol(0, 0)
        if self.tic_tac_toe_board.get_symbol(0, 2) == \
                self.tic_tac_toe_board.get_symbol(1, 1) == \
                self.tic_tac_toe_board.get_symbol(2, 0):
            if self.tic_tac_toe_board.get_symbol(0, 2):
                return self.tic_tac_toe_board.get_symbol(0, 2)
        return None
    
    def next_round(self) -> Tuple[bool, str]:
        winner = self.check_winner()
        next_move = self.check_move() if not winner else False
        self.change_player()
        return (next_move, winner)

        