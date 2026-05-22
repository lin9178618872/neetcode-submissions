class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        max_len = 0
        nums_set = set(nums)
        
        for num in nums:
            if num - 1 not in nums_set:
                current_num = num
                current_len = 0
                
                while current_num in nums_set:
                    current_len += 1
                    current_num += 1
                
                max_len = max(current_len, max_len)
                
        return max_len