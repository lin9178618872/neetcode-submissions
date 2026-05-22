class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # ==========================
        # 1️⃣ 统计每个任务出现次数
        # ==========================
        task_count = Counter(tasks)
        # 例如：["A","A","A","B","B"] → {"A":3,"B":2}

        # ==========================
        # 2️⃣ 把次数放进“最大堆”
        # Python 只有最小堆，所以取负数
        # ==========================
        max_heap = []
        for cnt in task_count.values():
            max_heap.append(-cnt)
        heapq.heapify(max_heap)

        # ==========================
        # 3️⃣ 冷却队列
        # 里面存：[剩余次数, 什么时候能再用]
        # ==========================
        cooldown = deque()

        # ==========================
        # 4️⃣ 时间计数器
        # ==========================
        time = 0

        # ==========================
        # 5️⃣ 只要还有任务没做完，就继续
        # ==========================
        while max_heap or cooldown:
            time += 1   # 每一轮 = 1 秒

            # --------------------------
            # ① 如果现在有任务可以做
            # --------------------------
            if max_heap:
                # 拿出剩余次数最多的任务
                remain = heapq.heappop(max_heap)

                # 做一次任务 → 次数 -1
                remain += 1

                # 如果这个任务还没做完
                if remain < 0:
                    # 放进冷却区，标记下次可用时间
                    cooldown.append([remain, time + n])

            # --------------------------
            # ② 检查有没有任务冷却完毕
            # --------------------------
            if cooldown and cooldown[0][1] == time:
                # 冷却结束，放回堆里
                heapq.heappush(max_heap, cooldown.popleft()[0])

        return time
