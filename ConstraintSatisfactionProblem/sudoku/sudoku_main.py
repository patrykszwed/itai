import time

from constants import SUDOKU_FILE_PATH
from sudoku.Board import Board
from sudoku.domains_helpers import init_fields_domains
from sudoku.helpers import backtracking, forward_checking
from sudoku.read_csv import read_sudoku


def backtracking_sudoku(boards_data):
    total_time = 0
    for i in range(len(boards_data)):
        if i != 9:
            continue
        board_data = boards_data[i]
        start_time = time.time()
        board = Board(board_data)
        print('------------- INITIAL SUDOKU - DIFFICULTY LEVEL =', board.difficulty, '-----------------')
        # print_board(board.rows)
        results = backtracking(board)
        is_solved = results
        if is_solved:
            print('------------- SOLVED SUDOKU -----------------')
            # print_board(board.rows)
        else:
            print('------------- THIS SUDOKU COULD NOT BE SOLVED -----------------')
        current_time = (time.time() - start_time)
        total_time += current_time
        print("--- Backtracking\'s execution time = %s seconds ---" % current_time)
        print("--- Number of backtrack steps in case of Backtracking algorithm: %d ---" % board.backtrack_steps)
        if len(board.solution) > 0:
            all_rows = []
            for i in range(9):
                rows_fields = board.rows[i].fields
                for j in range(9):
                    all_rows.append(rows_fields[j].value)
            all_rows_as_string = ''.join(str(e) for e in all_rows)
            print('Is sudoku solved correctly?', all_rows_as_string == board.solution)
    print('Total time for BT = ', total_time)


def forward_checking_sudoku(boards_data):
    total_time = 0
    for i in range(len(boards_data)):
        if i != 9:
            continue
        board_data = boards_data[i]
        start_time = time.time()
        board = Board(board_data)
        init_fields_domains(board)
        print('------------- INITIAL SUDOKU - DIFFICULTY LEVEL =', board.difficulty, '-----------------')
        # print_board(board.rows)
        results = forward_checking(board)
        is_solved = results
        if is_solved:
            print('------------- SOLVED SUDOKU -----------------')
            # print_board(board.rows)
        else:
            print('------------- THIS SUDOKU COULD NOT BE SOLVED -----------------')
            # print_board(board.rows)
        current_time = (time.time() - start_time)
        total_time += current_time
        print("--- Forward Checking\'s execution time = %s seconds ---" % current_time)
        print("--- Number of backtrack steps in case of Forward Checking algorithm: %d ---" % board.backtrack_steps)
        if len(board.solution) > 0:
            all_rows = []
            for i in range(9):
                rows_fields = board.rows[i].fields
                for j in range(9):
                    all_rows.append(rows_fields[j].value)
            all_rows_as_string = ''.join(str(e) for e in all_rows)
            print('Is sudoku solved correctly?', all_rows_as_string == board.solution)
    print('Total time for BT+FC = ', total_time)


def main():
    task = read_sudoku(SUDOKU_FILE_PATH)
    print('------------------------------------------ BT ------------------------------------------')
    backtracking_sudoku(task.boards_data)
    print('------------------------------------------ BT+FC ------------------------------------------')
    forward_checking_sudoku(task.boards_data)


main()
