class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        # 一共32位
        for i in range(32):
            # 取出 n 的第 i 位 (0/1)
            bit = (n >> i) & 1

            # 把这个 bit 放到 res 的 (31 - i) 位置
            res |= (bit << (31 - i))

        return res
