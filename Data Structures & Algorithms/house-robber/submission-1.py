class Solution:
    def rob(self, nums: list[int]) -> int:
        nums_len = len(nums)
        
        # 优化：对于这种动态规划问题，我们可以通过只保留前两个状态
        # 来避免创建一个完整的dp数组，从而将空间复杂度从 O(n) 降低到 O(1)。
        # 但为了更贴近C++代码的DP数组逻辑，我们先用 O(n) 的DP数组实现。
        
        # dp[i] 表示偷窃前 i 个房屋（即 nums[0] 到 nums[i-1]）能获得的最大金额
        # 数组大小为 nums_len + 1，dp[0] 保持为 0
        dp = [0] * (nums_len + 1)
        
        if nums_len == 0:
            return 0
        
        # 边界条件/初始化
        # 偷窃前 1 个房屋 (nums[0])
        dp[1] = nums[0]
        
        # 偷窃前 2 个房屋 (nums[0], nums[1])
        if nums_len > 1:
            dp[2] = max(nums[0], nums[1])
            
        # 状态转移
        # i 从 3 开始，直到 nums_len + 1 (不包含)，对应着计算 dp[3] 到 dp[nums_len]
        # nums[i-1] 对应着第 i 个房屋的金额
        for i in range(3, nums_len + 1):
            # 状态转移公式：
            # 1. 不偷第 i 个房屋：最大金额为 dp[i-1]
            # 2. 偷第 i 个房屋：最大金额为 dp[i-2]（因为不能偷第 i-1 个）+ nums[i-1]（第 i 个房屋的金额）
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
            
        # 最终结果是偷窃所有 nums_len 个房屋的最大金额
        return dp[nums_len]

# 示例测试
# solution = Solution()
# print(solution.rob([1, 2, 3, 1]))  # 输出: 4
# print(solution.rob([2, 7, 9, 3, 1]))  # 输出: 12