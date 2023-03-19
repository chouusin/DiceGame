import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
import io

from main import main


class TestMain(unittest.TestCase):
    test_data = [
        {
            'input': ['1 6 2 5 4 3\n', '4\n', '1\n', '5\n', '4\n', '3\n'],
            'expected_output': '4',
        },
        {
            'input': ['6 5 4 3 2 1\n', '6\n', '6\n', '2\n', '1\n', '3\n', '4\n', '3\n'],
            'expected_output': '8',
        },
    ]

    def test_result(self):
        for data in self.test_data:
            with patch('builtins.input', side_effect=data['input']):
                with io.StringIO() as captured_output:
                    with redirect_stdout(captured_output):
                        main()

                    self.assertEqual(captured_output.getvalue(), data['expected_output'])
