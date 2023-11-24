"""
74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/description/

You are given an m x n integer matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_up, row_down = 0, len(matrix) - 1
        while row_up <= row_down:
            mid_row = (row_up + row_down) // 2
            if target == matrix[mid_row][0]:
                return True
            elif target < matrix[mid_row][0]:
                row_down = mid_row - 1
            elif target > matrix[mid_row][0] and target > matrix[mid_row][-1]:
                row_up = mid_row + 1
            elif target > matrix[mid_row][0] and target <= matrix[mid_row][-1]:
                left, right = 0, len(matrix[0]) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if matrix[mid_row][mid] == target:
                        return True
                    elif matrix[mid_row][mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
                return False
        return False
