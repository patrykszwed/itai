from constants import PIECE_RANKS, KING_NAMES, PIECE_NAMES


class Piece:
    def __init__(self, value, x, y, rank=PIECE_RANKS['PIECE']):
        self.value = value
        self.x = x
        self.y = y
        self.rank = rank

    def move_piece(self, x, y):
        self.x = x
        self.y = y

    def upgrade_rank(self, fields):
        king_value = KING_NAMES['K1'] if self.value in PIECE_NAMES['P1'] else KING_NAMES['K2']
        self.rank = PIECE_RANKS['KING']
        fields[self.y][self.x].value = king_value
        self.value = king_value

    def print(self):
        print('Piece location: [', self.x, ',', self.y, '], value:', self.value, 'rank:', self.rank)

    value = 0
    x = 0
    y = 0
    rank = PIECE_RANKS['PIECE']
