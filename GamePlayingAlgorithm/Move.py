class Move:
    def __init__(self, x, y, score, piece=None):
        self.x = x
        self.y = y
        self.score = score
        self.piece = piece

    def print(self):
        print('Move location: [', self.x, ',', self.y, '], score:', self.score, ', piece:', self.piece)

    x = 0
    y = 0
    score = 0
    piece = None
