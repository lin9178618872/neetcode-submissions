class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3):
            return False

        m = len(s1)
        n = len(s2)

        dp = []
        for i in range(m + 1):
            row = [False] * (n + 1)
            dp.append(row)

        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):

                if i < m:
                    if s1[i] == s3[i + j] and dp[i + 1][j]:
                        dp[i][j] = True

                if j < n:
                    if s2[j] == s3[i + j] and dp[i][j + 1]:
                        dp[i][j] = True

        return dp[0][0]