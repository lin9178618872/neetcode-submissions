from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        path = []

        cols = set()
        diag1 = set()
        diag2 = set()

        def build_board():
            board = []
            for r in range(n):
                row = ['.'] * n
                row[path[r]] = 'Q'
                board.append(''.join(row))
            return board

        def backtrack(row: int):
            if row == n:
                result.append(build_board())
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                path.append(col)
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                path.pop()
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return result
