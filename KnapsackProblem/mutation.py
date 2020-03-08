import time
from random import random

from constants import NUMBER_OF_OBJECTS
from helpers import get_random_indexes_from_array


def mutate_selected_indexes(items_array, indexes_to_mutate):
    for index, individual_index in enumerate(indexes_to_mutate):
        if items_array[individual_index] == 1:
            items_array[individual_index] = 0
        else:
            items_array[individual_index] = 1


def mutate(individual, mutation_rate):
    start_time = time.time()
    items_to_mutate = int(NUMBER_OF_OBJECTS * mutation_rate)
    # print('items_to_mutate = ', items_to_mutate)
    random_indexes_to_mutate = get_random_indexes_from_array(individual.items_array, items_to_mutate)
    mutate_selected_indexes(individual.items_array, random_indexes_to_mutate)
    print('Mutation execution time = ', (time.time() - start_time), ' seconds')
