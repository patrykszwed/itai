from constants import PIECE_POINTS
from helpers import get_capture_points_coefficient, is_player_one
from move_helpers import get_all_correct_moves


def get_capture_points(board, player_name):
    capture_points = 0
    is_capture = is_capture_possible(player_name, board)
    if is_capture:
        capture_points += PIECE_POINTS['CAPTURE']
    # print('return capture_points', capture_points * get_capture_points_coefficient(player))
    return capture_points * get_capture_points_coefficient(player_name)


def get_pieces_count_points(board):
    flatten_fields_values = [field.value for sublist in board.fields for field in sublist]
    player1_pieces = sum(is_player_one(value) for value in flatten_fields_values)
    player2_pieces = sum(not is_player_one(value) for value in flatten_fields_values)
    return player1_pieces - player2_pieces


def is_capture_possible(player_name, board):
    all_correct_moves = get_all_correct_moves(board, player_name, board.fields, True)
    return len(all_correct_moves) > 0
