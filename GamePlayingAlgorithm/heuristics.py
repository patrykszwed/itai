from constants import PIECE_POINTS
from helpers import get_capture_points_coefficient, is_player_one, is_player_two
from move_helpers import get_all_correct_moves, move_single_piece


def get_capture_points(board, player_name):
    capture_count_max = 0
    capture_moves = get_capture_moves(player_name, board)
    for capture_move in capture_moves:
        board_copy = board.get_cloned_board()
        capture_count = move_single_piece(board_copy, player_name, capture_move)
        if capture_count > capture_count_max:
            capture_count_max = capture_count
    return PIECE_POINTS['CAPTURE'] * get_capture_points_coefficient(player_name) * capture_count_max


def get_pieces_count_points(board):
    flatten_fields_values = [field.value for sublist in board.fields for field in sublist]
    player1_pieces = sum(is_player_one(value) for value in flatten_fields_values)
    player2_pieces = sum(is_player_two(value) for value in flatten_fields_values)
    return player1_pieces - player2_pieces


def get_capture_moves(player_name, board):
    return get_all_correct_moves(board, player_name, board.fields, True)
