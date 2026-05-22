from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            # ❗关键：只需要遍历到倒数第三个
            if i >= len(nums) - 2:
                break

            # 跳过重复
            if i > 0 and num == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = num + nums[left] + nums[right]

                if total == 0:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # 跳过重复
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res