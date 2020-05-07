from constants import BOARD_START, BOARD_END, EMPTY_FIELD
from helpers import print_board


def run_game(board):
    players = board.players
    fields = board.fields
    # print('len(fields)1', len(fields))
    move_piece(players[0], fields)
    print_board(board)
    move_piece(players[0], fields)
    print_board(board)


def move_piece(player, fields):
    # print('player.name', player.name)
    # print('player.pieces', player.pieces)
    # [print('piece.value', piece.value) for piece in player.pieces]
    for piece in player.pieces:
        # piece.print()
        correct_moves = get_correct_moves(piece, fields)
        print('correct_moves', correct_moves)
        for correct_move in correct_moves:
            piece.calculate_max_points(correct_move)
    move_best_piece(player, fields)


def move_best_piece(player, fields):
    max_points = 0
    best_move = None
    best_piece = None
    for piece in player.pieces:
        if piece.points > max_points:
            best_move = piece.best_move
            best_piece = piece
    print('best_move', best_move)
    fields[best_piece.y][best_piece.x].value = EMPTY_FIELD
    fields[best_move[1]][best_move[0]].value = player.name
    best_piece.move_piece(best_move[0], best_move[1])
    clear_pieces_points_and_move(player.pieces)


def clear_pieces_points_and_move(pieces):
    for piece in pieces:
        piece.clear_points_and_move()


def get_correct_moves(piece, fields):
    correct_moves = []
    x = piece.x
    y = piece.y - 1
    if is_correct_move(x + 1, y, fields):
        correct_moves.append([x + 1, y])
    if is_correct_move(x - 1, y, fields):
        correct_moves.append([x - 1, y])
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
