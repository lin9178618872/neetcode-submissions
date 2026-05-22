# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_so_far):
            if node is None:
                return 0

            if node.val >= max_so_far:
                good = 1
            else:
                good = 0

            if node.val > max_so_far:
                max_so_far = node.val

            left_good = dfs(node.left, max_so_far)
            right_good = dfs(node.right, max_so_far)

            return good + left_good + right_good

        return dfs(root, root.val)
