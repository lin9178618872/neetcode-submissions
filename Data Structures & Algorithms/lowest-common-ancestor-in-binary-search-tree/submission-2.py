class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            # 👉 都在左边
            if p.val < root.val and q.val < root.val:
                root = root.left

            # 👉 都在右边
            elif p.val > root.val and q.val > root.val:
                root = root.right

            # 👉 分叉点（答案）
            else:
                return root

        return None