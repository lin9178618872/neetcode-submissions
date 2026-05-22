from typing import List

class Solution:
    """
    按螺旋顺序返回矩阵中的所有元素。
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # 检查矩阵是否为空
        if not matrix or not matrix[0]:
            return []
            
        res = []
        
        # 初始化 matrix 的四个边界：left, right, top, bottom
        # 注意：
        # left/top 是包含的起始索引
        # right/bottom 是不包含的结束索引 (类似 Python 的切片操作)
        rows = len(matrix)
        cols = len(matrix[0])
        
        left, right = 0, cols  # left: 0, right: 矩阵的列数
        top, bottom = 0, rows # top: 0, bottom: 矩阵的行数
        
        while left < right and top < bottom:
            
            # 1. 从左到右遍历最上面一行 (行索引为 top)
            # 遍历列索引从 left 到 right-1
            for i in range(left, right):
                res.append(matrix[top][i])
            
            # 最上面一行遍历完，修改 matrix 的 top 边界 (内缩)
            top += 1
            # 检查是否越界 (防止单行或单列矩阵的重复/越界访问)
            if top >= bottom:
                break
                
            # 2. 从上到下遍历最右边一列 (列索引为 right - 1)
            # 遍历行索引从 top 到 bottom-1
            for j in range(top, bottom):
                res.append(matrix[j][right - 1])
            
            # 最右边一列遍历完，修改 matrix 的 right 边界 (内缩)
            right -= 1
            # 检查是否越界
            if left >= right:
                break
                
            # 3. 从右到左遍历最下面一行 (行索引为 bottom - 1)
            # 遍历列索引从 right-1 倒序到 left
            for k in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][k])
            
            # 最下面一行遍历完，修改 matrix 的 bottom 边界 (内缩)
            bottom -= 1
            # 检查是否越界
            if top >= bottom:
                break
                
            # 4. 从下到上遍历最左边一列 (列索引为 left)
            # 遍历行索引从 bottom-1 倒序到 top
            for l in range(bottom - 1, top - 1, -1):
                res.append(matrix[l][left])
            
            # 最左边一列遍历完，修改 matrix 的 left 边界 (内缩)
            left += 1
            # 检查是否越界 (可以在循环开始时检查，这里不再赘述)
            # if left >= right:
            #     break # 实际上外层 while 循环会处理这个情况

        return res

# 示例用法:
# matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
# print(Solution().spiralOrder(matrix1)) 
# 期望输出: [1, 2, 3, 6, 9, 8, 7, 4, 5]

# matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# print(Solution().spiralOrder(matrix2)) 
# 期望输出: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]