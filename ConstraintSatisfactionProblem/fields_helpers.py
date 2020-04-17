import numpy as np


def is_field_valid(board, field, value):
    row = board.rows[field.y]
    column = board.columns[field.x]
    subgrid = board.subgrids[field.subgrid_index]
    fields = np.concatenate([row.fields, column.fields, subgrid.fields])
    unique_fields_values = {field.value for field in fields}
    return value in unique_fields_values


def find_best_field(board):
    min_len = 10
    field_to_return = None
    for field in board.fields:
        domain_length = len(field.domain)
        if field.value == 0 and domain_length > 0:
            if domain_length == 1:
                return field
            if domain_length < min_len:
                field_to_return = field
    return field_to_return


def find_empty_field(rows):
    for i in range(len(rows)):
        fields = rows[i].fields
        for j in range(len(fields)):
            field = fields[j]
            if field.value == 0:
                return field
    return None
