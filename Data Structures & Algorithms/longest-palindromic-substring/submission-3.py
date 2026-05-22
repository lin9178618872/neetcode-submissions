class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0
        n = len(s)

        dp = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(False)
            dp.append(row)

        i = n - 1
        while i >= 0:
            j = i
            while j < n:
                if s[i] == s[j]:
                    length = j - i + 1
                    if length <= 3:
                        dp[i][j] = True
                    else:
                        if dp[i + 1][j - 1] == True:
                            dp[i][j] = True

                if dp[i][j] == True:
                    curLen = j - i + 1
                    if curLen > resLen:
                        resLen = curLen
                        resIdx = i

                j = j + 1
            i = i - 1

        return s[resIdx:resIdx + resLen]

