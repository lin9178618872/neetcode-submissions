from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def backtrack(start: int, total: int):
            if total == target:
                result.append(path.copy())
                return

            if total > target:
                return

            for i in range(start, len(nums)):
                choice = nums[i]
                path.append(choice)
                backtrack(i, total + choice)
                path.pop()

        backtrack(0, 0)
        return result

