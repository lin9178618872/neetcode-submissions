class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        n_32bit = n & 0xFFFFFFFF
        for i in range(32):
            res <<= 1
            if n_32bit & 1:
                res += 1
            n_32bit >>= 1
        return res & 0xFFFFFFFF
