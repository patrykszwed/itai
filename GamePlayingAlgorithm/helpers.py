def print_board(board):
    fields = board.fields
    print('')
    print('Board state:')
    for i in range(len(fields)):
        for j in range(len(fields)):
            field = fields[i][j]

            if j == 9:
                if field.value == '_':
                    print('', field.value)
                else:
                    print(field.value)
            else:
                if field.value == '_':
                    print('', field.value + " ", end="")
                else:
                    print(field.value + " ", end="")


def print_board_fields(fields):
    print('')
    for i in range(len(fields)):
        for j in range(len(fields)):
            field = fields[i][j]

            if j == 9:
                if field.value == '_':
                    print('', field.value)
                else:
                    print(field.value)
            else:
                if field.value == '_':
                    print('', field.value + " ", end="")
                else:
                    print(field.value + " ", end="")
