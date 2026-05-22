from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ingree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for course, pre_course in prerequisites:
            adj[pre_course].append(course)
            ingree[course] += 1

        zero_ingree_queue = deque()
        for i in range(numCourses):
            if ingree[i] == 0:
                zero_ingree_queue.append(i)

        count = 0
        while zero_ingree_queue:
            u = zero_ingree_queue.popleft()
            count += 1
            for v in adj[u]:
                ingree[v] -= 1
                if ingree[v] == 0:
                    zero_ingree_queue.append(v)

        return count == numCourses
