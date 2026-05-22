from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        rows = len(grid)
        cols = len(grid[0])

        def backtrack(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == "0":
                return

            grid[r][c] = "0"

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                backtrack(new_r, new_c)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    result += 1
                    backtrack(i, j)

        return result