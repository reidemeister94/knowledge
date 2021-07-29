def isEscapePossible(blocked, source, target):
    row = source[0]
    col = source[1]
    visited = {}
    queue = [(row, col)]
    visited[(row, col)] = 1
    for elem in blocked:
        visited[(elem[0], elem[1])] = 1
    i = 0
    while queue:
        i += 1
        row, col = queue.pop()
        if i % 20000:
            print(row, col)
        kids = get_kids(visited, row, col)
        for kid in kids:
            if kid[0] == target[0] and kid[1] == target[1]:
                return True
            visited[kid] = 1
            queue.append(kid)
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
