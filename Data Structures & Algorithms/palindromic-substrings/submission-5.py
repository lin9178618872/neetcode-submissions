class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        dp = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(False)
            dp.append(row)

        result = 0

        for length in range(1, n + 1):   # 原来的 l
            for i in range(n - length + 1):
                j = i + length - 1

                if length == 1:
                    dp[i][j] = True
                elif length == 2:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

                if dp[i][j]:
                    result += 1

        return result