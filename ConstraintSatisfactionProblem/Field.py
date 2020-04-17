import numpy as np

from domains_helpers import get_fields_values


class Field:
    def __init__(self, value, x, y, subgrid_index):
        self.value = int(value)
        self.x = x
        self.y = y
        self.subgrid_index = subgrid_index
        self.domain = []
        self.domains_copy = []

    def init_domain(self, row, column, subgrid):
        initial_domain = []
        domain_to_check = np.concatenate(
            [get_fields_values(row), get_fields_values(column), get_fields_values(subgrid)])
        for value in range(1, 10):
            if value not in domain_to_check:
                initial_domain.append(value)
        self.domain = np.asarray(initial_domain)
        self.append_domain_copy(self.domain)

    def append_domain_copy(self, domain):
        self.domains_copy.append(domain)

    # def get_last_domain_copy(self):
    #     return self.domains_copy[len(self.domains_copy) - 1]
    #
    # def delete_last_domain_copy(self):
    #     self.domains_copy.pop(len(self.domains_copy) - 1)
    #
    # def pop_domain_copy(self):
    #     # if len(self.domains_copy) > 1:
    #     return self.domains_copy.pop(len(self.domains_copy) - 1)
    #     # return self.domains_copy[0]

    def print(self):
        print('Field location: [', self.x, ',', self.y, '], value:', self.value)

    value = 0
    x = 0
    y = 0
    subgrid_index = 0
    domain = 0
    domains_copy = 0
