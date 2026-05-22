import math

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        nums_len = len(nums)
        if nums_len == 0:
            return 0

        dp = [1] * nums_len

        for i in range(nums_len):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
