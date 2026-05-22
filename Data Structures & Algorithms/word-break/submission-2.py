class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        s_len = len(s)
        dp = [False] * (s_len + 1)
        dp[0] = True
        word_set = set(wordDict)

        for i in range(s_len):
            if dp[i]:
                for word in word_set:
                    word_len = len(word)
                    if i + word_len <= s_len and s[i:i + word_len] == word:
                        dp[i + word_len] = True

        return dp[s_len]
