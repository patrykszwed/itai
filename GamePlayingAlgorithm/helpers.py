from constants import BOARD_START, BOARD_END, PIECE_NAMES


def print_board(board):
    fields = board.fields
    print('')
    print('Board state:')
    for i in range(len(fields)):
        for j in range(len(fields)):
            field = fields[i][j]

            if j == 9:
                if field.value == '_':
                    print('', field.value)
                else:
                    print(field.value)
            else:
                if field.value == '_':
                    print('', field.value + " ", end="")
                else:
                    print(field.value + " ", end="")
    print('')


def print_board_fields(fields):
    print('')
    for i in range(len(fields)):
        for j in range(len(fields)):
            field = fields[i][j]

            if j == 9:
                if field.value == '_':
                    print('', field.value)
                else:
                    print(field.value)
            else:
                if field.value == '_':
                    print('', field.value + " ", end="")
                else:
                    print(field.value + " ", end="")


def get_piece_names_to_capture(player_name):
    return PIECE_NAMES['P2'] if is_player_one(player_name) else PIECE_NAMES['P1']


def get_opponent_player(board, player_name):
    return board.players[1] if is_player_one(player_name) else board.players[0]


def is_correct_coordinates(x, y):
    return is_correct_location(y) and is_correct_location(x)


def is_correct_location(location):
    return BOARD_START <= location <= BOARD_END


def get_capture_points_coefficient(player_name):
    return 1 if is_player_one(player_name) else -1


def get_pieces_for_player_name(board, player_name):
    return [p for p in board.pieces if p.value in PIECE_NAMES[player_name]]


def get_piece_from_location(board, player_name, piece_x, piece_y):
    pieces_for_player_name = get_pieces_for_player_name(board, player_name)
    return next((piece for piece in pieces_for_player_name if piece.x == piece_x and piece.y == piece_y), None)


def is_better_score(potential_move, best_move, player_name):
    if is_player_one(player_name):
        return potential_move.score > best_move.score
    return potential_move.score < best_move.score


def is_player_one(player_name):
    return player_name in PIECE_NAMES['P1']
