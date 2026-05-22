class Solution:
    def hammingWeight(self, n: int) -> int:
        n_32bit = n & 0xFFFFFFFF
        count = 0
        while n_32bit != 0:
            n_32bit &= (n_32bit - 1)
            count += 1
        return count
