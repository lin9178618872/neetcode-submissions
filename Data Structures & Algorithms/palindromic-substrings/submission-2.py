class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        if N == 0:
            return 0

        #dp = [[False] * N for _ in range(N)]
        dp = []                 # 先准备一个空列表（大盒子）
        for i in range(N):      # 循环 N 次，创建 N 行
            row = []            # 当前这一行（小盒子）
            
            for j in range(N):  # 每一行放 N 个 False
                row.append(False)

            dp.append(row)      # 把这一行放进 dp

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
