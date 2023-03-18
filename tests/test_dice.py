import unittest

from dice import Dice

class TestDice(unittest.TestCase):

    test_data = {
        'input': [1, 6, 2, 5, 4, 3],
        'expected_output': [6, 1, 5, 2, 3, 4],
    }

    rotate_distance_test_data = [
        {
            'input': (1, 6),
            'expected_output': 2
        },
        {
            'input': (1, 4),
            'expected_output': 1
        },
        {
            'input': (1, 1),
            'expected_output': 0
        },
    ]

    def setUp(self):
        self.dice = Dice(self.test_data['input'])

    def test_opposite_value(self):
        opposite_values = [self.dice.get_opposite_value(v) for v in self.test_data['input']]
        self.assertEqual(opposite_values, self.test_data['expected_output'])

    def test_rotate_distance(self):
        for data in self.rotate_distance_test_data:
            self.assertEqual(self.dice.rotate_distance(data['input'][0], data['input'][1]), data['expected_output'])
