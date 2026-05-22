class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        # 创建 dp 数组
        # dp[i] 表示：凑出金额 i 需要的最少硬币数
        dp = [float('inf')] * (amount + 1)

        # base case
        # 凑出金额0需要0个硬币
        dp[0] = 0

        # 从金额1开始计算，一直到 amount
        for i in range(1, amount + 1):

            # 尝试每一种硬币
            for coin in coins:

                # 如果当前硬币可以用
                if i >= coin:

                    # 状态转移
                    # 用一个 coin 后
                    # 剩下的钱是 i - coin
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # 如果还是无限大，说明凑不出来
        if dp[amount] == float('inf'):
            return -1

        # 否则返回最少硬币数
        return dp[amount]