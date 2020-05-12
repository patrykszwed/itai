from constants import PLAYER_NAMES, PIECE_POINTS
from helpers import get_capture_points_coefficient
from move_helpers import get_all_correct_moves


def get_capture_points(board, player):
    capture_points = 0
    is_capture = is_capture_possible(player, board)
    print('is_capture_possible', is_capture)
    if is_capture:
        # print('Capture possible for player', player.name)
        # print_board(board)
        capture_points += PIECE_POINTS['CAPTURE']
    # print('return capture_points', capture_points * get_capture_points_coefficient(player))
    return capture_points * get_capture_points_coefficient(player)


def get_pieces_count_points(board):
    flatten_fields_values = [field.value for sublist in board.fields for field in sublist]
    player1_pieces = sum(value == PLAYER_NAMES['P1'] for value in flatten_fields_values)
    player2_pieces = sum(value == PLAYER_NAMES['P2'] for value in flatten_fields_values)
    # return player1_pieces - player2_pieces
    return 0


def is_capture_possible(player, board):
    all_correct_moves = get_all_correct_moves(player, board.fields, True)
    print('all_correct_moves', all_correct_moves)
    return len(all_correct_moves) > 0  # TODO return unique moves
