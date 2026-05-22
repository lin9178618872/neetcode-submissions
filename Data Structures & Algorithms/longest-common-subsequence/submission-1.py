class Solution:
    """
    最长公共子序列 (Longest Common Subsequence, LCS) 问题，使用动态规划实现。
    
    dp[i][j] 表示 text1 的前 i 个字符和 text2 的前 j 个字符的最长公共子序列的长度。
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        text1_len = len(text1)
        text2_len = len(text2)
        
        # 1. 定义 DP 数组 (列表的列表)
        # dp 数组大小为 (text1_len + 1) x (text2_len + 1)。
        # 索引 0 行和 0 列都初始化为 0，这代表空字符串的 LCS 长度为 0。
        dp = [[0] * (text2_len + 1) for _ in range(text1_len + 1)]
        
        # 2. 状态转移计算
        # 注意: 这里的 i 和 j 遍历的是 dp 数组的索引 (从 1 到 len)，
        # 对应到字符串字符时需要使用 i-1 和 j-1
        
        # 遍历 dp 数组的行索引 i (对应 text1 的字符 i-1)
        for i in range(1, text1_len + 1):
            # 遍历 dp 数组的列索引 j (对应 text2 的字符 j-1)
            for j in range(1, text2_len + 1):
                
                # 检查当前字符 text1[i-1] 和 text2[j-1] 是否相等
                if text1[i - 1] == text2[j - 1]:
                    # 情况 1: 字符相等
                    # 状态转移公式: dp[i][j] = dp[i-1][j-1] + 1
                    # LCS 长度等于不包含这两个字符的前缀的 LCS 长度加 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    
                else:
                    # 情况 2: 字符不相等
                    # 状态转移公式: dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                    # LCS 长度等于以下两者中的较大值:
                    # a) text1 的前 i 个字符 与 text2 的前 j-1 个字符的 LCS 长度
                    # b) text1 的前 i-1 个字符 与 text2 的前 j 个字符的 LCS 长度
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
                
        # 3. 返回结果
        # 结果是 dp[text1_len][text2_len]，即整个 text1 和 text2 的 LCS 长度
        return dp[text1_len][text2_len]

# 示例用法
# solution = Solution()
# print(solution.longestCommonSubsequence("abcde", "ace"))  # 输出: 3 ("a", "c", "e")
# print(solution.longestCommonSubsequence("abc", "abc"))    # 输出: 3
# print(solution.longestCommonSubsequence("abc", "def"))    # 输出: 0