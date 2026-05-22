class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        memo = {}

        def dfs(cur):
            if cur in memo:
                return memo[cur]

            copy = Node(cur.val)
            memo[cur] = copy

            for nei in cur.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)