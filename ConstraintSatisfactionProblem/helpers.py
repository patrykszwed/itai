from Board import update_values
from Field import is_field_valid
from domains_helpers import remove_value_from_fields_domains, add_value_to_fields_domains, is_domain_wipe_out


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

    for value in field.domain:
        field.value = value
        update_values(board, field, False, value)
        is_wipe_out_new = remove_value_from_fields_domains(board, field, value)
        is_wipe_out_old = is_domain_wipe_out(board, field, value)
        # if is_wipe_out_new != is_wipe_out_old:
        #     print('DIFFF')
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


def find_empty_field(rows):
    for i in range(len(rows)):
        fields = rows[i].fields
        for j in range(len(fields)):
            field = fields[j]
            if field.value == 0:
                return field
    return None
