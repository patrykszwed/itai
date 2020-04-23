import time

from puzzle.Crossword import Crossword
from puzzle.Word import init_words_domains
from puzzle.fields_helpers import all_words_are_on_the_board
from puzzle.helpers import print_crossword, backtracking, forward_checking
from puzzle.read_csv import read_puzzle


def backtracking_puzzle(crosswords_data, words_data):
    total_time = 0
    for i in range(len(crosswords_data)):
        if i == 3:
            continue
        start_time = time.time()
        crossword = Crossword(crosswords_data[i], words_data[i], i)
        # sort_crossword_words_by_length(crossword)
        print('------------- INITIAL CROSSWORD - DIFFICULTY LEVEL =', crossword.difficulty, '-----------------')
        print_crossword(crossword.rows)
        results = backtracking(crossword)
        is_solved = results
        print('is_solved', is_solved)
        if is_solved:
            if all_words_are_on_the_board(crossword):
                print('------------- CROSSWORD HAS ALL WORDS FILLED :) -----------------')
                print_crossword(crossword.rows)
            else:
                print('------------- CROSSWORD HAS MISSING WORDS! -----------------')
        else:
            print('------------- THIS CROSSWORD COULD NOT BE SOLVED -----------------')
            print_crossword(crossword.rows)
        current_time = (time.time() - start_time)
        total_time += current_time
        print("--- Backtracking\'s execution time = %s seconds ---" % current_time)
        print("--- Number of backtrack steps in case of Backtracking algorithm: %d ---" % crossword.backtrack_steps)
    print('Total time for BT = ', total_time)


def forward_checking_puzzle(crosswords_data, words_data):
    total_time = 0
    for i in range(len(crosswords_data)):
        if i == 3:
            continue
        start_time = time.time()
        crossword = Crossword(crosswords_data[i], words_data[i], i)
        init_words_domains(crossword)
        # sort_crossword_words_by_length(crossword)
        # [print('wod.value', word.value) for word in crossword.words]
        print('------------- INITIAL CROSSWORD - DIFFICULTY LEVEL =', crossword.difficulty, '-----------------')
        print_crossword(crossword.rows)
        results = forward_checking(crossword)
        is_solved = results
        print('is_solved', is_solved)
        if is_solved:
            if all_words_are_on_the_board(crossword):
                print('------------- CROSSWORD HAS ALL WORDS FILLED :) -----------------')
                print_crossword(crossword.rows)
            else:
                print('------------- CROSSWORD HAS MISSING WORDS! -----------------')
        else:
            print('------------- THIS CROSSWORD COULD NOT BE SOLVED -----------------')
            print_crossword(crossword.rows)
        current_time = (time.time() - start_time)
        total_time += current_time
        print("--- Backtracking\'s execution time = %s seconds ---" % current_time)
        print("--- Number of backtrack steps in case of Backtracking algorithm: %d ---" % crossword.backtrack_steps)
    print('Total time for BT+FC = ', total_time)


def main():
    task = read_puzzle()
    # print('------------------------------------------ BT ------------------------------------------')
    # backtracking_puzzle(task.crosswords_data, task.words_data)
    print('------------------------------------------ BT+FC ------------------------------------------')
    forward_checking_puzzle(task.crosswords_data, task.words_data)


main()
