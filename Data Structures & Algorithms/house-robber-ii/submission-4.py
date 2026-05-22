class Solution:
    def rob(self, nums: list[int]) -> int:
        # 如果只有 1 间房子，直接偷它
        if len(nums) == 1:
            return nums[0]

        # 处理“打家劫舍 I（直线）”的函数
        def rob_linear(nums: list[int]) -> int:
            n = len(nums)

            # 没有房子
            if n == 0:
                return 0

            # dp[i] 表示：前 i 间房子最多能偷多少钱
            dp = [0] * (n + 1)

            # 前 1 间房子，最多偷 nums[0]
            dp[1] = nums[0]

            # 前 2 间房子，只能选钱多的那一间
            if n > 1:
                dp[2] = max(nums[0], nums[1])

            # 从第 3 间房子开始递推
            for i in range(3, n + 1):
                # 两种选择：
                # 1. 不偷第 i 间房子 -> dp[i - 1]
                # 2. 偷第 i 间房子 -> dp[i - 2] + nums[i - 1]
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

            # 返回前 n 间房子的最大值
            return dp[n]

        # 因为房子成环：
        # 不能同时偷第 1 间和最后 1 间
        # 所以分两种情况：
        # 1. 不偷第 1 间 -> nums[1:]
        # 2. 不偷最后 1 间 -> nums[:-1]
        return max(
            rob_linear(nums[1:]),
            rob_linear(nums[:-1])
        )