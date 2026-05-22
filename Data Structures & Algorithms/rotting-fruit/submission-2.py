from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        q = deque()
        fresh = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        step = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            sz = len(q)
            rotted_this_min = 0

            for _ in range(sz):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        rotted_this_min += 1
                        q.append((nr, nc))

            if rotted_this_min > 0:
                step += 1

            if fresh == 0:
                return step

        return -1