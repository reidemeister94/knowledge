"""
Write a function that takes in an integer matrix of potentially unequal height and width 
and returns the minimum number of passes required to convert all negative integers 
in the matrix to positive integers. 
A negative integer in the matrix can only be converted to a positive integer if one 
or more of its adjacent elements is positive. An adjacent element is an element that 
is to the left, to the right, above, or below the current element in the matrix. 
Converting a negative to a positive simply involves multiplying it by -1. 
Note that the 0 value is neither positive nor negative, meaning that a 0 
can't convert an adjacent negative to a positive. A single pass through the matrix 
involves converting all the negative integers that can be converted at a particular point in time.
"""


def minimumPassesOfMatrix(matrix):
    if len(matrix) == 1 and len(matrix[0]) == 1:
        if matrix[0][0] > 0:
            return 0
        return -1


n_passes = 0
queue = {}
processed = set()
n_rows = len(matrix)
n_cols = len(matrix[0])
finished = False
len_processed = 0

for i in range(n_rows):
    for j in range(n_cols):
        if matrix[i][j] < 0:
            is_conv = is_convertible(matrix, i, j, n_rows, n_cols)
            if is_conv:
                queue[(i, j)] = True
            else:
                queue[(i, j)] = False

while not finished:
    count_false = 0
    for k, v in queue.items():
        if v is True and (k[0], k[1]) not in processed:
            matrix[k[0]][k[1]] *= -1
            processed.add(k)
        elif v is False:
            count_false += 1
    if count_false == 0:
        if len(processed) == 0:
            return n_passes
        else:
            return n_passes + 1

    if len(processed) == len_processed and count_false > 0:
        return -1
    else:
        len_processed = len(processed)

    for k, v in queue.items():
        if v is False:
            is_conv = is_convertible(matrix, k[0], k[1], n_rows, n_cols)
            if is_conv:
                queue[(k[0], k[1])] = True

    n_passes += 1
return n_passes


def is_convertible(matrix, row, col, n_rows, n_cols):
    for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        x, y = row + i, col + j
        if 0 <= x < n_rows and 0 <= y < n_cols and matrix[x][y] > 0:
            return True
    return False
