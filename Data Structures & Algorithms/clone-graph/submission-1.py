"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        queue = deque()
        queue.append(node)

        visited = {node: Node(node.val)}

        while queue:
            current = queue.popleft()

            for nei in current.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val)
                    queue.append(nei)

                visited[current].neighbors.append(visited[nei])

        return visited[node]
