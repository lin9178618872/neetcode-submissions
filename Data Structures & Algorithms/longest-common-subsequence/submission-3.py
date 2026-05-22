class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1_len = len(text1)
        text2_len = len(text2)

        #dp = [[0] * (text2_len + 1) for _ in range(text1_len + 1)]
        dp = []  # 先创建一个空的二维列表

        for i in range(text1_len + 1):      # 外层循环：一共 text1_len + 1 行
            row = []                        # 每一行是一个新列表
            for j in range(text2_len + 1):  # 内层循环：一共 text2_len + 1 列
                row.append(0)               # 往这一行里放一个 0
            dp.append(row)                  # 把这一行加入 dp

        for i in range(1, text1_len + 1):
            for j in range(1, text2_len + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[text1_len][text2_len]
