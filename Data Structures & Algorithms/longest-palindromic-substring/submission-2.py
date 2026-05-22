class Solution:
    def longestPalindrome(self, s: str) -> str:

        # 用来记最长回文的起点
        resIdx = 0
        # 用来记最长回文的长度
        resLen = 0

        # 字符串长度
        n = len(s)

        # 创建 dp 表（最基础写法）
        dp = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(False)
            dp.append(row)

        # 从后往前遍历
        i = n - 1
        while i >= 0:

            # j 从 i 开始往后走
            j = i
            while j < n:

                # 判断左右字符是否相等
                if s[i] == s[j]:

                    # 计算当前字符串长度
                    length = j - i + 1

                    # 如果长度 <= 3，一定是回文
                    if length <= 3:
                        dp[i][j] = True

                    # 否则，看看中间那段是不是回文
                    else:
                        if dp[i + 1][j - 1] == True:
                            dp[i][j] = True

                # 如果确认是回文
                if dp[i][j] == True:

                    # 当前回文长度
                    curLen = j - i + 1

                    # 如果比之前记录的更长
                    if curLen > resLen:
                        resLen = curLen
                        resIdx = i

                j = j + 1
            i = i - 1

        # 返回最长回文
        return s[resIdx : resIdx + resLen]
