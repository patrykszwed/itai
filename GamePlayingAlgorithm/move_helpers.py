from Move import Move
from constants import PLAYER_NAMES, EMPTY_FIELD, BOARD_END, BOARD_START
from helpers import get_piece_names_to_capture, is_correct_coordinates, get_pieces_for_player_name, \
    get_piece_from_location, is_player_one, is_piece_king, is_empty_field


def move_single_piece(board, player_name, move):
    fields = board.fields

    piece_to_move = get_piece_from_location(board, player_name, move.piece_x, move.piece_y)
    is_capture_possible = is_capture_possible_for_piece(move, fields, player_name, piece_to_move)
    capture_count = 0
    if is_capture_possible:
        while is_capture_possible:
            direction_of_x = get_direction_of_x_for_move(move)
            direction_of_y = get_direction_of_y_for_move(move)
            capture_count += 1

            piece_after_move = capture_move(board, player_name, move, direction_of_x, direction_of_y)
            capture_moves_for_piece = get_correct_capture_moves_for_piece(piece_after_move, fields, player_name)
            is_capture_possible = False
            for capture_move_for_piece in capture_moves_for_piece:
                if is_capture_possible_for_piece(capture_move_for_piece, fields, player_name, piece_after_move):
                    move = capture_move_for_piece
                    is_capture_possible = True
                    break
    else:
        piece_after_move = regular_move(board, player_name, move)
    if is_piece_on_king_position(player_name, piece_after_move):
        piece_after_move.upgrade_rank(board.fields)
    return capture_count


def get_correct_capture_moves_for_piece(piece, fields, player_name):
    if is_piece_king(piece):
        return get_correct_moves_for_king(piece, fields, player_name, True)
    return get_correct_moves_for_piece(piece, fields, player_name, True)


def is_capture_possible_for_piece(move, fields, player_name, piece_to_move):
    direction_of_x = get_direction_of_x_for_move(move)
    direction_of_y = get_direction_of_y_for_move(move)
    if is_piece_king(piece_to_move):
        return is_capture_possible_on_field_for_king(move.piece_x, move.piece_y, move.x, move.y, fields,
                                                     player_name, direction_of_x,
                                                     direction_of_y)
    return is_capture_possible_on_field(move.x, move.y, fields, player_name, direction_of_x,
                                        direction_of_y)


def is_piece_on_king_position(player_name, piece_after_move):
    king_position = BOARD_START if player_name == PLAYER_NAMES['P1'] else BOARD_END
    return piece_after_move.y == king_position


def capture_move(board, player_name, move, direction_of_x, direction_of_y):
    fields = board.fields
    x, y, piece_x, piece_y = move.x, move.y, move.piece_x, move.piece_y

    # clear previous location
    fields[piece_y][piece_x].value = EMPTY_FIELD

    # remove opponent's piece
    field_to_clear = fields[y][x]
    field_to_clear.value = EMPTY_FIELD
    board.remove_piece(field_to_clear.x, field_to_clear.y)

    x, y = get_capture_location(x, y, direction_of_x, direction_of_y)

    # set new piece's location
    piece_from_location = get_piece_from_location(board, player_name, piece_x, piece_y)
    piece_from_location.move_piece(x, y)
    fields[y][x].value = piece_from_location.value

    return piece_from_location


def regular_move(board, player_name, move):
    fields = board.fields
    x, y, piece_x, piece_y = move.x, move.y, move.piece_x, move.piece_y
    fields[piece_y][piece_x].value = EMPTY_FIELD
    piece_from_location = get_piece_from_location(board, player_name, piece_x, piece_y)
    piece_from_location.move_piece(x, y)
    fields[y][x].value = piece_from_location.value

    return piece_from_location


def get_capture_location(x, y, direction_of_x, direction_of_y):
    return x + direction_of_x, y + direction_of_y


def get_all_correct_moves(board, player_name, fields, is_capture=False):
    all_correct_moves = []
    for piece in get_pieces_for_player_name(board, player_name):
        if is_piece_king(piece):
            correct_moves = get_correct_moves_for_king(piece, fields, player_name, is_capture)
        else:
            correct_moves = get_correct_moves_for_piece(piece, fields, player_name, is_capture)
        all_correct_moves.append(correct_moves)
    flatten_all_correct_moves = [all_correct_moves_for_one_piece for sublist in all_correct_moves for
                                 all_correct_moves_for_one_piece in sublist]
    return flatten_all_correct_moves


def get_correct_moves_for_king(piece, fields, player_name, is_capture):
    return get_correct_moves_for_king_for_one_direction(piece, fields, player_name, is_capture,
                                                        1) + get_correct_moves_for_king_for_one_direction(
        piece, fields, player_name, is_capture, -1)


