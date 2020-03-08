import time

import numpy as np
import random

from constants import POPULATION_SIZE
from helpers import get_random_indexes_from_array


def get_best_individual(population_individuals, random_indexes):
    best_individual_value = 0
    best_individual_index = -1
    for index, individual_index in enumerate(random_indexes):
        # print('individual_index = ', individual_index)
        # print('population_individuals = ', population_individuals)
        # print('len(population_individuals) = ', len(population_individuals))
        # print('population_individuals[individual_index] = ', population_individuals[individual_index])
        individual_value = population_individuals[individual_index].evaluate()
        if individual_value > best_individual_value:
            best_individual_index = individual_index
    return population_individuals[best_individual_index]


def tournament(population, tournament_size):
    start_time = time.time()
    random_indexes = get_random_indexes_from_array(population.individuals, tournament_size)
    # print('population1 = ', population)
    # print('population.individuals = ', population.individuals)
    best_individual = get_best_individual(population.individuals, random_indexes)
    # print('len(best_individual.items_array) = ', len(best_individual.items_array))
    return best_individual
