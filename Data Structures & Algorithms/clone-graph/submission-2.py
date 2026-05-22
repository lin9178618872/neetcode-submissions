from typing import Optional
'''
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
'''
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        memo = {}

        def dfs(cur: 'Node') -> 'Node':
            if cur in memo:
                return memo[cur]

            copy = Node(cur.val)
            memo[cur] = copy

            for nei in cur.neighbors:
                nei_copy = dfs(nei)
                copy.neighbors.append(nei_copy)

            return copy

        return dfs(node)
