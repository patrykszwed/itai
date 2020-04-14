from Board import update_values, update_fields_domains


def back_tracking(board, back_track_steps):
    empty_field = find_empty_field(board)
    if not empty_field:
        print('That is the last field!')
        return True, back_track_steps
    else:
        field = empty_field

    for i in range(1, 10):
        if is_field_valid(board, field, i):
            field.value = i
            update_values(board, field, False, i)

            if back_tracking(board, back_track_steps)[0]:
                return True, back_track_steps
            field.value = 0
            back_track_steps += 1
            update_values(board, field, True, i)

    return False, back_track_steps


def forward_checking(board, back_track_steps):
    empty_field = find_empty_field(board)
    if not empty_field:
        print('That is the last field!')
        return True, back_track_steps
    else:
        field = empty_field

    for i in range(1, 10):
        if field.domain[i - 1] != -1:
            field.value = i
            update_values(board, field, False, i)
            update_fields_domains(board, field, False, i)

            if forward_checking(board, back_track_steps)[0]:
                return True, back_track_steps
            field.value = 0
            back_track_steps += 1
            update_values(board, field, True, i)
            update_fields_domains(board, field, True, i)

    return False, back_track_steps


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def is_field_valid(board, field, value):
    row = board.rows[field.y]
    column = board.columns[field.x]
    subgrid = board.subgrids[field.subgrid_index]
    if value in row or value in column or value in subgrid:
        return False
    return True


def find_empty_field(board):
    fields = board.fields
    for i in range(len(fields)):
        field = fields[i]
        if field.value == 0:
            return field
    return None
