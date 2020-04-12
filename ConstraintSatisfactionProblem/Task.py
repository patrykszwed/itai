import numpy as np


class Task:
    def __init__(self, boards_data):
        self.number_of_board = len(boards_data)
        self.boards_data = np.asarray(boards_data)

    number_of_board = 0
    boards_data = np.asarray(0)
