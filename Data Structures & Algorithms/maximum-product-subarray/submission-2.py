class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            return 0

        max_res = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]

        for i in range(2, len(nums) + 1):
            num = nums[i - 1]
            prev_max = cur_max

            cur_max = max(prev_max * num, cur_min * num, num)
            cur_min = min(prev_max * num, cur_min * num, num)

            max_res = max(max_res, cur_max)

        return max_res