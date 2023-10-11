"""
https://leetcode.com/problems/decode-ways/description/
Decode Ways

A message containing letters from A-Z can be encoded into
numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped
then mapped back into letters using the reverse of the
mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06"
cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.



Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of
the leading zero ("6" is different from "06").


Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
"""


class Solution:
    def dp(self, s, idx):
        if (idx == len(s) - 1 and s[idx] != "0") or idx > len(s) - 1:
            return 1

        if s[idx] == "0":
            return 0

        if idx in self.memo:
            return self.memo[idx]

        if s[idx] == "1" or (s[idx] == "2" and int(s[idx + 1]) <= 6):
            self.memo[idx] = self.dp(s, idx + 1) + self.dp(s, idx + 2)
        else:
            self.memo[idx] = self.dp(s, idx + 1)

        return self.memo[idx]

    def numDecodings(self, s: str) -> int:
        self.memo = {}
        self.dp(s, 0)
        if len(s) == 1 and s[0] != "0":
            return 1

        return self.memo[0] if 0 in self.memo else 0


"""Iterative solution"""


class Solution2:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        dp = [0 for x in range(len(s) + 1)]

        # base case initialization
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1  # (1)

        for i in range(2, len(s) + 1):
            # One step jump
            if 0 < int(s[i - 1 : i]) <= 9:  # (2)
                dp[i] += dp[i - 1]
            # Two step jump
            if 10 <= int(s[i - 2 : i]) <= 26:  # (3)
                dp[i] += dp[i - 2]
        return dp[len(s)]
