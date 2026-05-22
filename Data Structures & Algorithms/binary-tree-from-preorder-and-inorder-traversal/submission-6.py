# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):

        # =========================
        # 1️⃣ 记录 inorder 里每个值的位置
        # =========================
        index_map = {}
        for i in range(len(inorder)):
            index_map[inorder[i]] = i

        # =========================
        # 2️⃣ 用列表包一个 index，方便在递归中修改
        # =========================
        pre_index = [0]

        # =========================
        # 3️⃣ 递归函数：根据 inorder 的范围建树
        # =========================
        def build(left, right):

            # 如果区间不合法，说明没有节点
            if left > right:
                return None

            # ① 从 preorder 取当前根节点
            root_value = preorder[pre_index[0]]
            pre_index[0] += 1

            # ② 创建根节点
            root = TreeNode(root_value)

            # ③ 找到这个根在 inorder 中的位置
            mid = index_map[root_value]

            # ④ 递归构建左子树
            root.left = build(left, mid - 1)

            # ⑤ 递归构建右子树
            root.right = build(mid + 1, right)

            return root

        # =========================
        # 4️⃣ 从整个 inorder 范围开始
        # =========================
        return build(0, len(inorder) - 1)