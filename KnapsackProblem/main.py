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
    print('Initial value of the knapsack =', population.individuals[0].evaluate())
    outer_iterator = 0
    while outer_iterator < MAX_ITERATIONS:
        inner_iterator = 0
        new_population = Population()
        while inner_iterator < POPULATION_SIZE:
            parent1 = tournament(population, TOURNAMENT_SIZE)
            parent2 = tournament(population, TOURNAMENT_SIZE)
            child = crossover(parent1, parent2, CROSSOVER_RATE)
            mutate(child, MUTATION_RATE)
            new_population.add_individual(child)
            inner_iterator += 1
        population = new_population
        outer_iterator += 1
    return population.best_individual()


def main():
    generate(NUMBER_OF_OBJECTS, MAXIMUM_WEIGHT, MAXIMUM_SIZE, FILE_NAME)
    task = read(FILE_NAME)
    start_time = time.time()
    good_solution = get_good_solution(task)
    print('Final value of the knapsack =', good_solution.evaluate())
    print('Execution time =', round(time.time() - start_time, 2), 'seconds')


main()
