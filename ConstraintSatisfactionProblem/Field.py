import numpy as np


def is_field_valid(board, field, value):
    row = board.rows[field.y]
    column = board.columns[field.x]
    subgrid = board.subgrids[field.subgrid_index]
    fields = np.concatenate([row.fields, column.fields, subgrid.fields])
    unique_fields_values = {field.value for field in fields}
    if value in unique_fields_values:
        return False
    return True


def is_fields_array_contains_value(fields, value):
    for i in range(9):
        if value == fields[i].value:
            return True
    return False


def get_fields_values(structure):
    fields = structure.fields
    fields_values = []
    for i in range(len(fields)):
        fields_values.append(fields[i].value)
    return np.asarray(fields_values)


def add_value_to_domain(board, field, value):
    if value not in field.domain:
        if is_field_valid(board, field, value):
            field.domain = np.concatenate([field.domain, [value]])


def remove_value_from_domain(field, value):
    if value in field.domain:
        index = np.where(field.domain == value)[0][0]
        field.domain = np.delete(field.domain, index)


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
