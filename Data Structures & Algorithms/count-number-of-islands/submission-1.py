from collections import deque

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        islands = 0

        def bfs(sr, sc):
            queue = deque()
            queue.append((sr, sc))
            grid[sr][sc] = '0'    # 标记为水，表示访问过

            while queue:
                r, c = queue.popleft()

                # 四个方向
                for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == '1':
                            queue.append((nr, nc))
                            grid[nr][nc] = '0'   # 标记访问过

        # 主循环：找每个岛的起点
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':   # 找到新岛
                    islands += 1
                    bfs(r, c)           # BFS 把整个岛淹掉

        return islands
