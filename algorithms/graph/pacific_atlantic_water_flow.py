"""
https://leetcode.com/problems/pacific-atlantic-water-flow/description/

417. Pacific Atlantic Water Flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches
the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer
matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring
cells directly north, south, east, and west if the neighboring cell's height
is less than or equal to the current cell's height.
Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci]
denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.



Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.


Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
"""

from collections import deque
from typing import List


class Solution:

    def bfs(self, heights, queue):

        reachable = set()

        while queue:
            r, c = queue.popleft()
            if (r, c) in reachable:
                continue

            reachable.add((r, c))

            for inc_r, inc_c in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                new_r = r + inc_r
                new_c = c + inc_c
                if (
                    (new_r, new_c) not in reachable
                    and 0 <= new_r < len(heights)
                    and 0 <= new_c < len(heights[0])
                    and heights[r][c] <= heights[new_r][new_c]
                ):
                    queue.append([new_r, new_c])
        return reachable

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific_starts = deque([])
        for i in range(len(heights[0])):
            pacific_starts.append([0, i])
        for i in range(1, len(heights)):
            pacific_starts.append([i, 0])

        reach_pacific = self.bfs(heights, pacific_starts)

        atlantic_starts = deque([])
        for i in range(len(heights[0])):
            atlantic_starts.append([len(heights) - 1, i])
        for i in range(len(heights) - 1):
            atlantic_starts.append([i, len(heights[0]) - 1])

        reach_atlantic = self.bfs(heights, atlantic_starts)

        return list(reach_atlantic.intersection(reach_pacific))


if __name__ == "__main__":

    heights = [[1, 1], [1, 1], [1, 1]]

    sol = Solution()
    print(sol.pacificAtlantic(heights))
