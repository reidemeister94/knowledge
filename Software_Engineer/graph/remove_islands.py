def get_kids(matrix, row, col):
    kids = []
    # left
    if col > 0 and matrix[row][col - 1] == 1:
        kids.append((row, col - 1))
    # right
    if col < len(matrix[0]) - 1 and matrix[row][col + 1] == 1:
        kids.append((row, col + 1))
    # up
    if row > 0 and matrix[row - 1][col] == 1:
        kids.append((row - 1, col))
    # down
    if row < len(matrix) - 1 and matrix[row + 1][col] == 1:
        kids.append((row + 1, col))
    return kids


def removeIslands(matrix):
    # for row in matrix:
    # 	print(row)
    # print('='*75)
    # first row
    for i in range(len(matrix[0])):
        queue = []
        if matrix[0][i] != 0:
            queue.append((0, i))
            matrix[0][i] = 2
            while queue:
                curr_node = queue.pop(0)
                kids = get_kids(matrix, curr_node[0], curr_node[1])
                for kid in kids:
                    queue.append(kid)
                    matrix[kid[0]][kid[1]] = 2

    # first col
    for i in range(len(matrix)):
        queue = []
        if matrix[i][0] != 0:
            queue.append((i, 0))
            matrix[i][0] = 2
            while queue:
                curr_node = queue.pop(0)
                kids = get_kids(matrix, curr_node[0], curr_node[1])
                for kid in kids:
                    queue.append(kid)
                    matrix[kid[0]][kid[1]] = 2

    # last row
    for i in range(len(matrix[0])):
        queue = []
        if matrix[len(matrix) - 1][i] != 0:
            queue.append((len(matrix) - 1, i))
            matrix[len(matrix) - 1][i] = 2
            while queue:
                curr_node = queue.pop(0)
                kids = get_kids(matrix, curr_node[0], curr_node[1])
                for kid in kids:
                    queue.append(kid)
                    matrix[kid[0]][kid[1]] = 2

    # last column
    for i in range(len(matrix)):
        queue = []
        if matrix[i][len(matrix[0]) - 1] != 0:
            queue.append((i, (len(matrix[0]) - 1)))
            matrix[i][len(matrix[0]) - 1] = 2
            while queue:
                curr_node = queue.pop(0)
                kids = get_kids(matrix, curr_node[0], curr_node[1])
                for kid in kids:
                    queue.append(kid)
                    matrix[kid[0]][kid[1]] = 2

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                matrix[row][col] = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 2:
                matrix[row][col] = 1
    return matrix
