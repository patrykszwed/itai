from constants import PLAYER_NAMES, EMPTY_FIELD, BOARD_END, BOARD_START
from helpers import print_board


def get_capture_points(board, player_move):
    print('board.fields', board.fields)
    for row_fields in board.fields:
        print('row_fields', row_fields)
        fields_to_check = get_fields_to_check(board, row_fields)
        print_board(board)
        print('fields_to_check', fields_to_check)
        # TODO is_capture possible????
    return 0


def get_fields_to_check(board, fields):
    fields_to_check = []
    for field in fields:
        x, y = field.x, field.y
        fields_to_check.append(get_fields_from_upper_rows(board, x, y))
    return fields_to_check


def get_fields_from_upper_rows(board, x, y):
    fields = []
    for i in range(5):
        y += 1
        fields.append(get_fields_from_single_row(board, x, y))
    return fields


def get_fields_from_single_row(board, x, y):
    fields = []
    if not is_correct_location(y):
        return fields
    x -= 2
    for i in range(5):
        if is_correct_location(x):
            fields.append(board.fields[y][x])
        x += 1
    return fields


def get_correct_moves_for_piece(piece, fields, player_name):
    move_direction = 1 if player_name == PLAYER_NAMES['P1'] else -1
    correct_moves = []
    x = piece.x
    y = piece.y - 1 * move_direction
    if is_correct_move(x + 1, y, fields):
        correct_moves.append([x + 1, y, piece])
    if is_correct_move(x - 1, y, fields):
        correct_moves.append([x - 1, y, piece])
    return correct_moves


def is_correct_move(x, y, fields):
    # print('len(fields)', len(fields))
    if not is_correct_location(x) or not is_correct_location(y):
        return False
    # print_board_fields(fields)
    # print('x', x, 'y', y)
    # print('fields[y][x].value', fields[y][x].value)
    return fields[y][x].value == EMPTY_FIELD


def is_correct_location(location):
    return BOARD_START <= location <= BOARD_END


def get_pieces_count_points(board):
    flatten_fields_values = [field.value for sublist in board.fields for field in sublist]
    player1_pieces = sum(value == PLAYER_NAMES['P1'] for value in flatten_fields_values)
    player2_pieces = sum(value == PLAYER_NAMES['P2'] for value in flatten_fields_values)
    return player1_pieces - player2_pieces
