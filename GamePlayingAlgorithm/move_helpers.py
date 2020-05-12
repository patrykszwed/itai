from Move import Move
from constants import PLAYER_NAMES, EMPTY_FIELD, PIECE_POINTS
from helpers import get_player_name_to_capture, is_correct_coordinates, get_opponent_player


def get_direction_of_x_for_move(move):
    return move.x - move.piece.x


def move_single_piece(board, player, move, is_final_move=False):
    fields = board.fields
    direction_of_x = get_direction_of_x_for_move(move)
    is_capture_possible = is_capture_possible_on_field(move.x, move.y, fields, player, direction_of_x, move.piece)
    if is_capture_possible:
        # print('Capture is possible for player', player.name)
        # move.print()
        # print_board(board)
        capture_move(board, player, move, direction_of_x)
        # print('After capture move')
        # print_board(board)
        # TODO assign score to move!!!!
        move.score = PIECE_POINTS['CAPTURE']
    else:
        # print('Capture is not possible for player', player.name)
        # move.print()
        # print_board(board)
        regular_move(fields, player, move)
        move.score = PIECE_POINTS['MOVE']


def capture_move(board, player, move, direction_of_x):
    fields = board.fields
    opponent_player = get_opponent_player(board, player)
    x, y, piece = move.x, move.y, move.piece

    # clear previous location
    fields[piece.y][piece.x].value = EMPTY_FIELD

    # TODO remove piece from player's pieces
    # TODO operate on field.piece
    # remove opponent's piece
    field_to_clear = fields[y][x]
    # field_to_clear.print()
    field_to_clear.value = EMPTY_FIELD
    opponent_player.remove_piece(field_to_clear.x, field_to_clear.y)

    # piece_to_clear = None
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


def regular_move(fields, player, move):
    x, y, piece = move.x, move.y, move.piece
    fields[piece.y][piece.x].value = EMPTY_FIELD
    fields[y][x].value = player.name
    piece.move_piece(x, y)


def get_all_correct_moves(player, fields, is_capture=False):
    all_correct_moves = []
    for piece in player.pieces:
        correct_moves_for_piece = get_correct_moves_for_piece(piece, fields, player, is_capture)
        all_correct_moves.append(correct_moves_for_piece)
    flatten_all_correct_moves = [all_correct_moves_for_one_piece for sublist in all_correct_moves for
                                 all_correct_moves_for_one_piece in sublist]
    return flatten_all_correct_moves


def get_correct_moves_for_piece(piece, fields, player, is_capture):
    move_direction = 1 if player.name == PLAYER_NAMES['P1'] else -1
    correct_moves = []
    x = piece.x
    y = piece.y - 1 * move_direction
    if is_correct_move(x + 1, y, fields, player, 1, piece, is_capture):
        correct_moves.append(Move(x + 1, y, 0, piece))
    if is_correct_move(x - 1, y, fields, player, -1, piece, is_capture):
        correct_moves.append(Move(x - 1, y, 0, piece))
    return correct_moves


def is_correct_move(x, y, fields, player, direction_of_x, piece, is_capture):
    if not is_correct_coordinates(x, y):
        return False

    if not is_capture and fields[y][x].value == EMPTY_FIELD:
        return True
    return is_capture_possible_on_field(x, y, fields, player, direction_of_x, piece)


def is_capture_possible_on_field(x, y, fields, player, direction_of_x, piece):
    move_direction = 1 if player.name == PLAYER_NAMES['P1'] else -1
    player_name_to_capture = get_player_name_to_capture(player)
    y_new = y - 1 * move_direction
    x_new = x + direction_of_x  # TODO something wrong here
    piece_y = piece.y
    piece_x = piece.x
    # x_new = x
    # fields[y][x].value as we are checking if on that field is an opponent's piece

    if is_correct_coordinates(x_new, y_new) and fields[y][x].value == player_name_to_capture:
        # print('INSIDE IF')
        if fields[y_new][x_new].value == EMPTY_FIELD:
            # print('POSSIBLE XD FOR PLAYER', player.name)
            # print('player_name_to_capture', player_name_to_capture)
            # print('x', x, 'y', y)
            # print('x_new', x_new, 'y_new', y_new)
            # print('piece_x', piece_x, 'piece_y', piece_y)
            # print_board_fields(fields)
            return True
    return False
