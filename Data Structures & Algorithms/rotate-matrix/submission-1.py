class Solution:
    """
    将 n x n 矩阵顺时针旋转 90 度（原地操作）。
    """
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # left 和 right 分别代表当前正在处理的矩阵层的左右边界（列索引）
        left, right = 0, len(matrix) - 1
        
        # 当 left < right 时，表示还有未处理的矩阵层
        while left < right:
            # 每一层的元素旋转次数是 right - left（边的长度 - 1）
            for i in range(right - left):
                # top 和 bottom 分别代表当前正在处理的矩阵层的上下边界（行索引）
                # 因为是正方形矩阵，所以 top=left, bottom=right
                top, bottom = left, right
                
                # 保存左上角的元素（即将被覆盖）
                # 位于 [top, left + i]
                topleft = matrix[top][left + i]
                
                # 1. 左下角 (bottom - i, left) 旋转到 左上角 (top, left + i)
                matrix[top][left + i] = matrix[bottom - i][left]
                
                # 2. 右下角 (bottom, right - i) 旋转到 左下角 (bottom - i, left)
                matrix[bottom - i][left] = matrix[bottom][right - i]
                
                # 3. 右上角 (top + i, right) 旋转到 右下角 (bottom, right - i)
                matrix[bottom][right - i] = matrix[top + i][right]
                
                # 4. 原来的 左上角 (top, left + i) 旋转到 右上角 (top + i, right)
                matrix[top + i][right] = topleft
            
            # 移动到下一层矩阵（向内收缩边界）
            left += 1
            right -= 1

# 示例用法:
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Solution().rotate(matrix)
# print(matrix) # 期望输出: [[7,4,1],[8,5,2],[9,6,3]]

# matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Solution().rotate(matrix2)
# print(matrix2) 
# 期望输出: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]