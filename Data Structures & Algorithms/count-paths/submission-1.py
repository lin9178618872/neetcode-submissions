class Solution:
    """
    不同路径 (Unique Paths) 问题，使用动态规划实现。
    
    dp[i][j] 表示到达网格 (i, j) 的不同路径总数。
    """
    def uniquePaths(self, m: int, n: int) -> int:
        
        # 1. 定义 DP 数组 (列表的列表)
        # 初始化: C++ 代码中将整个 DP 数组初始化为 1，
        # 因为第一行和第一列的路径数都只有 1 条。
        
        # 创建一个 m x n 的二维列表，所有元素初始化为 1
        dp = [[1] * n for _ in range(m)]
        
        # 2. 状态转移计算
        # 从 (1, 1) 开始遍历到 (m-1, n-1)
        # i 代表行索引 (从 1 到 m-1)
        for i in range(1, m):
            # j 代表列索引 (从 1 到 n-1)
            for j in range(1, n):
                
                # 状态转移公式:
                # 到达 (i, j) 的路径数 = 从上方 (i-1, j) 来的路径数 + 从左方 (i, j-1) 来的路径数
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                
        # 3. 返回结果
        # 结果是到达右下角 (m-1, n-1) 的路径总数
        return dp[m - 1][n - 1]

# 示例用法
# solution = Solution()
# print(solution.uniquePaths(3, 7))  # 输出: 28
# print(solution.uniquePaths(3, 2))  # 输出: 3 (RRD, RDR, DRR)