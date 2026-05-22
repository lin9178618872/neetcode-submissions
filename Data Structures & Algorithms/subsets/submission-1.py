from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []  # result = []  存放所有子集（答案）

        def backtrack(path: List[int], start: int):
            # ========== 满足结束条件？ ==========
            # 这题的“结束条件”不是到某个长度才加，而是：
            # 只要你来到这里，当前 path 就是一个合法子集
            res.append(path.copy())

            # ========== for 选择 in 选择列表 ==========
            # 选择列表：从 nums[start] 到 nums最后 的所有元素
            for i in range(start, len(nums)):
                # 做选择：把 nums[i] 加入路径
                path.append(nums[i])

                # 递归：下一层只能从 i+1 开始选（避免重复 & 保持顺序）
                backtrack(path, i + 1)

                # 撤销选择：把刚才加进去的 nums[i] 拿出来
                path.pop()

        # 从空路径开始，从下标0开始选
        backtrack([], 0)
        return res
