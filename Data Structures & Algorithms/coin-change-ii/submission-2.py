class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)

        # 凑出金额0只有1种方式（什么都不选）
        dp[0] = 1

        # 先遍历硬币
        for coin in coins:

            # 再遍历金额
            for i in range(coin, amount + 1):

                # 当前金额的组合数 += 去掉这个coin之前的组合数
                dp[i] += dp[i - coin]

        return dp[amount]