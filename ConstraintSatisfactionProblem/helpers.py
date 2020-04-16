from Board import update_values
from domains_helpers import remove_value_from_fields_domains, add_value_to_fields_domains, is_domain_wipe_out_v3


def backtracking(board):
    empty_field = find_empty_field(board.rows)
    if not empty_field:
        print('That is the last field!')
        return True
    else:
        field = empty_field

    for i in range(1, 10):
        if is_field_valid(board, field, i):
            field.value = i
            update_values(board, field, False, i)

            if backtracking(board):
                return True
            field.value = 0
            board.backtrack_steps += 1
            update_values(board, field, True, i)

    return False


def forward_checking(board):
    empty_field = find_empty_field(board.rows)
    if not empty_field:
        print('That is the last field!')
        return True
    else:
        field = empty_field

    for value in range(1, 10):
        # print('value', value)
        if is_field_valid(board, field, value):
            field.value = value
            update_values(board, field, False, value)
            is_wipe_out_new = remove_value_from_fields_domains(board, field, value)
            # print('is_wipe_out_new', is_wipe_out_new)
            is_wipe_out_old = is_domain_wipe_out_v3(board, field, value)
            # print('is_wipe_out_old', is_wipe_out_old)
            # if is_wipe_out_old != is_wipe_out_new:
            #     print('is_wipe_out_new', is_wipe_out_new)
            #     print('is_wipe_out_old', is_wipe_out_old)
            #     print_domains(board.rows)
            if not is_wipe_out_old:
                if forward_checking(board):
                    return True

            field.value = 0
            board.backtrack_steps += 1
            update_values(board, field, True, value)
            add_value_to_fields_domains(board, field, value)

    return False


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


def is_field_valid(board, field, value):
    row = board.rows[field.y]
    column = board.columns[field.x]
    subgrid = board.subgrids[field.subgrid_index]
    if is_fields_array_contains_value(row.fields, value) \
            or is_fields_array_contains_value(column.fields, value) \
            or is_fields_array_contains_value(subgrid.fields, value):
        return False
    return True


def is_fields_array_contains_value(fields, value):
    for i in range(9):
        if value == fields[i].value:
            return True
    return False


def find_empty_field(rows):
    for i in range(len(rows)):
        fields = rows[i].fields
        for j in range(len(fields)):
            field = fields[j]
            if field.value == 0:
                return field
    return None
