class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n - 1)   # 每次把最低位的1消掉
            res += 1
        return res
