"""
20. Valid Parenthesis
https://leetcode.com/problems/valid-parentheses/description/

Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for el in s:
            if el in ["(", "[", "{"]:
                stack.append(el)
            else:
                if not stack or stack[-1] != parenthesis_map[el]:
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        return True
