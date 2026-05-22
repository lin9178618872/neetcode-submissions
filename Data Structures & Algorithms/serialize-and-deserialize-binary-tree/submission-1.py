# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    """
    序列化是将一个数据结构（如二叉树）转化为位序列或其他可以存储或传输的格式，
    以便之后可以在不同环境中重建相同的树结构。
    
    反序列化是将此格式重新转化为原来的数据结构。
    """

    def serialize(self, root: TreeNode) -> str:
        """
        Encodes a tree to a single string using pre-order traversal.
        
        Args:
            root: The root of the binary tree.
            
        Returns:
            A string representing the serialized tree.
        """
        res = []
        
        def preorder(node):
            if not node:
                res.append("N")
                return
            
            # 根节点的值
            res.append(str(node.val))
            # 递归序列化左子树
            preorder(node.left)
            # 递归序列化右子树
            preorder(node.right)
            
        preorder(root)
        # 将列表中的元素用逗号连接成一个字符串
        return ",".join(res)

    def deserialize(self, data: str) -> TreeNode:
        """
        Decodes your encoded data to tree.
        
        Args:
            data: The string representing the serialized tree.
            
        Returns:
            The root of the deserialized binary tree.
        """
        # 将字符串按逗号分割成节点值的列表
        nodes = data.split(',')
        
        # 使用一个可变对象（如列表）来存储索引，以便在递归调用中更新
        # 否则可以直接使用一个全局变量或将其作为参数传递
        self.index = 0
        
        def deserialize_help():
            # 检查当前节点是否为 None（用 "N" 表示）
            if self.index >= len(nodes) or nodes[self.index] == "N":
                self.index += 1
                return None
            
            # 创建新的树节点
            node = TreeNode(int(nodes[self.index]))
            self.index += 1
            
            # 递归构建左子树和右子树
            node.left = deserialize_help()
            node.right = deserialize_help()
            
            return node

        return deserialize_help()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))