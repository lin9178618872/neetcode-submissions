class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums:
            return 0

        max_res = nums[0]
        cur_max = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            cur_max = max(cur_max + num, num)
            max_res = max(max_res, cur_max)

        return max_res
