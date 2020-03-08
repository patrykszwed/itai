import numpy as np
from Task import Task


def read(input_file):
    data = np.genfromtxt(input_file, delimiter=',', dtype=(int, int, int))
    print([list(t) for t in data])
    return Task([list(t) for t in data])
