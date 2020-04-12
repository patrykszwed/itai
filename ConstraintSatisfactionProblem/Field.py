import numpy as np


class Field:
    def __init__(self, value, x, y, subgrid_index):
        self.value = int(value)
        self.x = x
        self.y = y
        self.subgrid_index = subgrid_index

    def add_value_to_trial_set(self, value):
        index_to_set = 0
        for i in range(9):
            if self.trial_set[i] == -1:
                index_to_set = i
        self.trial_set[index_to_set] = value

    value = 0
    x = 0
    y = 0
    subgrid_index = 0
    trial_set = np.full(9, -1)