def get_correct_moves_for_king_for_one_direction(piece, fields, player_name, is_capture, direction_of_y):
    correct_moves = []
    piece_x = piece.x
    piece_y = piece.y
    is_correct_move1, is_correct_move2 = True, True
    iterator = 0
    while is_correct_move1 or is_correct_move2:
        x = piece_x + 1 + iterator
        y = piece_y - (1 * direction_of_y) - (iterator * direction_of_y)
        if is_correct_move1:
            correct_move = is_correct_move_for_king(piece_x, piece_y, x, y, fields, player_name, is_capture)
            if correct_move[0]:
                correct_moves.append(Move(x, y, 0, piece.x, piece.y))
                if correct_move[1]:
                    is_correct_move1 = False
            else:
                is_correct_move1 = False
        else:
            is_correct_move1 = False
        x = piece_x - 1 - iterator
        if is_correct_move2:
            correct_move = is_correct_move_for_king(piece_x, piece_y, x, y, fields, player_name, is_capture)
            if correct_move[0]:
                correct_moves.append(Move(x, y, 0, piece.x, piece.y))
                if correct_move[1]:
                    is_correct_move2 = False
            else:
                is_correct_move2 = False
        else:
            is_correct_move2 = False
        iterator += 1
    return correct_moves


def get_correct_moves_for_piece(piece, fields, player_name, is_capture):
    direction_of_y = 1 if is_player_one(player_name) else -1

    correct_moves = []
    x = piece.x
    y = piece.y - 1 * direction_of_y
    if is_correct_move(x + 1, y, fields, player_name, 1, direction_of_y, is_capture):
        correct_moves.append(Move(x + 1, y, 0, piece.x, piece.y))
    if is_correct_move(x - 1, y, fields, player_name, -1, direction_of_y, is_capture):
        correct_moves.append(Move(x - 1, y, 0, piece.x, piece.y))
    # check for possible capture moves back

    direction_of_y = -direction_of_y
    x = piece.x
    y = piece.y - 1 * direction_of_y
    if is_correct_move(x + 1, y, fields, player_name, 1, direction_of_y, True):
        correct_moves.append(Move(x + 1, y, 0, piece.x, piece.y))
    if is_correct_move(x - 1, y, fields, player_name, -1, direction_of_y, True):
        correct_moves.append(Move(x - 1, y, 0, piece.x, piece.y))
    return correct_moves


def is_correct_move(x, y, fields, player_name, direction_of_x, direction_of_y, is_capture):
    if not is_correct_coordinates(x, y):
        return False

    if not is_capture and is_empty_field(x, y, fields):
        return True
    return is_capture_possible_on_field(x, y, fields, player_name, direction_of_x, direction_of_y)


def is_correct_move_for_king(piece_x, piece_y, x, y, fields, player_name, is_capture):
    if not is_correct_coordinates(x, y):
        return False, False
    if not is_capture and is_empty_field(x, y, fields):
        return True, False
    return is_capture_possible_on_field_for_king(piece_x, piece_y, x, y, fields, player_name, None, None), True


def is_capture_possible_on_field_for_king(piece_x, piece_y, x, y, fields, player_name, direction_of_x,
                                          direction_of_y):
    piece_names_to_capture = get_piece_names_to_capture(player_name)
    if direction_of_x is None:
        direction_of_x = get_direction_of_x(x, piece_x)
    if direction_of_y is None:
        direction_of_y = get_direction_of_y(y, piece_y)
    pieces_to_check = abs(piece_x - x) + 1
    for i in range(1, pieces_to_check + 1):
        x_tmp = piece_x + direction_of_x * i
        y_tmp = piece_y + direction_of_y * i
        if is_correct_coordinates(x_tmp, y_tmp):
            if x_tmp == x and y_tmp == y:
                if i < pieces_to_check:
                    continue
                else:
                    return False
            if not is_empty_field(x_tmp, y_tmp, fields):
                return False
        else:
            return False
    return fields[y][x].value in piece_names_to_capture


def is_capture_possible_on_field(x, y, fields, player_name, direction_of_x, direction_of_y):
    piece_names_to_capture = get_piece_names_to_capture(player_name)
    y_new = y - 1 * direction_of_y
    x_new = x + direction_of_x

    if is_correct_coordinates(x_new, y_new) and fields[y][x].value in piece_names_to_capture:
        if is_empty_field(x_new, y_new, fields):
            return True
    return False


def get_direction_of_x_for_move(move):
    return -1 if move.x - move.piece_x < 0 else 1


def get_direction_of_y_for_move(move):
    return -1 if move.y - move.piece_y < 0 else 1


def get_direction_of_x(x, piece_x):
    return -1 if x - piece_x < 0 else 1


def get_direction_of_y(y, piece_y):
    return -1 if y - piece_y < 0 else 1
