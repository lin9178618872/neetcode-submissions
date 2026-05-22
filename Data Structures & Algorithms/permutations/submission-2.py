from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, choices):
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for num in choices:
                path.append(num)
                new_choices = choices.copy()
                new_choices.remove(num)

                backtrack(path, new_choices)

                path.pop()

        backtrack([], nums)
        return result