from Board import update_values


def back_tracking(board):
    empty_field = find_empty_field(board)
    if not empty_field:
        print('That is the last field!')
        return True
    else:
        field = empty_field

    for i in range(1, 10):
        # print_board(board.rows)
        if is_field_valid(board, field, i):
            field.value = i
            update_values(board, field, False, i)

            if back_tracking(board):
                return True
            field.value = 0
            update_values(board, field, True, i)

    return False


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
    # print('field.x', field.x)
    # print('field.y', field.y)
    # print('row', row)
    # print('column', column)
    # print('subgrid', subgrid)
    # print('value', value)
    # print('value in row', value in row)
    # print('value in column', value in column)
    # print('value in subgrid', value in subgrid)
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
