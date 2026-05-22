class Solution:
    """
    最大子数组和 (Maximum Subarray) 问题，使用 Kadane's Algorithm (动态规划) 实现。
    
    cur_max 维护以当前元素结尾的最大子数组和。
    """
    def maxSubArray(self, nums: list[int]) -> int:
        
        # 边界条件：如果数组为空，根据题意可能返回 0 或抛出错误，
        # 但 LeetCode 上该题通常保证数组非空。
        if not nums:
            # 根据具体要求返回，通常 LeetCode 约束 nums 非空
            # 如果允许空数组，返回 0
            return 0 
        
        # max_res 存储全局最大子数组和 (最终结果)
        # 初始化为数组的第一个元素
        max_res = nums[0]
        
        # cur_max 存储以当前元素结尾的最大子数组和 (当前状态)
        # 初始化为数组的第一个元素
        cur_max = nums[0]
        
        # 从第二个元素开始遍历 (索引 i = 1)
        for i in range(1, len(nums)):
            num = nums[i]
            
            # 状态转移公式:
            # 以当前元素 num 结尾的最大子数组和 cur_max 是以下两者中的较大者:
            # 1. (cur_max + num): 延续前一个子数组 (如果前一个子数组的和为正)
            # 2. (num): 从当前元素开始一个新的子数组 
            cur_max = max(cur_max + num, num)
            
            # 更新全局最大值
            # max_res 始终记录所有 cur_max 中出现的最大值
            max_res = max(max_res, cur_max)
            
        return max_res

# 示例用法
# solution = Solution()
# print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 输出: 6 ([4, -1, 2, 1])
# print(solution.maxSubArray([1]))                              # 输出: 1
# print(solution.maxSubArray([5, 4, -1, 7, 8]))                 # 输出: 23