from random import randint


def print_board(board):
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


def column(matrix, k):
    return [row[k]for row in matrix]


def box(matrix, a, b):
    if a < 3 and b < 3:
        return [matrix[j][i]for i in range(3) for j in range(3)]
    if a < 3 and (b < 6 and b > 2):
        return [matrix[j][i]for i in range(3, 6) for j in range(3)]
    if a < 3 and (b < 9 and b > 5):
        return [matrix[j][i]for i in range(6, 9) for j in range(3)]
    if (a < 6 and a > 2) and b < 3:
        return [matrix[j][i]for i in range(3) for j in range(3, 6)]
    if (a < 6 and a > 2) and (b < 6 and b > 2):
        return [matrix[j][i]for i in range(3, 6) for j in range(3, 6)]
    if (a < 6 and a > 2) and (b < 9 and b > 5):
        return [matrix[j][i]for i in range(6, 9) for j in range(3, 6)]
    if (a < 9 and a > 5) and b < 3:
        return [matrix[j][i]for i in range(3) for j in range(6, 9)]
    if (a < 9 and a > 5) and (b < 6 and b > 2):
        return [matrix[j][i]for i in range(3, 6) for j in range(6, 9)]
    if (a < 9 and a > 5) and (b < 9 and b > 5):
        return [matrix[j][i]for i in range(6, 9) for j in range(6, 9)]


def create_board():
    board = []
    for row in range(9):
        board.append([])
        for colum in range(9):
            board[row].append(0)
    row_min = 0
    row_max = 2
    col_min = 0
    col_max = 2
    for slot in range(3):
        for round in range(2):
            board[randint(row_min, row_max)][randint(col_min, col_max)] = randint(1, 9)
        row_min += 3
        row_max += 3
    return board
