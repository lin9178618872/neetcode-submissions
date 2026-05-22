from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        pac = set()
        atl = set()

        def isTarget(r, c, visited, prev_height):
            # 1. 越界
            if r < 0 or r >= m or c < 0 or c >= n:
                return False

            # 2. 已访问
            if (r, c) in visited:
                return False

            # 3. 高度不符合
            # 反向流动，所以只能从低处往高处走
            if heights[r][c] < prev_height:
                return False

            return True

        def dfs(r, c, visited, prev_height):
            # 1. 判断当前点是否可以走
            if not isTarget(r, c, visited, prev_height):
                return

            # 2. 标记访问
            visited.add((r, c))

            # 3. 四方向扩散
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])

        # 从太平洋边界出发：上边界 + 左边界
        for c in range(n):
            dfs(0, c, pac, heights[0][c])

        for r in range(m):
            dfs(r, 0, pac, heights[r][0])

        # 从大西洋边界出发：下边界 + 右边界
        for c in range(n):
            dfs(m - 1, c, atl, heights[m - 1][c])

        for r in range(m):
            dfs(r, n - 1, atl, heights[r][n - 1])

        # 同时能到太平洋和大西洋的点
        res = []

        for r in range(m):
            for c in range(n):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res