from Piece import Piece


class Field:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.piece = None

    def init_piece(self, player):
        self.piece = Piece(self.value, self.x, self.y, player)

    def set_piece(self, piece):
        self.piece = piece

    def remove_piece(self):
        self.piece = None

    def print(self):
        print('Field location: [', self.x, ',', self.y, '], value:', self.value)

    value = 0
    x = 0
    y = 0
    piece = None
