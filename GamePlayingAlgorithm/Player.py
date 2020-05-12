class Player:
    def __init__(self, name):
        self.name = name
        self.pieces = []

    def add_piece(self, piece):
        self.pieces.append(piece)

    def remove_piece(self, x, y):
        self.pieces = [piece for piece in self.pieces if piece.x != x or piece.y != y]

    name = ''
    pieces = []
