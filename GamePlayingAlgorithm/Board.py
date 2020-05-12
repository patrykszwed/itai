from Field import Field
from Player import Player
from constants import PLAYER_NAMES, EMPTY_FIELD, BOARD_END


def place_players_pieces(fields, players):
    def place_player_pieces(fields_to_set, player):
        pieces_count = 0
        all_pieces_placed = False
        fields_to_iterate = fields_to_set if player.name == PLAYER_NAMES['P2'] else reversed(fields_to_set)
        for row_fields in fields_to_iterate:
            if all_pieces_placed:
                break
            for field in row_fields:
                if field.value == EMPTY_FIELD:
                    field.value = player.name
                    field.init_piece(player)
                    player.add_piece(field.piece)
                    pieces_count += 1
                    if pieces_count == 20:
                        all_pieces_placed = True
                        break

    place_player_pieces(fields, players[0])
    place_player_pieces(fields, players[1])
    return fields


def get_fields(players):
    all_fields = []
    index = 0
    for i in range(BOARD_END + 1):
        fields = []
        for j in range(BOARD_END + 1):
            initial_value = '_' if (i + j) % 2 != 0 else ' '
            fields.append(Field(initial_value, j, i))
            index += 1
        all_fields.append(fields)

    return place_players_pieces(all_fields, players)


def get_copied_fields(fields):
    copied_fields = []
    for row_fields in fields:
        fields = []
        for field in row_fields:
            fields.append(Field(field.value, field.x, field.y))
        copied_fields.append(fields)
    return copied_fields


class Board:
    def __init__(self, fields=None, players=None):
        if fields is None or players is None:
            self.pieces = []
            self.players.append(Player(PLAYER_NAMES['P1']))
            self.players.append(Player(PLAYER_NAMES['P2']))
            self.fields = get_fields(self.players)
        else:
            self.players = []
            self.fields = []
            self.pieces = []
            self.players.append(Player(PLAYER_NAMES['P1'], fields))
            self.players.append(Player(PLAYER_NAMES['P2'], fields))
            self.fields = get_copied_fields(fields)

    def get_cloned_board(self):
        board = Board(self.fields, self.players)
        return board

    fields = []
    players = []
    pieces = []
