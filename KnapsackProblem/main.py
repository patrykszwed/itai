import time
import matplotlib.pyplot as plt

from Population import Population
from generate import generate
from mutation import mutate
from read import read
from init_population import init_population
from constants import *
from tournament import tournament
from crossover import crossover


def get_good_solution(task,
                      crossover_rate=CROSSOVER_RATE, mutation_rate=MUTATION_RATE,
                      tournament_size=TOURNAMENT_SIZE, population_size=POPULATION_SIZE):
    best_individuals_values = []
    generation_indexes = range(MAX_ITERATIONS)
    population = init_population(task, population_size)
    print('Initial value of the knapsack =', population.individuals[0].evaluate())
    outer_iterator = 0
    while outer_iterator < MAX_ITERATIONS:
        inner_iterator = 0
        new_population = Population()
        print('population_size = ', population_size)
        while inner_iterator < population_size:
            parent1 = tournament(population, tournament_size)
            parent2 = tournament(population, tournament_size)
            child = crossover(parent1, parent2, crossover_rate)
            print('Before mutation child.evaluate() = ', child.evaluate())
            mutate(child, mutation_rate)
            print('After mutation child.evaluate() = ', child.evaluate())
            new_population.add_individual(child)
            inner_iterator += 1
        population = new_population
        outer_iterator += 1
        # print('len(new_population.individuals) =', len(new_population.individuals))
        # print('population.best_individual() = ', population.best_individual())
        best_individuals_values.append(population.best_individual().evaluate())
    my_label = 'crossover_rate = ', crossover_rate
    plt.plot(generation_indexes, best_individuals_values, label=my_label)
    return population.best_individual()


def main():
    generate(NUMBER_OF_OBJECTS, MAXIMUM_WEIGHT, MAXIMUM_SIZE, FILE_NAME)
    task = read(FILE_NAME)

    for i in range(1):
        crossover_rate = CROSSOVER_RATES[i]
        start_time = time.time()
        good_solution = get_good_solution(task, crossover_rate)
        print('Final value of the knapsack =', good_solution.evaluate())
        print('Execution time =', round(time.time() - start_time, 2), 'seconds')
    plt.xlabel('Generation')
    plt.ylabel('Knapsack\'s value')
    plt.legend()
    plt.show()


main()
