class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            mid = (l + r) // 2
            
            total_hour = 0
            for p in piles:
                total_hour += (p - 1) // mid + 1
                
            if total_hour > h:
                l = mid + 1
            else:
                r = mid - 1
                
        return l