"""
347. Top K Frequent Elements

https://leetcode.com/problems/top-k-frequent-elements/description/
Given an integer array nums and an integer k,
return the k most frequent elements.
You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n),
where n is the array's size.
"""

from collections import defaultdict
import heapq

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurrences_map = defaultdict(int)
        occurrences_map_inverse = defaultdict(list)

        for elem in nums:
            occurrences_map[elem] += 1

        for el, occ in occurrences_map.items():
            occurrences_map_inverse[occ].append(el)

        n_largest = heapq.nlargest(k, list(occurrences_map_inverse.keys()))

        output = []
        idx = 0
        while len(output) < k:
            curr_occ = n_largest[idx]
            elems = occurrences_map_inverse[curr_occ]
            for elem in elems[:k]:
                output.append(elem)
            idx += 1

        return output
