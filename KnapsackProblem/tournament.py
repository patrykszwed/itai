from helpers import get_random_indexes_from_array


def get_best_individual(population_individuals, random_indexes):
    best_individual_value = 0
    best_individual = 0
    for individual_index in random_indexes:
        individual = population_individuals[individual_index]
        individual_value = individual.evaluate()
        if individual_value >= best_individual_value:
            best_individual_value = individual_value
            best_individual = individual
    return best_individual


def tournament(population, tournament_size):
    if tournament_size > len(population.individuals):
        tournament_size = len(population.individuals)
    random_indexes = get_random_indexes_from_array(population.individuals, tournament_size)
    best_individual = get_best_individual(population.individuals, random_indexes)
    return best_individual
