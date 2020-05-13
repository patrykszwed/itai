from math import inf as infinity

from Move import Move
from constants import PLAYER_NAMES, MAX_SEARCH_DEPTH
from helpers import print_board, get_opponent_player
from heuristics import get_capture_points
from move_helpers import move_single_piece, get_all_correct_moves


def run_game(board):
    players = board.players
    is_move_possible = True
    move = 0
    while is_move_possible:
        is_move_possible = move_piece_minimax(board, players[move % 2])
        move += 1

    print('\nFinal board state:')
    print_board(board)


def move_piece_minimax(board, player_name):
    best_move = minimax(board.get_cloned_board(), player_name, 0)

    # print('PLAYER MOVE', player_name)
    # print_board(board)
    # best_move.print()
    if best_move.score == +infinity or best_move.score == -infinity:
        return False
    # print('Before performing best move for player', player_name)
    # print_board(board)
    # [p.print() for p in get_pieces_for_player_name(board, player_name)]
    move_single_piece(board, player_name, best_move, True)
    print('After performing best move for player', player_name)
    # [p.print() for p in get_pieces_for_player_name(board, player_name)]
    print_board(board)
    return True


def minimax(board, player_name, depth):
    if depth == MAX_SEARCH_DEPTH or game_over(board):
        # print('Evaluate for player', player_name)
        # print_board(board)
        score = evaluate(board, player_name)
        # print('Player ', player_name, 'score = ', score)
        return Move(-1, -1, score)

    best_move = Move(-1, -1, -infinity if player_name == PLAYER_NAMES['P1'] else +infinity)

    for correct_move in get_all_correct_moves(board, player_name, board.fields):
        # correct_move_copy = copy.deepcopy(correct_move)  # I think I will have to do sth with this one
        board_copy = board.get_cloned_board()
        x, y, piece_x, piece_y = correct_move.x, correct_move.y, correct_move.piece_x, correct_move.piece_y
        move_single_piece(board_copy, player_name, correct_move)
        player_to_move = get_opponent_player(board_copy, player_name)
        move = minimax(board, player_to_move, depth + 1)  # <--- here is a recursion

        move.x = x
        move.y = y
        move.piece_x = piece_x
        move.piece_y = piece_y

        if player_name == PLAYER_NAMES['P1']:
            if move.score > best_move.score:
                best_move.x = move.x
                best_move.y = move.y
                best_move.piece_x = move.piece_x
                best_move.piece_y = move.piece_y
                best_move.score = move.score
        else:
            if move.score < best_move.score:
                best_move.x = move.x
                best_move.y = move.y
                best_move.piece_x = move.piece_x
                best_move.piece_y = move.piece_y
                best_move.score = move.score

    return best_move


def evaluate(board, player_name):
    # pieces_count_points = get_pieces_count_points(board)
    pieces_count_points = 0
    capture_points = get_capture_points(board, player_name)
    # print('pieces_count_points', pieces_count_points)
    # print('capture_points', capture_points)
    return pieces_count_points + capture_points


def game_over(board):
    flatten_fields_values = [field.value for sublist in board.fields for field in sublist]
    player1 = board.players[0]
    player2 = board.players[1]
    return player1 not in flatten_fields_values or player2 not in flatten_fields_values
