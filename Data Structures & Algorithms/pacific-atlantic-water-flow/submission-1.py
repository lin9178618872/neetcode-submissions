class Solution:
    """
    寻找可以同时将水流向太平洋和大西洋的网格坐标。
    采用从边界逆流而上的DFS方法。
    """
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """
        主函数，执行太平洋大西洋水流问题。
        """
        if not heights or not heights[0]:
            return []

        rows_cnt = len(heights)
        cols_cnt = len(heights[0])
        
        # 能流向太平洋的坐标 (从太平洋边界开始逆流而上)
        pac_visit = [[False] * cols_cnt for _ in range(rows_cnt)]
        # 能流向大西洋的坐标 (从大西洋边界开始逆流而上)
        atl_visit = [[False] * cols_cnt for _ in range(rows_cnt)]

        # --- 从边界开始DFS ---

        # 遍历第一行 (太平洋) 和最后一行 (大西洋)
        for j in range(cols_cnt):
            # 对矩阵的上边每个毗邻太平洋的坐标进行dfs (row=0)
            self.dfs(heights, 0, j, pac_visit, heights[0][j])
            # 对矩阵下边每个毗邻大西洋的坐标进行dfs (row=rows_cnt - 1)
            self.dfs(heights, rows_cnt - 1, j, atl_visit, heights[rows_cnt - 1][j])

        # 遍历第一列 (太平洋) 和最后一列 (大西洋)
        for i in range(rows_cnt):
            # 对矩阵左边每个毗邻太平洋的坐标进行dfs (col=0)
            # 注意: 避免重复处理四个角，但因为 visit 数组会处理，所以重复调用是安全的。
            if not pac_visit[i][0]: # 优化：如果角点已经被上面的循环处理了，可以跳过
                 self.dfs(heights, i, 0, pac_visit, heights[i][0])
            
            # 对矩阵右边每个毗邻大西洋的坐标进行dfs (col=cols_cnt - 1)
            if not atl_visit[i][cols_cnt - 1]: # 优化：如果角点已经被上面的循环处理了，可以跳过
                self.dfs(heights, i, cols_cnt - 1, atl_visit, heights[i][cols_cnt - 1])

        # --- 收集结果 ---
        
        res = []
        for i in range(rows_cnt):
            for j in range(cols_cnt):
                if pac_visit[i][j] and atl_visit[i][j]:
                    # 保存既可以流向大西洋又可以流向太平洋的坐标点
                    res.append([i, j])

        return res

    def dfs(self, heights: list[list[int]], row: int, col: int, visit: list[list[bool]], prevHeight: int) -> None:
        """
        深度优先搜索函数，从当前点 (row, col) 开始，逆流而上标记所有可到达的点。

        Args:
            heights: 地形高度矩阵。
            row: 当前行索引。
            col: 当前列索引。
            visit: 标记是否可到达该海洋的布尔矩阵。
            prevHeight: 逆流方向上，上一个格子的高度 (即当前格子的高度必须 >= prevHeight 才能逆流而上)。
        """
        rows_cnt = len(heights)
        cols_cnt = len(heights[0])
        
        # 递归的返回条件：
        # 1. 当前坐标超出矩阵范围
        # 2. 当前坐标已经被标记过 (已经确定可到达该海洋)
        # 3. 当前坐标对应的高度小于上一个坐标对应的高度 (水不能逆流而上)
        if (row < 0 or col < 0 or row >= rows_cnt or col >= cols_cnt or 
            visit[row][col] or heights[row][col] < prevHeight):
            return
            
        # 标记当前点可以流向目标海洋
        visit[row][col] = True
        
        currentHeight = heights[row][col]
        
        # 四个方向进行DFS (逆流而上)
        
        # 下 (流向 row + 1, col)
        self.dfs(heights, row + 1, col, visit, currentHeight)
        # 上 (流向 row - 1, col)
        self.dfs(heights, row - 1, col, visit, currentHeight)
        # 右 (流向 row, col + 1)
        self.dfs(heights, row, col + 1, visit, currentHeight)
        # 左 (流向 row, col - 1)
        self.dfs(heights, row, col - 1, visit, currentHeight)

# # 示例用法 (如果您需要运行测试)
# solution = Solution()
# heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# result = solution.pacificAtlantic(heights)
# print(result)
# # 预期输出: [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]