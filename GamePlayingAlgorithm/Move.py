class Move:
    def __init__(self, x, y, score, piece_x=None, piece_y=None):
        self.x = x
        self.y = y
        self.score = score
        self.piece_x = piece_x
        self.piece_y = piece_y

    def print(self):
        print('Move location: [', self.x, ',', self.y, '], score:', self.score, ', piece_x:', self.piece_x,
              ', piece_y:', self.piece_y)

    x = 0
    y = 0
    score = 0
