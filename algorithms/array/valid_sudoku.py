"""
36. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/description/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells
need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:


Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8.
Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

"""
from typing import List


class Solution:
    def check_block(self, board, row, col):
        nums = set()

        for i in range(row, row + 3):
            for j in range(col, col + 3):
                if board[i][j] != ".":
                    if int(board[i][j]) in nums:
                        return False
                    nums.add(int(board[i][j]))
        return True

    def check_row(self, board, row):
        nums = set()

        for col in range(9):
            if board[row][col] != ".":
                if int(board[row][col]) in nums:
                    return False
                nums.add(int(board[row][col]))
        return True

    def check_col(self, board, col):
        nums = set()

        for row in range(9):
            if board[row][col] != ".":
                if int(board[row][col]) in nums:
                    return False
                nums.add(int(board[row][col]))
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in [0, 3, 6]:
            for col in [0, 3, 6]:
                if not self.check_block(board, row, col):
                    return False

        for i in range(9):
            if not self.check_row(board, i):
                return False
            if not self.check_col(board, i):
                return False

        return True
