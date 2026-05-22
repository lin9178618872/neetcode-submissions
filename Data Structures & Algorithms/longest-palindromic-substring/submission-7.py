class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        #dp = [[False] * n for _ in range(n)]
        dp = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(False)
            dp.append(row)
        
        res = s[0]
        
        for i in range(n):
            dp[i][i] = True
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                if s[i] == s[j]:
                    if length <= 3 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if length > len(res):
                            res = s[i:j + 1]
        
        return res

