class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []

        rows_cnt = len(heights)
        cols_cnt = len(heights[0])

        pac_visit = [[False] * cols_cnt for _ in range(rows_cnt)]
        atl_visit = [[False] * cols_cnt for _ in range(rows_cnt)]

        for j in range(cols_cnt):
            self.dfs(heights, 0, j, pac_visit, heights[0][j])
            self.dfs(heights, rows_cnt - 1, j, atl_visit, heights[rows_cnt - 1][j])

        for i in range(rows_cnt):
            if not pac_visit[i][0]:
                self.dfs(heights, i, 0, pac_visit, heights[i][0])
            if not atl_visit[i][cols_cnt - 1]:
                self.dfs(heights, i, cols_cnt - 1, atl_visit, heights[i][cols_cnt - 1])

        res = []
        for i in range(rows_cnt):
            for j in range(cols_cnt):
                if pac_visit[i][j] and atl_visit[i][j]:
                    res.append([i, j])

        return res

    def dfs(self, heights: list[list[int]], row: int, col: int, visit: list[list[bool]], prevHeight: int) -> None:
        rows_cnt = len(heights)
        cols_cnt = len(heights[0])

        if (
            row < 0 or col < 0 or
            row >= rows_cnt or col >= cols_cnt or
            visit[row][col] or
            heights[row][col] < prevHeight
        ):
            return

        visit[row][col] = True
        currentHeight = heights[row][col]

        self.dfs(heights, row + 1, col, visit, currentHeight)
        self.dfs(heights, row - 1, col, visit, currentHeight)
        self.dfs(heights, row, col + 1, visit, currentHeight)
        self.dfs(heights, row, col - 1, visit, currentHeight)
