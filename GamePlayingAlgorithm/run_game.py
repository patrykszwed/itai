import copy
from math import inf as infinity

from constants import BOARD_START, BOARD_END, EMPTY_FIELD, PLAYER_NAMES, MAX_SEARCH_DEPTH
from helpers import print_board, print_board_fields
from heuristics import get_pieces_count_points, get_capture_points


def run_game(board):
    players = board.players
    fields = board.fields
    is_move_possible = True
    move = 0
    while is_move_possible and move < 20:
        is_move_possible = move_piece_minimax(board, players[move % 2])
        # is_move_possible = move_piece(players[move % 2], board.fields)
        print('is_move_possible', is_move_possible)
        print_board(board)
        move += 1
        board.player_move = players[move % 2].name
        # print('game_ove ? ', game_over(board))
        # evaluate(board)


def move_piece_minimax(board, player):
    fields_copy = copy.copy(board.fields)
    pieces_1_copy = copy.copy(board.players[0].pieces)
    pieces_2_copy = copy.copy(board.players[1].pieces)
    best_move = minimax(board, player, 0)
    # print('move_piece_minimax', move_piece_minimax)
    if best_move[2] == +infinity:
        return False
    print('COPIED')
    print_board_fields(fields_copy)
    board.fields = fields_copy
    board.players[0].pieces = pieces_1_copy
    board.players[1].pieces = pieces_2_copy
    move_single_piece(board.fields, player, best_move)
    return True


def minimax(board, player, depth):
    if player.name == PLAYER_NAMES['P1']:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == MAX_SEARCH_DEPTH or game_over(board):
        score = evaluate(board, player)
        # print('score', score)
        return [-1, -1, score]

    # print('get_all_correct_moves(player, board.fields)', get_all_correct_moves(player, board.fields))
    for correct_move in get_all_correct_moves(player, board.fields):
        # print_board(board)
        # print('correct_move', correct_move)
        x, y, piece = correct_move[0], correct_move[1], correct_move[2]
        piece_x, piece_y = piece.x, piece.y
        fields_copy = board.fields[:]  # copy the previous list
        # print('minimax move_single_piece', correct_move)
        move_single_piece(board.fields, player, correct_move)
        player_to_move = get_player_to_move(board, player)
        score = minimax(board, player_to_move, depth + 1)
        board.fields = fields_copy
        piece.x = piece_x
        piece.y = piece_y
        score[0], score[1] = x, y

        if player.name == PLAYER_NAMES['P1']:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    print('player.name', player.name)
    print('best', best)
    return best


def get_player_to_move(board, prev_player):
    return board.players[1] if prev_player.name == PLAYER_NAMES['P1'] else board.players[0]


def move_single_piece(fields, player, move):
    # print('move', move)
    piece = move[2]
    fields[piece.y][piece.x].value = EMPTY_FIELD
    fields[move[1]][move[0]].value = player.name
    piece.move_piece(move[0], move[1])


def evaluate(board, player):
    pieces_count_points = get_pieces_count_points(board)
    capture_points = get_capture_points(board, player)
    # print('player1_pieces', player1_pieces)
    # print('player2_pieces', player2_pieces)
    # print('evaluate return', (player1_pieces - player2_pieces))
    return pieces_count_points + capture_points


def game_over(board):
    flatten_fields_values = [field.value for sublist in board.fields for field in sublist]
    player1 = board.players[0].name
    player2 = board.players[1].name
    return player1 not in flatten_fields_values or player2 not in flatten_fields_values


def get_all_correct_moves(player, fields):
    all_correct_moves = []
    for piece in player.pieces:
        correct_moves_for_piece = get_correct_moves_for_piece(piece, fields, player.name)
        all_correct_moves.append(correct_moves_for_piece)
    # print('all_correct_moves', all_correct_moves)
    flatten_all_correct_moves = [all_correct_moves_for_one_piece for sublist in all_correct_moves for
                                 all_correct_moves_for_one_piece in sublist]
    # print('flatten_all_correct_moves', flatten_all_correct_moves)
    return flatten_all_correct_moves


def get_correct_moves_for_piece(piece, fields, player_name):
    move_direction = 1 if player_name == PLAYER_NAMES['P1'] else -1
    correct_moves = []
    x = piece.x
    y = piece.y - 1 * move_direction
    if is_correct_move(x + 1, y, fields):
        correct_moves.append([x + 1, y, piece])
    if is_correct_move(x - 1, y, fields):
        correct_moves.append([x - 1, y, piece])
    return correct_moves


def is_correct_move(x, y, fields):
    # print('len(fields)', len(fields))
    if not is_correct_location(x) or not is_correct_location(y):
        return False
    # print_board_fields(fields)
    # print('x', x, 'y', y)
    # print('fields[y][x].value', fields[y][x].value)
    return fields[y][x].value == EMPTY_FIELD


def is_correct_location(location):
    return BOARD_START <= location <= BOARD_END
