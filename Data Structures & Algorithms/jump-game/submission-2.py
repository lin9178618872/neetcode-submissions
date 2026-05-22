class Solution:
    def canJump(self, nums: list[int]) -> bool:
        nums_len = len(nums)

        if nums_len <= 1:
            return True

        target = nums_len - 1

        for i in range(nums_len - 2, -1, -1):
            if i + nums[i] >= target:
                target = i

        return target == 0
