"""
266. Palindrome Permutation
https://leetcode.com/problems/palindrome-permutation/description/

Given a string s, return true if a permutation of the string could form a
palindrome and false otherwise.



Example 1:

Input: s = "code"
Output: false
Example 2:

Input: s = "aab"
Output: true
Example 3:

Input: s = "carerac"
Output: true


Constraints:

1 <= s.length <= 5000
s consists of only lowercase English letters.
"""
from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count_s = Counter(s)

        n_odd = False

        for i, c in count_s.items():
            if c % 2 != 0:
                if n_odd:
                    return False
                n_odd = True

        return True
