import numpy as np

from Field import add_value_to_domain, remove_value_from_domain


def is_domain_wipe_out(board, field, value):
    x = field.x
    y = field.y
    subgrid_index = field.subgrid_index
    row = board.rows[y]
    column = board.columns[x]
    subgrid = board.subgrids[subgrid_index]
    fields_to_check = row.fields.tolist() + column.fields.tolist() + subgrid.fields.tolist()
    for field in fields_to_check:
        if len(field.domain) == 1 and field.domain[0] == value:
            return True


def update_board_domains(board, fields, is_remove, value):
    if is_remove:
        is_wipe_out = False
        for field_to_update in fields:
            remove_value_from_domain(field_to_update, value)
        return is_wipe_out
    else:
        for field_to_update in fields:
            add_value_to_domain(board, field_to_update, value)
        return False


def remove_value_from_fields_domains(board, field, value):
    x = field.x
    y = field.y
    subgrid_index = field.subgrid_index
    row = board.rows[y]
    column = board.columns[x]
    subgrid = board.subgrids[subgrid_index]
    fields_to_check = np.concatenate(
        [row.fields, column.fields, subgrid.fields])
    return update_board_domains(board, fields_to_check, True, value)


def add_value_to_fields_domains(board, field, value):
    x = field.x
    y = field.y
    subgrid_index = field.subgrid_index
    row = board.rows[y]
    column = board.columns[x]
    subgrid = board.subgrids[subgrid_index]
    fields_to_check = np.concatenate(
        [row.fields, column.fields, subgrid.fields])
    return update_board_domains(board, fields_to_check, False, value)


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
