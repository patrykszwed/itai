from Piece import Piece


class Player:
    def __init__(self, name, fields=None):
        self.name = name
        self.pieces = []
        if fields is not None:
            for row_fields in fields:
                for field in row_fields:
                    if field.value == self.name:
                        self.pieces.append(Piece(field.value, field.x, field.y, self.name))

    def add_piece(self, piece):
        self.pieces.append(piece)

    def remove_piece(self, x, y):
        self.pieces = [piece for piece in self.pieces if piece.x != x or piece.y != y]

    name = ''
    pieces = []
