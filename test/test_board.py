from unittest import TestCase
from model.board import Board


class Test(TestCase):
    def test_grid_width(self):
        default_board = Board()
        default_width = default_board.get_width()

        board_100 = Board(100, 4)
        width_100 = board_100.get_width()

        self.assertEqual(default_width, 10)
        self.assertEqual(width_100, 100)

    def test_create_grid_height(self):
        tested_board = Board()
        default_height = tested_board.get_height()

        board_4 = Board(100, 4)
        height_4 = board_4.get_height()

        self.assertEqual(default_height, 10)
        self.assertEqual(height_4, 4, 10)

    def test_board_print(self):
        board = Board(5, 3, ".")
        board.print_board()
        board.fill_board("@")
        board.print_board()
        pass
