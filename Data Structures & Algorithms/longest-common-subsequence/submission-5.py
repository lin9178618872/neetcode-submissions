class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        len1 = len(text1)
        len2 = len(text2)

        dp = []

        for i in range(len1 + 1):

            row = []

            for j in range(len2 + 1):

                row.append(0)

            dp.append(row)

        # 先处理 i = 1
        for j in range(1, len2 + 1):

            if text1[0] == text2[j - 1]:

                dp[1][j] = 1

            else:

                dp[1][j] = dp[1][j - 1]

        # 从 i = 2 开始
        for i in range(2, len1 + 1):

            for j in range(1, len2 + 1):

                if text1[i - 1] == text2[j - 1]:

                    dp[i][j] = dp[i - 1][j - 1] + 1

                else:

                    left = dp[i][j - 1]
                    up = dp[i - 1][j]

                    dp[i][j] = max(left, up)

        return dp[len1][len2]