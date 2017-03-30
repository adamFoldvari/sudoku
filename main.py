
from menu import *
from boardfunctions import *
from insertfunc import *


def main():
    difficulty = menu()
    board = create_board(difficulty)
    print_board(board)
    result = 1
    while result != 0:
        win = 0
        board, message = user_insert(board)
        print_board(board, message)
        result = check_win(board, win)


if __name__ == '__main__':
    main()
