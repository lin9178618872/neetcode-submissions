import math

class Solution:
    """
    最长递增子序列 (Longest Increasing Subsequence, LIS) 问题，使用动态规划实现。
    
    dp[i] 表示以 nums[i] 结尾的最长递增子序列的长度。
    """
    def lengthOfLIS(self, nums: list[int]) -> int:
        
        nums_len = len(nums)
        
        # 如果数组为空，则最长递增子序列的长度为 0
        if nums_len == 0:
            return 0
        
        # 定义 DP 数组 (列表)
        # dp 列表的大小与 nums 相同。
        # 边界条件初始化: 每一个元素本身都可以构成长度为 1 的递增子序列。
        dp = [1] * nums_len
        
        # 遍历数组中的每一个元素作为递增子序列的终点 (i)
        for i in range(nums_len):
            
            # 遍历 i 之前的所有元素 (j)
            for j in range(i):
                
                # 检查状态转移条件: nums[i] 必须大于 nums[j]
                if nums[i] > nums[j]:
                    
                    # 状态转移公式:
                    # 如果 nums[i] > nums[j]，则 nums[i] 可以接在以 nums[j] 结尾的子序列后面。
                    # 更新 dp[i] 为当前值 (dp[i]) 和 (dp[j] + 1) 中的较大者。
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        # LIS 的最终长度是 dp 数组中的最大值
        # C++ 使用 *max_element(dp.begin(), dp.end())
        # Python 使用内置的 max() 函数
        return max(dp)

# 示例用法
# solution = Solution()
# print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 输出: 4 (如 [2, 3, 7, 18])
# print(solution.lengthOfLIS([0, 1, 0, 3, 2, 3]))            # 输出: 4
# print(solution.lengthOfLIS([7, 7, 7, 7, 7]))              # 输出: 1