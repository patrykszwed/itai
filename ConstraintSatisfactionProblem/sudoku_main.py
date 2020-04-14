import time

from Board import Board, init_fields_domains
from constants import SUDOKU_FILE_PATH
from helpers import back_tracking, print_board, forward_checking
from read_csv import read_sudoku


def back_tracking_sudoku(boards_data):
    for board_data in boards_data:
        start_time = time.time()
        board = Board(board_data)
        print('------------- INITIAL SUDOKU - DIFFICULTY LEVEL =', board.difficulty, '-----------------')
        print_board(board.rows)
        results = back_tracking(board, 0)
        is_solved = results[0]
        back_track_steps = results[1]
        if is_solved:
            print('------------- SOLVED SUDOKU -----------------')
            print_board(board.rows)
        else:
            print('------------- THIS SUDOKU COULD NOT BE SOLVED -----------------')
        print("--- Backtracking\'s execution time = %s seconds ---" % (time.time() - start_time))
        print("--- Number of back track steps in case of Backtracking algorithm: %d ---" % back_track_steps)
        if len(board.solution) > 0:
            all_rows = []
            for i in range(9):
                for j in range(len(board.rows[i])):
                    all_rows.append(board.rows[i][j])
            all_rows_as_string = ''.join(str(e) for e in all_rows)
            print('Is sudoku solved correctly?', all_rows_as_string == board.solution)


def forward_checking_sudoku(boards_data):
    for board_data in boards_data:
        start_time = time.time()
        board = Board(board_data)
        init_fields_domains(board)
        print('------------- INITIAL SUDOKU - DIFFICULTY LEVEL =', board.difficulty, '-----------------')
        print_board(board.rows)
        results = forward_checking(board, 0)
        is_solved = results[0]
        back_track_steps = results[1]
        if is_solved:
            print('------------- SOLVED SUDOKU -----------------')
            print_board(board.rows)
        else:
            print('------------- THIS SUDOKU COULD NOT BE SOLVED -----------------')
        print("--- Forward Checking\'s execution time = %s seconds ---" % (time.time() - start_time))
        print("--- Number of back track steps in case of Forward Checking algorithm: %d ---" % back_track_steps)
        if len(board.solution) > 0:
            all_rows = []
            for i in range(9):
                for j in range(len(board.rows[i])):
                    all_rows.append(board.rows[i][j])
            all_rows_as_string = ''.join(str(e) for e in all_rows)
            print('Is sudoku solved correctly?', all_rows_as_string == board.solution)


def main():
    task = read_sudoku(SUDOKU_FILE_PATH)
    # back_tracking_sudoku(task.boards_data)
    forward_checking_sudoku(task.boards_data)


main()
