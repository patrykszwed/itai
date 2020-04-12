from Board import Board
from constants import SUDOKU_FILE_PATH
from helpers import back_tracking, print_board
from read_csv import read_sudoku

task = read_sudoku(SUDOKU_FILE_PATH)
board_data = task.boards_data[0]
for board_data in task.boards_data:
    board = Board(board_data)
    print('-------------INITIAL SUDOKU - DIFFICULTY LEVEL = ', board.difficulty, '-----------------')

    print(board.rows)
    print(board.solution)
    print_board(board.rows)
    back_tracking(board)
    print('-------------SOLVED SUDOKU-----------------')
    print_board(board.rows)
    if len(board.solution) > 0:
        all_rows = []
        for i in range(9):
            for j in range(len(board.rows[i])):
                all_rows.append(board.rows[i][j])
        print('all_rows', all_rows)
        all_rows_as_string = ''.join(str(e) for e in all_rows)
        print('Is sudoku solved correctly?', all_rows_as_string == board.solution)
