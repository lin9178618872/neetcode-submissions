class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1

        # 初始化 i = 1 对应的情况
        if n >= 1:
            dp[1] = 1 if s[0] != '0' else 0

        # 从 i = 2 开始更新
        for i in range(2, n + 1):
            # 选择1：解码一位
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            # 选择2：解码两位
            num = int(s[i-2:i])
            if 10 <= num <= 26:
                dp[i] += dp[i-2]

        return dp[n]