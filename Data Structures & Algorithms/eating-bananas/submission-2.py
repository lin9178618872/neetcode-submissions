class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            m = (l + r) // 2
            
            total_hour = 0
            for pile in piles:
                # 向上取整公式：(pile + m - 1) // m 
                # 图片中的写法 (pile - 1) // m + 1 效果一致
                total_hour += (pile - 1) // m + 1
                
            if total_hour <= h:
                # 速度可行，尝试更小的速度以找到最小值
                r = m - 1
            else:
                # 速度太慢，需要增加速度
                l = m + 1
                
        return l