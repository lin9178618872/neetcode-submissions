class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1. window: 存储当前窗口 [left, right) 中的字符集合
        # 用于 O(1) 地检查字符是否重复
        window = set() 
        
        left, right = 0, 0
        max_len = 0  # 记录找到的最长无重复字符子串的长度

        while right < len(s):
            # c 是将移入窗口的字符
            c = s[right]
            
            # 判断左侧窗口是否要收缩
            # 如果新字符 c 已经在 window 中，说明出现了重复，需要收缩左边界 left
            while left < right and c in window:
                # d 是将移出窗口的字符
                d = s[left]
                
                # 移出窗口
                window.remove(d)
                
                # 缩小窗口
                left += 1
            
            # 此时，窗口 [left, right) 已经不包含 c，安全地将 c 加入窗口
            window.add(c)
            
            # 增大窗口
            right += 1
            
            # 更新答案：当前窗口 [left, right) 是一个有效的无重复子串
            # 长度为 right - left
            max_len = max(max_len, right - left)

        return max_len

# 示例测试（在 LeetCode 环境中不需要这部分）
# solution = Solution()
# print(f"Input: 'zxyzxyz', Output: {solution.lengthOfLongestSubstring('zxyzxyz')}") # 3
# print(f"Input: 'xxxx', Output: {solution.lengthOfLongestSubstring('xxxx')}")       # 1
# print(f"Input: 'abcabcbb', Output: {solution.lengthOfLongestSubstring('abcabcbb')}") # 3