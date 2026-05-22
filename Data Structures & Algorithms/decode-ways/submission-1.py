class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        # 初始化 base case
        dp[0] = 1

        # 进行状态转移
        for i in range(1, n + 1):          # 状态1 取值：i
            # 选择1：解码一位
            if s[i-1] != '0':
                # 求最值 -> 求和
                dp[i] += dp[i-1]

            # 选择2：解码两位
            if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        return dp[n]
