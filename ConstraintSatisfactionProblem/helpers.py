from Board import update_values
from domains_helpers import remove_value_from_fields_domains, is_field_valid, load_previous_domains


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
    empty_field = find_best_field(board)
    if not empty_field:
        print('That is the last field!')
        return True
    else:
        field = empty_field

    for value in field.domain:
        field.value = value
        update_values(board, field, False, value)
        is_wipe_out = remove_value_from_fields_domains(board, field, value)

        if not is_wipe_out:
            if forward_checking(board):
                return True
        # print('board.domains_index', board.domains_index)
        field.value = 0
        board.backtrack_steps += 1
        update_values(board, field, True, value)
        load_previous_domains(board, field, value)

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


def find_empty_field(rows):
    for i in range(len(rows)):
        fields = rows[i].fields
        for j in range(len(fields)):
            field = fields[j]
            if field.value == 0:
                return field
    return None
