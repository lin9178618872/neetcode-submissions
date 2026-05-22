class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        dp = [[False] * n for _ in range(n)]
        result = 0

        # All length-1 substrings are palindromes
        for i in range(n):
            dp[i][i] = True
        result += n

        # Consider substrings of length >= 2
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if length == 2:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

                if dp[i][j]:
                    result += 1

        return result