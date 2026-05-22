from collections import defaultdict
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = []
        for i in range(len(nums) + 1):
            dp.append(defaultdict(int))
        dp[0][0] = 1

        for i in range(len(nums)):
            num = nums[i]
            for current_sum in dp[i]:
                ways = dp[i][current_sum]
                new_sum1 = current_sum + num
                dp[i + 1][new_sum1] += ways
                new_sum2 = current_sum - num
                dp[i + 1][new_sum2] += ways

        return dp[len(nums)][target]