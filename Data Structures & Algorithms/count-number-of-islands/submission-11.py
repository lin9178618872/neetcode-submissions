class Solution:

    def numIslands(self, grid):

        m, n = len(grid), len(grid[0])

        visited = set()

        # 统一模板
        def dfs(cur, visited, extra):

            grid = extra

            r, c = cur#这个为主函数传入的坐标(0,1)变0为r，1为c

            # 越界
            if r < 0 or r >= m or c < 0 or c >= n:
                return

            # 海水
            if grid[r][c] == '0':
                return

            # 已访问
            if cur in visited:
                return

            # 标记
            visited.add(cur)

            # 四个方向
            dirs = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in dirs:

                nr = r + dr
                nc = c + dc

                dfs((nr, nc), visited, grid)

        res = 0

        for r in range(m):
            for c in range(n):

                if grid[r][c] == '1' and (r, c) not in visited:

                    res += 1

                    dfs((r, c), visited, grid)

        return res