class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = []                     # 创建一个空列表，用来存二维数组
        for i in range(m + 1):      # 循环 m+1 次，表示创建 m+1 行
            row = [0] * (n + 1)     # 创建一行，里面有 n+1 个 0
            dp.append(row)          # 把这一行加入 dp

        for j in range(n + 1):
            dp[m][j] = n - j

        for i in range(m + 1):
            dp[i][n] = m - i

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    delete = dp[i + 1][j]
                    insert = dp[i][j + 1]
                    replace = dp[i + 1][j + 1]
                    dp[i][j] = 1 + min(delete, insert, replace)

        return dp[0][0]