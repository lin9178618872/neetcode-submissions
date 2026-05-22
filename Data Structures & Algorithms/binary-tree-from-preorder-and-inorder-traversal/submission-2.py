from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    m_inorderIndex = {}

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.m_inorderIndex = {}
        for i in range(len(inorder)):
            self.m_inorderIndex[inorder[i]] = i

        preorder_len = len(preorder)
        inorder_len = len(inorder)

        return self._buildTree_help(
            preorder, inorder,
            preorder_start=0, preorder_len=preorder_len,
            inorder_start=0, inorder_len=inorder_len
        )

    def _buildTree_help(
        self,
        preorder: List[int],
        inorder: List[int],
        preorder_start: int,
        preorder_len: int,
        inorder_start: int,
        inorder_len: int
    ) -> Optional[TreeNode]:
        if preorder_len <= 0 or inorder_len <= 0:
            return None

        root_val = preorder[preorder_start]
        node = TreeNode(root_val)

        node_in_inorder = self.m_inorderIndex[root_val]
        left_len = node_in_inorder - inorder_start

        node.left = self._buildTree_help(
            preorder, inorder,
            preorder_start=preorder_start + 1,
            preorder_len=left_len,
            inorder_start=inorder_start,
            inorder_len=left_len
        )

        right_len = inorder_len - left_len - 1

        node.right = self._buildTree_help(
            preorder, inorder,
            preorder_start=preorder_start + 1 + left_len,
            preorder_len=right_len,
            inorder_start=node_in_inorder + 1,
            inorder_len=right_len
        )

        return node
