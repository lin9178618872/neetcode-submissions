from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_pal(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(path: List[str], start: int):
            if start == len(s):
                result.append(path.copy())
                return

            for end in range(start, len(s)):
                if not is_pal(start, end):
                    continue

                path.append(s[start:end + 1])
                backtrack(path, end + 1)
                path.pop()

        backtrack([], 0)
        return result
