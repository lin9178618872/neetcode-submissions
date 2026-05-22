from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        res = []
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, cols
        top, bottom = 0, rows

        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            if top >= bottom:
                break

            for j in range(top, bottom):
                res.append(matrix[j][right - 1])
            right -= 1
            if left >= right:
                break

            for k in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][k])
            bottom -= 1
            if top >= bottom:
                break

            for l in range(bottom - 1, top - 1, -1):
                res.append(matrix[l][left])
            left += 1

        return res
