from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        return max(self._robLinear(nums[:-1]), self._robLinear(nums[1:]))

    def _robLinear(self, nums: List[int]) -> int:
        # 线性房子偷窃，O(n) 时间，O(n) 空间（可改成滚动变量优化到 O(1) 空间）
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, len(nums) + 1):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])

        return dp[len(nums)]