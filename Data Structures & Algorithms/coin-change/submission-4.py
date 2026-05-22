class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        # handle i = 1 (if amount >= 1)
        if amount >= 1:
            for coin in coins:
                if 1 - coin >= 0:
                    dp[1] = min(dp[1], dp[1 - coin] + 1)

        # start from i = 2
        for i in range(2, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[amount] == float('inf') else dp[amount]