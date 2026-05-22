class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}              # 记录窗口中字符出现次数
        left = right = 0
        res = 0                  # 结果：最长无重复子串长度

        while right < len(s):
            c = s[right]         # 即将进入窗口的字符
            window[c] = window.get(c, 0) + 1
            right += 1           # 扩大窗口

            # 如果某个字符出现次数 > 1，说明需要缩小窗口
            while window[c] > 1:
                d = s[left]      # 移出窗口的字符
                window[d] -= 1
                left += 1        # 缩小窗口

            # 更新结果（此时窗口一定是无重复字符）
            res = max(res, right - left)

        return res
