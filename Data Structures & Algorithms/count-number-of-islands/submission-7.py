class Solution:

    def numIslands(self, grid):

        m, n = len(grid), len(grid[0])

        visited = set()

        # 统一模板
        def dfs(cur, visited, extra):

            grid = extra

            i, j = cur

            # 越界
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            # 海水
            if grid[i][j] == '0':
                return

            # 已访问
            if cur in visited:
                return

            # 标记
            visited.add(cur)

            # 四个方向
            dirs = [(1,0), (-1,0), (0,1), (0,-1)]

            for dx, dy in dirs:

                ni = i + dx
                nj = j + dy

                dfs((ni, nj), visited, grid)

        res = 0

        for i in range(m):
            for j in range(n):

                if grid[i][j] == '1' and (i,j) not in visited:

                    res += 1

                    dfs((i,j), visited, grid)

        return res

