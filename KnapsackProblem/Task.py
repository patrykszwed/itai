import numpy as np
from constants import *


class Task:
    def __init__(self, data):
        self.w_i = [row[0] for row in data if data.index(row) != 0]
        self.s_i = [row[1] for row in data if data.index(row) != 0]
        self.c_i = [row[2] for row in data if data.index(row) != 0]
        self.n_items = [row[0] for row in data if data.index(row) == 0]
        self.w = [row[1] for row in data if data.index(row) == 0]
        self.s = [row[2] for row in data if data.index(row) == 0]

    w_i = np.empty(NUMBER_OF_OBJECTS + 1)
    s_i = np.empty(NUMBER_OF_OBJECTS + 1)
    c_i = np.empty(NUMBER_OF_OBJECTS + 1)
    n_items = 0
    w = 0
    s = 0
