import numpy as np

from Task import Task


def read_sudoku(input_file):
    data = np.genfromtxt(input_file, delimiter=';', skip_header=1, dtype=str)
    return Task([list(t) for t in data])
