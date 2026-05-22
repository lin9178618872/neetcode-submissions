from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return

        rows, cols = len(matrix), len(matrix[0])
        zero_row_flag = 1

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        zero_row_flag = 0

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if matrix[0][0] == 0:
            for row in range(1, rows):
                matrix[row][0] = 0

        if zero_row_flag == 0:
            for col in range(cols):
                matrix[0][col] = 0
