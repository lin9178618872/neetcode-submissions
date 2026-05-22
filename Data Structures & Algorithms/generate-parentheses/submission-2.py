from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(path, left, right):
            if left == n and right == n:
                result.append(path)
                return

            if left < n:
                backtrack(path + "(", left + 1, right)

            if right < left:
                backtrack(path + ")", left, right + 1)

        backtrack("", 0, 0)
        return result
