from constants import PIECE_RANKS


class Piece:
    def __init__(self, value, x, y, player_name):
        self.value = value
        self.x = x
        self.y = y
        self.rank = PIECE_RANKS['PIECE']
        self.player_name = player_name

    def move_piece(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print('Piece location: [', self.x, ',', self.y, '], value:', self.value, 'rank:', self.rank)

    value = 0
    x = 0
    y = 0
    rank = PIECE_RANKS['PIECE']
    player_name = ''
