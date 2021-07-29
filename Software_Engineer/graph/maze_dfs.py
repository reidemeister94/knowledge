def dfs_util(row, col, target_row, target_col, visited):
    visited[(row, col)] = 1
    kids = get_kids(visited, row, col)
    for kid in kids:
        if kid[0] == target_row and kid[1] == target_col:
            return True
        if kid not in visited:
            dfs_util(kid[0], kid[1], target_row, target_col, visited)
    return False


def isEscapePossible(blocked, source, target):
    row = source[0]
    col = source[1]
    visited = {}
    for elem in blocked:
        visited[(elem[0], elem[1])] = 1
    reachable = dfs_util(row, col, target[0], target[1], visited)

    if reachable:
        return True
    return False


def get_kids(visited, row, col):
    kids = []
    # left
    if col > 0 and (row, col - 1) not in visited:
        kids.append((row, col - 1))
    # right
    if col < 999999 and (row, col + 1) not in visited:
        kids.append((row, col + 1))
    # up
    if row > 0 and (row - 1, col) not in visited:
        kids.append((row - 1, col))
    # down
    if row < 999999 and (row + 1, col) not in visited:
        kids.append((row + 1, col))
    return kids


if __name__ == "__main__":
    blocked = []
    source = [0, 0]
    target = [999999, 999999]
    isEscapePossible(blocked, source, target)
