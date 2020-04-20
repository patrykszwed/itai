import numpy as np

from sudoku.Column import Column
from sudoku.Field import Field
from sudoku.Row import Row
from sudoku.Subgrid import Subgrid


def update_subgrid(subgrid_fields, value, is_set_to_zero):
    value_to_search = value if is_set_to_zero else 0
    value_to_set = 0 if is_set_to_zero else value
    for subgrid_field in subgrid_fields:
        if subgrid_field == value_to_search:
            subgrid_field.value = value_to_set
            return


def update_values(board, field, value, is_set_to_zero):
    column = board.columns[field.x]
    column.fields[field.y].value = 0 if is_set_to_zero else value
    row = board.rows[field.y]
    row.fields[field.x].value = 0 if is_set_to_zero else value
    subgrid = board.subgrids[field.subgrid_index]
    update_subgrid(subgrid.fields, value, is_set_to_zero)


def get_rows(numbers):
    rows = []
    index = 0
    for i in range(9):
        fields = []
        for j in range(9):
            subgrid_index = int(i / 3) * 3 + int(j / 3)
            fields.append(Field(numbers[index], j, i, subgrid_index))
            index += 1
        rows.append(Row(i, fields))
    return rows


def get_columns(rows):
    fields = []
    for i in range(9):
        fields.append([])
    for i in range(9):
        row_fields = rows[i].fields
        for j in range(len(row_fields)):
            fields[j].append(row_fields[j])
    columns = []
    for i in range(9):
        columns.append(Column(i, fields[i]))
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
    subgrids = []
    for i in range(9):
        subgrids.append(Subgrid(i, fields[i]))
    return subgrids


def get_fields(rows):
    fields = []
    for i in range(9):
        row_fields = rows[i].fields
        for j in range(len(row_fields)):
            fields.append(row_fields[j])
    return fields


class Board:
    def __init__(self, board_data):
        self.difficulty = int(float(board_data[1]))
        self.solution = board_data[3]

        board_data[2] = np.char.replace(board_data[2], '.', '0')
        strings_list = list(board_data[2])
        int_list = [int(numeric_string) for numeric_string in strings_list]
        numbers = int_list

        self.rows = get_rows(numbers)
        self.columns = get_columns(self.rows)
        self.subgrids = get_subgrids(self.rows)
        self.fields = get_fields(self.rows)

    difficulty = 0
    solution = 0
    columns = []
    rows = []
    subgrids = []
    fields = []
    backtrack_steps = 0
