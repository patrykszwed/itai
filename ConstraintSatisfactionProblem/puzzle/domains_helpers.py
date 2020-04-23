from puzzle.fields_helpers import are_fields_the_same


def is_domain_wipe_out(words, fields_to_check):
    for word in words:
        if len(word.domain) == 1 and are_fields_the_same(word.domain[0], fields_to_check):
            return True
    return False


def update_words(crossword, fields_to_check, word, check_for_wipe_out):
    word_value = word.value
    words_to_check = {word for word in crossword.words if
                      len(word.value) == len(word_value) and word.value != word_value}
    if check_for_wipe_out:
        word.domain = []
        print('word_value', word_value)
        [print('words_to_check_value', word_to_check.value) for word_to_check in words_to_check]
        if is_domain_wipe_out(words_to_check, fields_to_check):
            return True
    update_words_domains(crossword, words_to_check)
    return False


def update_words_domains(crossword, words):
    for word in words:
        word.init_domain(crossword)
