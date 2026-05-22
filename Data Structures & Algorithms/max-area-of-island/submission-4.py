class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 记录岛屿的最大面积
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # 淹没岛屿，并更新最大岛屿面积
                    res = max(res, self.dfs(grid, i, j))
        return res

    # 淹没与 (i, j) 相邻的陆地，并返回淹没的陆地面积
    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if i < 0  or i >= m or j < 0 or j >= n:
            # 超出索引边界
            return 0
        if grid[i][j] == 0:
            # 已经是海水了
            return 0
        # 将 (i, j) 变成海水
        grid[i][j] = 0

        return self.dfs(grid, i - 1, j) \
             + self.dfs(grid, i + 1, j) \
             + self.dfs(grid, i, j - 1) \
             + self.dfs(grid, i, j + 1) + 1