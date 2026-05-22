class Solution:
    """
    使用位操作计算两个整数的和，不允许使用 '+' 和 '-' 运算符。
    """
    def getSum(self, a: int, b: int) -> int:
        
        # 32 位整数的掩码
        # 0xFFFFFFFF 是 32 个 1
        MASK = 0xFFFFFFFF
        
        # Python 整数是无限精度的，我们只关注 32 位。
        # 循环继续，直到没有进位 (b == 0)
        while b != 0:
            
            # 1. 计算进位 (Carry): a & b
            # 进位发生在 a 和 b 对应位都是 1 的地方。
            # 这里需要使用 MASK 确保操作在 32 位范围内进行。
            carry = (a & b) & MASK
            
            # 2. 计算无进位和 (Sum without Carry): a ^ b
            # 异或运算相当于执行不考虑进位的加法。
            a = (a ^ b) & MASK
            
            # 3. 更新 b (新的进位): carry << 1
            # 将进位左移一位，准备在下一轮加到 a 上。
            b = (carry << 1) & MASK

        # 当循环结束时，a 存储了最终的无进位和，即最终结果。
        
        # 结果处理：
        # 如果 a 的第 31 位是 1 (即 a > 0x7FFFFFFF)，则它表示一个负数。
        # 我们需要将 32 位无符号结果转换回 Python 的有符号整数表示。
        if a > 0x7FFFFFFF:
            # 如果是负数，则用 (a - 2^32) 得到其补码对应的有符号值
            return ~(a ^ MASK)
        else:
            return a