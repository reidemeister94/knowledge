"""
https://leetcode.com/problems/walls-and-gates/description/

286. Walls and Gates

You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room.
We use the value 231 - 1 = 2147483647 to represent INF as you may assume
that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate.
If it is impossible to reach a gate, it should be filled with INF.



Example 1:


Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],
[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Input: rooms = [[-1]]
Output: [[-1]]


Constraints:

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 231 - 1.
"""

from typing import List
from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return

        m, n = len(rooms), len(rooms[0])
        queue = deque()

        # Initialize the queue with all gates
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        # Perform BFS from all gates
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and rooms[r][c] == 2147483647:
                    rooms[r][c] = rooms[row][col] + 1
                    queue.append((r, c))


if __name__ == "__main__":
    rooms = [
        [
            0,
            2147483647,
            -1,
            2147483647,
            2147483647,
            -1,
            -1,
            0,
            0,
            -1,
            2147483647,
            2147483647,
            0,
            -1,
            2147483647,
            2147483647,
            2147483647,
            2147483647,
            0,
            2147483647,
            0,
            -1,
            -1,
            -1,
            -1,
            2147483647,
            -1,
            -1,
            2147483647,
            2147483647,
            -1,
            -1,
            0,
            0,
            -1,
            0,
            0,
            0,
            2147483647,
            0,
            2147483647,
            -1,
            -1,
            0,
            -1,
            0,
            0,
            0,
            2147483647,
        ],
        [
            2147483647,
            0,
            -1,
            2147483647,
            0,
            -1,
            -1,
            -1,
            -1,
            0,
            0,
            2147483647,
            2147483647,
            -1,
            -1,
            2147483647,
            -1,
            -1,
            2147483647,
            2147483647,
            -1,
            0,
            -1,
            2147483647,
            0,
            2147483647,
            -1,
            2147483647,
            0,
            2147483647,
            0,
            2147483647,
            -1,
            2147483647,
            0,
            2147483647,
            -1,
            2147483647,
            0,
            2147483647,
            2147483647,
            0,
            -1,
            2147483647,
            -1,
            -1,
            -1,
            0,
            2147483647,
        ],
    ]

    sol = Solution()
    sol.wallsAndGates(rooms)

    assert rooms == [
        [
            0,
            1,
            -1,
            2,
            1,
            -1,
            -1,
            0,
            0,
            -1,
            1,
            1,
            0,
            -1,
            4,
            3,
            2,
            1,
            0,
            1,
            0,
            -1,
            -1,
            -1,
            -1,
            2,
            -1,
            -1,
            1,
            2,
            -1,
            -1,
            0,
            0,
            -1,
            0,
            0,
            0,
            1,
            0,
            1,
            -1,
            -1,
            0,
            -1,
            0,
            0,
            0,
            1,
        ],
        [
            1,
            0,
            -1,
            1,
            0,
            -1,
            -1,
            -1,
            -1,
            0,
            0,
            1,
            1,
            -1,
            -1,
            4,
            -1,
            -1,
            1,
            2,
            -1,
            0,
            -1,
            1,
            0,
            1,
            -1,
            1,
            0,
            1,
            0,
            1,
            -1,
            1,
            0,
            1,
            -1,
            1,
            0,
            1,
            1,
            0,
            -1,
            1,
            -1,
            -1,
            -1,
            0,
            1,
        ],
    ]
