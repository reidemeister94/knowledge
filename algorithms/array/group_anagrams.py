from collections import defaultdict
from typing import List

"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/description/
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        occurrences_map = defaultdict(list)
        for elem in strs:
            occurrences_elem = [0] * 26
            for char in elem:
                pos = ord(char) - ord("a")
                occurrences_elem[pos] += 1
            occurrences_elem = tuple(occurrences_elem)
            occurrences_map[occurrences_elem].append(elem)

        return occurrences_map.values()
