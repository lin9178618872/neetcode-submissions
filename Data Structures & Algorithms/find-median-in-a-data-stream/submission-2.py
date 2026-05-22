import heapq

class MedianFinder:
    def __init__(self):
        self.m_small = []
        self.m_large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.m_small, -num)

        if self.m_large and -self.m_small[0] > self.m_large[0]:
            max_small = -heapq.heappop(self.m_small)
            heapq.heappush(self.m_large, max_small)

        if len(self.m_small) > len(self.m_large) + 1:
            max_small = -heapq.heappop(self.m_small)
            heapq.heappush(self.m_large, max_small)

        if len(self.m_large) > len(self.m_small):
            min_large = heapq.heappop(self.m_large)
            heapq.heappush(self.m_small, -min_large)

    def findMedian(self) -> float:
        total_size = len(self.m_small) + len(self.m_large)

        if total_size == 0:
            return 0.0

        if len(self.m_small) > len(self.m_large):
            return float(-self.m_small[0])
        else:
            return (-self.m_small[0] + self.m_large[0]) / 2.0
