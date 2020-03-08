import random
import time

import numpy as np

from Individual import Individual
from constants import *


def crossover(parent1, parent2, crossover_rate):
    child = parent1
    start_time = time.time()
    if random.uniform(0, 1) < crossover_rate:
        parent1_items = parent1.items_array
        parent2_items = parent2.items_array
        # print('parent1_items = ', parent1_items)
        # print('parent2_items = ', parent2_items)
        # print('len1 = ', len(parent1_items))
        # print('len2 = ', len(parent2_items))
        # parent1_items = np.split(parent1_items, 2)
        # parent2_items = np.split(parent2_items, 2)
        # print(parent1_individuals)
        # print(parent2_individuals)
        # print('len1 = ', len(parent1_items[0]))
        # print('len2 = ', len(parent2_items[1]))
        # print('type parent1_individuals = ', type(parent1_individuals))
        # print('type parent1_individuals = ', type(parent1_individuals))
        split_index = int(NUMBER_OF_OBJECTS / 2)
        # print('split_index = ', split_index)
        # print('parent1_items[0: split_index] = ', len(parent1_items[0: split_index]))
        # print('parent2_items[split_index: NUMBER_OF_OBJECTS] = ', len(parent2_items[split_index: NUMBER_OF_OBJECTS]))
        child_items = np.append(parent1_items[0: split_index], parent2_items[split_index: NUMBER_OF_OBJECTS])
        # print('len(child_items) = ', len(child_items))
        child = Individual(parent1.task, child_items)
    # print('child = ', child)
    print('Crossover execution time = ', (time.time() - start_time), ' seconds')
    return child
