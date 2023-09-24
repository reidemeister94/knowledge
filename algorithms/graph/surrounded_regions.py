"""
https://leetcode.com/problems/surrounded-regions/description/

Given an m x n matrix board containing 'X' and 'O',
capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's
into 'X's in that surrounded region.

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""
from typing import List


class Solution:
    def bfs(self, row, col):
        queue = [[row, col]]

        while queue:
            r, c = queue.pop()
            if self.new_board[r][c] == "-1":
                continue

            for i, j in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                new_r, new_c = r + i, c + j
                if (
                    0 <= new_r < self.n_rows
                    and 0 <= new_c < self.n_cols
                    and self.new_board[new_r][new_c] == "O"
                ):
                    queue.append([new_r, new_c])

            self.new_board[r][c] = "-1"

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.new_board = board
        self.n_rows = len(self.new_board)
        self.n_cols = len(self.new_board[0])

        for i in range(self.n_cols):
            if self.new_board[0][i] == "O":
                self.bfs(0, i)
            if self.new_board[self.n_rows - 1][i] == "O":
                self.bfs(self.n_rows - 1, i)

        for i in range(self.n_rows):
            if self.new_board[i][0] == "O":
                self.bfs(i, 0)
            if self.new_board[i][self.n_cols - 1] == "O":
                self.bfs(i, self.n_cols - 1)

        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if self.new_board[i][j] == "X" or self.new_board[i][j] == "O":
                    board[i][j] = "X"
                else:
                    board[i][j] = "O"
