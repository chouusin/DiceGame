import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
import io

from utils import parse_dice_values, parse_board_values, show_result


class TestUtils(unittest.TestCase):
    def test_parse_dice_values(self):
        with patch('builtins.input', side_effect=['1 6 2 5 4 3\n']):
            dice_values = parse_dice_values()

            self.assertEqual(dice_values, [1, 6, 2, 5, 4, 3])

    def test_parse_board_values(self):
        with patch('builtins.input', side_effect=['4\n', '1\n', '5\n', '4\n', '3\n']):
            board_values = parse_board_values()

            self.assertEqual(board_values, [1, 5, 4, 3])

    def test_show_result(self):
        with io.StringIO() as captured_output:
            with redirect_stdout(captured_output):
                show_result(4)

            self.assertEqual(captured_output.getvalue(), '4')
