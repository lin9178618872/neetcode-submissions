from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
#创图
        graph = defaultdict(list)

        for i in range(len(equations)):

            a, b = equations[i]#在equation中a为第一个，b为第二个
            val = values[i]

            graph[a].append((b, val))#a/b=val
            graph[b].append((a, 1 / val))#b/a=1/val
#dfs
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

        res = []

        for a, b in queries:
#查不到的图就-1
            if a not in graph or b not in graph:
                res.append(-1.0)
#查到就加进去进入递归
            else:
                res.append(dfs(a, set(), b))

        return res