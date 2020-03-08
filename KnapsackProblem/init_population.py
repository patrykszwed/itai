import numpy as np
import random

from Individual import Individual
from Population import Population

"""
def init_population(n_items, size)
n_items - number of items from which the subset to be
packed into the knapsack is selected
size - population size
"""


def init_population(task, size):
    n_items = task.n_items
    init_pop = np.zeros(n_items)

    for index in range(size):
        init_pop[index] = random.randrange(0, 2)

    return Population(n_items, np.array([Individual(task, init_pop)]))
