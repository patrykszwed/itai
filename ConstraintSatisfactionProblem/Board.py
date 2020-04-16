import numpy as np

from Column import Column
from Field import Field, add_value_to_domain, remove_value_from_domain
from Row import Row
from Subgrid import Subgrid


def update_subgrid(subgrid_fields, value, is_set_to_zero):
    value_to_search = value if is_set_to_zero else 0
    value_to_set = 0 if is_set_to_zero else value
    for i in range(len(subgrid_fields)):
        if subgrid_fields[i] == value_to_search:
            subgrid_fields[i].value = value_to_set
            return


def update_values(board, field, is_set_to_zero, value):
    x = field.x
    y = field.y
    column = board.columns[x]
    column.fields[y].value = 0 if is_set_to_zero else value
    row = board.rows[y]
    row.fields[x].value = 0 if is_set_to_zero else value
    subgrid_index = int(y / 3) * 3 + int(x / 3)
    subgrid = board.subgrids[subgrid_index]
    update_subgrid(subgrid.fields, value, is_set_to_zero)


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


def is_domain_wipe_out_v3(board, field, value):
    fields = board.fields
    for field_to_update in fields:
        x = field_to_update.x
        y = field_to_update.y
        subgrid_index = int(y / 3) * 3 + int(x / 3)
        if x == field.x or y == field.y or subgrid_index == field.subgrid_index:
            if len(field.domain) == 1 and field.domain[0] == value:
                return True


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


def reset_fields_domains(board):
    # print('update_fields_domain value', value)
    for i in range(9):
        row = board.rows[i]
        column = board.columns[i]
        subgrid = board.subgrids[i]
        fields_to_check = np.concatenate(
            [row.fields, column.fields, subgrid.fields])
        unique_fields_to_check = {e for e in fields_to_check}
        print('----------------RESET')
        update_board_domains(unique_fields_to_check, )


def update_fields_domains(board, field, is_remove, value):
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

    update_board_domains(unique_fields_to_check, is_remove, value)


def remove_value_from_fields_domains(board, field, value):
    x = field.x
    y = field.y
    subgrid_index = int(y / 3) * 3 + int(x / 3)
    row = board.rows[y]
    column = board.columns[x]
    subgrid = board.subgrids[subgrid_index]
    fields_to_check = np.concatenate(
        [row.fields, column.fields, subgrid.fields])
    unique_fields_to_check = {e for e in fields_to_check}

    update_board_domains(unique_fields_to_check, True, value)


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

    update_board_domains(unique_fields_to_check, False, value)


def get_all_fields_domains_from_board(board):
    fields = []
    for i in range(9):
        row = board.rows[i]
        column = board.columns[i]
        subgrid = board.subgrids[i]
        fields_to_check = np.concatenate(
            [row.fields, column.fields, subgrid.fields])
        unique_fields_to_check = {e for e in fields_to_check}
        fields.append([field.domain for field in unique_fields_to_check])


def update_board_domains(fields, is_remove, value):
    function_to_call = remove_value_from_domain if is_remove else add_value_to_domain
    for field_to_update in fields:
        # print('Before update domain', field_to_update.domain)
        function_to_call(field_to_update, value)
        # print('After update domain', field_to_update.domain)


# def update_fields_domains(board, field, is_remove, value):
#     # print('update_fields_domain value', value)
#     x = field.x
#     y = field.y
#     subgrid_index = int(y / 3) * 3 + int(x / 3)
#     row = board.rows[y]
#     column = board.columns[x]
#     subgrid = board.subgrids[subgrid_index]
#     fields_to_check = np.concatenate(
#         [row.fields, column.fields, subgrid.fields])
#     unique_fields_to_check = {e for e in fields_to_check}
#     # print('update unique_fields_to_check', [(field.x, field.y) for field in unique_fields_to_check])
#
#     # update_structure_domains(unique_fields_to_check, row, column, subgrid)

# def update_structure_domains(fields, row, column, subgrid):
#     for field_to_update in fields:
#         print('Before update domain', field_to_update.domain)
#         field_to_update.set_domain(row, column, subgrid)
#         print('After update domain', field_to_update.domain)

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


def get_rows(numbers):
    rows = np.empty(9, dtype=object)
    index = 0
    for i in range(9):
        fields = np.empty(9, dtype=object)
        for j in range(9):
            subgrid_index = int(i / 3) * 3 + int(j / 3)
            fields[j] = Field(numbers[index], j, i, subgrid_index)
            index += 1
        rows[i] = Row(i, fields)
    return rows


def get_columns(rows):
    fields = []
    for i in range(9):
        fields.append([])
    for i in range(9):
        row_fields = rows[i].fields
        for j in range(len(row_fields)):
            fields[j].append(row_fields[j])
    columns = np.empty(9, dtype=object)
    for i in range(9):
        columns[i] = Column(i, fields[i])
    return columns


def get_subgrids(rows):
    fields = []
    for i in range(9):
        fields.append([])

    for i in range(9):
        row_fields = rows[i].fields
        for j in range(len(row_fields)):
            index = int(i / 3) * 3 + int(j / 3)
            fields[index].append(row_fields[j])
    subgrids = np.empty(9, dtype=object)
    for i in range(9):
        subgrids[i] = Subgrid(i, fields[i])
    return subgrids


def get_fields(rows):
    fields = []
    for i in range(9):
        row_fields = rows[i].fields
        for j in range(len(row_fields)):
            fields.append(row_fields[j])
    return np.asarray(fields)


class Board:
    def __init__(self, board_data):
        self.difficulty = int(float(board_data[1]))
        self.solution = board_data[3]

        board_data[2] = np.char.replace(board_data[2], '.', '0')
        strings_list = list(board_data[2])
        int_list = [int(numeric_string) for numeric_string in strings_list]
        numbers = np.array(int_list)

        self.rows = get_rows(numbers)
        self.columns = get_columns(self.rows)
        self.subgrids = get_subgrids(self.rows)
        self.fields = get_fields(self.rows)

    difficulty = 0
    solution = 0
    columns = np.empty(9)
    rows = np.empty(9)
    subgrids = np.empty(9)
    fields = np.empty(81)
    backtrack_steps = 0
    domain_wipe_out = False
