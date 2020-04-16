import numpy as np


def get_fields_values(structure):
    fields = structure.fields
    fields_values = []
    for i in range(len(fields)):
        fields_values.append(fields[i].value)
    return np.asarray(fields_values)


def add_value_to_domain(field, value):
    # print('Before add_value_to_domain value = ', value, ' domain = ', field.domain)
    if value not in field.domain:
        field.domain = np.concatenate([field.domain, [value]])
    # print('After add_value_to_domain domain = ', field.domain)


def remove_value_from_domain(field, value):
    # print('Before remove_value_from_domain value = ', value, ' domain = ', field.domain)
    if value in field.domain:
        # field.domain = np.setdiff1d(field.domain, [field.domain[0]])
        # print('field.domain', field.domain)
        index = np.where(field.domain == value)[0][0]
        # print('index', index)
        field.domain = np.delete(field.domain, index)
    # print('After remove_value_from_domain domain = ', field.domain)


class Field:
    def __init__(self, value, x, y, subgrid_index):
        self.value = int(value)
        self.x = x
        self.y = y
        self.subgrid_index = subgrid_index

    def init_domain(self, row, column, subgrid):
        initial_domain = []
        domain_to_check = np.concatenate(
            [get_fields_values(row), get_fields_values(column), get_fields_values(subgrid)])
        for value in range(1, 10):
            if value not in domain_to_check:
                initial_domain.append(value)
        self.domain = np.asarray(initial_domain)

    value = 0
    x = 0
    y = 0
    subgrid_index = 0
    domain = 0
