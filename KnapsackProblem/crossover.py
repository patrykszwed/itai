import random
import time

import numpy as np

from Individual import Individual
from constants import *


def crossover(parent1, parent2, crossover_rate):
    print('TEST')
    child = parent1
    print('parent1 = ', parent1)
    if random.uniform(0, 1) < crossover_rate:
        print('THERE IS CROSSOVER')
        print('parent1.evaluate() =', parent1.evaluate())
        print('parent2.evaluate() =', parent2.evaluate())
        parent1_items = parent1.items_array
        parent2_items = parent2.items_array
        split_index = int(NUMBER_OF_OBJECTS / 2)
        child_items = np.append(parent1_items[0: split_index], parent2_items[split_index: NUMBER_OF_OBJECTS])
        child = Individual(parent1.task, child_items)
        print('CROSSOVER child.evaluate() = ', child.evaluate())
    return child
