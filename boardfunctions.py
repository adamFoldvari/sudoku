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
    board[0][1] = 4
    board[0][2] = 3
    board[0][4] = 1
    board[0][6] = 7
    board[0][7] = 8
    board[1][0] = 1
    board[1][3] = 8
    board[1][4] = 7
    board[1][5] = 5
    board[2][1] = 8
    board[2][3] = 3
    board[2][4] = 4
    board[2][8] = 1
    board[3][2] = 9
    board[3][3] = 7
    board[3][4] = 8
    board[3][6] = 1
    board[4][1] = 6
    board[4][7] = 7
    board[5][2] = 7
    board[5][4] = 2
    board[5][5] = 6
    board[5][6] = 8
    board[6][0] = 9
    board[6][4] = 3
    board[6][5] = 4
    board[6][7] = 1
    board[7][3] = 1
    board[7][4] = 9
    board[7][5] = 8
    board[7][8] = 4
    board[8][1] = 3
    board[8][2] = 1
    board[8][4] = 6
    board[8][6] = 2
    board[8][7] = 9
    return board
