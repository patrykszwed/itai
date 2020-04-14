import numpy as np


class Field:
    def __init__(self, value, x, y, subgrid_index):
        self.value = int(value)
        self.x = x
        self.y = y
        self.subgrid_index = subgrid_index

    def set_domain(self, row, column, subgrid):
        initial_domain = np.asarray(list(range(1, 10)))
        domain_to_check = np.concatenate([row, column, subgrid])
        # print('set_domain for row =', row, ' column =', column, ' subgrid =', subgrid)
        print('domain_to_check', domain_to_check)
        for i in range(9):
            value = initial_domain[i]
            if value in domain_to_check:
                initial_domain[i] = -1
        print('set domain to', initial_domain)
        self.domain = initial_domain

    def update_domain(self, row, column, subgrid, is_set_to_zero, value):
        self.domain[value - 1] = value if is_set_to_zero else -1

    def add_value_to_domain(self, value):
        print('Before add_value_to_domain value = ', value, ' domain = ', self.domain)
        self.domain[value - 1] = value
        print('After add_value_to_domain domain = ', self.domain)

    def remove_value_from_domain(self, value):
        print('Before remove_value_from_domain value = ', value, ' domain = ', self.domain)
        self.domain[value - 1] = -1
        print('After remove_value_from_domain domain = ', self.domain)

    value = 0
    x = 0
    y = 0
    subgrid_index = 0
    domain = 0
