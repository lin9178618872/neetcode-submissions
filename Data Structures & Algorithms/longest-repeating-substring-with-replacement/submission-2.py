class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}              # 记录窗口字符频次
        left = 0
        max_freq = 0            # 窗口内出现最多的字符次数
        res = 0
        
        for right in range(len(s)):
            c = s[right]
            count[c] = count.get(c, 0) + 1
            max_freq = max(max_freq, count[c])  # 更新最大频次
            
            # 若需要替换的字符超过 k，则收缩窗口
            # (window_size - max_freq) > k
            while (right - left + 1) - max_freq > k:
                d = s[left]
                count[d] -= 1
                left += 1
            
            # 当前有效窗口大小
            res = max(res, right - left + 1)
        
        return res
