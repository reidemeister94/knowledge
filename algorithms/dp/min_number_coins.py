"""
Given an array of positive integers representing coin denominations and 
a single non-negative integer n representing a target amount of money, 
write a function that returns the smallest number of coins needed to make 
change for (to sum up to) that target amount using the given coin denominations.
Note that you have access to an unlimited amount of coins. In other words, 
if the denominations are [1, 5, 10], you have access to an unlimited amount of 1s, 5s, and 10s.
If it's impossible to make change for the target amount, return -1.
"""


def minNumberOfCoinsForChange(n, denoms):
    min_coins = [float("inf") for _ in range(n + 1)]
    min_coins[0] = 0
    for i in range(1, len(min_coins)):
        for j in range(len(denoms)):
            if denoms[j] <= i and min_coins[i - denoms[j]] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - denoms[j]] + 1
    if min_coins[n] != float("inf"):
        return min_coins[n]
    return -1
