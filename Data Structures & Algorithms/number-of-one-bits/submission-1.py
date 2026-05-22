class Solution:
    """
    计算一个 32 位整数的汉明重量（即二进制表示中 1 的个数）。
    使用 Brian Kernighan 算法。
    """
    def hammingWeight(self, n: int) -> int:
        
        # 1. 确保只考虑 32 位，将其转换为无符号的 32 位表示。
        # 0xFFFFFFFF 是 32 个 1。
        n_32bit = n & 0xFFFFFFFF
        
        count = 0
        
        # 循环直到 n_32bit 变为 0
        while n_32bit != 0:
            # 关键步骤：n_32bit &= (n_32bit - 1)
            # 这一操作会清除 n_32bit 最右边的 '1'。
            # 例如: n = 12 (1100), n-1 = 11 (1011)
            # n & (n-1) = 1100 & 1011 = 1000 (8)
            n_32bit &= (n_32bit - 1)
            count += 1
        
        return count