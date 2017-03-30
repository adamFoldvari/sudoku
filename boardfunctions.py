from random import randint
from insertfunc import *
from boxcol import *


def print_board(board, message=0):
    print ("\033c")
    print("-" * 37)
    for i, row in enumerate(board):
        print(("|" + " {}   {}   {} |" * 3).format(*[x if x != 0 else " " for x in row]))
        if i == 8:
            print("-" * 37)
        elif i % 3 == 2:
            print("|" + "---+" * 8 + "---|")
        else:
            print("|" + "   +" * 8 + "   |")
    if message == 1:
        print("This number is already in this row!")
    if message == 2:
        print("This number is already in this column!")
    if message == 3:
        print("This number is already in this 3*3 box!")
    if message == 4:
        print("You cannot change this number.")
    if message == 5:
        print("Invalid format!")


def find_empty_location(arr, l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col] == 0):
                l[0] = row
                l[1] = col
                return True
    return False


def used_in_row(arr, row, num):
    for i in range(9):
        if(arr[row][i] == num):
            return True
    return False


def used_in_col(arr, col, num):
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False


def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if(arr[i + row][j + col] == num):
                return True
    return False


def check_location_is_safe(arr, row, col, num):
    return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 3, col - col % 3, num)


def solve_sudoku(arr):
    l = [0, 0]

    if(not find_empty_location(arr, l)):
        return True

    row = l[0]
    col = l[1]

    for num in range(1, 10):
        if(check_location_is_safe(arr, row, col, num)):
            arr[row][col] = num

            if(solve_sudoku(arr)):
                return True

            arr[row][col] = 0

    return False


def create_board():
    board = [[0] * 9 for i in range(9)]

    board[0][1] = randint(1, 9)
    board[1][5] = randint(1, 9)
    board[2][6] = randint(1, 9)
    board[3][0] = randint(1, 9)
    board[4][3] = randint(1, 9)
    board[5][7] = randint(1, 9)
    board[6][2] = randint(1, 9)
    board[7][4] = randint(1, 9)
    board[8][8] = randint(1, 9)

    solve_sudoku(board)

    row_min = 0
    row_max = 2
    col_min = 0
    col_max = 2
    for round3 in range(3):
        for round2 in range(3):
            for round in range(3):
                board[randint(row_min, row_max)][randint(col_min, col_max)] = 0
            row_min += 3
            row_max += 3
        col_max += 3
        col_min += 3
        row_min = 0
        row_max = 2

    return board
