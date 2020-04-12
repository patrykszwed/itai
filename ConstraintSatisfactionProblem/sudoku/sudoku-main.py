from constants import SUDOKU_FILE_PATH
from read_csv import read_sudoku
from sudoku.Game import Game

task = read_sudoku(SUDOKU_FILE_PATH)
print('task', task)

for game_data in task.games_data:
    game = Game(game_data)
    print('game', game)
