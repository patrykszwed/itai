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
    init_pop = []
    print('n_items', n_items)

    for individual_index in range(size):
        items_array = []
        for item_index in range(n_items[0]):
            items_array.append(random.uniform(0, 1) < PACKING_ITEM_RATE)
        print('items_array', items_array)
        init_pop.append(Individual(task, items_array))
        print('after')

    return Population(n_items, init_pop)
