from typing import Optional
'''
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
'''
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # DFS 遍历图，顺便构建克隆图
        self.traverse(node)
        # 从 map 里找到克隆图的对应节点
        return self.originToClone.get(node)

    def __init__(self):
        # 记录 DFS 遍历过的节点，防止走回头路
        self.visited = set()
        # 记录原节点到克隆节点的映射
        self.originToClone = {}

    # DFS 图遍历框架
    def traverse(self, node: 'Node'):
        if node is None:
            return
        if node in self.visited:
            return
        # 前序位置，标记为已访问
        self.visited.add(node)
        # 前序位置，克隆节点
        if node not in self.originToClone:
            self.originToClone[node] = Node(node.val)
        cloneNode = self.originToClone[node]

        # 递归遍历邻居节点，并构建克隆图
        for neighbor in node.neighbors:
            self.traverse(neighbor)
            # 递归之后，邻居节点一定存在 originToClone 中
            cloneNeighbor = self.originToClone[neighbor]
            cloneNode.neighbors.append(cloneNeighbor)
