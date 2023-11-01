"""
78. Subsets
https://leetcode.com/problems/subsets/description/
Given an integer array nums of unique elements, return all possible
subsets (the power set).

The solution set must not contain duplicate subsets.
Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
from typing import List


# dp like approach
class Solution:
    def find_subsets(self, nums, idx):
        if idx in self.memo:
            return self.memo[idx]

        if idx == len(nums) - 1:
            self.memo[idx] = [[nums[idx]]]
            return self.memo[idx]

        self.memo[idx] = [[nums[idx]]]
        for subset in self.find_subsets(nums, idx + 1):
            self.memo[idx].append([nums[idx]] + subset)
            self.memo[idx].append(subset)

        return self.memo[idx]

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.memo = {}
        self.find_subsets(nums, 0)
        return [[]] + self.memo[0]


# backtracking approach
class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def backtrack(idx, subset):
            # Base case: If idx is at the end of nums, append the subset and return.
            if idx == len(nums):
                subsets.append(subset.copy())
                return

            # Exclude the current number and recurse.
            backtrack(idx + 1, subset)

            # Include the current number and recurse.
            subset.append(nums[idx])
            backtrack(idx + 1, subset)
            subset.pop()

        backtrack(0, [])
        return subsets
