
from menu import *
from boardfunctions import *
from insertfunc import *


def main():
    difficulty = menu()
    board = create_board(difficulty)
    print_board(board)
    while True:
        u = 0
        board, message = user_insert(board)
        print_board(board, message)
        result = check_win(board, u)
        if result == 0:
            break


if __name__ == '__main__':
    main()
