class Solution:
    def rob(self, nums: list[int]) -> int:
        nums_len = len(nums)

        if nums_len == 0:
            return 0
        
        dp = [0] * (nums_len + 1)
        dp[0]=nums[0]

        dp[1] = nums[0]

        if nums_len > 1:
            dp[2] = max(nums[0], nums[1])

        for i in range(3, nums_len + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

        return dp[nums_len]
