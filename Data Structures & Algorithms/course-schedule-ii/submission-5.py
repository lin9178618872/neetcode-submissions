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

        def dfs(course):
            if state[course] == 1:
                return True

            if state[course] == 2:
                return False

            state[course] = 1

            for nextCourse in graph[course]:
                if dfs(nextCourse):
                    return True

            state[course] = 2
            result.append(course)
            return False

        for i in range(numCourses):
            if state[i] == 0:
                if dfs(i):
                    return []

        result.reverse()
        return result