from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(path, start, total):
            if total == target:
                result.append(path.copy())
                return

            if total > target:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(path, i, total + nums[i])
                path.pop()

        backtrack([], 0, 0)
        return result
