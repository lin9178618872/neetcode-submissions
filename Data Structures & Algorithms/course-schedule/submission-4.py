from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}

        for i in range(numCourses):
            graph[i] = []

        for pair in prerequisites:
            course = pair[0]
            pre = pair[1]
            graph[course].append(pre)

        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return False

            if state[course] == 2:
                return True

            state[course] = 1

            for pre in graph[course]:
                if dfs(pre) == False:
                    return False

            state[course] = 2

            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return False

        return True