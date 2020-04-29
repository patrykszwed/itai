from Field import Field


def place_players_pieces(fields):
    pieces_count = 0
    all_pieces_placed = False
    for i in range(len(fields)):
        if all_pieces_placed:
            break
        for field in fields[i]:
            if field.value == '_':
                field.value = 'P2'
                pieces_count += 1
                if pieces_count == 20:
                    all_pieces_placed = True
                    break

    # [[print('single_field.value', single_field.value) for single_field in field] for field in fields]
    # print('new')
    # [[print('single_field.value', single_field.value) for single_field in field] for field in reversed(fields)]
    pieces_count = 0
    all_pieces_placed = False
    for row_fields in reversed(fields):
        if all_pieces_placed:
            break
        for field in row_fields:
            if field.value == '_':
                field.value = 'P1'
                pieces_count += 1
                if pieces_count == 20:
                    all_pieces_placed = True
                    break
    return fields


def get_fields():
    all_fields = []
    index = 0
    for i in range(10):
        fields = []
        for j in range(10):
            initial_value = '_' if (i + j) % 2 != 0 else ' '
            fields.append(Field(initial_value, j, i))
            index += 1
        all_fields.append(fields)

    return place_players_pieces(all_fields)


class Board:
    def __init__(self):
        self.fields = get_fields()

    fields = []
