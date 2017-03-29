import random
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


def create_board():
    while True:
        try:
            board = [[0] * 9 for i in range(9)]
            rows = [set(range(1, 10))for i in range(9)]
            columns = [set(range(1, 10)) for i in range(9)]
            squares = [set(range(1, 10)) for i in range(9)]
            for i in range(9):
                for j in range(9):
                    choices = rows[i].intersection(columns[j]).intersection(squares[int((i / 3) * 3 + j / 3)])
                    choice = random.choice(list(choices))

                    board[i][j] = choice

                    rows[i].discard(choice)
                    columns[j].discard(choice)
                    squares[int((i / 3) * 3 + j / 3)].discard(choice)

            return board

        except IndexError:
            pass
