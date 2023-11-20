"""
22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/description/

Given n pairs of parentheses,
write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses = []

        def generate(open, close=0, curr=""):
            if open == 0:
                curr += ")" * close
                parentheses.append(curr)
                return

            if close == 0:
                generate(open - 1, close + 1, curr + "(")
            else:
                generate(open - 1, close + 1, curr + "(")
                if close <= (n - open):
                    generate(open, close - 1, curr + ")")

        generate(n)
        return parentheses
