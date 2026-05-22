class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n

        # 初始化 base case
        # dp[i] 表示到达第 i 级台阶的方法总数
        dp = [0] * (n + 1)
        dp[0] = 1  # 到达第 0 级 (起点) 的方法数
        dp[1] = 1  # 到达第 1 级的方法数 (1)
        
        # 进行状态转移
        for i in range(2, n + 1):
            # dp[i] = 求最值(选择1，选择2...)
            # 状态转移方程：dp[i] = dp[i-1] + dp[i-2]
            # 可以迈 1 步从 i-1 到达 i，或迈 2 步从 i-2 到达 i
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]