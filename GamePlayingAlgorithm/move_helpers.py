from Move import Move
from constants import PLAYER_NAMES, EMPTY_FIELD, BOARD_END, BOARD_START
from helpers import get_player_name_to_capture, print_board_fields


def get_player_to_move(board, prev_player):
    return board.players[1] if prev_player.name == PLAYER_NAMES['P1'] else board.players[0]


def get_direction_of_x_for_move(move):
    return move.x - move.piece.x


def move_single_piece(fields, player, move, is_final_move=False):
    if is_final_move:
        print('move_single_piece for player', player.name, 'move')
        direction_of_x = get_direction_of_x_for_move(move)
        is_capture_possible = is_capture_possible_on_field(move.x, move.y, fields, player, direction_of_x)
        print('move_single_piece - is_capture_possible', is_capture_possible)
        if is_capture_possible:
            capture_move(move, fields, player, direction_of_x)
        else:
            regular_move(move, fields, player, is_final_move)
        # print('AFter move is_capture_possible', is_capture_possible)
        # print_board_fields(fields)
    else:
        # print('move_single_piece for player', player.name, 'move')
        # print_board_fields(fields)
        direction_of_x = get_direction_of_x_for_move(move)
        is_capture_possible = is_capture_possible_on_field(move.x, move.y, fields, player, direction_of_x)
        # print('move_single_piece - is_capture_possible', is_capture_possible)
        if is_capture_possible:
            capture_move(move, fields, player, direction_of_x)
        else:
            regular_move(move, fields, player, is_final_move)
        # print('AFter move is_capture_possible', is_capture_possible)
        # print_board_fields(fields)


def capture_move(move, fields, player, direction_of_x):
    # print('capture_move')
    x, y, piece = move.x, move.y, move.piece

    # clear previous location
    fields[piece.y][piece.x].value = EMPTY_FIELD

    # remove opponent's piece
    fields[y][x].value = EMPTY_FIELD
    capture_location = get_capture_location(x, y, player, direction_of_x)
    # print('capture_location', capture_location)
    x, y = capture_location

    # set new piece's location
    fields[y][x].value = player.name
    piece.move_piece(x, y)


def get_capture_location(x, y, player, direction_of_x):
    move_direction = 1 if player.name == PLAYER_NAMES['P1'] else -1
    y = y - 1 * move_direction
    return x + direction_of_x, y


def regular_move(move, fields, player, is_final_move):
    if is_final_move:
        print('before regular_move')
        print_board_fields(fields)
        x, y, piece = move.x, move.y, move.piece
        fields[piece.y][piece.x].value = EMPTY_FIELD
        fields[y][x].value = player.name
        piece.move_piece(x, y)
        print('after regular_move')
        print_board_fields(fields)
    else:
        # print('before regular_move')
        # print_board_fields(fields)
        x, y, piece = move.x, move.y, move.piece
        fields[piece.y][piece.x].value = EMPTY_FIELD
        fields[y][x].value = player.name
        piece.move_piece(x, y)
        # print('after regular_move')
        # print_board_fields(fields)


def get_all_correct_moves(player, fields):
    # print('get_all_correct_moves for player ', player.name)
    # print_board_fields(fields)
    all_correct_moves = []
    for piece in player.pieces:
        correct_moves_for_piece = get_correct_moves_for_piece(piece, fields, player)
        all_correct_moves.append(correct_moves_for_piece)
    # print('all_correct_moves', all_correct_moves)
    flatten_all_correct_moves = [all_correct_moves_for_one_piece for sublist in all_correct_moves for
                                 all_correct_moves_for_one_piece in sublist]
    # print('player.name:', player.name, 'flatten_all_correct_moves:', flatten_all_correct_moves)
    return flatten_all_correct_moves


def get_correct_moves_for_piece(piece, fields, player):
    move_direction = 1 if player.name == PLAYER_NAMES['P1'] else -1
    correct_moves = []
    x = piece.x
    y = piece.y - 1 * move_direction
    if is_correct_move(x + 1, y, fields, player, 1):
        correct_moves.append(Move(x + 1, y, 0, piece))
    if is_correct_move(x - 1, y, fields, player, -1):
        correct_moves.append(Move(x - 1, y, 0, piece))
    return correct_moves


def is_correct_move(x, y, fields, player, direction_of_x):
    # print('len(fields)', len(fields))
    if not is_correct_location(x) or not is_correct_location(y):
        return False

    # print('x', x, 'y', y)
    # print('fields[y][x].value', fields[y][x].value)
    if fields[y][x].value == EMPTY_FIELD:
        return True
    # print('is_capture_possible_on_field', is_capture_possible_on_field(x, y, fields, player))
    is_capture_possible = is_capture_possible_on_field(x, y, fields, player, direction_of_x)
    return is_capture_possible


def is_capture_possible_on_field(x, y, fields, player, direction_of_x):
    move_direction = 1 if player.name == PLAYER_NAMES['P1'] else -1
    player_name_to_capture = get_player_name_to_capture(player)
    y_new = y - 1 * move_direction
    x_new = x + direction_of_x
    # fields[y][x].value as we are checking if on that field is an opponent's piece
    if is_correct_coordinates(x_new, y_new) and fields[y][x].value == player_name_to_capture:
        if fields[y_new][x_new].value == EMPTY_FIELD:
            return True
    return False


def is_correct_coordinates(x, y):
    return is_correct_location(x) and is_correct_location(y)


def is_correct_location(location):
    return BOARD_START <= location <= BOARD_END
