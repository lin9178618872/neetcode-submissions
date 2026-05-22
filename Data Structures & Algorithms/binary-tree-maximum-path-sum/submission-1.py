# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # 使用一个列表来存储最大路径和的结果，
        # 因为 Python 的整数是不可变类型，需要传递引用（或使用实例变量）来在递归中更新它。
        # 初始值设为根节点的值，因为路径至少包含一个节点。
        self.max_sum = float('-inf')  # 初始结果应设为负无穷大，以确保任何路径和都能更新它。

        self._dfs(root)
        
        return self.max_sum

    def _dfs(self, root: TreeNode) -> int:
        """
        递归函数，计算从当前节点'root'向下延伸的**最大单边路径和**。
        同时，在递归过程中更新全局的最大路径和'self.max_sum'。
        """
        if not root:
            return 0

        # 递归计算左子树和右子树向下延伸的最大路径和。
        # 如果子树的最大路径和为负，则选择 0，即不选择该分支。
        left_max = max(self._dfs(root.left), 0)
        right_max = max(self._dfs(root.right), 0)

        # 1. 更新全局最大路径和 (max_sum):
        # 考虑以当前 'root' 为**最高点**的路径。
        # 路径和为：root.val + left_max + right_max
        current_path_sum = root.val + left_max + right_max
        self.max_sum = max(self.max_sum, current_path_sum)
        
        # 2. 返回当前节点'root'能贡献给其父节点的最大单边路径和:
        # 必须选择当前节点'root'，并从左/右子树中选择最大的那条单边路径。
        # 路径和为：root.val + max(left_max, right_max)
        return root.val + max(left_max, right_max)