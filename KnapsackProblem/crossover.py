import random
import time

import numpy as np

from Individual import Individual
from constants import *


def crossover(parent1, parent2, crossover_rate):
    child = parent1
    if random.uniform(0, 1) < crossover_rate:
        parent1_items = parent1.items_array
        parent2_items = parent2.items_array
        split_index = int(NUMBER_OF_OBJECTS / 2)
        child_items = np.append(parent1_items[0: split_index], parent2_items[split_index: NUMBER_OF_OBJECTS])
        child = Individual(parent1.task, child_items)
    return child
