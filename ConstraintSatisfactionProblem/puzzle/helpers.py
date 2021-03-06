import sys

from puzzle.Crossword import update_values
from puzzle.domains_helpers import update_words
from puzzle.fields_helpers import is_word_valid, find_empty_fields, is_word_anywhere_on_the_board, \
    check_if_crossword_is_filled, all_words_are_on_the_board


def backtracking(crossword):
    if check_if_crossword_is_filled(crossword):
        print('Everything is filled!')
        if all_words_are_on_the_board(crossword):
            return True
        print('But not all words were on the board!')
        return False

    used_words = []
    for word in crossword.words:
        word_value = word.value
        if word_value not in used_words:
            if is_word_anywhere_on_the_board(crossword, word_value):
                used_words.append(word_value)
            else:
                empty_fields = find_empty_fields(crossword, word_value)
                for fields in empty_fields:
                    if is_word_valid(fields, word_value):
                        used_words.append(word_value)
                        update_values(crossword, fields, word_value, False)

                        if backtracking(crossword):
                            return True

                        crossword.backtrack_steps += 1
                        update_values(crossword, fields, word_value, True)
        if not is_word_anywhere_on_the_board(crossword, word_value):
            return False

    return False


def get_best_word(crossword):
    min_domain = sys.maxsize
    word_to_return = 0
    for word in crossword.words:
        if not is_word_anywhere_on_the_board(crossword, word.value):
            if len(word.domain) == 1:
                return word
            if 0 < len(word.domain) < min_domain:
                word_to_return = word
                min_domain = len(word.domain)
    return word_to_return


def forward_checking(crossword):
    if check_if_crossword_is_filled(crossword):
        print('Everything is filled!')
        if all_words_are_on_the_board(crossword):
            return True
        print('But not all words were on the board!')
        return False

    used_words = []
    for i in range(len(crossword.words)):
        word = get_best_word(crossword)
        word_value = word.value
        if word_value not in used_words:
            if is_word_anywhere_on_the_board(crossword, word_value):
                used_words.append(word_value)
            else:
                empty_fields = find_empty_fields(crossword, word_value)
                for fields in empty_fields:
                    if is_word_valid(fields, word_value):
                        used_words.append(word_value)
                        is_wipe_out = update_words(crossword, fields, word, True)
                        update_values(crossword, fields, word_value, False)

                        if not is_wipe_out:
                            if forward_checking(crossword):
                                return True

                        crossword.backtrack_steps += 1
                        update_values(crossword, fields, word_value, True)
                        update_words(crossword, fields, word, False)
        if not is_word_anywhere_on_the_board(crossword, word_value):
            return False

    return False


def print_crossword(rows):
    for i in range(len(rows)):
        row_fields = rows[i].fields
        for j in range(len(row_fields)):
            print(row_fields[j].value, end='')
        print('')
    print('')
