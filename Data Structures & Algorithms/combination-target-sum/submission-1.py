class Solution:
    """
    组合总和问题 (Combination Sum)
    使用回溯法，允许candidates中的数字重复使用。
    """
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # 存储最终结果的列表
        res = []
        # 存储当前组合的列表
        temp = []
        
        # 调用回溯辅助函数
        # 从索引 0 开始
        self._help(candidates, target, 0, res, temp)
        
        return res

    def _help(self, candidates: list[int], target: int, start: int, res: list[list[int]], temp: list[int]):
        """
        回溯辅助函数
        
        :param candidates: 候选数字列表
        :param target: 剩余的目标值
        :param start: 当前遍历的起始索引，用于避免重复组合
        :param res: 存储所有符合条件组合的列表
        :param temp: 存储当前路径上的组合
        """
        # 递归终止条件/回溯条件
        if target == 0:
            # 找到符合条件的解，保存起来。
            # 注意：必须保存 temp 的副本，因为 temp 后续会被 pop_back 修改。
            res.append(list(temp))
            # 开始回溯
            return
        
        # 递归终止条件/回溯条件
        # 如果剩余目标值小于0，说明当前路径不符合，直接剪枝/回溯
        if target < 0:
            # 开始回溯
            return

        candidates_len = len(candidates)
        
        # 从 start 索引开始遍历，这是防止产生重复组合的关键“剪枝”操作。
        # 因为元素可以重复使用，所以下一层递归的起始索引仍然是 i。
        for i in range(start, candidates_len):
            current_candidate = candidates[i]
            
            # 优化：如果 target - candidates[i] < 0，则无需进入，因为下一层会立即返回。
            # 但为了与 C++ 原代码逻辑更贴近，这里保留了逻辑结构。
            
            # 1. 做出选择 (Choose)
            temp.append(current_candidate)
            
            # 2. 探索子问题 (Explore)
            # 因为可以重复使用，所以下一轮递归仍然从当前索引 i 开始
            self._help(candidates, target - current_candidate, i, res, temp)
            
            # 3. 撤销选择 (Unchoose / Backtrack)
            # 回到上一个状态，为下一个循环迭代做准备
            temp.pop()

# --- 示例用法 ---
# sol = Solution()
# candidates = [2, 3, 6, 7]
# target = 7
# result = sol.combinationSum(candidates, target)
# print(result)  # 预期输出: [[2, 2, 3], [7]]