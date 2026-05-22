class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        if N == 0:
            return 0

        dp = [[False] * N for _ in range(N)]
        result = 0

        for L in range(1, N + 1):
            for i in range(N - L + 1):
                j = i + L - 1

                if L == 1:
                    dp[i][j] = True
                elif L == 2:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

                if dp[i][j]:
                    result += 1

        return result
