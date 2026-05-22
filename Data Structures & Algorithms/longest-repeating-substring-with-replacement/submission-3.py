class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        right = 0
        max_freq = 0
        res = 0
        
        while right < len(s):
            c = s[right]
            count[c] = count.get(c, 0) + 1
            max_freq = max(max_freq, count[c])
            right += 1    # 扩大窗口
            
            # 判断是否需要收缩窗口
            while (right - left) - max_freq > k:
                d = s[left]
                count[d] -= 1
                left += 1
            
            # 记录最大窗口
            res = max(res, right - left)
        
        return res
