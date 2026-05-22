class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # 1. 创建一个 m 行 n 列 的二维数组
        dp = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(0)
            dp.append(row)

        # 2. 第一行只能一直向右走，所以路径数都是 1
        for j in range(n):
            dp[0][j] = 1

        # 3. 第一列只能一直向下走，所以路径数都是 1
        for i in range(m):
            dp[i][0] = 1

        # 4. 计算其他位置
        for i in range(1, m):
            for j in range(1, n):
                # 当前格子的路径 = 上面 + 左边
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # 5. 右下角就是答案
        return dp[m-1][n-1]