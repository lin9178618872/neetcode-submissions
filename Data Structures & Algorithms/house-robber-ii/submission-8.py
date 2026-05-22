from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        return max(self.robLinear(nums[:-1]), self.robLinear(nums[1:]))

    def robLinear(self, nums: List[int]) -> int:
        # 线性房子偷窃，O(n) 时间，O(n) 空间（可改成滚动变量优化到 O(1) 空间）
        n=len(nums)
        if not nums:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, n + 1):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])

        return dp[n]