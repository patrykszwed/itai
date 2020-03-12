import time
import matplotlib.pyplot as plt
import numpy as np

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
    return population.best_individual(), best_individuals_values


def main():
    generate(NUMBER_OF_OBJECTS, MAXIMUM_WEIGHT, MAXIMUM_SIZE, FILE_NAME)
    task = read(FILE_NAME)
    generation_indexes = np.asarray(range(MAX_ITERATIONS))

    for i in range(3):
        crossover_rate = CROSSOVER_RATES[i]
        start_time = time.time()
        all_solutions = []
        for j in range(5):
            sol = get_good_solution(task, crossover_rate)[1]
            print('sol = ', sol)
            print('np.asarray(sol) = ', np.asarray(sol))
            all_solutions.append(np.asarray(sol))
            # print('Final value of the knapsack =', good_solution.evaluate())
            # print('Execution time =', round(time.time() - start_time, 2), 'seconds')
        all_solutions = np.asarray(all_solutions)
        summed_solution = all_solutions[0] + all_solutions[1] + all_solutions[2] + all_solutions[3] + all_solutions[4]
        print('summed_solution = ', summed_solution)
        average_solution = np.true_divide(summed_solution, 5)
        my_label = 'crossover_rate = ', crossover_rate
        print('average_solution = ', average_solution)
        print('type(generation_indexes) = ', type(generation_indexes))
        print('type(average_solution) = ', type(average_solution))
        plt.plot(generation_indexes, average_solution, label=my_label)
    plt.xlabel('Generation')
    plt.ylabel('Knapsack\'s value')
    plt.legend()
    plt.show()


main()
