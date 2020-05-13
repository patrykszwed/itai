from Move import Move
from constants import PLAYER_NAMES, EMPTY_FIELD, BOARD_END, BOARD_START
from helpers import get_piece_names_to_capture, is_correct_coordinates, get_pieces_for_player_name, \
    get_piece_from_location, is_player_one, print_board, is_piece_king, print_board_fields


def move_single_piece(board, player_name, move, is_final_move=False, is_from_minimax=False):
    # if is_from_minimax:
    #     print('move_single_piece FROM MINIMAX FOR PLAYER', player_name)
    #     print_board(board)
    fields = board.fields
    direction_of_x = get_direction_of_x_for_move(move)
    # print('IN move_single_piece')
    direction_of_y = get_direction_of_y_for_move(move)
    # print('BEFOREEE')
    is_capture_possible = is_capture_possible_on_field(move.x, move.y, fields, player_name, direction_of_x,
                                                       direction_of_y)
    # print('Before move_single_piece')
    # [p.print() for p in player.pieces]
    # print_board(board)
    if is_capture_possible:
        if is_final_move:
            print('Capture is possible for player', player_name)
            move.print()
            print('Before capture move for player', player_name)
            print_board(board)
        piece_after_move = capture_move(board, player_name, move, direction_of_x, direction_of_y, is_final_move)
        if is_final_move:
            print('After capture move for player', player_name)
            print_board(board)
            print()
    else:
        piece_after_move = regular_move(board, player_name, move)
    # print('before is_piece_on_king_position for player_name', player_name)
    # move.print()
    if is_piece_on_king_position(player_name, piece_after_move):
        # print('move.y', move.y)
        # print('Player ', player_name, ' has a piece is on king position!')
        # print_board(board)
        piece_after_move.upgrade_rank(board.fields)
        # print('After upgrading piece')
        # print_board(board)
        # print()
    # if is_from_minimax:
    #     print('move_single_piece AFTER MINIMAX FOR PLAYER', player_name)
    #     print_board(board)


def is_piece_on_king_position(player_name, piece_after_move):
    king_position = BOARD_START if player_name == PLAYER_NAMES['P1'] else BOARD_END
    # print('is_piece_on_king_position ', player_name, 'y', piece_after_move.y, 'king_position', king_position)
    return piece_after_move.y == king_position


def capture_move(board, player_name, move, direction_of_x, direction_of_y, is_final_move=False):
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
    fields[y][x].value = player_name
    piece_from_location = get_piece_from_location(board, player_name, piece_x, piece_y)
    piece_from_location.move_piece(x, y)

    return piece_from_location


def regular_move(board, player_name, move):
    fields = board.fields
    x, y, piece_x, piece_y = move.x, move.y, move.piece_x, move.piece_y
    fields[piece_y][piece_x].value = EMPTY_FIELD
    fields[y][x].value = player_name

    piece_from_location = get_piece_from_location(board, player_name, piece_x, piece_y)
    piece_from_location.move_piece(x, y)
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
    # print('get_correct_moves_for_king for player', player_name)
    # piece.print()
    correct_moves = get_correct_moves_for_king_for_one_direction(piece, fields, player_name, is_capture,
                                                                 1) + get_correct_moves_for_king_for_one_direction(
        piece, fields, player_name, is_capture, -1)
    print('Correct moves for King for player', player_name)
    [m.print() for m in correct_moves]
    print('And board state')
    print_board_fields(fields)
    return correct_moves


def get_correct_moves_for_king_for_one_direction(piece, fields, player_name, is_capture, direction_of_y):
    correct_moves = []
    piece_x = piece.x
    piece_y = piece.y
    is_correct_move1, is_correct_move2 = True, True
    iterator = 0
    while is_correct_move1 or is_correct_move2:
        x = piece_x + 1 + iterator
        y = piece_y - (1 * direction_of_y) - (iterator * direction_of_y)
        if is_correct_move1 and is_correct_move_for_king(piece_x, piece_y, x, y, fields, player_name, 1, 1, is_capture):
            correct_moves.append(Move(x, y, 0, piece.x, piece.y))
        else:
            is_correct_move1 = False
        x = piece_x - 1 - iterator
        if is_correct_move2 and is_correct_move_for_king(piece_x, piece_y, x, y, fields, player_name, -1, 1,
                                                         is_capture):
            correct_moves.append(Move(x, y, 0, piece.x, piece.y))
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

    if not is_capture and fields[y][x].value == EMPTY_FIELD:
        return True
    return is_capture_possible_on_field(x, y, fields, player_name, direction_of_x, direction_of_y)


def is_correct_move_for_king(piece_x, piece_y, x, y, fields, player_name, direction_of_x, direction_of_y, is_capture):
    if not is_correct_coordinates(x, y):
        return False

    if not is_capture and is_correct_empty_field_for_king(piece_x, piece_y, x, y, fields, direction_of_x,
                                                          direction_of_y):
        return True
    return is_capture_possible_on_field(x, y, fields, player_name, direction_of_x, direction_of_y)


def is_correct_empty_field_for_king(piece_x, piece_y, x, y, fields, direction_of_x, direction_of_y):
    print('is_correct_empty_field_for_king x', x, 'y', y, 'piece_x', piece_x, 'piece_y', piece_y, )
    print_board_fields(fields)
    y_new = y + 1 * direction_of_y
    x_new = x - direction_of_x
    if not is_correct_coordinates(x_new, y_new):
        return False
    print('fields[y_new][x_new].value', fields[y_new][x_new].value)
    return (x_new == piece_x and y_new == piece_y and fields[y][x].value == EMPTY_FIELD) or fields[y_new][
        x_new].value == EMPTY_FIELD


def is_capture_possible_on_field(x, y, fields, player_name, direction_of_x, direction_of_y):
    piece_names_to_capture = get_piece_names_to_capture(player_name)
    y_new = y - 1 * direction_of_y
    x_new = x + direction_of_x
    # fields[y][x].value as we are checking if on that field is an opponent's piece

    if is_correct_coordinates(x_new, y_new) and fields[y][x].value in piece_names_to_capture:
        if fields[y_new][x_new].value == EMPTY_FIELD:
            return True
    return False


def get_direction_of_x_for_move(move):
    return move.x - move.piece_x


def get_direction_of_y_for_move(move):
    return move.y - move.piece_y
