class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp_buy = [0] * (n + 1)
        dp_sell = [0] * (n + 1)

        dp_buy[1] = -prices[0]

        for i in range(2, n + 1):
            dp_buy[i] = max(dp_buy[i - 1], dp_sell[i - 2] - prices[i - 1])
            dp_sell[i] = max(dp_sell[i - 1], dp_buy[i - 1] + prices[i - 1])

        return dp_sell[n]