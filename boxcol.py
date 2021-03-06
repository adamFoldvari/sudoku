def column(matrix, col):
    # returns a list with the elements from the given colum
    return [row[col]for row in matrix]


def box(matrix, row, col):
    # returns a list with the elements from the given box
    row = int(row / 3)
    col = int(col / 3)
    box = []
    for index1 in range(3):
        for index2 in range(3):
            box.append(matrix[row * 3 + index1][col * 3 + index2])
    return box
