import copy
from math import inf as infinity

from Move import Move
from constants import PLAYER_NAMES, MAX_SEARCH_DEPTH
from helpers import print_board
from heuristics import get_capture_points
from move_helpers import move_single_piece, get_all_correct_moves


def run_game(board):
    players = board.players
    is_move_possible = True
    move = 0
    while is_move_possible:
        # is_move_possible = move_piece_minimax(board, players[0])
        is_move_possible = move_piece_minimax(board, players[move % 2])
        move += 1
    print('\nFinal board state:')
    print_board(board)


def move_piece_minimax(board, player):
    best_move = minimax(copy.deepcopy(board), player, 0)
    best_move.print()
    if best_move.score == +infinity or best_move.score == -infinity:
        return False
    # print('Before performing best move for player', player.name)
    # print_board(board)
    # [p.print() for p in player.pieces]
    move_single_piece(board, player, best_move, True)
    print('After performing best move for player', player.name)
    print_board(board)
    # [p.print() for p in player.pieces]
    return True


def minimax(board, player, depth):
    if depth == MAX_SEARCH_DEPTH or game_over(board):
        score = evaluate(board, player)
        return Move(-1, -1, score)

    best_move = Move(-1, -1, -infinity if player.name == PLAYER_NAMES['P1'] else +infinity)
    if player.name == PLAYER_NAMES['P1']:  # maximizing player
        max_move = Move(-1, -1, -infinity)
        all_correct_moves = get_all_correct_moves(player, board.fields)
        # print('len(all_correct_moves)', len(all_correct_moves))
        board_copy = board
        # board_copy = copy.deepcopy(board)
        for correct_move in all_correct_moves:
            # pieces_copy0 = copy.deepcopy(board_copy.players[0].pieces)
            # pieces_copy1 = copy.deepcopy(board_copy.players[1].pieces)
            fields_copy = copy.deepcopy(board_copy.fields)
            piece = correct_move.piece
            x, y = piece.x, piece.y
            # [p.print() for p in pieces_copy0]
            move_single_piece(board_copy, player, correct_move)
            move = minimax(board_copy, board_copy.players[1], depth + 1)
            # move_single_piece_back(board_copy.fields, player, correct_move)
            # board_copy.players[0].pieces = pieces_copy0
            # board_copy.players[1].pieces = pieces_copy1
            board_copy.fields = fields_copy
            piece.x = x
            piece.y = y
            # print('correct_move', correct_move)
            # correct_move.print()
            # print('After minimax')
            # print_board(board_copy)
            if move.score > max_move.score:
                max_move = move
                max_move.x = correct_move.x
                max_move.y = correct_move.y
                max_move.piece = correct_move.piece
        return max_move
    else:  # minimizing player
        min_move = Move(-1, -1, +infinity)
        all_correct_moves = get_all_correct_moves(player, board.fields)
        board_copy = board
        # print('len(all_correct_moves)', len(all_correct_moves))
        for correct_move in all_correct_moves:
            # pieces_copy0 = copy.deepcopy(board_copy.players[0].pieces)
            # pieces_copy1 = copy.deepcopy(board_copy.players[1].pieces)
            fields_copy = copy.deepcopy(board_copy.fields)
            piece = correct_move.piece
            x, y = piece.x, piece.y
            move_single_piece(board_copy, player, correct_move)
            move = minimax(board_copy, board_copy.players[0], depth + 1)
            # move_single_piece_back(board_copy.fields, player, correct_move)
            # board_copy.players[0].pieces = pieces_copy0
            # board_copy.players[1].pieces = pieces_copy1
            board_copy.fields = fields_copy
            piece.x = x
            piece.y = y
            if move.score < min_move.score:
                # print('Decided to take move.score', move.score, 'rather than min_move.score', min_move.score)
                min_move = move
                min_move.x = correct_move.x
                min_move.y = correct_move.y
                min_move.piece = correct_move.piece
                # min_move.print()
        print('Returning min_move')
        print_board(board)
        min_move.print()
        return min_move


def evaluate(board, player):
    # pieces_count_points = get_pieces_count_points(board)
    pieces_count_points = 0
    capture_points = get_capture_points(board, player)
    # print('pieces_count_points', pieces_count_points)
    # print('capture_points', capture_points)
    return pieces_count_points + capture_points


def game_over(board):
    flatten_fields_values = [field.value for sublist in board.fields for field in sublist]
    player1 = board.players[0].name
    player2 = board.players[1].name
    return player1 not in flatten_fields_values or player2 not in flatten_fields_values