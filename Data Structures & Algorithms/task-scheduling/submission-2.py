class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)

        max_heap = []
        for cnt in task_count.values():
            max_heap.append(-cnt)
        heapq.heapify(max_heap)

        cooldown = deque()

        time = 0

        while max_heap or cooldown:
            time += 1

            if max_heap:
                remain = heapq.heappop(max_heap)
                remain += 1
                if remain < 0:
                    cooldown.append([remain, time + n])

            if cooldown and cooldown[0][1] == time:
                heapq.heappush(max_heap, cooldown.popleft()[0])

        return time
