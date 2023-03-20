from enum import IntEnum


class Face(IntEnum):
    TOP = 0
    BOTTOM = 1
    UP = 2
    DOWN = 3
    LEFT = 4
    RIGHT = 5


OPPOSITE_FACE_PAIRS = (
    (Face.TOP, Face.BOTTOM),
    (Face.BOTTOM, Face.TOP),
    (Face.UP, Face.DOWN),
    (Face.DOWN, Face.UP),
    (Face.LEFT, Face.RIGHT),
    (Face.RIGHT, Face.LEFT),
)


class Dice:
    def __init__(self, values):
        self.values = values
        self.opposite_value = {self.values[k]: self.values[v] for k, v in OPPOSITE_FACE_PAIRS}

    def get_opposite_value(self, value):
        return self.opposite_value[value]

    def rotate_distance(self, from_value, to_value):
        if to_value == from_value:
            return 0
        elif to_value == self.opposite_value[from_value]:
            return 2
        else:
            return 1


class Game:
    def __init__(self, dice, board_values):
        self.dice = dice
        self.board_values = board_values

        self.dice_value = self.board_values[0]
        self.total_turns = 0

    def run(self):
        for board_value in self.board_values:
            turns = self.dice.rotate_distance(self.dice_value, board_value)
            self.total_turns += turns
            self.dice_value = board_value


def parse_dice_values():
    dice_input = input()
    dice_values = [int(num) for num in dice_input.split()]
    return dice_values


def parse_board_values():
    board_count = int(input())
    board_values = [int(input()) for _ in range(board_count)]
    return board_values


def show_result(turns):
    print(turns, end='')


def main():
    dice_values = parse_dice_values()
    dice = Dice(dice_values)

    board_values = parse_board_values()

    game = Game(dice, board_values)
    game.run()

    show_result(game.total_turns)


if __name__ == '__main__':
    main()
