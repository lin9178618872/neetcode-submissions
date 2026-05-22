import heapq

class MedianFinder:
    def __init__(self):
        # 左边：存较小的一半（大顶堆，用负数）
        self.m_small = []

        # 右边：存较大的一半（小顶堆）
        self.m_large = []

    def addNum(self, num: int) -> None:
        # ==========================
        # 第 1 步：先把数扔进左边
        # ==========================
        # 因为左边是「大顶堆」
        # Python 没有大顶堆 → 用负数
        heapq.heappush(self.m_small, -num)

        # ==========================
        # 第 2 步：保证 左最大 <= 右最小
        # ==========================
        if self.m_large:
            # 左边最大值
            left_max = -self.m_small[0]

            # 右边最小值
            right_min = self.m_large[0]

            # 如果左边最大 > 右边最小 → 不合法
            if left_max > right_min:
                # 把左边最大的拿出来
                moved = -heapq.heappop(self.m_small)

                # 放到右边
                heapq.heappush(self.m_large, moved)

        # ==========================
        # 第 3 步：控制数量平衡
        # ==========================

        # 左边最多只能比右边多 1 个
        if len(self.m_small) > len(self.m_large) + 1:
            moved = -heapq.heappop(self.m_small)
            heapq.heappush(self.m_large, moved)

        # 如果右边比左边多 → 不行
        if len(self.m_large) > len(self.m_small):
            moved = heapq.heappop(self.m_large)
            heapq.heappush(self.m_small, -moved)

    def findMedian(self) -> float:
        # 总元素数量
        total = len(self.m_small) + len(self.m_large)

        if total == 0:
            return 0.0

        # 如果左边多一个 → 中位数是左边最大
        if len(self.m_small) > len(self.m_large):
            return float(-self.m_small[0])

        # 否则左右一样多 → 取中间两个平均
        return (-self.m_small[0] + self.m_large[0]) / 2
