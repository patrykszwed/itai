from Move import Move
from constants import PLAYER_NAMES, EMPTY_FIELD
from helpers import get_player_name_to_capture, is_correct_coordinates, get_pieces_for_player_name, \
    get_piece_from_location


def get_direction_of_x_for_move(move):
    return move.x - move.piece_x


def get_direction_of_y_for_move(move):
    return move.y - move.piece_y


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
        # if is_final_move:
        #     print('Capture is possible for player', player_name)
        #     move.print()
        #     print('Before capture move for player', player_name)
        #     print_board(board)
        capture_move(board, player_name, move, direction_of_x, direction_of_y, is_final_move)
        # if is_final_move:
        #     print('After capture move for player', player_name)
        #     print_board(board)
        #     print()
        # TODO assign score to move!!!!
    else:
        # move.score = PIECE_POINTS['MOVE']
        # print('Capture is not possible for player', player.name)
        # move.print()
        # print_board(board)
        regular_move(board, player_name, move)
    # if is_from_minimax:
    #     print('move_single_piece AFTER MINIMAX FOR PLAYER', player_name)
    #     print_board(board)


def capture_move(board, player_name, move, direction_of_x, direction_of_y, is_final_move=False):
    # print('Before capture_move for player', player_name)
    # print_board(board)
    fields = board.fields
    x, y, piece_x, piece_y = move.x, move.y, move.piece_x, move.piece_y

    # clear previous location
    fields[piece_y][piece_x].value = EMPTY_FIELD

    # remove opponent's piece
    field_to_clear = fields[y][x]
    # field_to_clear.print()
    field_to_clear.value = EMPTY_FIELD
    # print('BEFORE REMOVING')
    # print('field_to_clear.x, field_to_clear.y', field_to_clear.x, field_to_clear.y)
    # [p.print() for p in get_pieces_for_player_name(board, get_player_name_to_capture(player_name))]
    # print('len(get_pieces_for_player_name(board, get_player_name_to_capture(player_name)))',
    #       len(get_pieces_for_player_name(board, get_player_name_to_capture(player_name))))
    board.remove_piece(field_to_clear.x, field_to_clear.y)
    # print('AFTER REMOVING')
    # print('field_to_clear.x, field_to_clear.y', field_to_clear.x, field_to_clear.y)
    # [p.print() for p in get_pieces_for_player_name(board, get_player_name_to_capture(player_name))]
    # print('len(get_pieces_for_player_name(board, get_player_name_to_capture(player_name)))',
    #       len(get_pieces_for_player_name(board, get_player_name_to_capture(player_name))))

    # piece_to_clear = None
    capture_location = get_capture_location(x, y, player_name, direction_of_x, direction_of_y, is_final_move)
    # if is_final_move:
    #     print('Final capture_location', capture_location)
    # print('capture_location', capture_location)
    x, y = capture_location

    # set new piece's location
    fields[y][x].value = player_name
    piece_from_location = get_piece_from_location(board, player_name, piece_x, piece_y)
    piece_from_location.move_piece(x, y)

    # [p.print() for p in get_pieces_for_player_name(board, player_name)]
    # print('len(get_pieces_for_player_name(board, player_name))',
    #       len(get_pieces_for_player_name(board, player_name)))
    # print('After capture_move')
    # print_board(board)
    # [p.print() for p in get_pieces_for_player_name(board, get_player_name_to_capture(player_name))]
    # print('len(get_pieces_for_player_name(board, get_player_name_to_capture(player_name)))',
    #       len(get_pieces_for_player_name(board, get_player_name_to_capture(player_name))))
    # print()


def get_capture_location(x, y, player_name, direction_of_x, direction_of_y, is_final_move):
    move_direction = 1 if player_name == PLAYER_NAMES['P1'] else -1
    # if is_final_move:
    #     print('y + direction_of_y', y + direction_of_y)
    #     print('y - 1 * move_direction', y - 1 * move_direction)
    # y = y - 1 * move_direction
    return x + direction_of_x, y + direction_of_y


def regular_move(board, player_name, move):
    fields = board.fields
    x, y, piece_x, piece_y = move.x, move.y, move.piece_x, move.piece_y
    fields[piece_y][piece_x].value = EMPTY_FIELD
    fields[y][x].value = player_name

    piece_from_location = get_piece_from_location(board, player_name, piece_x, piece_y)
    piece_from_location.move_piece(x, y)


def get_all_correct_moves(board, player_name, fields, is_capture=False):
    all_correct_moves = []
    # print('get_pieces_for_player_name(board, player_name)', len(get_pieces_for_player_name(board, player_name)))
    for piece in get_pieces_for_player_name(board, player_name):
        correct_moves_for_piece = get_correct_moves_for_piece(piece, fields, player_name, is_capture)
        all_correct_moves.append(correct_moves_for_piece)
    flatten_all_correct_moves = [all_correct_moves_for_one_piece for sublist in all_correct_moves for
                                 all_correct_moves_for_one_piece in sublist]
    return flatten_all_correct_moves


def get_correct_moves_for_piece(piece, fields, player_name, is_capture):
    direction_of_y_old = 1 if player_name == PLAYER_NAMES['P1'] else -1
    direction_of_y = 1 if player_name == PLAYER_NAMES['P1'] else -1
    # print('IN get_correct_moves_for_piece')
    # print('direction_of_y', direction_of_y)
    # print('direction_of_y_old', direction_of_y_old)
    correct_moves = []
    x = piece.x
    y = piece.y - 1 * direction_of_y
    if is_correct_move(x + 1, y, fields, player_name, 1, direction_of_y, is_capture):
        correct_moves.append(Move(x + 1, y, 0, piece.x, piece.y))
    if is_correct_move(x - 1, y, fields, player_name, -1, direction_of_y, is_capture):
        correct_moves.append(Move(x - 1, y, 0, piece.x, piece.y))
    # check for possible capture moves back
    # print('direction_of_y', direction_of_y)
    # print('-direction_of_y', -direction_of_y)
    direction_of_y = -direction_of_y
    # print('IN get_correct_moves_for_piece')
    # print('direction_of_y', direction_of_y)
    # print('direction_of_y_old', direction_of_y_old)
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


def is_capture_possible_on_field(x, y, fields, player_name, direction_of_x, direction_of_y):
    direction_of_y_old = 1 if player_name == PLAYER_NAMES['P1'] else -1
    # print('IN is_capture_possible_on_field')
    # print('direction_of_y', direction_of_y)
    # print('direction_of_y_old', direction_of_y_old)
    player_name_to_capture = get_player_name_to_capture(player_name)
    y_new = y - 1 * direction_of_y
    x_new = x + direction_of_x
    # fields[y][x].value as we are checking if on that field is an opponent's piece

    if is_correct_coordinates(x_new, y_new) and fields[y][x].value == player_name_to_capture:
        if fields[y_new][x_new].value == EMPTY_FIELD:
            return True
    return False
