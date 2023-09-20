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


class Solution:
    def dfs(self, a, adj_list):
        queue = [a]

        while queue:
            elem = queue.pop(0)
            to_visit = adj_list[elem]
            for el in to_visit:
                if el not in self.visited:
                    queue.append(el)
            self.visited.add(elem)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.visited = set()
        n_comp = 0

        adj_list = {}

        for a, b in edges:
            if a not in adj_list:
                adj_list[a] = {b}
            elif b not in adj_list[a]:
                adj_list[a].add(b)

            if b not in adj_list:
                adj_list[b] = {a}
            elif a not in adj_list[b]:
                adj_list[b].add(a)

        for a, adj in adj_list.items():
            if a not in self.visited:
                n_comp += 1
                self.dfs(a, adj_list)

        return n_comp + (n - len(self.visited))
