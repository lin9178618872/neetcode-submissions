class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            m = (l + r) // 2
            
            total_hour = 0
            for p in piles:
                total_hour += (p - 1) // m + 1
                
            if total_hour > h:
                l = m + 1
            else:
                r = m - 1
                
        return l