from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}

        for i in range(numCourses):
            graph[i] = []

        for pair in prerequisites:
            course = pair[0]
            pre = pair[1]
            graph[pre].append(course)

        state = [0] * numCourses
        result = []
        hasCycle = False

        def dfs(course):
            nonlocal hasCycle

            if hasCycle == True:
                return

            if state[course] == 1:
                hasCycle = True
                return

            if state[course] == 2:
                return

            state[course] = 1

            for nextCourse in graph[course]:
                dfs(nextCourse)

            state[course] = 2
            result.append(course)

        for i in range(numCourses):
            if state[i] == 0:
                dfs(i)

        if hasCycle == True:
            return []

        result.reverse()
        return result