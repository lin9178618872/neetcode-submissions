from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 



class Solution:
    # 存储中序遍历值到索引的映射，以便快速查找
    m_inorderIndex = {}

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        从前序和中序遍历序列构造二叉树的主函数。
        """
        # 1. 构建中序遍历值到索引的映射
        self.m_inorderIndex = {}  # 确保每次调用都清空或初始化
        for i in range(len(inorder)):
            val = inorder[i]
            self.m_inorderIndex[val] = i

        preorder_len = len(preorder)
        inorder_len = len(inorder)

        # 2. 调用辅助函数进行递归构建
        # 注意：在 Python 中，通常直接传递列表（或其切片），或者使用索引和长度来定义子数组范围。
        # 此处我们保持 C++ 代码中**索引**和**长度**的定义方式，以便直接转换逻辑。
        # 范围：[start, start + length)
        
        # 初始调用：
        # 前序遍历范围：[0, preorder_len)
        # 中序遍历范围：[0, inorder_len)
        return self._buildTree_help(preorder, inorder, 
                                    preorder_start=0, preorder_len=preorder_len, 
                                    inorder_start=0, inorder_len=inorder_len)

    def _buildTree_help(self, preorder: List[int], inorder: List[int], 
                        preorder_start: int, preorder_len: int, 
                        inorder_start: int, inorder_len: int) -> Optional[TreeNode]:
        """
        递归辅助函数，用于构造指定范围的子树。
        """
        # 递归结束的条件：当前子数组长度为 0
        if preorder_len <= 0 or inorder_len <= 0:
            return None

        # 1. 前序遍历的第一个元素是当前子树的根节点
        root_val = preorder[preorder_start]
        node = TreeNode(root_val)

        # 2. 找到根节点在中序遍历中的位置
        node_in_inorder = self.m_inorderIndex[root_val]

        # 3. 计算左子树的长度
        # 左子树的节点个数 = 根节点在中序遍历中的索引 - 中序遍历子数组的起始索引
        left_len = node_in_inorder - inorder_start

        # 4. 递归生成左子树
        # 左子树的前序遍历范围：[preorder_start + 1, preorder_start + 1 + left_len)
        # 左子树的中序遍历范围：[inorder_start, inorder_start + left_len)
        node.left = self._buildTree_help(preorder, inorder, 
                                         preorder_start=preorder_start + 1, 
                                         preorder_len=left_len, 
                                         inorder_start=inorder_start, 
                                         inorder_len=left_len)

        # 5. 计算右子树的长度
        # 右子树的节点个数 = 中序遍历子数组的总长度 - 左子树长度 - 根节点 (1)
        right_len = inorder_len - left_len - 1

        # 6. 递归生成右子树
        # 右子树的前序遍历范围：[preorder_start + 1 + left_len, preorder_start + 1 + left_len + right_len)
        # 右子树的中序遍历范围：[node_in_inorder + 1, node_in_inorder + 1 + right_len)
        node.right = self._buildTree_help(preorder, inorder, 
                                          preorder_start=preorder_start + 1 + left_len, 
                                          preorder_len=right_len, 
                                          inorder_start=node_in_inorder + 1, 
                                          inorder_len=right_len)
        
        return node