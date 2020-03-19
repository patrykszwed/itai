from helpers import *


def mutate_selected_indexes(items_array, indexes_to_mutate):
    for index, individual_index in enumerate(indexes_to_mutate):
        items_array[individual_index] = 1 - items_array[individual_index]


def mutate(individual, mutation_rate):
    items_to_mutate = int(NUMBER_OF_OBJECTS * mutation_rate)
    random_indexes_to_mutate = get_random_indexes_from_array(individual.items_array, items_to_mutate)
    mutate_selected_indexes(individual.items_array, random_indexes_to_mutate)
