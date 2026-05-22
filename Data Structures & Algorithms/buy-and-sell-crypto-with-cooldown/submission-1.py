class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)

            if buying:
                buy = dfs(i + 1, False) - prices[i]
                profit = max(buy, cooldown)
            else:
                sell = dfs(i + 2, True) + prices[i]
                profit = max(sell, cooldown)

            dp[(i, buying)] = profit
            return profit

        return dfs(0, True)