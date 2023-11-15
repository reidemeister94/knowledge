"""
567. Permutation in String
https://leetcode.com/problems/permutation-in-string/description/

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        occ_1 = [0] * 26
        for el in s1:
            occ_1[ord(el) - ord("a")] += 1

        occ_2 = [0] * 26
        for i in range(len(s1)):
            occ_2[ord(s2[i]) - ord("a")] += 1

        if occ_1 == occ_2:
            return True

        for i in range(1, len(s2) - len(s1) + 1):
            occ_2[ord(s2[i + len(s1) - 1]) - ord("a")] += 1
            occ_2[ord(s2[i - 1]) - ord("a")] -= 1
            if occ_1 == occ_2:
                return True
        return False
