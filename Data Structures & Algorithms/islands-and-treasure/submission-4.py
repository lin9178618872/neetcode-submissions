from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF=2147483647
        m, n = len(grid), len(grid[0])

        q = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))

        step = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            sz = len(q)
            for _ in range(sz):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == INF:
                        grid[nr][nc] = step + 1
                        q.append((nr, nc))
            step += 1