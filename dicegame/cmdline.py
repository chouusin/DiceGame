from dicegame.utils import parse_dice_values, parse_board_values, show_result
from dicegame.dice import Dice
from dicegame.game import Game


def main():
    dice_values = parse_dice_values()
    dice = Dice(dice_values)

    board_values = parse_board_values()

    game = Game(dice, board_values)
    game.run()

    show_result(game.total_turns)
