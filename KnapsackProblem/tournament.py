from helpers import get_random_indexes_from_array


def get_best_individual(population_individuals, random_indexes):
    best_individual_value = 0
    best_individual = 0
    for index, individual_index in enumerate(random_indexes):
        print('individual_index', individual_index)
        individual = population_individuals[individual_index]
        individual_value = individual.evaluate()
        print('individual_value = ', individual_value)
        if individual_value >= best_individual_value:
            best_individual_value = individual_value
            best_individual = individual
    return best_individual


def tournament(population, tournament_size):
    print('tournament')
    print('population = ', population)
    print('population.individuals = ', population.individuals)
    print('len(population.individuals) = ', len(population.individuals))
    if tournament_size > len(population.individuals):
        tournament_size = len(population.individuals)
    random_indexes = get_random_indexes_from_array(population.individuals, tournament_size)
    # print('random_indexes = ', random_indexes)
    # print('len(population.individuals) =', len(population.individuals))
    best_individual = get_best_individual(population.individuals, random_indexes)
    print('best_individual = ', best_individual)
    return best_individual
