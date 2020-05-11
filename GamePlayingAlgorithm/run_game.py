import copy
from math import inf as infinity

from Move import Move
from constants import PLAYER_NAMES, MAX_SEARCH_DEPTH
from helpers import print_board
from heuristics import get_pieces_count_points
from move_helpers import move_single_piece, get_all_correct_moves, get_player_to_move


def run_game(board):
    players = board.players
    is_move_possible = True
    move = 0
    while is_move_possible:
        is_move_possible = move_piece_minimax(board, players[move % 2])
        move += 1
    print('\nFinal board state:')
    print_board(board)


def move_piece_minimax(board, player):
    best_move = minimax(copy.deepcopy(board), player, 0)
    best_move.print()
    if best_move.score == +infinity or best_move.score == -infinity:
        return False
    move_single_piece(board.fields, player, best_move)
    return True


def minimax(board, player, depth):
    best_move = Move(-1, -1, -infinity if player.name == PLAYER_NAMES['P1'] else +infinity)

    if depth == MAX_SEARCH_DEPTH or game_over(board):
        score = evaluate(board)
        return Move(-1, -1, score)

    for correct_move in get_all_correct_moves(player, board.fields):
        x, y, piece = correct_move.x, correct_move.y, correct_move.piece
        move_single_piece(board.fields, player, correct_move)
        player_to_move = get_player_to_move(board, player)
        move = minimax(board, player_to_move, depth + 1)
        move.x = x
        move.y = y
        move.piece = piece

        if player.name == PLAYER_NAMES['P1']:
            if move.score > best_move.score:
                best_move = move  # max value
        else:
            if move.score < best_move.score:
                best_move = move  # min value

    return best_move


def evaluate(board):
    pieces_count_points = get_pieces_count_points(board)
    # capture_points = get_capture_points(board)
    # print('pieces_count_points', pieces_count_points)
    return pieces_count_points + 0


def game_over(board):
    flatten_fields_values = [field.value for sublist in board.fields for field in sublist]
    player1 = board.players[0].name
    player2 = board.players[1].name
    return player1 not in flatten_fields_values or player2 not in flatten_fields_values
