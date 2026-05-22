# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            
            # 当前节点的值必须大于下界并且小于上界
            if node.val <= lower or node.val >= upper:
                return False
            
            # 递归检查左子树和右子树
            return (dfs(node.left, lower, node.val) and 
                    dfs(node.right, node.val, upper))
        
        return dfs(root)