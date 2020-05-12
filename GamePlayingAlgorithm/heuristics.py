from constants import PLAYER_NAMES, PIECE_POINTS
from helpers import get_capture_points_coefficient, get_opponent_player, print_board
from move_helpers import get_all_correct_moves


def get_capture_points(board, player):
    capture_points = 0
    capture_points_coefficient = get_capture_points_coefficient(player)
    if is_capture_possible(player, board):
        print('Capture possible for player', player.name)
        print_board(board)
        capture_points += (capture_points_coefficient * PIECE_POINTS['CAPTURE'])
    opponent_player = get_opponent_player(board, player)
    if is_capture_possible(opponent_player, board):
        print('OPPONENT Capture possible for player', opponent_player.name)
        print_board(board)
        capture_points += (-capture_points_coefficient * PIECE_POINTS['CAPTURE'])
    # print('return capture_points', capture_points)
    return capture_points


def get_pieces_count_points(board):
    flatten_fields_values = [field.value for sublist in board.fields for field in sublist]
    player1_pieces = sum(value == PLAYER_NAMES['P1'] for value in flatten_fields_values)
    player2_pieces = sum(value == PLAYER_NAMES['P2'] for value in flatten_fields_values)
    return player1_pieces - player2_pieces


def is_capture_possible(player, board):
    # print('is_capture_possible', player.name)
    # print_board(board)
    # [p.print() for p in player.pieces]
    all_correct_moves = get_all_correct_moves(player, board.fields, True)
    # print('all_correct_moves', all_correct_moves)
    return len(all_correct_moves) > 0  # TODO return unique moves
