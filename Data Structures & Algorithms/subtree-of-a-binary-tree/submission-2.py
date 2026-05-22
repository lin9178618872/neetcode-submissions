# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        检查两棵树是否完全相同。
        """
        # 递归结束的条件：两个节点都为空，则相同
        if not p and not q:
            return True
        
        # 递归结束的条件：
        # 1. 其中一个为空，另一个不为空
        # 2. 两个节点的值不同
        if not p or not q or p.val != q.val:
            return False
        
        # 子问题：递归检查左右子树
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        """
        判断 subRoot 是否是 root 的一棵子树。
        """
        # 递归结束的条件：如果 subRoot 是 None，则它总是任何树的子树
        if not subRoot:
            return True
        
        # 递归结束的条件：如果 root 是 None (此时 subRoot 不为 None)，则 subRoot 不可能是 root 的子树
        if not root:
            return False
        
        # 递归结束的条件：检查以当前 root 节点为起点，是否与 subRoot 完全相同
        if self.isSameTree(root, subRoot):
            return True
        
        # 子问题：检查 subRoot 是否是 root 的左子树或右子树的子树
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

# 注意：在 LeetCode 或类似环境中，TreeNode 的定义通常会提前提供，
# 你只需要实现 Solution 类及其方法。
