import copy
from math import inf as infinity

from constants import PLAYER_NAMES, MAX_SEARCH_DEPTH
from helpers import print_board
from heuristics import get_pieces_count_points, get_capture_points
from move_helpers import get_player_to_move, move_single_piece, get_all_correct_moves


def run_game(board):
    players = board.players
    fields = board.fields
    is_move_possible = True
    move = 0
    print('ORIGINAL!')
    print_board(board)
    # board_copy = copy.deepcopy(board)
    # print('COPIED!')
    # print_board(board_copy)
    # board.fields[3][3] = Field('DD', 3, 3)
    # print('ORIGINAL!')
    # print_board(board)
    # print('COPIED!')
    # print_board(board_copy)
    while is_move_possible:
        is_move_possible = move_piece_minimax(board, players[move % 2])
        # print('is_move_possible', is_move_possible)
        print('MAIN!')
        print_board(board)
        move += 1
        board.player_move = players[move % 2].name
        # print('game_ove ? ', game_over(board))
        # evaluate(board)


def move_piece_minimax(board, player):
    # fields_copy = copy.deepcopy(board.fields)
    # pieces_1_copy = copy.deepcopy(board.players[0].pieces)
    # pieces_2_copy = copy.deepcopy(board.players[1].pieces)
    print('BEFORE MINIMAX')
    print_board(board)
    # print_board_fields(fields_copy)
    # print_board_fields(fields_copy)
    best_move = minimax(board, player, 0)
    print('AFTER MINIMAX best_move', best_move)
    print_board(board)
    # print_board_fields(fields_copy)
    # print('move_piece_minimax', move_piece_minimax)
    if best_move[2] == +infinity or best_move[2] == -infinity:
        return False
    # print('COPIED')
    # print_board_fields(fields_copy)
    # board.fields = fields_copy
    # board.players[0].pieces = pieces_1_copy
    # board.players[1].pieces = pieces_2_copy
    move_single_piece(board.fields, player, best_move)
    return True


def minimax(board, player, depth):
    best_move = [-1, -1, -infinity if player.name == PLAYER_NAMES['P1'] else +infinity]

    if depth == MAX_SEARCH_DEPTH or game_over(board):
        score = evaluate(board, player)
        # print('score', score)
        return [-1, -1, score]

    # print('get_all_correct_moves(player, board.fields)', get_all_correct_moves(player, board.fields))
    for correct_move in get_all_correct_moves(player, board.fields):
        # print_board(board)
        # print('correct_move', correct_move)
        x, y, piece = correct_move[0], correct_move[1], correct_move[2]
        board_copy = copy.deepcopy(board)  # copy the previous list
        move_single_piece(board_copy.fields, player, correct_move)
        player_to_move = get_player_to_move(board_copy, player)
        score = minimax(board_copy, player_to_move, depth + 1)
        board = board_copy
        score[0], score[1] = x, y

        if player.name == PLAYER_NAMES['P1']:
            if score[2] > best_move[2]:
                best_move = score  # max value
        else:
            if score[2] < best_move[2]:
                best_move = score  # min value

    print('player.name', player.name)
    print('best_move', best_move)
    return best_move


def evaluate(board, player):
    pieces_count_points = get_pieces_count_points(board)
    capture_points = get_capture_points(board, player)
    # capture_points = 0
    # print('player1_pieces', player1_pieces)
    # print('player2_pieces', player2_pieces)
    # print('evaluate return', (player1_pieces - player2_pieces))
    # print('capture_points', capture_points)
    return pieces_count_points + capture_points


def game_over(board):
    flatten_fields_values = [field.value for sublist in board.fields for field in sublist]
    player1 = board.players[0].name
    player2 = board.players[1].name
    return player1 not in flatten_fields_values or player2 not in flatten_fields_values
