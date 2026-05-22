from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        state = [0] * numCourses   # 0=未访问, 1=正在访问(路径上), 2=已完成

        def backtrack(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True

            state[course] = 1
            for pre in graph[course]:
                if backtrack(pre) == False:
                    return False
            state[course] = 2
            return True

        for c in range(numCourses):
            if backtrack(c) == False:
                return False
        return True