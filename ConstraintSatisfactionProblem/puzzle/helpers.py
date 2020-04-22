from puzzle.Crossword import update_values
from puzzle.fields_helpers import is_word_valid, find_empty_fields, is_word_anywhere_on_the_board, \
    check_if_crossword_is_filled, all_words_are_on_the_board


def backtracking(crossword):
    # empty_fields = find_empty_fields(crossword)
    # if not empty_fields:
    #     print('There is no more empty space!')
    #     return True
    if check_if_crossword_is_filled(crossword):
        print('Everything is filled!')
        if all_words_are_on_the_board(crossword):
            return True
        print('But not all words were on the board!')
        return False

    # print('crossword.words', crossword.words)
    # print('len(empty_fields)', len(empty_fields))
    used_words = []
    for word in crossword.words:
        # print('next word', word)
        if word not in used_words:
            if word == 'EVO':
                print('WORD IS EVO')
                print_crossword(crossword.rows)
            if is_word_anywhere_on_the_board(crossword, word):
                if word == 'EVO':
                    print('WORD IS ALREADY ON THE BOARD!')
                    print_crossword(crossword.rows)
                used_words.append(word)
            else:
                empty_fields = find_empty_fields(crossword, word)
                for fields in empty_fields:
                    if word == 'EVO':
                        print('EVOOO! len(empty_fields) = ', len(empty_fields))
                        print('EVOOO! len(fields) = ', len(fields))
                        print_crossword(crossword.rows)
                    if is_word_valid(fields, word):
                        if word == 'EVO':
                            print('WORD EVO IS VALID!')
                            print_crossword(crossword.rows)
                        used_words.append(word)
                        # print('word is valid!')
                        for i in range(len(word)):
                            field = fields[i]
                            field.add_word_to_contained_words(word)
                            field.value = word[i]
                        update_values(crossword, fields, word, False)
                        # print_crossword(crossword.rows)

                        if backtracking(crossword):
                            return True

                        # print('BEFORE BACKTRACKING!!!! for word', word)
                        # print_crossword(crossword.rows)
                        for i in range(len(word)):
                            field = fields[i]
                            field.remove_word_from_contained_words(word)
                            # print('field.contained_words', field.contained_words)
                            if len(field.contained_words) == 0:
                                field.value = '_'
                        crossword.backtrack_steps += 1
                        update_values(crossword, fields, word, True)
                        # print('AFTER BACKTRACKING!!!! for word', word)
                        # print_crossword(crossword.rows)
                    else:
                        if word == 'EVO':
                            print('EVOOO! INVALID FIELDS ', len(fields))
                            print_crossword(crossword.rows)
        if not is_word_anywhere_on_the_board(crossword, word):
            # print('Word', word, 'is nowhere on the board! Return false')
            # print_crossword(crossword.rows)
            return False

    return False


def print_crossword(rows):
    for i in range(len(rows)):
        row_fields = rows[i].fields
        for j in range(len(row_fields)):
            print(row_fields[j].value, end='')
        print('')
    print('')
