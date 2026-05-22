from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):

        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[a].append(b)

        # 0=未访问
        # 1=正在访问
        # 2=访问结束
        state = [0] * numCourses

        # 统一模板
        def dfs(cur, visited, extra):

            graph = extra

            # 出现环
            if visited[cur] == 1:
                return False

            # 已经检查完
            if visited[cur] == 2:
                return True

            # 标记正在访问
            visited[cur] = 1

            # 遍历邻居
            for nei in graph[cur]:

                if dfs(nei, visited, graph) == False:
                    return False

            # 标记完成
            visited[cur] = 2

            return True

        for course in range(numCourses):

            if dfs(course, state, graph) == False:
                return False

        return True