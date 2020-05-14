from math import inf as infinity

from Move import Move
from constants import PLAYER_NAMES, MAX_SEARCH_DEPTH, KING_NAMES
from helpers import print_board, get_opponent_player, is_better_score, is_player_one
from heuristics import get_capture_points, get_pieces_count_points
from move_helpers import move_single_piece, get_all_correct_moves


def run_game(board):
    players = board.players
    is_move_possible = True
    move = 0
    while is_move_possible:
        print('MOVE', move)
        print_board(board)
        is_move_possible = move_piece_minimax(board, players[move % 2], True)
        move += 1

    print('\nFinal board state:')
    print_board(board)


def move_piece_minimax(board, player_name, final_move=False):
    best_move = minimax(board.get_cloned_board(), player_name, 0)

    # print('PLAYER MOVE', player_name)
    # print_board(board)
    # best_move.print()
    if best_move.score == +infinity or best_move.score == -infinity:
        return False
    # if final_move:
    #     print('Before performing best move for player', player_name)
    #     print_board(board)
    #     # [p.print() for p in get_pieces_for_player_name(board, player_name)]
    move_single_piece(board, player_name, best_move, True)
    # if final_move:
    #     print('After performing best move for player', player_name)
    #     print_board(board)
    #     best_move.print()
    # [p.print() for p in get_pieces_for_player_name(board, player_name)]

    return True


def minimax(board, player_name, depth):
    # print('Entered minimax for player', player_name, ' with board state:')
    # print_board(board)
    if depth == MAX_SEARCH_DEPTH or game_over(board):
        # print('EVALUATING FOR PLAYER', player_name, '......')
        score = evaluate(board, player_name)
        # print('Evaluate for player', player_name, 'score =', score)
        # print_board(board)
        return Move(-1, -1, score)

    best_move = Move(-1, -1, -infinity if player_name == PLAYER_NAMES['P1'] else +infinity)
    i = 0
    board_copy = board.get_cloned_board()
    for correct_move in get_all_correct_moves(board, player_name, board.fields):
        # print('player = ', player_name, 'i = ', i)
        i += 1
        x, y, piece_x, piece_y = correct_move.x, correct_move.y, correct_move.piece_x, correct_move.piece_y
        move_single_piece(board, player_name, correct_move, False, True)
        # print('AFTER MOVING SINGLE PIECE FOR PLAYER', player_name, 'BOARD STATE:')
        # print_board(board)
        # print('BOARD COPY')
        # print_board(board_copy)
        player_to_move = get_opponent_player(board, player_name)
        potential_move = minimax(board, player_to_move, depth + 1)  # <--- here is a recursion
        # print('GOT POTENTIAL_MOVE - AFTER MINIMAX FOR PLAYER', player_name)
        # correct_move.print()

        potential_move.x = x
        potential_move.y = y
        potential_move.piece_x = piece_x
        potential_move.piece_y = piece_y
        # print('potential_move for player', player_name)
        # potential_move.print()
        # print('and for board state:')
        # print_board(board_copy)

        if is_better_score(potential_move, best_move, player_name):
            # print('Player', player_name, 'takes potential_move:')
            # potential_move.print()
            # print('instead of best_move:')
            # best_move.print()
            best_move.x = potential_move.x
            best_move.y = potential_move.y
            best_move.piece_x = potential_move.piece_x
            best_move.piece_y = potential_move.piece_y
            best_move.score = potential_move.score
        board = board_copy.get_cloned_board()

    # print('RETURN BEST_MOVE FOR PLAYER', player_name)
    # best_move.print()
    # print_board(board_copy)
    return best_move


def evaluate(board, player_name):
    points = 0
    if is_player_one(player_name):
        points += get_capture_points(board, player_name)
    else:
        points += get_pieces_count_points(board)
    return points


def game_over(board):
    flatten_fields_values = [field.value for sublist in board.fields for field in sublist]
    return (PLAYER_NAMES['P1'] not in flatten_fields_values and KING_NAMES['K1'] not in flatten_fields_values) or (
            PLAYER_NAMES['P2'] not in flatten_fields_values and KING_NAMES['K2'] not in flatten_fields_values)
