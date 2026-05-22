from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 先排序
        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # 跳过重复元素
                continue
            
            left, right = i + 1, len(nums) - 1  # 双指针
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:  # 跳过重复
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:  # 跳过重复
                        right -= 1
                elif total < 0:
                    left += 1  # 让和变大
                else:
                    right -= 1  # 让和变小
        return res
