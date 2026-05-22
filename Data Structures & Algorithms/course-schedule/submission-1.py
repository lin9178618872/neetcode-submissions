from collections import deque
from typing import List

class Solution:
    """
    判断是否可以完成所有课程（拓扑排序）
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # 1. 初始化数据结构
        # ingree[i]：课程 i 的入度（即 i 有多少先修课程）
        ingree = [0] * numCourses
        
        # preCourse[i]：课程 i 的后续课程列表（即学完 i 之后可以学哪些课）
        # 这里的 C++ 代码中的 preCourse 实际上存的是：
        # key: 某个课程 B
        # value: 依赖于 B 的课程 A 的列表，即 A -> B 的边，表示 B 是 A 的先修课。
        #
        # 原始 C++ 代码逻辑：
        # for (const auto& pre : prerequisites) {
        #     preCourse[pre[0]].push_back(pre[1]);
        #     ingree[pre[1]]++;
        # }
        # 这里的 prerequisites[i][0] 是课程 A，prerequisites[i][1] 是课程 B，表示要学 A 必须先学 B (B -> A)。
        # preCourse[A].push_back(B) 存的是：学完 A 可以解锁的课程 B。
        # 原始代码的注释和实现有歧义。根据代码逻辑，这表示 A -> B 的边，即 A 是 B 的先修课。
        # **我们应该按图的拓扑排序标准定义：A 是 B 的先修课，表示 B -> A 的边。**
        # 
        # **根据问题描述：** `[a, b]` 表示要学课程 `a` 必须先学课程 `b`。
        # **即有向边：** $b \to a$
        # **入度：** 课程 $a$ 的入度增加 1。
        # **邻接表：** 键 $b$ 对应的值是 $a$ 的列表。
        
        # 邻接表：adj[u] 存储所有依赖于课程 u 的课程 v (边 $u \to v$)
        adj = [[] for _ in range(numCourses)]
        
        # 2. 建立图和计算入度
        for course, pre_course in prerequisites:
            # 要学 course 必须先学 pre_course，即 pre_course -> course
            adj[pre_course].append(course) # pre_course 的后续课程是 course
            ingree[course] += 1           # course 的入度增加
            
        # 3. 拓扑排序：Kahn 算法
        
        # 存储所有入度为 0 的课程
        zero_ingree_queue = deque()
        for i in range(numCourses):
            if ingree[i] == 0:
                zero_ingree_queue.append(i)
        
        # 已完成的课程计数
        count = 0
        
        while zero_ingree_queue:
            # 取出当前入度为 0 的课程
            u = zero_ingree_queue.popleft()
            count += 1
            
            # 遍历 u 的所有后续课程 v
            for v in adj[u]:
                # 移除边 u -> v，即 v 的入度减 1
                ingree[v] -= 1
                
                # 如果 v 的入度变为 0，将其加入队列
                if ingree[v] == 0:
                    zero_ingree_queue.append(v)
                    
        # 4. 判断结果
        # 如果完成的课程数等于总课程数，则说明可以完成所有课程（无环）
        return count == numCourses