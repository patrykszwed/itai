from constants import PLAYER_NAMES, EMPTY_FIELD, BOARD_END, BOARD_START, PIECE_POINTS
from helpers import get_player_name_to_capture


def get_capture_points(board, player):
    capture_points = 0
    capture_points_coefficient = 1 if player.name == PLAYER_NAMES['P1'] else -1
    for row_fields in board.fields:
        fields_to_check = get_fields_to_check(board, row_fields)
        if is_capture_possible(fields_to_check, player):
            # print('Capture possible for P1')
            # print_board(board)
            capture_points += PIECE_POINTS['CAPTURE']
        # elif is_capture_possible(fields_to_check, board.players[1]):
        #     print('Capture possible for P2')
        #     print_board(board)
        #     capture_points -= PIECE_POINTS['CAPTURE']
    return capture_points * capture_points_coefficient


def is_capture_possible(fields, player):
    player_name_to_capture = get_player_name_to_capture(player)
    # print('fields', fields)
    for row_fields in fields:
        # print('row_fields', row_fields)
        for fields_to_check_for_one_field in row_fields:
            for field in fields_to_check_for_one_field:
                # print('field', field)
                if field.value == player_name_to_capture:
                    return True
    return False


def get_fields_to_check(board, fields):
    fields_to_check = []
    # print('fields', fields)
    for field in fields:
        x, y = field.x, field.y
        fields_to_check_for_one_field = get_fields_to_check_for_one_field(board, x, y)
        if len(fields_to_check_for_one_field) > 0:
            fields_to_check.append(fields_to_check_for_one_field)
    return fields_to_check


def get_fields_to_check_for_one_field(board, x, y):
    fields = []
    x -= 1
    y -= 1
    for i in range(3):
        fields_from_single_column = get_fields_from_single_column(board, x, y)
        if len(fields_from_single_column) > 0:
            fields.append(fields_from_single_column)
        x += 1
    return fields


def get_fields_from_single_column(board, x, y):
    # print('get_fields_from_single_column x, y', x, y)
    fields = []
    # print('is_correct_field(x, y)', is_correct_field(x, y))
    if not is_correct_field(x, y):
        return fields
    for i in range(3):
        if is_correct_location(y):
            fields.append(board.fields[y][x])
        y += 1
    return fields


def is_correct_field(x, y):
    return is_correct_location(y) and is_correct_location(x)


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
