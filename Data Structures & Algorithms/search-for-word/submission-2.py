class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        visit = [[False] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if self._dfs(row, col, 0, board, word, visit, rows, cols):
                    return True

        return False

    def _dfs(
        self,
        row: int,
        col: int,
        i: int,
        board: list[list[str]],
        word: str,
        visit: list[list[bool]],
        rows: int,
        cols: int
    ) -> bool:
        if i == len(word):
            return True

        if (
            row < 0 or row >= rows or
            col < 0 or col >= cols or
            board[row][col] != word[i] or
            visit[row][col]
        ):
            return False

        visit[row][col] = True

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            if self._dfs(row + dr, col + dc, i + 1, board, word, visit, rows, cols):
                visit[row][col] = False
                return True

        visit[row][col] = False
        return False
