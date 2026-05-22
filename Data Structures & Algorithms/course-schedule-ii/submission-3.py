from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)   # b -> a

        # 0=没访问, 1=正在访问(递归栈里), 2=访问完成
        state = [0] * numCourses
        order = []
        has_cycle = False

        def dfs(course: int):
            nonlocal has_cycle
            if has_cycle:
                return

            if state[course] == 1:   # 再次回到“正在访问”的点 => 有环
                has_cycle = True
                return
            if state[course] == 2:   # 已经处理完了
                return

            state[course] = 1        # 标记：正在访问
            for nxt in graph[course]:
                dfs(nxt)
            state[course] = 2        # 标记：访问完成
            order.append(course)     # 后序加入（保证先修在前）

        for c in range(numCourses):
            if state[c] == 0:
                dfs(c)

        if has_cycle:
            return []

        order.reverse()
        return order
