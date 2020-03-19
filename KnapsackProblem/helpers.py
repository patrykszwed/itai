import random
import numpy as np
from constants import *


def get_random_indexes_from_array(array, number_of_indexes_to_pick):
    already_picked_indexes = np.full(number_of_indexes_to_pick, -1)
    random_indexes = np.full(number_of_indexes_to_pick, -1)
    iterator = 0
    while iterator < number_of_indexes_to_pick:
        picked_index = int(random.randrange(0, len(array)))
        if picked_index not in already_picked_indexes:
            random_indexes[iterator] = picked_index
            already_picked_indexes[iterator] = picked_index
            iterator += 1
    return random_indexes


def get_values_array(value_to_sketch):
    return {
        'crossover_rate': CROSSOVER_RATES,
        'mutation_rate': MUTATION_RATES,
        'tournament_size': TOURNAMENT_SIZES,
        'population_size': POPULATION_SIZES
    }[value_to_sketch]
