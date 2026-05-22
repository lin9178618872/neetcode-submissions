class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        left = 0
        right = m * n - 1   # 注意：按一维处理

        while left <= right:
            mid = left + (right - left) // 2

            # 把一维 mid 映射回二维
            row = mid // n
            col = mid % n
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:  # val > target
                right = mid - 1

        return False
