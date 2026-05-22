from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        visited = set()

        def backtrack(r, c, k):
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            if (r, c) in visited:
                return False
            if board[r][c] != word[k]:
                return False

            if k == len(word) - 1:
                return True

            visited.add((r, c))

            for dr, dc in [(-1, 0),(1,0),(0,-1),(0,1)]:
                nr = r + dr
                nc = c + dc
                if backtrack(nr, nc, k + 1):
                    return True

            visited.remove((r, c))
            return False

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True

        return False
