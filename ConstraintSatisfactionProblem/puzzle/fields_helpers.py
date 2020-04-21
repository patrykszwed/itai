def is_word_valid(fields, word):
    # print('is_word_valid word', word)
    # print('len(word)', len(word))
    # print('len(fields)', len(fields))
    if len(fields) == len(word):
        for i in range(len(fields)):
            field = fields[i]
            if field.value != '_' and field.value != word[i]:
                return False
        return True
    return False


def find_empty_fields_in_structure(structure):
    fields = []
    longest_fields = []
    longest_fields_count = 0
    for elem in structure:
        # print('len(elem.fields)', len(elem.fields))
        for field in elem.fields:
            # print('field.value', field.value)
            if field.value != '#':
                fields.append(field)
            else:
                fields_count = len(fields)
                # print('There is #')
                # print('fields_count', fields_count)
                if fields_count > 0 and fields_count >= longest_fields_count:
                    if fields_count > longest_fields_count:
                        longest_fields = []
                    longest_fields.append(fields)
                    longest_fields_count = fields_count
                fields = []
                continue
        fields_count = len(fields)
        # print('After loop len(fields)', len(fields))
        # print('longest_fields_count', longest_fields_count)
        if fields_count > 0 and fields_count >= longest_fields_count:
            if fields_count > longest_fields_count:
                longest_fields = []
            longest_fields.append(fields)
            longest_fields_count = fields_count
        fields = []
    return longest_fields


def check_if_crossword_is_filled(crossword):
    for field in crossword.fields:
        print('field.value', field.value)
        if field.value == '_':
            return False
    return True


def find_empty_fields(crossword):
    is_crossword_filled = check_if_crossword_is_filled(crossword)
    print('is_crossword_filled', is_crossword_filled)
    if is_crossword_filled:
        return None
    rows_empty_fields = find_empty_fields_in_structure(crossword.rows)
    columns_empty_fields = find_empty_fields_in_structure(crossword.columns)
    # print('rows_empty_fields', rows_empty_fields)
    # print('len(rows_empty_fields)', len(rows_empty_fields))
    crossword_empty_fields = rows_empty_fields + columns_empty_fields
    # print('crossword_empty_fields', crossword_empty_fields)
    return crossword_empty_fields
