from constants import PIECE_RANKS, PIECE_POINTS


class Piece:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.rank = PIECE_RANKS['PIECE']
        self.points = 0
        self.best_move = None

    def calculate_max_points(self, possible_move):
        # print('calculate_points')
        points = PIECE_POINTS['MOVE']
        if points > self.points:
            self.points = points
            self.best_move = possible_move
        # starting_field.print()

    def move_piece(self, x, y):
        self.x = x
        self.y = y

    def clear_points_and_move(self):
        self.points = 0
        self.best_move = None

    def print(self):
        print('Piece location: [', self.x, ',', self.y, '], value:', self.value, 'rank:', self.rank)

    value = 0
    x = 0
    y = 0
    rank = PIECE_RANKS['PIECE']
    points = 0
    best_move = None
