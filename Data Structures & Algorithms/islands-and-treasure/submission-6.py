from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        m, n = len(grid), len(grid[0])

        # 1️⃣ 初始化队列（多源 BFS：所有 0 入队）
        q = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))

        # 2️⃣ 初始化 step（层数）
        step = 0

        # 3️⃣ 定义方向（neighbors）
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # 4️⃣ BFS 主循环
        while q:
            # 5️⃣ 遍历当前层
            for _ in range(len(q)):
                r, c = q.popleft()

                # 6️⃣ 扩展邻居
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    # 7️⃣ 判断是否合法 + 是否访问过（INF = 未访问）
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == INF:
                        grid[nr][nc] = step + 1   # 更新距离
                        q.append((nr, nc))

            # 8️⃣ 进入下一层
            step += 1
        