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
