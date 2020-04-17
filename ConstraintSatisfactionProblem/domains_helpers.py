def is_domain_wipe_out(fields, value):
    for field in fields:
        if len(field.domain) == 1 and field.value == 0 and field.domain[0] == value:
            return True
    return False


def update_fields(board, field, value, check_for_wipe_out):
    row = board.rows[field.y]
    column = board.columns[field.x]
    subgrid = board.subgrids[field.subgrid_index]
    fields_to_check = set(row.fields + column.fields + subgrid.fields)
    if check_for_wipe_out:
        if is_domain_wipe_out(fields_to_check, value):
            return True
    update_fields_domains(board, fields_to_check)
    return False


def update_fields_domains(board, fields):
    for field in fields:
        column = board.columns[field.x]
        row = board.rows[field.y]
        subgrid = board.subgrids[field.subgrid_index]
        field.calculate_domain(row, column, subgrid)


def get_fields_values(structure):
    fields_values = []
    for field in structure.fields:
        fields_values.append(field.value)
    return fields_values


def init_fields_domains(board):
    for field in board.fields:
        column = board.columns[field.x]
        row = board.rows[field.y]
        subgrid = board.subgrids[field.subgrid_index]
        field.calculate_domain(row, column, subgrid)
