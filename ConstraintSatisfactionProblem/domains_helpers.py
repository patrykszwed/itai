import numpy as np

from Field import add_value_to_domain, remove_value_from_domain


def is_domain_wipe_out(board, field):
    x = field.x
    y = field.y
    subgrid_index = int(y / 3) * 3 + int(x / 3)
    row = board.rows[y]
    column = board.columns[x]
    subgrid = board.subgrids[subgrid_index]
    fields_to_check = np.concatenate(
        [row.fields, column.fields, subgrid.fields])
    unique_fields_to_check = {e for e in fields_to_check}
    for field in unique_fields_to_check:
        if len(field.domain) == 0:
            return True


def is_domain_wipe_out_v4(board, field, value):
    fields = board.fields
    for field_to_update in fields:
        x = field_to_update.x
        y = field_to_update.y
        subgrid_index = int(y / 3) * 3 + int(x / 3)
        row = board.rows[y]
        column = board.columns[x]
        subgrid = board.subgrids[subgrid_index]
        fields_to_check = np.concatenate(
            [row.fields, column.fields, subgrid.fields])
        unique_fields_to_check = {e for e in fields_to_check}
        for field in unique_fields_to_check:
            if len(field.domain) == 1 and field.domain[0] == value:
                return True


def is_domain_wipe_out_v3(board, field, value):
    fields = board.fields
    for field_to_update in fields:
        x = field_to_update.x
        y = field_to_update.y
        subgrid_index = int(y / 3) * 3 + int(x / 3)
        if x == field.x or y == field.y or subgrid_index == field.subgrid_index:
            if len(field.domain) == 1 and field.domain[0] == value:
                return True
    return False


def is_domain_wipe_out_v2(board, field, value):
    x = field.x
    y = field.y
    subgrid_index = int(y / 3) * 3 + int(x / 3)
    row = board.rows[y]
    column = board.columns[x]
    subgrid = board.subgrids[subgrid_index]
    fields_to_check = np.concatenate(
        [row.fields, column.fields, subgrid.fields])
    unique_fields_to_check = {e for e in fields_to_check}
    for field in unique_fields_to_check:
        if len(field.domain) == 1 and field.domain[0] == value:
            return True


def remove_value_from_fields_domains(board, field, value):
    x = field.x
    y = field.y
    subgrid_index = int(y / 3) * 3 + int(x / 3)
    row = board.rows[y]
    column = board.columns[x]
    subgrid = board.subgrids[subgrid_index]
    fields_to_check = np.concatenate(
        [row.fields, column.fields, subgrid.fields])
    # print('len(fields_to_check)', len(fields_to_check))
    unique_fields_to_check = {e for e in fields_to_check}
    # print('len(unique_fields_to_check)', len(unique_fields_to_check))
    return update_board_domains(unique_fields_to_check, True, value)


def add_value_to_fields_domains(board, field, value):
    # print('update_fields_domain value', value)
    x = field.x
    y = field.y
    subgrid_index = int(y / 3) * 3 + int(x / 3)
    row = board.rows[y]
    column = board.columns[x]
    subgrid = board.subgrids[subgrid_index]
    fields_to_check = np.concatenate(
        [row.fields, column.fields, subgrid.fields])
    unique_fields_to_check = {e for e in fields_to_check}
    # print('update unique_fields_to_check', [(field.x, field.y) for field in unique_fields_to_check])

    return update_board_domains(unique_fields_to_check, False, value)


def update_board_domains(fields, is_remove, value):
    function_to_call = remove_value_from_domain if is_remove else add_value_to_domain
    is_wipe_out = False
    for field_to_update in fields:
        # if is_remove:
        #     print('REMOVE value = ', value)
        #     print('Before remove domain', field_to_update.domain)
        if len(field_to_update.domain) == 0:
            is_wipe_out = True
        # print('Before update domain', field_to_update.domain)
        function_to_call(field_to_update, value)
        # if is_remove:
        #     print('After remove domain', field_to_update.domain)
        # print('After update domain', field_to_update.domain)
    return is_wipe_out


def init_fields_domains(board):
    rows = board.rows
    for i in range(len(rows)):
        fields = rows[i].fields
        for field in fields:
            x = field.x
            y = field.y
            column = board.columns[x]
            row = board.rows[y]
            subgrid_index = int(y / 3) * 3 + int(x / 3)
            subgrid = board.subgrids[subgrid_index]
            field.init_domain(row, column, subgrid)
