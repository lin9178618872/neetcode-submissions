class Solution:
    """
    跳跃游戏 (Jump Game) 问题，使用逆向贪心算法实现。
    
    目标: 找到能够到达最后一个索引的最左侧索引 (target)。
    """
    def canJump(self, nums: list[int]) -> bool:
        
        nums_len = len(nums)
        
        # 边界条件：如果数组只有一个元素，直接返回 True
        if nums_len <= 1:
            return True
        
        # 1. 初始化目标值 (target)
        # target 指向当前需要到达的最左侧索引。
        # 初始目标是数组的最后一个索引。
        target = nums_len - 1
        
        # 2. 逆向遍历数组
        # 遍历所有可能的起始点 i，从倒数第二个位置开始 (nums_len - 2)
        # 循环到索引 0 (包含)
        for i in range(nums_len - 2, -1, -1):
            
            # 检查当前位置 i 是否能跳到或越过当前的 target
            # i + nums[i] 是从 i 能到达的最远距离
            if i + nums[i] >= target:
                # 如果能到达 target，则将 target 更新为 i
                # 这意味着我们现在只需要找到能到达 i 的位置即可。
                target = i
        
        # 3. 结果判断
        # 如果最终的 target 移动到了索引 0，说明从起点 0 可以到达终点。
        return target == 0

# 示例用法
# solution = Solution()
# print(solution.canJump([2, 3, 1, 1, 4]))  # 输出: True
# print(solution.canJump([3, 2, 1, 0, 4]))  # 输出: False
# print(solution.canJump([0]))              # 输出: True