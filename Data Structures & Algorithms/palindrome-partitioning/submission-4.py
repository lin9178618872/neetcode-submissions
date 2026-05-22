from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_pal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(path, start):
            if start == len(s):
                result.append(path.copy())
                return

            for i in range(start, len(s)):
                if not is_pal(start, i):
                    continue

                path.append(s[start:i + 1])
                backtrack(path, i + 1)
                path.pop()

        backtrack([], 0)
        return result
