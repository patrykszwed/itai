def is_word_valid(fields, word):
    if word == 'EVO':
        print('IS VALID? EVO!')
        print('len(fields)', len(fields))
    if len(fields) == len(word):
        for i in range(len(fields)):
            field = fields[i]
            # field.print()
            if field.value != '_' and field.value != word[i]:
                # print('1 INVALID word', word)
                return False
        # print('VALID word', word)
        return True
    # print('2 INVALID word', word)
    return False


def find_filled_fields_in_structure(structure, word):
    word_length = len(word)
    fields = []
    filled_fields = []
    for elem in structure:
        for field in elem.fields:
            if field.value != '#':
                fields.append(field)
            else:
                if len(fields) == word_length and is_all_fields_filled(fields):
                    filled_fields.append(fields)
                fields = []
        if len(fields) == word_length and is_all_fields_filled(fields):
            filled_fields.append(fields)
        fields = []
    return filled_fields


def all_words_are_on_the_board(crossword):
    for word in crossword.words:
        if not is_word_anywhere_on_the_board(crossword, word):
            return False
    return True


def is_word_anywhere_on_the_board(crossword, word):
    rows_filled_fields = find_filled_fields_in_structure(crossword.rows, word)
    columns_filled_fields = find_filled_fields_in_structure(crossword.columns, word)
    filled_fields = rows_filled_fields + columns_filled_fields
    # if word == 'GI':
    #     print('is_word_anywhere_on_the_board', word)
    #     print('len(filled_fields)', len(filled_fields))
    if word == 'EVO':
        print('is_word_anywhere_on_the_board', word)
        print('len(filled_fields)', len(filled_fields))
    for fields in filled_fields:
        is_found = True
        for i in range(len(fields)):
            field = fields[i]
            if word == 'EVO':
                field.print()
                print('is_word_anywhere_on_the_board', field.value)
            if field.value != word[i]:
                is_found = False
                break
        if is_found:
            return True
    return False


def is_all_fields_filled(fields):
    for field in fields:
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


def check_if_crossword_is_filled(crossword):
    for field in crossword.fields:
        # print('field.value', field.value)
        if field.value == '_':
            return False
    return True


def find_empty_fields(crossword, word):
    word_length = len(word)
    rows_empty_fields = find_empty_fields_in_structure(crossword.rows, word_length)
    columns_empty_fields = find_empty_fields_in_structure(crossword.columns, word_length)
    crossword_empty_fields = rows_empty_fields + columns_empty_fields
    return crossword_empty_fields