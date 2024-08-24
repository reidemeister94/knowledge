import heapq  # Import the heapq module for priority queue operations
from typing import List  # Import List from typing for type annotations


# A helper class to manage Union-Find (Disjoint Set Union) operations
class UnionFind:
    def __init__(self, n: int):
        # Initialize the size of each set as 1
        self.size = [1] * n
        # Initialize the parent of each element to be itself
        self.parent = [x for x in range(n)]
        # Initialize the count of disjoint sets to n
        self.count = n

    def find(self, elem: int):
        # Path compression to find the root of the set containing elem
        while elem != self.parent[elem]:
            # Point elem directly to its grandparent (path compression)
            self.parent[elem] = self.parent[self.parent[elem]]
            elem = self.parent[elem]
        return elem

    def union(self, a: int, b: int):
        # Find the roots of the sets containing elements a and b
        root_a = self.find(a)
        root_b = self.find(b)

        # If both elements are already in the same set, do nothing
        if root_a == root_b:
            return

        # Union by size: attach the smaller tree under the larger tree
        if self.size[root_a] >= self.size[root_b]:
            self.parent[root_b] = root_a
            self.size[root_a] += 1
        elif self.size[root_b] > self.size[root_a]:
            self.parent[root_a] = root_b
            self.size[root_b] += 1

        # Decrement the number of disjoint sets
        self.count -= 1

    def is_connected(self, a: int, b: int) -> bool:
        # Check if elements a and b are in the same set
        return self.find(a) == self.find(b)


# Main solution class to solve the problem
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Map to store points and their corresponding index
        points_map = {}
        # Priority queue to store edges based on their distances
        dists = []
        heapq.heapify(dists)  # Initialize the priority queue

        # Generate all pairs of points and calculate the Manhattan distance between them
        for i in range(len(points) - 1):
            points_map[(points[i][0], points[i][1])] = i  # Map the point to its index
            for j in range(i + 1, len(points)):
                # Calculate Manhattan distance
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                # Push the distance and corresponding points to the priority queue
                heapq.heappush(
                    dists, (dist, points[i][0], points[i][1], points[j][0], points[j][1])
                )

        # Add the last point to the points map
        points_map[(points[len(points) - 1][0], points[len(points) - 1][1])] = len(points) - 1

        cost = 0  # Variable to store the total cost
        edges = 0  # Variable to count the number of edges added to the MST
        uf = UnionFind(len(points))  # Initialize UnionFind with the number of points

        # Process edges in ascending order of their distance
        while dists and edges < len(points) - 1:
            # Get the smallest edge from the priority queue
            dist, x1, y1, x2, y2 = heapq.heappop(dists)
            # Check if the two points are already connected
            if not uf.is_connected(points_map[(x1, y1)], points_map[(x2, y2)]):
                # If not connected, connect them and add the distance to the total cost
                uf.union(points_map[(x1, y1)], points_map[(x2, y2)])
                cost += dist
                edges += 1  # Increment the number of edges in the MST

        # Return the minimum cost to connect all points
        return cost
