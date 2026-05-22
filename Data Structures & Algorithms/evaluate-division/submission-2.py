from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):

        graph = defaultdict(list)

        # 建图
        for i in range(len(equations)):

            a = equations[i][0]
            b = equations[i][1]
            val = values[i]

            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        # DFS
        def dfs(cur, target, visited):

            if cur == target:
                return 1.0

            visited.add(cur)

            for nei, weight in graph[cur]:

                if nei in visited:
                    continue

                sub = dfs(nei, target, visited)

                if sub != -1:
                    return weight * sub

            return -1

        ans = []

        for i in range(len(queries)):

            a = queries[i][0]
            b = queries[i][1]

            if a not in graph or b not in graph:
                ans.append(-1.0)

            else:
                ans.append(dfs(a, b, set()))

        return ans