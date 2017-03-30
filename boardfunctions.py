from random import randint


def print_board(board, message=0):
    # displays the board in a nice form
    print("\033c")
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


def find_empty_location(arr, location):
    # finds an empyt location in the sudoku matrix, and stores its coordinates in a list
    for row in range(9):
        for col in range(9):
            if(arr[row][col] == 0):
                location[0] = row
                location[1] = col
                return True
    return False


def used_in_row(arr, row, num):
    # checks if a number is exist in a row
    for index in range(9):
        if(arr[row][index] == num):
            return True
    return False


def used_in_col(arr, col, num):
    # checks if a number is exist in a colum
    for index in range(9):
        if(arr[index][col] == num):
            return True
    return False


def used_in_box(arr, row, col, num):
    # checks if a number is exist in a 3*3 box
    for index1 in range(3):
        for index2 in range(3):
            if(arr[index1 + row][index2 + col] == num):
                return True
    return False


def check_location_is_safe(arr, row, col, num):
    # checks if a number is exist in the row, col, or box
    return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(
        arr, row - row % 3, col - col % 3, num)


def solve_sudoku(arr):
    # solves the given sudoku matrix with a recursive backtracking algorithm
    location = [0, 0]

    if(not find_empty_location(arr, location)):
        return True

    row = location[0]
    col = location[1]

    for num in range(1, 10):
        if(check_location_is_safe(arr, row, col, num)):
            arr[row][col] = num

            if(solve_sudoku(arr)):
                return True

            arr[row][col] = 0

    return False


def create_board(diffic):
    # this function will create a random valid suoku board

    # creatse an empty 2d list as sudoku board
    board = [[0] * 9 for lists in range(9)]
    # we will some random numbers, for predefined places
    board[0][1] = randint(1, 9)
    board[1][5] = randint(1, 9)
    board[2][6] = randint(1, 9)
    board[3][0] = randint(1, 9)
    board[4][3] = randint(1, 9)
    board[5][7] = randint(1, 9)
    board[6][2] = randint(1, 9)
    board[7][4] = randint(1, 9)
    board[8][8] = randint(1, 9)

    # run the sudoku solver, to make a valid sudoku game for the given table
    solve_sudoku(board)

    # we delete some numbers, from  each box in the filled sudoku grid
    # number of deleted numbers is depending by the difficulty choice
    row_min = 0
    row_max = 2
    col_min = 0
    col_max = 2
    for round3 in range(3):
        for round2 in range(3):
            for round in range(diffic):
                board[randint(row_min, row_max)][randint(col_min, col_max)] = 0
            row_min += 3
            row_max += 3
        col_max += 3
        col_min += 3
        row_min = 0
        row_max = 2

    return board
