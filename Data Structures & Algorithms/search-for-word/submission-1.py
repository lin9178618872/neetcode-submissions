class Solution:
    """
    在网格中查找单词路径的类。
    """
    def exist(self, board: list[list[str]], word: str) -> bool:
        """
        判断网格板上是否存在一个路径可以组成给定的单词。
        
        Args:
            board: 字符网格。
            word: 要查找的单词。

        Returns:
            如果存在路径则返回 True，否则返回 False。
        """
        rows = len(board)
        cols = len(board[0])
        
        # 记录元素是否被访问过，初始化为 False
        # 在 Python 中，我们可以利用 DFS 的特性，在每次递归中传递或使用更巧妙的方式处理访问状态，
        # 例如，在访问时修改 board 上的字符（如果允许）或使用一个内部函数来捕获访问状态。
        # 这里，我们遵循 C++ 版本的逻辑，使用一个单独的 visit 数组。
        visit = [[False] * cols for _ in range(rows)] 

        for row in range(rows):
            for col in range(cols):
                # 从板上每个可能的起点开始尝试 DFS 搜索
                if self._dfs(row, col, 0, board, word, visit, rows, cols):
                    return True
        
        return False

    def _dfs(self, row: int, col: int, i: int, board: list[list[str]], word: str, visit: list[list[bool]], rows: int, cols: int) -> bool:
        """
        深度优先搜索辅助函数。

        Args:
            row: 当前行索引。
            col: 当前列索引。
            i: 当前要匹配的 word 字符索引。
            board: 字符网格。
            word: 要查找的单词。
            visit: 访问状态数组。
            rows: 网格总行数。
            cols: 网格总列数。

        Returns:
            是否找到从 (row, col) 开始的 word 的剩余部分。
        """
        # 递归终止条件 1：如果整个单词都匹配完了，返回 True
        if i == len(word):
            return True
        
        # 递归终止条件 2：越界、字符不匹配、或当前位置已被访问
        if (row >= rows or row < 0 or 
            col >= cols or col < 0 or 
            board[row][col] != word[i] or 
            visit[row][col]):
            return False

        # 标记当前位置已访问
        visit[row][col] = True
        
        # 尝试向四个方向递归搜索
        # 这里使用 directions 数组和循环来简化四个方向的搜索逻辑
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # (右, 左, 下, 上)

        res = False
        for dr, dc in directions:
            next_row, next_col = row + dr, col + dc
            # 如果任何一个方向的搜索成功，则将结果设置为 True
            if self._dfs(next_row, next_col, i + 1, board, word, visit, rows, cols):
                res = True
                break # 找到了就立即停止搜索

        # 回溯：将当前位置的访问状态重置为 False，以便其他路径可以访问
        visit[row][col] = False
        
        return res

# 示例用法（可选）：
# sol = Solution()
# board = [
#     ["A","B","C","E"],
#     ["S","F","C","S"],
#     ["A","D","E","E"]
# ]
# word1 = "ABCCED"
# word2 = "SEE"
# word3 = "ABCB"
# print(sol.exist(board, word1)) # True
# print(sol.exist(board, word2)) # True
# print(sol.exist(board, word3)) # False