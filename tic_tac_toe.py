from typing import Literal
import random

class TicTacToe():
    players = ['O', 'X']

    def __init__(self):
        self.create_board()
        self.first_player = random.sample(['O', 'X'], 1)[0]
        self.current_player = self.first_player

    def create_board(self) -> None:
        self.board = [[None, None, None], [None, None, None], [None, None, None]]

    def get_current_player(self) -> Literal['O', 'X']:
        return self.current_player
    
    def change_player(self):
        current_player_index = self.players.index(self.current_player)
        self.current_player = self.players[1 - current_player_index]

    def get_board(self) -> None:
        return self.board
    
    def set_symbol(self, x: Literal[0,1,2], y: Literal[0,1,2], 
                   symbol: Literal['O', 'X']) -> None:
        if symbol not in ['O', 'X']:
            raise AttributeError(f"Symbol {symbol} not in ['O', 'X']")
        if self.get_symbol(x, y):
            raise AttributeError(f"Field [{x}, {y}] already set to \
                                {self.get_symbol(x, y)}")
        self.board[x][y] = symbol
    
    def get_symbol(self, x: Literal[0,1,2], y: Literal[0,1,2]) -> Literal['O', 'X', None]:
        return self.board[x][y]
    
    def check_winner(self) -> Literal['O', 'X', None]:
        for i in range(3):
            if self.get_symbol(i, 0) == self.get_symbol(i, 1) == self.get_symbol(i, 2):
                if self.get_symbol(i, 0):
                    return self.get_symbol(i, 0)
            if self.get_symbol(0, i) == self.get_symbol(1, i) == self.get_symbol(2, i):
                if self.get_symbol(0, i):
                    return self.get_symbol(0, i)
        if self.get_symbol(0, 0) == self.get_symbol(1, 1) == self.get_symbol(2, 2):
            if self.get_symbol(0, 0):
                return self.get_symbol(0, 0)
        if self.get_symbol(0, 2) == self.get_symbol(1, 1) == self.get_symbol(2, 0):
            if self.get_symbol(0, 2):
                return self.get_symbol(0, 2)
        