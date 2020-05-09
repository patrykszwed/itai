from math import inf as infinity

from constants import BOARD_START, BOARD_END, EMPTY_FIELD, PLAYER_NAMES, MAX_SEARCH_DEPTH
from helpers import print_board


def run_game(board):
    players = board.players
    fields = board.fields
    is_move_possible = True
    move = 0
    while is_move_possible:
        is_move_possible = move_piece(players[move % 2], fields)
        print_board(board)
        move += 1
        board.player_move = players[move % 2].name
        # print('game_ove ? ', game_over(board))
        # evaluate(board)


def minimax(board, player, depth):
    if player.name == PLAYER_NAMES['P1']:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == MAX_SEARCH_DEPTH or game_over(board):
        score = evaluate(board)
        return [-1, -1, score]

    for correct_move in get_all_correct_moves(player, board.fields):
        x, y, piece = correct_move[0], correct_move[1], correct_move[2]
        piece_x, piece_y = piece.x, piece.y
        fields_copy = board.fields[:]  # copy the previous list
        move_single_piece(board.fields, player, correct_move)
        player_to_move = get_player_to_move(board, player)
        score = minimax(board, player_to_move, depth)
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

    return best


def get_player_to_move(board, prev_player):
    return board.players[1] if prev_player.name == PLAYER_NAMES['P1'] else board.players[0]


def move_single_piece(fields, player, move):
    piece = move[2]
    fields[piece.y][piece.x].value = EMPTY_FIELD
    fields[move[1]][move[0]].value = player.name
    piece.move_piece(move[0], move[1])


def move_piece_minimax(board, player):
    best_move = minimax(board, player, 0)
    move_single_piece(board.fields, player, best_move)


def move_piece(player, fields):
    for piece in player.pieces:
        # piece.print()
        correct_moves = get_correct_moves_for_piece(piece, fields, player.name)
        # print('correct_moves', correct_moves)
        for correct_move in correct_moves:
            piece.calculate_max_points(correct_move)
    return move_best_piece(player, fields)


def move_best_piece(player, fields):
    max_points = 0
    best_move = None
    best_piece = None
    for piece in player.pieces:
        if piece.points > max_points:
            best_move = piece.best_move
            best_piece = piece
    print('best_move', best_move)
    if best_piece is None:
        return False
    fields[best_piece.y][best_piece.x].value = EMPTY_FIELD
    fields[best_move[1]][best_move[0]].value = player.name
    best_piece.move_piece(best_move[0], best_move[1])
    clear_pieces_points_and_move(player.pieces)
    return True


def evaluate(board):
    flatten_fields_values = [field.value for sublist in board.fields for field in sublist]
    player1_pieces = sum(value == PLAYER_NAMES['P1'] for value in flatten_fields_values)
    player2_pieces = sum(value == PLAYER_NAMES['P2'] for value in flatten_fields_values)
    print('player1_pieces', player1_pieces)
    print('player2_pieces', player2_pieces)
    print('evaluate return', (player1_pieces - player2_pieces))
    return player1_pieces - player2_pieces


def game_over(board):
    flatten_fields_values = [field.value for sublist in board.fields for field in sublist]
    player1 = board.players[0].name
    player2 = board.players[1].name
    return player1 not in flatten_fields_values or player2 not in flatten_fields_values


def get_all_correct_moves(player, fields):
    all_correct_moves = []
    for piece in player.pieces:
        all_correct_moves.append(get_correct_moves_for_piece(piece, fields, player.name))
    return all_correct_moves


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


def clear_pieces_points_and_move(pieces):
    for piece in pieces:
        piece.clear_points_and_move()


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
