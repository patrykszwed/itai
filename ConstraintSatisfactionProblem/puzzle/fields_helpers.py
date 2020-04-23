def is_word_valid(fields, word):
    if len(fields) == len(word):
        for i in range(len(fields)):
            field = fields[i]
            if field.value != '_' and field.value != word[i]:
                return False
        return True
    return False


def all_words_are_on_the_board(crossword):
    for word in crossword.words:
        word_value = word.value
        if not is_word_anywhere_on_the_board(crossword, word_value):
            return False
    return True


def is_field_in_structure(structure, word):
    word_length = len(word)
    for elem in structure:
        fields = []
        for field in elem.fields:
            if field.value != '#':
                fields.append(field)
            else:
                if len(fields) == word_length:
                    is_found = True
                    for i in range(len(fields)):
                        if fields[i].value != word[i]:
                            is_found = False
                            break
                    if is_found:
                        return True
                fields = []
        if len(fields) == word_length:
            is_found = True
            for i in range(len(fields)):
                if fields[i].value != word[i]:
                    is_found = False
                    break
            if is_found:
                return True
    return False


def is_word_anywhere_on_the_board(crossword, word_value):
    is_field_in_rows = is_field_in_structure(crossword.rows, word_value)
    if is_field_in_rows:
        return True
    return is_field_in_structure(crossword.columns, word_value)


def is_all_fields_filled(fields):
    for field in fields:
        if field.value == '_':
            return False
    return True


def check_if_crossword_is_filled(crossword):
    for field in crossword.fields:
        if field.value == '_':
            return False
    return True


def find_empty_fields_in_structure(structure, word_length):
    fields = []
    empty_fields = []
    for elem in structure:
        for field in elem.fields:
            if field.value != '#':
                fields.append(field)
            else:
                if not is_all_fields_filled(fields):
                    fields_count = len(fields)
                    if fields_count == word_length:
                        empty_fields.append(fields)
                fields = []
                continue
        if not is_all_fields_filled(fields):
            fields_count = len(fields)
            if fields_count == word_length:
                empty_fields.append(fields)
        fields = []
    return empty_fields


def find_empty_fields(crossword, word):
    word_length = len(word)
    rows_empty_fields = find_empty_fields_in_structure(crossword.rows, word_length)
    columns_empty_fields = find_empty_fields_in_structure(crossword.columns, word_length)
    crossword_empty_fields = rows_empty_fields + columns_empty_fields
    return crossword_empty_fields


def are_fields_the_same(word_fields, fields_to_check):
    """check for empty fields"""
    for i in range(len(word_fields)):
        if word_fields[i] != '_':
            return False
    for i in range(len(word_fields)):
        word_field = word_fields[i]
        field_to_check = fields_to_check[i]
        # word_field.print()
        # field_to_check.print()
        if word_field != field_to_check:
            return False
    return True
