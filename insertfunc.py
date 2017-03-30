from boxcol import *


def user_insert(board):
    # ask for a user input and checks if it meets the given requirement
    try:
        list1 = list(input("""Give me rows, columns, number to write separated by one character
                            (e.g.:3 5 7 or 3,5,7):"""))
        if len(list1) < 6:
            row = int(list1[0])
            col = int(list1[2])
            num = int(list1[4])
            board, message = check_insert(board, row, col, num)
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


def check_insert(board, row, col, num):
    # cheks if the valid user input matches the sudoku rules
    if 0 < board[row - 1].count(num):
        return board, 1
    elif 0 < column(board, col - 1).count(num):
        return board, 2
    elif 0 < box(board, row - 1, col - 1).count(num):
        return board, 3
    elif board[row - 1][col - 1] == 0:
        board[row - 1][col - 1] = num
        return board, 0
    else:
        return board, 4


def check_win(board, win):
    # after every input, we run this, to check if the table is filled already
    # becouse we let the user only good solutions to fill, when the table is filled, you won the game
    for row in board:
        if row.count(0):
            win += 1
    if win == 0:
        print("Coungratulation, you won!!!")
        return win
