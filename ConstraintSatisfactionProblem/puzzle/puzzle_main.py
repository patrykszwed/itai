import time

from puzzle.Crossword import Crossword
from puzzle.fields_helpers import all_words_are_on_the_board
from puzzle.helpers import print_crossword, backtracking
from puzzle.read_csv import read_puzzle


def backtracking_puzzle(crosswords_data, words_data):
    total_time = 0
    # for i in range(len(crosswords_data)):
    start_time = time.time()
    crossword = Crossword(crosswords_data[1], words_data[1], 1)
    print('------------- INITIAL CROSSWORD - DIFFICULTY LEVEL =', crossword.difficulty, '-----------------')
    print_crossword(crossword.rows)
    results = backtracking(crossword)
    is_solved = results
    if is_solved:
        print('------------- SOLVED CROSSWORD -----------------')
        print_crossword(crossword.rows)
        if all_words_are_on_the_board(crossword):
            print('------------- SOLVED CROSSWORD -----------------')
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


def main():
    task = read_puzzle()
    print('------------------------------------------ BT ------------------------------------------')
    backtracking_puzzle(task.crosswords_data, task.words_data)


main()
