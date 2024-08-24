"""
1584. Min Cost to Connect All Points
https://leetcode.com/problems/min-cost-to-connect-all-points/description/

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them:
|xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is
exactly one simple path between any two points.



Example 1:


Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18


Constraints:

1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.
"""

import heapq
import copy
from typing import List


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

    def is_connected(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)


class Solution:
    def is_cycle(graph, x1, y1, x2, y2):
        temp_graph = copy.deepcopy(graph)
        temp_graph[(x1, y1)].add((x2, y2))
        temp_graph[(x2, y2)].add((x1, y1))

        visited = set()
        queue = [(x1, y1)]

        while queue:
            elem = queue.pop()
            visited.add(elem)
            for neighbour in temp_graph[elem]:
                if neighbour in visited:
                    return True
                queue.append(neighbour)
        return False

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points_map = {}
        dists = []
        heapq.heapify(dists)
        for i in range(len(points) - 1):
            points_map[(points[i][0], points[i][1])] = i
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(
                    dists, (dist, points[i][0], points[i][1], points[j][0], points[j][1])
                )
        points_map[(points[len(points) - 1][0], points[len(points) - 1][1])] = len(points) - 1

        cost = 0
        edges = 0
        uf = UnionFind(len(points))

        while dists and edges < len(points) - 1:
            dist, x1, y1, x2, y2 = heapq.heappop(dists)
            if not uf.is_connected(points_map[(x1, y1)], points_map[(x2, y2)]):
                uf.union(points_map[(x1, y1)], points_map[(x2, y2)])
                cost += dist
                edges += 1

        return cost
