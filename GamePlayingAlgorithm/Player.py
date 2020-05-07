class Player:
    def __init__(self, name):
        self.name = name
        self.pieces = []

    def add_piece(self, piece):
        self.pieces.append(piece)

    name = ''
    pieces = []
