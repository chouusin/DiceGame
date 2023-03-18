import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
import io

from utils import parse_dice_values, parse_board_values, show_result


class TestGame(unittest.TestCase):

    dice_test_data = {
        'input': ['1 6 2 5 4 3\n'],
        'expected_output': [1, 6, 2, 5, 4, 3],
    }

    board_test_data = {
        'input': ['4\n', '1\n', '5\n', '4\n', '3\n'],
        'expected_output': [1, 5, 4, 3],
    }

    result_test_data = {
        'input': 4,
        'expected_output': '4',
    }

    def test_parse_dice_value(self):
        with patch('builtins.input', side_effect=self.dice_test_data['input']):
            dice_values = parse_dice_values()
            self.assertEqual(dice_values, self.dice_test_data['expected_output'])

    def test_parse_board_values(self):
        with patch('builtins.input', side_effect=self.board_test_data['input']):
            board_values = parse_board_values()
            self.assertEqual(board_values, self.board_test_data['expected_output'])

    def test_show_result(self):
        with io.StringIO() as captured_output:
            with redirect_stdout(captured_output):
                show_result(self.result_test_data['input'])

            self.assertEqual(captured_output.getvalue(), self.result_test_data['expected_output'])
