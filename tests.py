import unittest
import tic_tac_toe as ttt

class TestTicTacToe(unittest.TestCase):

    def test_empty_board(self):
        ttt_board = ttt.TicTacToeBoard()
        board = ttt_board.get_board()
        for i in range(3):
            for j in range(3):
                self.assertIsNone(board[i][j])

    def test_set_symbol(self):
        ttt_board = ttt.TicTacToeBoard()
        ttt_board.set_symbol(row=1, col=2, symbol='O')
        ttt_board.set_symbol(row=2, col=1, symbol='X')
        expected_board = [[None, None, None], [None, None, 'O'], [None, 'X', None]]
        self.assertEqual(expected_board, ttt_board.get_board())
    
    def test_set_symbol_wrong_symbol(self):
        ttt_board = ttt.TicTacToeBoard()
        with self.assertRaises(AttributeError):
            ttt_board.set_symbol(row=1, col=2, symbol='0')
        
    def test_set_symbol_out_of_range(self):
        ttt_board = ttt.TicTacToeBoard()
        with self.assertRaises(IndexError):
            ttt_board.set_symbol(row=1, col=3, symbol='O')

    def test_set_symbol_existing_symbol(self):
        ttt_board = ttt.TicTacToeBoard()
        ttt_board.set_symbol(row=1, col=2, symbol='O')
        with self.assertRaises(AttributeError):
            ttt_board.set_symbol(row=1, col=2, symbol='X')
        
    def test_first_player(self):
        ttt_game = ttt.TicTacToeGame()
        current_player = ttt_game.get_current_player()
        self.assertTrue(current_player in ['O', 'X'])
    
    def test_player_change(self):
        ttt_game = ttt.TicTacToeGame()
        current_player = ttt_game.get_current_player()
        players = ['O', 'X']
        players.pop(players.index(current_player))
        ttt_game.change_player()
        current_player = ttt_game.get_current_player()
        self.assertEqual(players[0], current_player)

    def test_check_winner_row(self):
        ttt_game = ttt.TicTacToeGame()
        current_player = ttt_game.get_current_player()
        for i in range(3):
            ttt_game.player_move(row=0, col=i)
        self.assertEqual(current_player, ttt_game.check_winner())

    def test_check_winner_column(self):
        ttt_game = ttt.TicTacToeGame()
        current_player = ttt_game.get_current_player()
        for i in range(3):
            ttt_game.player_move(row=i, col=1)
        self.assertEqual(current_player, ttt_game.check_winner())

    def test_check_winner_axis_1(self):
        ttt_game = ttt.TicTacToeGame()
        current_player = ttt_game.get_current_player()
        for i in range(3):
            ttt_game.player_move(row=i, col=i)
        self.assertEqual(current_player, ttt_game.check_winner())

    def test_check_winner_axis_2(self):
        ttt_game = ttt.TicTacToeGame()
        current_player = ttt_game.get_current_player()
        for i in range(3):
            ttt_game.player_move(row=2-i, col=i)
        self.assertEqual(current_player, ttt_game.check_winner())
    
    def test_check_winner_no_winner(self):
        ttt_game = ttt.TicTacToeGame()
        self.assertIsNone(ttt_game.check_winner())

    def tect_check_move_exist(self):
        ttt_game = ttt.TicTacToeGame()
        self.assertTrue(ttt_game.check_move())

    def test_check_no_move_exist(self):
        ttt_game = ttt.TicTacToeGame()
        for i in range(3):
            for j in range(3):
                ttt_game.player_move(i, j)
        self.assertFalse(ttt_game.check_move())

    def test_next_round_winner(self):
        ttt_game = ttt.TicTacToeGame()
        current_player = ttt_game.get_current_player()
        for i in range(3):
            ttt_game.player_move(row=2-i, col=i)
        next_move, winner = ttt_game.next_round()
        self.assertEqual([False, current_player], [next_move, winner])

    def test_next_round_no_winner(self):
        ttt_game = ttt.TicTacToeGame()
        next_move, winner = ttt_game.next_round()
        self.assertEqual([True, None], [next_move, winner])

    def test_next_round_tie(self):
        ttt_game = ttt.TicTacToeGame()
        ttt_game.player_move(row=0, col=0)
        ttt_game.player_move(row=0, col=1)
        ttt_game.player_move(row=1, col=2)
        ttt_game.player_move(row=2, col=0)
        ttt_game.player_move(row=2, col=2)
        ttt_game.change_player()
        ttt_game.player_move(row=0, col=2)
        ttt_game.player_move(row=1, col=0)
        ttt_game.player_move(row=1, col=1)
        ttt_game.player_move(row=2, col=1)
        next_move, winner = ttt_game.next_round()
        self.assertEqual([False, None], [next_move, winner])

if __name__ == '__main__':
    unittest.main()