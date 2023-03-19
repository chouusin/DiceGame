import unittest

from dicegame.dice import Dice


class TestDice(unittest.TestCase):
    def setUp(self):
        self.dice = Dice([1, 6, 2, 5, 4, 3])

    def test_opposite_value(self):
        opposite_values = [self.dice.get_opposite_value(v) for v in self.dice.values]
        self.assertEqual(opposite_values, [6, 1, 5, 2, 3, 4])

    def test_rotate_distance_opposite_value(self):
        self.assertEqual(self.dice.rotate_distance(1, 6), 2)

    def test_rotate_distance_adjacent_value(self):
        self.assertEqual(self.dice.rotate_distance(1, 4), 1)

    def test_rotate_distance_same_value(self):
        self.assertEqual(self.dice.rotate_distance(1, 1), 0)
