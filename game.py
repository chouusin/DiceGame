def parse_dice_values():
    dice_input = input()
    dice_values = [int(num) for num in dice_input.split()]
    return dice_values

def parse_board_values():
    board_count = int(input())
    board_values = [int(input()) for _ in range(board_count)]
    return board_values

if __name__ == '__main__':
    dice_values = parse_dice_values()
    board_values = parse_board_values()
