import time
import matplotlib.pyplot as plt
import numpy as np

from Population import Population
from generate import generate
from helpers import get_values_array
from mutation import mutate
from read import read
from init_population import init_population
from constants import *
from tournament import tournament
from crossover import crossover


def main():
    generate(NUMBER_OF_OBJECTS, MAXIMUM_WEIGHT, MAXIMUM_SIZE, FILE_NAME)
    task = read(FILE_NAME)
    generation_indexes = np.asarray(range(MAX_ITERATIONS))
    # sketch_plot_for_values('crossover_rate', task, generation_indexes)
    # sketch_plot_for_values('mutation_rate', task, generation_indexes)
    # sketch_plot_for_values('tournament_size', task, generation_indexes)
    # sketch_plot_for_values('population_size', task, generation_indexes)
    non_genetic_algorithm(task)
    genetic_algorithm(task, 0.75, 0.001, 10, 150)


def get_good_solution(task,
                      crossover_rate=CROSSOVER_RATE, mutation_rate=MUTATION_RATE,
                      tournament_size=TOURNAMENT_SIZE, population_size=POPULATION_SIZE):
    best_individuals_values = np.empty(MAX_ITERATIONS)

    population = init_population(task, population_size)
    outer_iterator = 0
    best_individual = 0
    best_individual_value = 0
    global_best_individual = 0
    global_best_individual_value = 0
    print('Initial value of the knapsack =', population.individuals[0].evaluate())
    while outer_iterator < MAX_ITERATIONS:
        inner_iterator = 0
        new_population = Population()
        while inner_iterator < population_size:
            parent1 = tournament(population, tournament_size)
            parent2 = tournament(population, tournament_size)
            child = crossover(parent1, parent2, crossover_rate)
            mutate(child, mutation_rate)
            new_population.add_individual(child)
            inner_iterator += 1
        best_individual = population.best_individual()
        best_individual_value = best_individual.evaluate()
        if best_individual_value >= global_best_individual_value:
            global_best_individual = best_individual
            global_best_individual_value = best_individual_value
        new_population.set_first_individual(global_best_individual)
        population = new_population
        best_individuals_values[outer_iterator] = global_best_individual_value
        outer_iterator += 1
    return global_best_individual, best_individuals_values


def run_proper_function(task, value_to_sketch, value):
    if value_to_sketch == 'crossover_rate':
        return get_good_solution(task, value)[1]
    elif value_to_sketch == 'mutation_rate':
        return get_good_solution(task, CROSSOVER_RATE, value)[1]
    elif value_to_sketch == 'tournament_size':
        return get_good_solution(task, CROSSOVER_RATE, MUTATION_RATE, value)[1]
    return get_good_solution(task, CROSSOVER_RATE, MUTATION_RATE, POPULATION_SIZE, value)[1]


def sketch_plot_for_values(value_to_sketch, task, generation_indexes):
    values_array = get_values_array(value_to_sketch)
    for i in range(3):
        value = values_array[i]
        all_solutions = []
        for j in range(5):
            sol = run_proper_function(task, value_to_sketch, value)
            all_solutions.append(np.asarray(sol))
        all_solutions = np.asarray(all_solutions)
        summed_solution = all_solutions[0] + all_solutions[1] + all_solutions[2] + all_solutions[3] + all_solutions[4]
        average_solution = np.true_divide(summed_solution, 5)
        my_label = value_to_sketch, ' = ', value
        plt.plot(generation_indexes, average_solution, label=my_label)
    plt.xlabel('Generation')
    plt.ylabel('Knapsack\'s value')
    plt.legend()
    plt.show()


def non_genetic_algorithm(task):
    start_time = time.time()
    already_picked_indexes = np.empty(NUMBER_OF_OBJECTS + 1)
    total_weight = 0
    total_size = 0
    total_cost = 0
    while total_weight < MAXIMUM_WEIGHT and total_size < MAXIMUM_SIZE:
        max_cost = 0
        for item_index in range(NUMBER_OF_OBJECTS):
            current_cost = task.c_i[item_index]
            if item_index not in already_picked_indexes and \
                    current_cost > max_cost:
                max_cost = current_cost
                total_weight += task.w_i[item_index]
                total_size += task.s_i[item_index]
                np.append(already_picked_indexes, item_index)
        total_cost += max_cost
    print("--- Non genetic algorithm\'s execution time = %s seconds ---" % (time.time() - start_time))
    print('Non genetic algorithm\'s final result =', total_cost)
    return total_cost


def genetic_algorithm(task,
                      crossover_rate=CROSSOVER_RATE, mutation_rate=MUTATION_RATE,
                      tournament_size=TOURNAMENT_SIZE, population_size=POPULATION_SIZE):
    best_individuals_values = np.empty(MAX_ITERATIONS)
    start_time = time.time()

    population = init_population(task, population_size)
    outer_iterator = 0
    best_individual = 0
    best_individual_value = 0
    global_best_individual = 0
    global_best_individual_value = 0
    while outer_iterator < MAX_ITERATIONS:
        inner_iterator = 0
        new_population = Population()
        while inner_iterator < population_size:
            parent1 = tournament(population, tournament_size)
            parent2 = tournament(population, tournament_size)
            child = crossover(parent1, parent2, crossover_rate)
            mutate(child, mutation_rate)
            new_population.add_individual(child)
            inner_iterator += 1
        best_individual = population.best_individual()
        best_individual_value = best_individual.evaluate()
        if best_individual_value >= global_best_individual_value:
            global_best_individual = best_individual
            global_best_individual_value = best_individual_value
        new_population.set_first_individual(global_best_individual)
        population = new_population
        best_individuals_values[outer_iterator] = global_best_individual_value
        outer_iterator += 1
    print("--- Genetic algorithm\'s execution time = %s seconds ---" % (time.time() - start_time))
    print('Genetic algorithm\'s final result =', global_best_individual_value)


main()
