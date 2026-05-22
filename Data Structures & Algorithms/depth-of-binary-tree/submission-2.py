# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:  # 如果节点为空，深度为 0
            return 0
        
        # 递归计算左子树和右子树的深度
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # 返回左右子树深度的最大值加 1（当前节点）
        return max(left_depth, right_depth) + 1
