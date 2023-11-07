"""

3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string s, find the length of the longest
substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_map = {}
        left, right = 0, 0
        longest_substring = 0

        while right < len(s):
            if s[right] in seen_map and seen_map[s[right]] >= left:
                longest_substring = max(longest_substring, right - left)
                left = seen_map[s[right]] + 1
            seen_map[s[right]] = right
            right += 1
        return max(longest_substring, right - left)
