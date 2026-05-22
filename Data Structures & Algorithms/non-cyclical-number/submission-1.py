class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # 记录出现过的数字
        
        while n != 1:
            if n in seen:  # 如果重复了 → 说明进入循环
                return False
            
            seen.add(n)
            
            # 计算下一步（各位平方和）
            n = self.getSum(n)
        
        return True
    
    def getSum(self, n):
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total