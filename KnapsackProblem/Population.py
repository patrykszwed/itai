import numpy as np


class Population:
    n_items = 0
    individuals = np.empty(n_items)

    def __init__(self, n_items=0, individuals=np.empty(0)):
        self.n_items = n_items
        self.individuals = individuals

    def add_individual(self, individual_to_add):
        self.individuals = np.append(self.individuals, individual_to_add)

    def best_individual(self):
        best_individual_value = 0
        best_individual = 0
        for individual in self.individuals:
            individual_value = individual.evaluate()
            if individual_value > best_individual_value:
                best_individual_value = individual_value
                best_individual = individual
        return best_individual
