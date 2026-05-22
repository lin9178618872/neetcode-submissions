class Solution:
    def rob(self, nums: List[int]) -> int:
        # 特殊情况
        if len(nums) == 1:
            return nums[0]

        # 工具：求线性 rob（House Robber I）
        def rob_linear(arr):
            n = len(arr)
            # ---- 自底向上 DP（按模板） ----
            if n == 0:
                return 0
            if n == 1:
                return arr[0]

            dp = [0] * n
            # base case
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            # 状态转移
            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

            return dp[-1]

        # 环形 → 两次线性 DP
        return max(
            rob_linear(nums[1:]),   # 不包含第0个
            rob_linear(nums[:-1])   # 不包含最后一个
        )
