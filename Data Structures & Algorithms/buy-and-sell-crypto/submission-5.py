class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        maxProfit = 0

        while right < len(prices):
            # 增大窗口：把 prices[right] 加进来
            # 这里不用真的存 window，因为我们只关心 left 和 right 的价格关系

            # 当前窗口表示 [left, right]
            # left 是买入点，right 是卖出点
            if prices[right] < prices[left]:
                # 相当于“当前窗口不适合继续用了”，重置买入点
                left = right
            else:
                # 可以在 right 这天卖出
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)

            right += 1

        return maxProfit