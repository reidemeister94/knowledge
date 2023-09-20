from typing import List

"""
You have a graph of n nodes. 
You are given an integer n and an array edges 
where edges[i] = [ai, bi] indicates that 
there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.

https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
"""


class UnionFind:
    def __init__(self, n: int):
        self.size = [1] * n
        self.parent = [x for x in range(n)]
        self.count = n

    def find(self, elem: int):
        while elem != self.parent[elem]:
            self.parent[elem] = self.parent[self.parent[elem]]
            elem = self.parent[elem]
        return elem

    def union(self, a: int, b: int):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return

        if self.size[root_a] >= self.size[root_b]:
            self.parent[root_b] = root_a
            self.size[root_a] += 1

        elif self.size[root_b] > self.size[root_a]:
            self.parent[root_a] = root_b
            self.size[root_b] += 1

        self.count -= 1


class Solution:
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        union_find = UnionFind(n=n)

        for a, b in edges:
            union_find.union(a, b)

        return union_find.count
