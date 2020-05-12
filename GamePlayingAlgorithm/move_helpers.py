from Move import Move
from constants import PLAYER_NAMES, EMPTY_FIELD, PIECE_POINTS
from helpers import get_player_name_to_capture, is_correct_coordinates, get_opponent_player, print_board


def get_direction_of_x_for_move(move):
    return move.x - move.piece_x


def move_single_piece(board, player_name, move, is_final_move=False):
    fields = board.fields
    direction_of_x = get_direction_of_x_for_move(move)
    is_capture_possible = is_capture_possible_on_field(move.x, move.y, fields, player_name, direction_of_x)
    print('Before move_single_piece')
    # [p.print() for p in player.pieces]
    print_board(board)
    if is_capture_possible:
        move.score = PIECE_POINTS['CAPTURE']
        # print('Capture is possible for player', player.name)
        # move.print()
        # print_board(board)
        capture_move(board, player_name, move, direction_of_x)
        # print('After capture move')
        # print_board(board)
        # TODO assign score to move!!!!
    else:
        move.score = PIECE_POINTS['MOVE']
        # print('Capture is not possible for player', player.name)
        # move.print()
        # print_board(board)
        regular_move(board, player_name, move)
    print('After move_single_piece')
    # [p.print() for p in player.pieces]
    print_board(board)


def capture_move(board, player_name, move, direction_of_x):
    print('capture_move')
    fields = board.fields
    opponent_player = get_opponent_player(board, player_name)
    x, y, piece_x, piece_y = move.x, move.y, move.piece_x, move.piece_y

    # clear previous location
    fields[piece_y][piece_x].value = EMPTY_FIELD

    # TODO remove piece from player's pieces
    # TODO operate on field.piece
    # remove opponent's piece
    field_to_clear = fields[y][x]
    # field_to_clear.print()
    field_to_clear.value = EMPTY_FIELD
    opponent_player.remove_piece(field_to_clear.x, field_to_clear.y)

    # piece_to_clear = None
    capture_location = get_capture_location(x, y, player_name, direction_of_x)
    # print('capture_location', capture_location)
    x, y = capture_location

    # set new piece's location
    fields[y][x].value = player_name
    piece_to_move = get_piece_to_move(board, player_name, piece_x, piece_y)
    piece_to_move.move_piece(x, y)


def get_capture_location(x, y, player_name, direction_of_x):
    move_direction = 1 if player_name == PLAYER_NAMES['P1'] else -1
    y = y - 1 * move_direction
    return x + direction_of_x, y


def regular_move(board, player_name, move):
    # print('regular_move for player', player.name)
    fields = board.fields
    x, y, piece_x, piece_y = move.x, move.y, move.piece_x, move.piece_y
    # piece.print()
    # move.print()
    # print_board_fields(fields)
    fields[piece_y][piece_x].value = EMPTY_FIELD
    fields[y][x].value = player_name
    print_board(board)
    print('x', x, 'y', y)
    print('player_name', player_name, 'piece_x', piece_x, 'piece_y', piece_y)
    piece_to_move = get_piece_to_move(board, player_name, piece_x, piece_y)
    piece_to_move.move_piece(x, y)


def get_piece_to_move(board, player_name, piece_x, piece_y):
    pieces_to_search = board.players[0].pieces if player_name == PLAYER_NAMES['P1'] else board.players[1].pieces
    [p.print() for p in pieces_to_search]
    return next((piece for piece in pieces_to_search if piece.x == piece_x and piece.y == piece_y), None)


def get_all_correct_moves(player, fields, is_capture=False):
    all_correct_moves = []
    # print('player.pieces', len(player.pieces))
    # [p.print() for p in player.pieces]
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
        correct_moves.append(Move(x + 1, y, 0, piece.x, piece.y))
    if is_correct_move(x - 1, y, fields, player, -1, piece, is_capture):
        correct_moves.append(Move(x - 1, y, 0, piece.x, piece.y))
    return correct_moves


def is_correct_move(x, y, fields, player, direction_of_x, piece, is_capture):
    if not is_correct_coordinates(x, y):
        return False

    if not is_capture and fields[y][x].value == EMPTY_FIELD:
        return True
    return is_capture_possible_on_field(x, y, fields, player, direction_of_x)


def is_capture_possible_on_field(x, y, fields, player_name, direction_of_x):
    move_direction = 1 if player_name == PLAYER_NAMES['P1'] else -1
    player_name_to_capture = get_player_name_to_capture(player_name)
    y_new = y - 1 * move_direction
    x_new = x + direction_of_x  # TODO something wrong here
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
