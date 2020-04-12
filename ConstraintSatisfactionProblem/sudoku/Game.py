import numpy as np


def get_columns(rows):
    columns = list(range(9))
    for column_index in range(9):
        columns[column_index] = list(range(9))
        for row_index in range(len(rows)):
            columns[column_index][row_index] = rows[row_index][column_index]
    return np.asarray(columns)


def get_squares(rows):
    squares = np.zeros((9, 9))
    indexes_to_assign = np.zeros(9, dtype=int)

    for row_index in range(len(rows)):
        for column_index in range(len(rows)):
            number = rows[row_index][column_index]
            index = int(row_index / 3) * 3 + int(column_index / 3)
            index_to_assign = indexes_to_assign[index]
            squares[index][index_to_assign] = number
            indexes_to_assign[index] = indexes_to_assign[index] + 1
    return squares


class Game:
    def __init__(self, game_data):
        self.game_id = game_data[0]
        self.difficulty = game_data[1]

        game_data[2] = np.char.replace(game_data[2], '.', '0')
        numbers = np.array(list(game_data[2]))
        self.rows = np.split(numbers, len(numbers) / 9)
        self.columns = get_columns(self.rows)
        self.squares = get_squares(self.rows)

    game_id = 0
    difficulty = 0
    columns = np.empty(9)
    rows = np.empty(9)
    squares = np.empty(9)
