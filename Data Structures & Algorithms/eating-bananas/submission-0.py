class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # 定义：以速度 k 吃，所需的总时间
        def can_finish(k):
            time = 0
            for p in piles:
                # 吃完一个 pile 需要 ceil(p/k) 小时
                time += (p + k - 1) // k
            return time <= h
        
        left = 1
        right = max(piles)   # 最大速度不可能超过最大 pile
        
        # 套用模板：搜索最小可行值，因此找到第一个 True
        while left <= right:
            mid = left + (right - left) // 2
            if can_finish(mid):
                # mid 可行，尝试更小的 k
                right = mid - 1
            else:
                # mid 不可行，需要更大的 k
                left = mid + 1
        
        return left  # left 会停在第一个可行解
