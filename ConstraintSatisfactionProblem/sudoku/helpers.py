from sudoku.Board import update_values
from sudoku.domains_helpers import update_fields
from sudoku.fields_helpers import find_empty_field, is_field_valid, find_best_field


def backtracking(board):
    empty_field = find_empty_field(board)
    if not empty_field:
        print('That is the last field!')
        return True
    else:
        field = empty_field

    for value in range(1, 10):
        if is_field_valid(board, field, value):
            field.value = value
            update_values(board, field, value, False)

            if backtracking(board):
                return True
            field.value = 0
            board.backtrack_steps += 1
            update_values(board, field, value, True)

    return False


def forward_checking(board):
    best_field = find_best_field(board)
    if not best_field:
        print('That is the last field!')
        return True
    else:
        field = best_field

    for value in field.domain:
        field.value = value
        update_values(board, field, value, False)
        is_wipe_out = update_fields(board, field, value, True)

        if not is_wipe_out:
            if forward_checking(board):
                return True

        field.value = 0
        board.backtrack_steps += 1
        update_values(board, field, value, True)
        update_fields(board, field, value, False)

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
