import numpy as np


class Population:
    n_items = 0
    individuals = np.asarray(0)

    def __init__(self, n_items=0, individuals=None):
        if individuals is None:
            individuals = np.asarray(0)
        self.n_items = n_items
        self.individuals = np.asarray(individuals)

    def add_individual(self, individual_to_add):
        self.individuals = np.append(self.individuals, individual_to_add)

    def set_first_individual(self, individual_to_set):
        self.individuals[0] = individual_to_set

    def best_individual(self):
        best_individual_value = 0
        best_individual = 0
        for individual in self.individuals:
            individual_value = individual.evaluate()
            if individual_value >= best_individual_value:
                best_individual_value = individual_value
                best_individual = individual
        return best_individual
