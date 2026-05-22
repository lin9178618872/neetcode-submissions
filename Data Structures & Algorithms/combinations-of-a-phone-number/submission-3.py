from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(path, start):

            if start == len(digits):
                result.append("".join(path))
                return

            choices = phone[digits[start]]

            for ch in choices:
                path.append(ch)
                backtrack(path, start + 1)
                path.pop()

        backtrack([], 0)
        return result
