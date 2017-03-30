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
