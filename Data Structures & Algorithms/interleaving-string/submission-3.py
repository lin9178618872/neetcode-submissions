class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # 如果长度对不上，直接不可能
        if len(s1) + len(s2) != len(s3):
            return False

        m = len(s1)
        n = len(s2)

        # dp[i][j] 表示
        # s1前i个 + s2前j个
        # 能否组成 s3前 i+j 个
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # 空字符串 + 空字符串 = 空字符串
        dp[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):

                # 情况1：当前字符来自 s1
                if i > 0:
                    if s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]:
                        dp[i][j] = True

                # 情况2：当前字符来自 s2
                if j > 0:
                    if s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]:
                        dp[i][j] = True

        return dp[m][n]