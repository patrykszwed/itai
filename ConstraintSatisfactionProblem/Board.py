import numpy as np

from Field import Field


def get_columns(rows):
    columns = list(range(9))
    for column_index in range(9):
        columns[column_index] = list(range(9))
        for row_index in range(len(rows)):
            columns[column_index][row_index] = rows[row_index][column_index]
    return np.asarray(columns)


def get_subgrids(rows):
    subgrids = np.zeros((9, 9), dtype=int)
    indexes_to_assign = np.zeros(9, dtype=int)

    for row_index in range(len(rows)):
        for column_index in range(len(rows)):
            number = rows[row_index][column_index]
            index = int(row_index / 3) * 3 + int(column_index / 3)
            index_to_assign = indexes_to_assign[index]
            subgrids[index][index_to_assign] = number
            indexes_to_assign[index] = indexes_to_assign[index] + 1
    return np.asarray(subgrids)


def get_fields(numbers):
    fields = np.empty(81, dtype=object)
    index = 0
    for i in range(9):
        for j in range(9):
            subgrid_index = int(i / 3) * 3 + int(j / 3)
            fields[index] = Field(numbers[index], j, i, subgrid_index)
            index = index + 1
    return fields


def update_values(board, field, is_set_to_zero, value):
    x = field.x
    y = field.y
    column = board.columns[x]
    column[y] = 0 if is_set_to_zero else value
    row = board.rows[y]
    row[x] = 0 if is_set_to_zero else value
    subgrid_index = int(y / 3) * 3 + int(x / 3)
    subgrid = board.subgrids[subgrid_index]
    # print('before update_subgrid value=', value, ' x=', x, ' y=', y)
    update_subgrid(subgrid, value, is_set_to_zero)


def init_fields_domains(board):
    fields = board.fields
    for field in fields:
        x = field.x
        y = field.y
        column = board.columns[x]
        row = board.rows[y]
        subgrid_index = int(y / 3) * 3 + int(x / 3)
        subgrid = board.subgrids[subgrid_index]
        field.set_domain(row, column, subgrid)


def update_fields_domains(board, field, is_set_to_zero, value):
    fields = board.fields
    for field_to_update in fields:
        x = field_to_update.x
        y = field_to_update.y
        subgrid_index = int(y / 3) * 3 + int(x / 3)
        # print('x', x)
        # print('field.x', field.x)
        # print('y', y)
        # print('field.y', field.y)
        # print('subgrid_index', subgrid_index)
        # print('field.subgrid_index', field.subgrid_index)
        if x == field.x or y == field.y or subgrid_index == field.subgrid_index:
            column = board.columns[x]
            row = board.rows[y]
            subgrid = board.subgrids[subgrid_index]
            field.set_domain(row, column, subgrid)
            # field_to_update.update_domain(row, column, subgrid, is_set_to_zero, value)


def update_subgrid(subgrid, value, is_set_to_zero):
    # print('update_subgrid is_set_to_zero =', is_set_to_zero, ' value =', value, ' subgrid=', subgrid)
    if is_set_to_zero:
        for i in range(len(subgrid)):
            if subgrid[i] == value:
                subgrid[i] = 0
                return
    else:
        for i in range(len(subgrid)):
            if subgrid[i] == 0:
                subgrid[i] = value
                return


class Board:
    def __init__(self, board_data):
        self.board_id = board_data[0]
        self.difficulty = int(float(board_data[1]))
        self.solution = board_data[3]

        board_data[2] = np.char.replace(board_data[2], '.', '0')
        strings_list = list(board_data[2])
        int_list = [int(numeric_string) for numeric_string in strings_list]
        numbers = np.array(int_list)

        self.rows = np.split(numbers, len(numbers) / 9)
        self.columns = get_columns(self.rows)
        self.subgrids = get_subgrids(self.rows)
        self.fields = get_fields(numbers)

    board_id = 0
    difficulty = 0
    solution = 0
    columns = np.empty(9)
    rows = np.empty(9)
    subgrids = np.empty(9)
    fields = np.empty(81)
