import copy
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
    # print('-------- ORIGINAL --------')
    # print('fields:', board.fields)
    # print('players:', board.players)
    # board_copy = board.get_cloned_board()
    # print('-------- COPIED --------')
    # print('fields:', board_copy.fields)
    # print('players:', board_copy.players)
    #
    # piece = board_copy.players[0].pieces[0]
    # piece.x = -500
    # board.fields[4][5].value = '5342'
    #
    # print('COPIEDDDD')
    # print_board(board_copy)
    # print('len = ', len(board_copy.players[0].pieces))
    # [p.print() for p in board_copy.players[0].pieces]
    # print('ORIGINALLLL')
    # print_board(board)
    # print('len = ', len(board.players[0].pieces))
    # [p.print() for p in board.players[0].pieces]

    print('\nFinal board state:')
    print_board(board)


def move_piece_minimax(board, player):
    best_moves = [[], []]
    best_move = minimax(board.get_cloned_board(), player, 0, best_moves)
    # print('BEST MOVES')
    # [move.print() for best_moves_for_player in best_moves for move in best_moves_for_player]

    print('PLAYER MOVE', player.name)
    print_board(board)
    best_move.print()
    if best_move.score == +infinity or best_move.score == -infinity:
        return False
    print('Before performing best move for player', player.name)
    print_board(board)
    # [p.print() for p in player.pieces]
    move_single_piece(board, player.name, best_move, True)
    print('After performing best move for player', player.name)
    # [p.print() for p in player.pieces]
    print_board(board)
    # [p.print() for p in player.pieces]
    return True


def minimax(board, player, depth, best_moves):
    if depth == MAX_SEARCH_DEPTH or game_over(board):
        print('Evaluate for player', player.name)
        print_board(board)
        score = evaluate(board, player)
        print('score = ', score)
        return Move(-1, -1, score)

    best_move = Move(-1, -1, -infinity if player.name == PLAYER_NAMES['P1'] else +infinity)

    for correct_move in get_all_correct_moves(player, board.fields):
        correct_move_copy = copy.deepcopy(correct_move)  # I think I will have to do sth with this one
        board_copy = board.get_cloned_board()
        move_single_piece(board_copy, player.name, correct_move_copy)
        player_to_move = get_opponent_player(board_copy, player.name)
        move = minimax(board_copy, player_to_move, depth + 1, best_moves)  # <--- here is a recursion

        move.x = correct_move.x
        move.y = correct_move.y
        move.piece_x = correct_move.piece_x
        move.piece_y = correct_move.piece_y
        print('AFTER MINIMAX FOR PLAYER', player.name)
        print_board(board)
        [p.print() for p in player.pieces]
        print('===')
        print('---- CORRECT MOVE')
        correct_move.print()
        print('---- MOVE')
        move.print()
        print('---- BEST MOVE')
        best_move.print()
        if player.name == PLAYER_NAMES['P1']:
            # best_moves[0].append(move)
            if move.score > best_move.score:
                print('-------------------------')
                print_board(board)
                print('PLAYER P1 takes move:')
                move.print()
                print('INSTEAD OF:')
                best_move.print()
                print('-------------------------')
                # best_move = move  # max value
                best_move.x = move.x
                best_move.y = move.y
                best_move.piece_x = move.piece_x
                best_move.piece_y = move.piece_y
                best_move.score = move.score
        else:
            # best_moves[1].append(move)
            if move.score < best_move.score:
                print('-------------------------')
                print_board(board)
                print('PLAYER P2 takes move:')
                move.print()
                print('INSTEAD OF:')
                best_move.print()
                print('-------------------------')
                # best_move = move  # min value
                best_move.x = move.x
                best_move.y = move.y
                best_move.piece_x = move.piece_x
                best_move.piece_y = move.piece_y
                best_move.score = move.score

    return best_move


def evaluate(board, player):
    # pieces_count_points = get_pieces_count_points(board)
    pieces_count_points = 0
    capture_points = get_capture_points(board, player)
    # print('pieces_count_points', pieces_count_points)
    print('capture_points', capture_points)
    return pieces_count_points + capture_points


def game_over(board):
    flatten_fields_values = [field.value for sublist in board.fields for field in sublist]
    player1 = board.players[0].name
    player2 = board.players[1].name
    return player1 not in flatten_fields_values or player2 not in flatten_fields_values
