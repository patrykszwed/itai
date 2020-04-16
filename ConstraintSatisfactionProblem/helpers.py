from Board import update_values, is_domain_wipe_out, remove_value_from_fields_domains, add_value_to_fields_domains


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
        if is_field_valid(board, field, value):
            field.value = value
            update_values(board, field, False, value)
            remove_value_from_fields_domains(board, field, value)

            if not is_domain_wipe_out(board, field):
                if forward_checking(board):
                    return True

            field.value = 0
            board.backtrack_steps += 1
            update_values(board, field, True, value)
            add_value_to_fields_domains(board, field, value)

    return False


# def forward_checking(board):
#     empty_field = find_empty_field(board.rows)
#     if not empty_field:
#         print('That is the last field!')
#         return True
#     else:
#         field = empty_field
#
#     # print('field x', field.x, ' field y', field.y)
#     # print('field.domain', field.domain)
#     if len(field.domain) == 0:
#         print('DOMAIN WIPE OUT for x', field.x, ' y', field.y)
#         print('field.domain_copy', field.domain_copy)
#         # field.domain_copy = np.setdiff1d(field.domain_copy, [field.domain_copy[0]])
#         field.domain = field.domain_copy
#         field.value = 0
#         board.backtrack_steps += 1
#
#         update_values(board, field, True, value)
#         update_fields_domains(board, field, False, value)
#         domain_wipe_out = True
#         # print('domain_copy', domain_copy)
#     for value in field.domain:
#         # print('value', value)
#         field.value = value
#         domain_wipe_out = False
#         print('field.domain', field.domain)
#         update_values(board, field, False, value)
#         update_fields_domains(board, field, True, value)
#
#         print('field.domain_copy', field.domain_copy)
#
#         if forward_checking(board):
#             return True
#         # print('NOT WORKING!')
#         # print_board(board.rows)
#
#     return False


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
