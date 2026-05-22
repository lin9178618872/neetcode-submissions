# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 如果当前节点为空，说明没找到
        if not root:
            return None

        # 如果当前节点就是 p 或 q，直接返回当前节点
        if root == p or root == q:
            return root

        # 去左子树找 p 或 q
        left = self.lowestCommonAncestor(root.left, p, q)

        # 去右子树找 p 或 q
        right = self.lowestCommonAncestor(root.right, p, q)

        # 如果左右两边都找到了，说明当前节点就是最低公共祖先
        if left and right:
            return root

        # 如果只有左边找到了，就把左边的结果传上去
        if left:
            return left

        # 如果只有右边找到了，就把右边的结果传上去
        return right