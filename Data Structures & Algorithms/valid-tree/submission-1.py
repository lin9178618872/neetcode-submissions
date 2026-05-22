class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # 空图视为有效树
        if not n:
            return True

        # 构建无向图邻接表
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i, prev):
            # 如果访问过，说明有环
            if i in visit:
                return False

            visit.add(i)

            for j in adj[i]:
                if j == prev:   # 跳过父节点，避免误判
                    continue
                if not dfs(j, i):
                    return False
            return True

        # 必须：1️⃣ 无环 2️⃣ 所有节点都连通
        return dfs(0, -1) and n == len(visit)

