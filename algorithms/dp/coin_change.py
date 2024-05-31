"""
https://leetcode.com/problems/coin-change/description/
322. Coin Change
-----------
You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0


Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""

from collections import deque
from typing import List


class Solution:
    def bfs(self, coins, amount):
        queue = deque([(c, c, 1) for c in coins])
        visited = set()

        while queue:
            coin, curr, n_coins = queue.popleft()

            if curr == amount:
                return n_coins

            if curr not in visited:
                visited.add(curr)
            else:
                continue

            for c in coins:
                if curr + c == amount:
                    return n_coins + 1
                elif curr + c < amount and curr + c not in visited:
                    queue.append((c, curr + c, n_coins + 1))
        return -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort(reverse=True)

        min_coins = self.bfs(coins, amount)
        return min_coins


"""dynamic programming solution"""


class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        return dp[-1] if dp[-1] != amount + 1 else -1
