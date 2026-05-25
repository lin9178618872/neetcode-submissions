from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):

        graph = defaultdict(list)

        for i in range(len(equations)):

            a, b = equations[i]
            val = values[i]

            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        # 统一模板
        def dfs(cur, visited, extra):
            target=extra

            # 终止条件
            if cur == target:
                return 1.0

            # 标记
            visited.add(cur)

            # 遍历邻居
            for nei, weight in graph[cur]:

                if nei in visited:#a,c,a,c
                    continue

                sub = dfs(nei, visited, target)

                if sub != -1:#跟前面=1相对
                    return weight * sub#1*（数（数））

            return -1

        ans = []

        for a, b in queries:

            if a not in graph or b not in graph:
                ans.append(-1.0)

            else:
                ans.append(dfs(a, set(), b))

        return ans