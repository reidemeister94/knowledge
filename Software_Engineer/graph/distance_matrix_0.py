from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited = {}
        queue = deque()
        n_rows = len(mat)
        n_cols = len(mat[0])

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    visited[(row, col)] = 1
                    queue.append((row, col))

        while queue:
            row, col = queue.popleft()
            kids = self.get_kids(visited, n_rows, n_cols, row, col)
            for k in kids:
                mat[k[0]][k[1]] = mat[row][col] + 1
                visited[k] = 1
                queue.append(k)
        return mat

    def get_kids(self, visited, n_rows, n_cols, row, col):
        kids = []
        for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            x, y = row + i, col + j
            if 0 <= x < n_rows and 0 <= y < n_cols and (x, y) not in visited:
                kids.append((x, y))
        return kids
