from constants import PLAYER_NAMES, BOARD_START, BOARD_END


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


def get_player_name_to_capture(player_name):
    return PLAYER_NAMES['P1'] if player_name == PLAYER_NAMES['P2'] else PLAYER_NAMES['P2']


def get_opponent_player(board, player_name):
    return board.players[1] if player_name == PLAYER_NAMES['P1'] else board.players[0]


def is_correct_coordinates(x, y):
    return is_correct_location(y) and is_correct_location(x)


def is_correct_location(location):
    return BOARD_START <= location <= BOARD_END


def get_capture_points_coefficient(player):
    return 1 if player.name == PLAYER_NAMES['P1'] else -1
