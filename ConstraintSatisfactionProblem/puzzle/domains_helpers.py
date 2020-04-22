from puzzle.fields_helpers import is_all_fields_filled


def update_words(crossword, fields_to_check, word_value, check_for_wipe_out):
    words_to_check = [word for word in crossword.words if
                      len(word.value) == len(word_value) and word.value != word_value]
    # print('update_words', word_value)
    # print('words_to_check', words_to_check)
    # print('word_value', word_value)
    # [print('word_to_check.value', word_to_check.value) for word_to_check in words_to_check]
    if check_for_wipe_out:
        if is_domain_wipe_out(words_to_check, fields_to_check, word_value):
            # print('DOMAIN WIPE OUT')
            print_crossword(crossword.rows)
            return True
    # print('len(words_to_check)', len(words_to_check))
    # update_words_domains(crossword, words_to_check)
    return False


def print_crossword(rows):
    for i in range(len(rows)):
        row_fields = rows[i].fields
        for j in range(len(row_fields)):
            print(row_fields[j].value, end='')
        print('')
    print('')


def update_words_domains(crossword, words):
    print('update_words_domains')
    for word in words:
        word.init_domain(crossword)


def is_domain_wipe_out(words, fields_to_check, word_value):
    # print('is_domain_wipe_out', word_value)
    for word in words:
        # print('word.value', word.value)
        # print('word.domain', word.domain)
        if len(word.domain) == 1 and word.value != word_value:
            print('check if fields are the same for word.value', word.value, 'and word_value', word_value)
            # print('1word.domain[0]', word.domain[0])
            # print('len(word.domain[0])', len(word.domain[0]))
            if are_fields_the_same(word.domain[0], fields_to_check):
                # print('Fields are the same')
                return True
    return False


def are_fields_the_same(word_fields, fields_to_check):
    # print('are_fields_the_same word_fields', word_fields, 'fields_to_check', fields_to_check)
    if are_fields_values_equal(word_fields, fields_to_check):
        return False
    for i in range(len(word_fields)):
        word_field = word_fields[i]
        field_to_check = fields_to_check[i]
        word_field.print()
        field_to_check.print()
        print('i', i)
        # print('word_fields[i]', word_fields[i])
        # print('fields_to_check[i]', fields_to_check[i])
        if word_field != field_to_check:
            return False
    return True


def are_fields_values_equal(word_fields, fields_to_check):
    if is_all_fields_filled(word_fields) and is_all_fields_filled(fields_to_check):
        for i in range(len(word_fields)):
            if word_fields[i].value != fields_to_check[i].value:
                return False
        return True
    return False
