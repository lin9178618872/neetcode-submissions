# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#12/11
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 中序遍历结果列表
        self.result = []
        
        # 定义递归的中序遍历函数
        def inorder(node):
            if not node:
                return
            inorder(node.left)  # 递归遍历左子树
            self.result.append(node.val)  # 访问当前节点
            inorder(node.right)  # 递归遍历右子树
        
        inorder(root)  # 调用中序遍历
        
        # 返回第 k 小的元素（注意是 1-indexed）
        return self.result[k - 1]