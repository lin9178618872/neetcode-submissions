import heapq

class MedianFinder:
    """
    数据流的中位数
    使用两个堆：
    1. m_small: 大根堆（存储数据流中较小的或等于中位数的一半元素），Python中通过存储负数模拟大根堆。
       堆顶是这部分元素的最大值（即负数的最小值，实际数值的最大值）。
    2. m_large: 小根堆（存储数据流中较大的或等于中位数的一半元素）。
       堆顶是这部分元素的最小值。
    始终保持 m_small.size() >= m_large.size() 或 m_small.size() == m_large.size() + 1。
    这样，中位数要么是 m_small 的堆顶，要么是 (m_small.top() + m_large.top()) / 2.0。
    """
    def __init__(self):
        # 大根堆 (max_heap): 存储较小的部分, 使用负数模拟, 堆顶是 max(较小部分)
        self.m_small = [] 
        # 小根堆 (min_heap): 存储较大的部分, 堆顶是 min(较大分)
        self.m_large = []

    def addNum(self, num: int) -> None:
        # 1. 元素先插入到大根堆 (m_small)
        # 插入时要取反以模拟大根堆
        heapq.heappush(self.m_small, -num)

        # 2. 保证大根堆 m_small 的最大值 <= 小根堆 m_large 的最小值
        # m_small.top() 是 -self.m_small[0], m_large.top() 是 self.m_large[0]
        # 如果 -self.m_small[0] > self.m_large[0]
        if self.m_large and -self.m_small[0] > self.m_large[0]:
            # 将 m_small 的最大值移到 m_large
            max_small = -heapq.heappop(self.m_small)
            heapq.heappush(self.m_large, max_small)

        # 3. 保持 m_small 的元素个数 >= m_large 的元素个数，且个数差不超过 1
        # 如果 m_small 的元素过多 (m_small.size() > m_large.size() + 1)
        if len(self.m_small) > len(self.m_large) + 1:
            # 将 m_small 的最大值移到 m_large
            # 注意：从 m_small pop 出来的是负数，需要取反
            max_small = -heapq.heappop(self.m_small)
            heapq.heappush(self.m_large, max_small)
        
        # 4. 如果 m_large 的元素过多 (m_large.size() > m_small.size())
        # 保持 m_small 的元素个数 >= m_large 的元素个数
        if len(self.m_large) > len(self.m_small):
            # 将 m_large 的最小值移到 m_small
            min_large = heapq.heappop(self.m_large)
            # 插入 m_small 时要取反
            heapq.heappush(self.m_small, -min_large)

    def findMedian(self) -> float:
        total_size = len(self.m_small) + len(self.m_large)

        if total_size == 0:
            return 0.0 # 或者抛出异常，根据具体要求

        # 元素总数为奇数，中位数在大根堆 m_small 的堆顶
        # 总是保证 len(m_small) >= len(m_large)
        if len(self.m_small) > len(self.m_large):
            # m_small[0] 是负数，取反得到实际最大值
            return float(-self.m_small[0])
        
        # 元素总数为偶数，中位数是两个堆顶的平均值
        else: # len(self.m_small) == len(self.m_large)
            # -self.m_small[0] 是较小部分的最大值
            # self.m_large[0] 是较大部分的最小值
            median_sum = -self.m_small[0] + self.m_large[0]
            return median_sum / 2.0

# 示例用法
# finder = MedianFinder()
# finder.addNum(1)
# finder.addNum(2)
# print(finder.findMedian()) # 输出 1.5
# finder.addNum(3)
# print(finder.findMedian()) # 输出 2.0