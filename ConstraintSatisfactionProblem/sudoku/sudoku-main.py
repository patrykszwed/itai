from constants import SUDOKU_FILE_PATH
from read_csv import read_sudoku
from sudoku.Game import Game

task = read_sudoku(SUDOKU_FILE_PATH)
game = Game(task.games_data[0])
for game_data in task.games_data:
    game = Game(game_data[0])
    print('game', game)
