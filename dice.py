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
        self.opposite_value = {
            self.values[k]: self.values[v]
            for k, v in OPPOSITE_FACE_PAIRS
        }

    def get_opposite_value(self, value):
        return self.opposite_value[value]

    def rotate_distance(self, from_value, to_value):
        if to_value == from_value:
            return 0
        elif to_value == self.opposite_value[from_value]:
            return 2
        else:
            return 1
