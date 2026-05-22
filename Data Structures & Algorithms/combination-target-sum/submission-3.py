from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []  # 路径（当前选了哪些数）

        # backtrack(路径, 选择列表)
        # 这里的“选择列表”用 start 表示：从 nums[start:] 里选
        def backtrack(start: int, total: int):
            # if 满足结束条件
            if total == target:
                result.append(path.copy())
                return

            # 剪枝：超过 target 就没必要继续
            if total > target:
                return

            # for 选择 in 选择列表:
            for i in range(start, len(nums)):
                choice = nums[i]

                # 做选择
                path.append(choice)

                # 递归：i 不变 => 允许重复使用同一个数
                backtrack(i, total + choice)

                # 撤销选择
                path.pop()

        backtrack(0, 0)
        return result
