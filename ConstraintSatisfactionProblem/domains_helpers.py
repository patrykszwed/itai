import numpy as np


def print_board(rows):
    for i in range(len(rows)):
        row_fields = rows[i].fields
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(row_fields)):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(row_fields[j].value)
            else:
                print(str(row_fields[j].value) + " ", end="")


def print_domains(rows):
    for i in range(len(rows)):
        row_fields = rows[i].fields
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(row_fields)):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(row_fields[j].domain)
            else:
                print(str(row_fields[j].domain) + " ", end="")


def is_domain_wipe_out(fields, value):
    for field in fields:
        if len(field.domain) == 1 and field.value == 0 and field.domain[0] == value:
            return True
    return False


def remove_value_from_fields_domains(board, field, value):
    x = field.x
    y = field.y
    subgrid_index = field.subgrid_index
    row = board.rows[y]
    column = board.columns[x]
    subgrid = board.subgrids[subgrid_index]
    fields_to_check = np.concatenate([row.fields, column.fields, subgrid.fields])
    unique_fields_to_check = {e for e in fields_to_check}
    return update_fields_domains(board, unique_fields_to_check, True, value)


def load_previous_domains(board, field, value):
    x = field.x
    y = field.y
    subgrid_index = field.subgrid_index
    row = board.rows[y]
    column = board.columns[x]
    subgrid = board.subgrids[subgrid_index]
    fields_to_check = np.concatenate([row.fields, column.fields, subgrid.fields])
    return update_fields_domains(board, fields_to_check, False, value)


def update_fields_domains(board, fields, is_remove, value):
    if is_remove:
        if is_domain_wipe_out(fields, value):
            return True
        for field in fields:
            remove_value_from_domain(field, value)
        add_domains_copies_for_board(board, fields)
        board.domains_index += 1
    else:
        board.domains_index -= 1
        restore_previous_domains_copies_for_board(board)
    return False


def restore_previous_domains_copies_for_board(board):
    index = board.domains_index
    for field in board.fields:
        field.domain = field.domains_copy[index]


def add_domains_copies_for_board(board, fields):
    for field in board.fields:
        if field not in fields:
            field.append_domain_copy(field.domain)


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
    field.append_domain_copy(field.domain)


def init_fields_domains(board):
    rows = board.rows
    for i in range(len(rows)):
        fields = rows[i].fields
        for field in fields:
            x = field.x
            y = field.y
            subgrid_index = field.subgrid_index
            column = board.columns[x]
            row = board.rows[y]
            subgrid = board.subgrids[subgrid_index]
            field.init_domain(row, column, subgrid)
