def is_word_valid(fields, word):
    # print('is_word_valid word', word)
    # print('len(word)', len(word))
    # print('len(fields)', len(fields))
    return len(fields) == len(word)


def find_empty_fields(crossword):
    """ iterate over rows """
    fields = []
    for row in crossword.rows:
        for field in row.fields:
            if field.value == '_':
                fields.append(field)
            elif field.value == '#':
                fields = []
                break
        if len(fields) > 0:
            return fields

    """ iterate over columns """
    fields = []
    for column in crossword.columns:
        for field in column.fields:
            if field.value == '_':
                fields.append(field)
            elif field.value == '#':
                fields = []
                break
        if len(fields) > 0:
            return fields
    return None
