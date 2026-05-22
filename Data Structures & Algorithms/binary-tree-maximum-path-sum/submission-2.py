class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')
        self._dfs(root)
        return self.max_sum

    def _dfs(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_max = max(self._dfs(root.left), 0)
        right_max = max(self._dfs(root.right), 0)

        current_path_sum = root.val + left_max + right_max
        self.max_sum = max(self.max_sum, current_path_sum)

        return root.val + max(left_max, right_max)
