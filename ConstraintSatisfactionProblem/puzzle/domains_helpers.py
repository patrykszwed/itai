from puzzle.fields_helpers import is_all_fields_filled


def update_words(crossword, fields_to_check, word_value, check_for_wipe_out):
    words_to_check = [word for word in crossword.words if
                      len(word.value) == len(word_value) and word.value != word_value]
    if check_for_wipe_out:
        if is_domain_wipe_out(words_to_check, fields_to_check):
            return True
    update_words_domains(crossword, words_to_check)
    return False


def update_words_domains(crossword, words):
    for word in words:
        word.init_domain(crossword)


def is_domain_wipe_out(words, fields_to_check):
    for word in words:
        if len(word.domain) == 1 and are_fields_the_same(word.domain[0], fields_to_check):
            return True
    return False


def are_fields_the_same(word_fields, fields_to_check):
    if are_fields_values_equal(word_fields, fields_to_check):
        return False
    for i in range(len(word_fields)):
        word_field = word_fields[i]
        field_to_check = fields_to_check[i]
        word_field.print()
        field_to_check.print()
        if word_field != field_to_check:
            return False
    return True


def are_fields_values_equal(word_fields, fields_to_check):
    if is_all_fields_filled(word_fields) and is_all_fields_filled(fields_to_check):
        for i in range(len(word_fields)):
            print('word_fields[i].value', word_fields[i].value)
            print('fields_to_check[i].value', fields_to_check[i].value)
            if word_fields[i].value != fields_to_check[i].value:
                return False
        return True
    return False
