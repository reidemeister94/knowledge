"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation."""


def productExceptSelf(nums):
    p = 1
    n = len(nums)
    output = []
    for i in range(0, n):
        output.append(p)
        p = p * nums[i]
    p = 1
    for i in range(n - 1, -1, -1):
        output[i] = output[i] * p
        p = p * nums[i]
    return output
