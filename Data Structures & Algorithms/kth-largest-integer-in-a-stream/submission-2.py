import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # ==========================
        # k：我们要找的是第 k 大
        # nums：一开始给的一堆数字
        # ==========================

        # 保存 k 的值，后面 add 会用
        self.k = k

        # 用 nums 直接当作一个堆
        self.minHeap = nums

        # 把普通数组变成【小根堆】
        # 变完之后：最小值在 minHeap[0]
        heapq.heapify(self.minHeap)

        # 如果堆里的数超过 k 个
        # 就一直弹出最小的
        # 👉 只留下 k 个最大的数
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # ==========================
        # 每次来一个新数字 val
        # ==========================

        # 先把新数字丢进堆里
        heapq.heappush(self.minHeap, val)

        # 如果堆的大小超过 k
        # 说明有多余的小数字
        if len(self.minHeap) > self.k:
            # 把最小的踢掉
            heapq.heappop(self.minHeap)

        # 堆顶元素：
        # 👉 当前第 k 大
        return self.minHeap[0]