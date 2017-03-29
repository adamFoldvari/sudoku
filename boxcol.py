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


def check_insert(board, x, y, z):
    if x % 3 == 1 and y % 3 == 0:
        return board, 1
    elif x % 3 == 2 and y % 3 == 2:
        return board, 1
    elif x % 3 == 0 and y % 3 == 1:
        return board, 1
    elif 0 < board[x - 1].count(z):
        return board, 1
    elif 0 < column(board, y - 1).count(z):
        return board, 2
    elif 0 < box(board, x - 1, y - 1).count(z):
        return board, 3
    elif board[x - 1][y - 1] != 0:
        return board, 4
    else:
        board[x - 1][y - 1] = z
        return board, 0
