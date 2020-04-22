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
                        for i in range(len(word_value)):
                            field = fields[i]
                            field.add_word_to_contained_words(word_value)
                            field.value = word_value[i]
                        update_values(crossword, fields, word_value, False)

                        if backtracking(crossword):
                            return True

                        for i in range(len(word_value)):
                            field = fields[i]
                            field.remove_word_from_contained_words(word_value)
                            if len(field.contained_words) == 0:
                                field.value = '_'
                        crossword.backtrack_steps += 1
                        update_values(crossword, fields, word_value, True)
        if not is_word_anywhere_on_the_board(crossword, word_value):
            return False

    return False


def forward_checking(crossword):
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
                        # print('VALID WORD')
                        used_words.append(word_value)
                        for i in range(len(word_value)):
                            field = fields[i]
                            field.add_word_to_contained_words(word_value)
                            field.value = word_value[i]
                        update_values(crossword, fields, word_value, False)
                        is_wipe_out = update_words(crossword, fields, word_value, True)
                        # print('is_wipe_out', is_wipe_out)
                        # print_crossword(crossword.rows)

                        if not is_wipe_out:
                            if forward_checking(crossword):
                                return True

                        for i in range(len(word_value)):
                            field = fields[i]
                            field.remove_word_from_contained_words(word_value)
                            if len(field.contained_words) == 0:
                                field.value = '_'
                        # print('backtrack')
                        crossword.backtrack_steps += 1
                        update_values(crossword, fields, word_value, True)
                        update_words(crossword, fields, word_value, False)
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
