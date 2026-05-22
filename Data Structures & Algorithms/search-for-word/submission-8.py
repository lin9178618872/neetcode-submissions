from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = set()

        def backtrack(path, choices):
            r, c, k = path

            # 剪枝 / 非法情况
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            if (r, c) in visited:
                return False
            if board[r][c] != word[k]:
                return False

            # 满足结束条件
            if k == len(word) - 1:
                return True

            # 做选择
            visited.add((r, c))

            # 选择列表：上下左右
            for dr, dc in choices:
                nr, nc = r + dr, c + dc
                if backtrack((nr, nc, k + 1), choices):
                    return True

            # 撤销选择
            visited.remove((r, c))
            return False

        choices = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(m):
            for j in range(n):
                if backtrack((i, j, 0), choices):
                    return True

        return False
