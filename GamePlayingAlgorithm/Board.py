from Field import Field
from Piece import Piece
from constants import PLAYER_NAMES, EMPTY_FIELD, BOARD_END


def get_copied_fields(fields):
    copied_fields = []
    for row_fields in fields:
        fields = []
        for field in row_fields:
            fields.append(Field(field.value, field.x, field.y))
        copied_fields.append(fields)
    return copied_fields


def get_copied_pieces(pieces):
    copied_pieces = []
    for piece in pieces:
        copied_pieces.append(Piece(piece.value, piece.x, piece.y, piece.rank))
    return copied_pieces


def get_fields():
    all_fields = []
    index = 0
    for i in range(BOARD_END + 1):
        fields = []
        for j in range(BOARD_END + 1):
            initial_value = '_' if (i + j) % 2 != 0 else ' '
            fields.append(Field(initial_value, j, i))
            index += 1
        all_fields.append(fields)

    return all_fields


def get_players_pieces(fields):
    def place_player_pieces(fields_to_set, player_name):
        pieces_count = 0
        all_pieces_placed = False
        fields_to_iterate = fields_to_set if player_name == PLAYER_NAMES['P2'] else reversed(fields_to_set)
        pieces = []
        for row_fields in fields_to_iterate:
            if all_pieces_placed:
                break
            for field in row_fields:
                if field.value == EMPTY_FIELD:
                    field.value = player_name
                    pieces.append(Piece(player_name, field.x, field.y))
                    pieces_count += 1
                    if pieces_count == 20:
                        all_pieces_placed = True
                        break
        return pieces

    player0_pieces = place_player_pieces(fields, PLAYER_NAMES['P1'])
    player1_pieces = place_player_pieces(fields, PLAYER_NAMES['P2'])
    return player0_pieces + player1_pieces


class Board:
    def __init__(self, fields=None, pieces=None):
        if fields is None or pieces is None:
            self.fields = get_fields()
            self.pieces = get_players_pieces(self.fields)
            self.players.append('P1')
            self.players.append('P2')
        else:
            self.fields = get_copied_fields(fields)
            self.pieces = get_copied_pieces(pieces)

    def get_cloned_board(self):
        return Board(self.fields, self.pieces)

    def remove_piece(self, x, y):
        self.pieces = [piece for piece in self.pieces if piece.x != x or piece.y != y]

    fields = []
    players = []
    pieces = []
