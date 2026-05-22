class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        res = []

        def preorder(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(res)

    def deserialize(self, data: str) -> TreeNode:
        nodes = data.split(',')
        self.index = 0

        def deserialize_help():
            if self.index >= len(nodes) or nodes[self.index] == "N":
                self.index += 1
                return None

            node = TreeNode(int(nodes[self.index]))
            self.index += 1
            node.left = deserialize_help()
            node.right = deserialize_help()
            return node

        return deserialize_help()
