import unittest

from dicegame.dice import Dice
from dicegame.game import Game


class TestGame(unittest.TestCase):
    def test_total_turns1(self):
        dice = Dice([1, 6, 2, 5, 4, 3])

        game = Game(dice, [1, 5, 4, 3])
        game.run()

        self.assertEqual(game.total_turns, 4)

    def test_total_turns2(self):
        dice = Dice([6, 5, 4, 3, 2, 1])

        game = Game(dice, [6, 2, 1, 3, 4, 3])
        game.run()

        self.assertEqual(game.total_turns, 8)
