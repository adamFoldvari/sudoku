from boardfunctions import print_board, column, box


def user_insert(board):
    def check_insert(board, x, y, z):
        if 0 < board[x - 1].count(z):
            print_board(board)
            print("This number is already in this row!")
        elif 0 < column(board, y - 1).count(z):
            print_board(board)
            print("This number is already in this column!")
        elif 0 < box(board, x - 1, y - 1).count(z):
            print_board(board)
            print("This number is already in this 3*3 box!")
        elif board[x - 1][y - 1] == 0:
            board[x - 1][y - 1] = z
            print_board(board)
        else:
            print_board(board)
            print("You cannot change this number.")
    try:
        list1 = list(input("""Give me rows, columns, number to write separated by one character
                            (e.g.:3 5 7 or 3,5,7):"""))
        if len(list1) < 6:
            x = int(list1[0])
            y = int(list1[2])
            z = int(list1[4])
            check_insert(board, x, y, z)
        else:
            print("Invalid format!")
    except ValueError:
        print("Invalid format!")
    except IndexError:
        print("Invalid format!")


def check_win(board, u):
    for row in board:
        if row.count(0):
            u += 1
    if u == 0:
        print("Coungratulation, you won!!!")
        return u
