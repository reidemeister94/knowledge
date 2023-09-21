"""
https://leetcode.com/problems/max-area-of-island/description/

You are given an m x n binary matrix grid.
An island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells
with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""
class Solution:
    def bfs(self, row, col):
        queue = [[row,col]]
        area = 0

        while queue:
            curr_row, curr_col = queue.pop()
            if self.grid[curr_row][curr_col] == -1:
                continue
            area += 1
            for inc_r, inc_c in [[-1,0],[0,1],[1,0],[0,-1]]:
                r,c = curr_row + inc_r, curr_col + inc_c
                if  0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] == 1:
                    queue.append([r,c])
            self.grid[curr_row][curr_col] = -1
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        self.grid = grid
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:
                    max_area = max(max_area, self.bfs(i,j))

        return max_area