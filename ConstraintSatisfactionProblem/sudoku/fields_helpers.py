from sudoku.domains_helpers import get_fields_values


def is_field_valid(board, field, value):
    row = board.rows[field.y]
    column = board.columns[field.x]
    subgrid = board.subgrids[field.subgrid_index]
    fields_values = get_fields_values(row) + get_fields_values(column) + get_fields_values(subgrid)
    return value not in fields_values


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


def find_empty_field(board):
    for field in board.fields:
        if field.value == 0:
            return field
    return None
