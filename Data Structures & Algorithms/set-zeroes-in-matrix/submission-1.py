from typing import List

class Solution:
    """
    如果矩阵中的一个元素为 0，则将其所在行和列的所有元素都清零。
    使用 O(1) 额外空间。
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # 检查矩阵是否为空
        if not matrix or not matrix[0]:
            return
            
        rows = len(matrix)
        cols = len(matrix[0])
        
        # 独立变量，用于记录第 0 行是否需要被清零。
        # 初始为 1，表示第 0 行不置为 0。
        zero_row_flag = 1 
        
        # --- 第一次遍历：标记需要清零的行和列 ---
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    
                    # 1. 标记第 col 列需要清零：
                    # matrix[0][col] 用于保存第 col 列的状态。
                    matrix[0][col] = 0
                    
                    if row > 0:
                        # 2. 标记第 row 行（非第 0 行）需要清零：
                        # matrix[row][0] 用于保存第 row 行的状态。
                        matrix[row][0] = 0
                    else:
                        # 3. 标记第 0 行需要清零：
                        # 如果是第 0 行的元素为 0，则单独用 zero_row_flag 标记。
                        zero_row_flag = 0
        
        # --- 第二次遍历：根据标记，清零非第 0 行/列的区域 (从 [1][1] 开始) ---
        for row in range(1, rows):
            for col in range(1, cols):
                # 如果当前元素的行标记 (matrix[row][0]) 或列标记 (matrix[0][col]) 为 0，则将其置 0。
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        # --- 第三次处理：根据标记，清零第 0 列 ---
        # 检查 matrix[0][0]（它存储了第 0 列的状态）
        # 注意：这里需要考虑第 0 行的状态在第一步中被单独保存在 zero_row_flag 中。
        # matrix[0][0] 在这里只代表第 0 列的状态（从行索引 1 开始）。
        if matrix[0][0] == 0:
            for row in range(1, rows):
                matrix[row][0] = 0
        
        # --- 第四次处理：根据标记，清零第 0 行 ---
        # 检查 zero_row_flag (它存储了第 0 行的状态)
        if zero_row_flag == 0:
            for col in range(cols):
                matrix[0][col] = 0

# 示例用法:
# matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
# Solution().setZeroes(matrix1)
# print(matrix1) # 期望输出: [[1,0,1],[0,0,0],[1,0,1]]

# matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Solution().setZeroes(matrix2)
# print(matrix2) # 期望输出: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]