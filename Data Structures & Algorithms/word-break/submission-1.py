class Solution:
    """
    单词拆分 (Word Break) 问题，使用动态规划实现。
    
    dp[i] 表示字符串 s 的前 i 个字符 (s[0...i-1]) 是否可以被 wordDict 拆分。
    """
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        
        s_len = len(s)
        
        # 定义 DP 数组 (列表)
        # 列表大小为 s_len + 1。
        # dp[i] = True 表示 s 的前 i 个字符 (s[:i]) 可以被拆分。
        # 初始化为 False。
        dp = [False] * (s_len + 1)
        
        # 边界条件/基本情况: 
        # 空字符串 (s[:0]) 总是可以被拆分的。
        dp[0] = True
        
        # 优化: 将 wordDict 转换为集合 (set) 以实现 O(1) 的查找时间
        word_set = set(wordDict)
        
        # 遍历所有可能的子字符串结束位置 i (从 1 到 s_len)
        # 这里的 C++ 代码遍历的是可能的起始位置 i (0 到 s_len - 1)，
        # 我们按照 C++ 的逻辑来转换：i 代表子串起始位置
        
        # i 代表当前子串的起始索引 (C++ 代码中的 i)
        for i in range(s_len):
            # 只有当 s[:i] 已经被成功拆分 (即 dp[i] 为 True) 时，才需要继续检查
            if dp[i]:
                # 遍历字典中的每一个单词
                for word in word_set:
                    word_len = len(word)
                    
                    # 检查是否满足以下三个条件:
                    # 1. dp[i] 必须为 True (已在外部检查)
                    # 2. 当前单词能放入剩余字符串中 (i + word_len <= s_len)
                    # 3. 剩余字符串 s[i:i+word_len] 等于字典中的当前单词
                    if i + word_len <= s_len and s[i:i + word_len] == word:
                        
                        # 状态转移公式:
                        # 如果 s[:i] 可以被拆分 (dp[i] == True)
                        # 并且 s[i:i+word_len] 是一个有效的单词
                        # 那么 s[:i+word_len] 也可以被拆分。
                        dp[i + word_len] = True
                        
        # 最终结果是 dp[s_len]，表示整个字符串 s[:s_len] 是否可以被拆分。
        return dp[s_len]

# 示例用法
# solution = Solution()
# print(solution.wordBreak("leetcode", ["leet", "code"]))  # 输出: True
# print(solution.wordBreak("applepenapple", ["apple", "pen"]))  # 输出: True
# print(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # 输出: False