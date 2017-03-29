from boardfunctions import *
from boxcol import *


def check_insert1(board, x, y, z):
    if 0 < board[x - 1].count(z):
        return board, 1
    elif 0 < column(board, y - 1).count(z):
        return board, 2
    elif 0 < box(board, x - 1, y - 1).count(z):
        return board, 3
    elif board[x - 1][y - 1] == 0:
        board[x - 1][y - 1] = z
        return board, 0
    else:
        return board, 4


def user_insert(board):

    try:
        list1 = list(input("""Give me rows, columns, number to write separated by one character
                            (e.g.:3 5 7 or 3,5,7):"""))
        if len(list1) < 6:
            x = int(list1[0])
            y = int(list1[2])
            z = int(list1[4])
            board, message = check_insert1(board, x, y, z)
            return board, message
        else:
            message = 5
            return board, message
    except ValueError:
        message = 5
        return board, message
    except IndexError:
        message = 5
        return board, message


def check_win(board, u):
    for row in board:
        if row.count(0):
            u += 1
    if u == 0:
        print("Coungratulation, you won!!!")
        return u
