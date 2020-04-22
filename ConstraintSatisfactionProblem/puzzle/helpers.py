from puzzle.Crossword import update_values
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
        if word not in used_words:
            if is_word_anywhere_on_the_board(crossword, word):
                used_words.append(word)
            else:
                empty_fields = find_empty_fields(crossword, word)
                for fields in empty_fields:
                    if is_word_valid(fields, word):
                        used_words.append(word)
                        for i in range(len(word)):
                            field = fields[i]
                            field.add_word_to_contained_words(word)
                            field.value = word[i]
                        update_values(crossword, fields, word, False)

                        if backtracking(crossword):
                            return True

                        for i in range(len(word)):
                            field = fields[i]
                            field.remove_word_from_contained_words(word)
                            if len(field.contained_words) == 0:
                                field.value = '_'
                        crossword.backtrack_steps += 1
                        update_values(crossword, fields, word, True)
        if not is_word_anywhere_on_the_board(crossword, word):
            return False

    return False


def print_crossword(rows):
    for i in range(len(rows)):
        row_fields = rows[i].fields
        for j in range(len(row_fields)):
            print(row_fields[j].value, end='')
        print('')
    print('')
