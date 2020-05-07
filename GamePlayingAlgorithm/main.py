from Board import Board
from helpers import print_board
from run_game import run_game


def main():
    print('------------------------------')
    print('Checkers - legend:')
    print('_ - empty field')
    print('P1 - player1\'s piece')
    print('P2 - player2\'s piece')
    print('K1 - player1\'s king')
    print('K2 - player2\'s king')
    print('------------------------------')

    board = Board()
    print_board(board)
    run_game(board)


main()
