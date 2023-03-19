import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
import io

from main import main


class TestMain(unittest.TestCase):
    def test_main1(self):
        input_values = ['1 6 2 5 4 3\n', '4\n', '1\n', '5\n', '4\n', '3\n']
        with patch(
            'builtins.input',
            side_effect=input_values,
        ):
            with io.StringIO() as captured_output:
                with redirect_stdout(captured_output):
                    main()

                self.assertEqual(captured_output.getvalue(), '4')

    def test_main2(self):
        input_values = ['6 5 4 3 2 1\n', '6\n', '6\n', '2\n', '1\n', '3\n', '4\n', '3\n']
        with patch(
            'builtins.input',
            side_effect=input_values,
        ):
            with io.StringIO() as captured_output:
                with redirect_stdout(captured_output):
                    main()

                self.assertEqual(captured_output.getvalue(), '8')
