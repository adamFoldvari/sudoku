

from boardfunctions import *
from insertfunc import *


def main():
    board = create_board()
    print_board(board)
    while True:
        u = 0
        user_insert(board)
        result = check_win(board, u)
        if result == 0:
            break


if __name__ == '__main__':
    main()
