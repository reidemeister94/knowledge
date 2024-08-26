"""
684. Redundant Connection
https://leetcode.com/problems/redundant-connection/description/

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n,
with one additional edge added. The added edge has two different vertices chosen from 1 to n,
and was not an edge that already existed.
The graph is represented as an array edges of length n where edges[i] = [ai, bi]
indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes.
If there are multiple answers, return the answer that occurs last in the input.



Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]


Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""

from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def find(self, elem: int):
        if self.parent[elem] != elem:
            self.parent[elem] = self.find(self.parent[elem])
        return self.parent[elem]

    def union(self, a: int, b: int):
        a_par = self.find(a)
        b_par = self.find(b)
        if a_par == b_par:
            return False

        if self.size[a_par] >= self.size[b_par]:
            self.parent[a_par] = b_par
            self.size[b_par] += 1
        else:
            self.parent[b_par] = a_par
            self.size[a_par] += 1
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))

        for a, b in edges:
            if not uf.union(a, b):
                return [a, b]
