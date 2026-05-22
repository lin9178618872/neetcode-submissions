class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robRange(arr):
            if len(arr) == 0:
                return 0
            if len(arr) == 1:
                return arr[0]

            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 2] + arr[i], dp[i - 1])

            return dp[-1]

        return max(robRange(nums[:-1]), robRange(nums[1:]))