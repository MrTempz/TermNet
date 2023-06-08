import unittest
import tic_tac_toe as ttt

class TestTicTacToe(unittest.TestCase):

    def test_new_game(self):
        ticTacToe = ttt.TicTacToe()
        board = ticTacToe.get_board()
        for i in range(3):
            for j in range(3):
                self.assertIsNone(board[i][j])
        
    def test_first_player(self):
        ticTacToe = ttt.TicTacToe()
        current_player = ticTacToe.get_current_player()
        self.assertTrue(current_player in ['O', 'X'])
    
    def test_player_change(self):
        ticTacToe = ttt.TicTacToe()
        current_player = ticTacToe.get_current_player()
        players = ['O', 'X']
        players.pop(players.index(current_player))
        ticTacToe.change_player()
        current_player = ticTacToe.get_current_player()
        self.assertEqual(players[0], current_player)

    def test_set_symbol(self):
        ticTacToe = ttt.TicTacToe()
        ticTacToe.set_symbol(x=1, y=2, symbol='O')
        ticTacToe.set_symbol(x=2, y=1, symbol='X')
        expected_board = [[None, None, None], [None, None, 'O'], [None, 'X', None]]
        self.assertEqual(expected_board, ticTacToe.get_board())
    
    def test_set_symbol_wrong_symbol(self):
        ticTacToe = ttt.TicTacToe()
        with self.assertRaises(AttributeError):
            ticTacToe.set_symbol(x=1, y=2, symbol='0')
        
    def test_set_symbol_out_of_range(self):
        ticTacToe = ttt.TicTacToe()
        with self.assertRaises(IndexError):
            ticTacToe.set_symbol(x=1, y=3, symbol='O')

    def test_set_symbol_existing_symbol(self):
        ticTacToe = ttt.TicTacToe()
        ticTacToe.set_symbol(x=1, y=2, symbol='O')
        with self.assertRaises(AttributeError):
            ticTacToe.set_symbol(x=1, y=2, symbol='X')


    def test_winner_row(self):
        ticTacToe = ttt.TicTacToe()
        for i in range(3):
            ticTacToe.set_symbol(x=0, y=i, symbol='O')
        self.assertEqual('O', ticTacToe.check_winner())

    def test_winner_column(self):
        ticTacToe = ttt.TicTacToe()
        for i in range(3):
            ticTacToe.set_symbol(x=i, y=1, symbol='X')
        self.assertEqual('X', ticTacToe.check_winner())

    def test_winner_axis_1(self):
        ticTacToe = ttt.TicTacToe()
        for i in range(3):
            ticTacToe.set_symbol(x=i, y=i, symbol='O')
        self.assertEqual('O', ticTacToe.check_winner())

    def test_winner_axis_2(self):
        ticTacToe = ttt.TicTacToe()
        for i in range(3):
            ticTacToe.set_symbol(x=2-i, y=i, symbol='X')
        self.assertEqual('X', ticTacToe.check_winner())
    
if __name__ == '__main__':
    unittest.main()