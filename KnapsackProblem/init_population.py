import numpy as np
import random

from Individual import Individual
from Population import Population
from constants import PACKING_ITEM_RATE

"""
def init_population(n_items, size)
n_items - number of items from which the subset to be
packed into the knapsack is selected
size - population size
"""


def init_population(task, size):
    n_items = task.n_items
    init_pop = np.empty(size, dtype=object)

    for individual_index in range(size):
        items_array = np.empty(n_items[0])
        for item_index in range(n_items[0]):
            items_array[item_index] = random.uniform(0, 1) < PACKING_ITEM_RATE
        init_pop[individual_index] = Individual(task, items_array)

    return Population(n_items, init_pop)
