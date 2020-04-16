import numpy as np

from Column import Column
from Field import Field
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
