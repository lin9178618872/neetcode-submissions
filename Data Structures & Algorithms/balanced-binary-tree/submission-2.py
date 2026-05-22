# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root):

        def dfs(node):
            if not node:
                return True, 0

            l_bal, l_h = dfs(node.left)
            r_bal, r_h = dfs(node.right)

            balanced = l_bal and r_bal and abs(l_h - r_h) <= 1
            height = 1 + max(l_h, r_h)

            return balanced, height

        return dfs(root)[0]