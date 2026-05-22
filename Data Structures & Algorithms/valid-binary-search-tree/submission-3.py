# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root):

        # 用一个函数检查树
        def check(node, min_val, max_val):

            # 走到空节点，说明这条路没问题
            if node is None:
                return True

            # 如果当前值不在允许范围内
            if node.val <= min_val or node.val >= max_val:
                return False

            # 检查左子树（最大值变成当前节点值）
            left_ok = check(node.left, min_val, node.val)

            # 检查右子树（最小值变成当前节点值）
            right_ok = check(node.right, node.val, max_val)

            # 左右都合法才算合法
            return left_ok and right_ok


        # 从根节点开始，范围无限大
        return check(root, float("-inf"), float("inf"))
