import unittest
from solution import Piece
from solution import Board
import io
import sys


class Test(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_add_piece(self):
        piece = Piece("P", "white", (1, 1))
        self.board.add(piece)
        self.assertTrue((1, 1) in self.board.position)
        king_black = self.board.find_piece((10, 10))
        self.assertTrue(king_black.color == Board.black)

    def test_invalid_addpiece(self):
        self.board.clear_board()
        statement = self.board.add(Piece(Board.king, Board.white, (1, 3)))
        self.assertIs(statement, None)
