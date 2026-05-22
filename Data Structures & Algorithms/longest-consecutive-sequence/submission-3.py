class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        max_len = 0
        # 使用 set 存储所有元素，方便 O(1) 查找
        nums_set = set(nums)
        
        # 遍历数组中的每个元素
        for num in nums:
            # 检查 num - 1 是否在 set 中，
            # 如果不在，则 num 可能是连续序列的起始元素
            if num - 1 not in nums_set:
                current_num = num
                current_len = 0
                
                # 从 num 开始向后查找连续的元素
                # current_num + current_len 相当于 C++ 中的 num + len
                while current_num in nums_set:
                    current_len += 1
                    current_num += 1  # 检查下一个连续的数
                
                # 更新最大长度
                max_len = max(current_len, max_len)
                
        return max_len

# 示例用法（可选）：
# solution = Solution()
# print(solution.longestConsecutive([100, 4, 200, 1, 3, 2])) # 输出 4
# print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])) # 输出 9