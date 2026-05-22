class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset.copy())   # ✅ 使用 copy()
                return

            # 1️⃣ 选择 nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # 2️⃣ 不选择 nums[i]（跳过所有重复元素）
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res
