import time

from Population import Population
from generate import generate
from mutation import mutate
from read import read
from init_population import init_population
from constants import *
from tournament import tournament
from crossover import crossover


def get_good_solution(task):
    population = init_population(task, POPULATION_SIZE)
    print('First value = ', population.individuals[0].evaluate())
    outer_iterator = 0
    while outer_iterator < MAX_ITERATIONS:
        inner_iterator = 0
        new_population = Population()
        start_time = time.time()
        while inner_iterator < POPULATION_SIZE:
            parent1 = tournament(population, TOURNAMENT_SIZE)
            parent2 = tournament(population, TOURNAMENT_SIZE)
            # print('parent1.evaluate() = ', parent1.evaluate())
            # print('parent2.evaluate() = ', parent2.evaluate())
            # print('IN MAIN')
            # print('len(parent1.items_array) = ', len(parent1.items_array))
            # print('len(parent2.items_array) = ', len(parent2.items_array))
            child = crossover(parent1, parent2, CROSSOVER_RATE)
            mutate(child, MUTATION_RATE)
            new_population.add_individual(child)
            inner_iterator += 1
        # print('new_population.individuals = ', new_population.individuals)
        print('Inner loop execution time = ', (time.time() - start_time), ' seconds')
        population = new_population
        outer_iterator += 1
    best_individual = population.best_individual()
    return best_individual


def main():
    generate(NUMBER_OF_OBJECTS, MAXIMUM_WEIGHT, MAXIMUM_SIZE, FILE_NAME)
    task = read(FILE_NAME)
    start_time = time.time()
    good_solution = get_good_solution(task)
    print('Final value = ', good_solution.evaluate())
    print('Execution time = ', (time.time() - start_time), ' seconds')


main()
