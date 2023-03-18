import unittest

from dice import Dice
from game import Game


class TestDice(unittest.TestCase):

    test_data = [
        {
            'dice_values': [1, 6, 2, 5, 4, 3],
            'board_values': [1, 5, 4, 3],
            'expected_output': 4
        },
        {
            'dice_values': [6, 5, 4, 3, 2, 1],
            'board_values': [6, 2, 1, 3, 4, 3],
            'expected_output': 8
        }
    ]

    def test_total_turns(self):
        for data in self.test_data:
            dice = Dice(data['dice_values'])

            game = Game(dice, data['board_values'])
            game.run()

            self.assertEqual(game.total_turns, data['expected_output'])
