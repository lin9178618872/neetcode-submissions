
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # ==========================
        # 第 1 步：把石头变成“负数”
        # 目的：用 Python 的最小堆，模拟最大堆
        # ==========================
        for i in range(len(stones)):
            stones[i] = -stones[i]

        # 把数组变成堆
        heapq.heapify(stones)

        # ==========================
        # 第 2 步：只要堆里还有 ≥2 块石头，就一直砸
        # ==========================
        while len(stones) > 1:

            # 取出最重的石头（负数中最小的）
            first = heapq.heappop(stones)

            # 取出第二重的石头
            second = heapq.heappop(stones)

            # ==========================
            # 第 3 步：如果重量不一样
            # ==========================
            if first != second:
                # 剩下的重量 = 重的 - 轻的
                # 注意：这里全是负数
                remain = first - second

                # 把剩下的石头放回堆里
                heapq.heappush(stones, remain)

            # 如果一样重，就什么都不做（等于两块都没了）

        # ==========================
        # 第 4 步：处理最后结果
        # ==========================
        if len(stones) == 0:
            return 0

        # stones[0] 是负数，取绝对值
        return abs(stones[0])
