from puzzle.Crossword import update_values
from puzzle.fields_helpers import is_word_valid, find_empty_fields


def backtracking(crossword):
    empty_fields = find_empty_fields(crossword)
    if not empty_fields:
        print('There is no more empty space!')
        return True

    # print('crossword.words', crossword.words)
    # print('len(empty_fields)', len(empty_fields))
    for word in crossword.words:
        # print('word', word)
        for fields in empty_fields:
            if is_word_valid(fields, word):
                for i in range(len(word)):
                    fields[i].value = word[i]
                update_values(crossword, fields, word, False)
                print_crossword(crossword.rows)

                if backtracking(crossword):
                    return True
                for i in range(len(word)):
                    fields[i].value = '_'
                crossword.backtrack_steps += 1
                update_values(crossword, fields, word, True)

    return False


def print_crossword(rows):
    for i in range(len(rows)):
        row_fields = rows[i].fields
        for j in range(len(row_fields)):
            print(row_fields[j].value, end='')
        print('')
    print('')
