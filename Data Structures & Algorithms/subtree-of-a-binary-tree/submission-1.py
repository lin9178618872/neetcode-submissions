# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # 如果 root 为空，subRoot 不可能是其子树
        if not root:
            return False
        
        # 如果当前节点相同，判断从当前节点开始的子树是否与 subRoot 相同
        if self.isSameTree(root, subRoot):
            return True
        
        # 否则递归检查左子树和右子树
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    # 判断两棵树是否相同
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 如果两个节点都为空，说明相同
        if not p and not q:
            return True
        # 如果一个为空，一个不为空，说明不同
        if not p or not q:
            return False
        # 如果当前节点的值不同，说明不同
        if p.val != q.val:
            return False
        
        # 递归检查左右子树
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
